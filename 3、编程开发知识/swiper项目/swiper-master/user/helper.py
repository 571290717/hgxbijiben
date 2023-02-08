# -*- coding: utf-8  -*-
# @Author: ty
# @File name: helper.py 
# @IDE: PyCharm
# @Create time: 2/1/21 4:54 PM
# @Description: 逻辑处理函数
import os

from django.conf import settings
from swiper import config


def save_upload_file(user, upload_file):
    """
    将上传的文件保存到本地
    """
    # 文件名不需要文件后缀去识别文件的类型
    filename = 'avatar_%s' % user.id
    # 拼接文件路径
    filepath = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)
    # 文件写入
    with open(filepath, 'wb') as f:
        for chunk in upload_file.chunks():  # chunks 实现是生成器的方式实现的 yield
            f.write(chunk)

    return filepath, filename


def get_qiniu_url(filename):
    """
    将七牛域名和上传文件的文件名进行拼接, 得到上传头像的url
    """
    from urllib.parse import urljoin
    return urljoin(config.QN_BASE_URL, filename)


from worker import call_by_worker
@call_by_worker
def upload_avatar_to_qiniu(user, filepath, filename):
    """
    将用户头像上传到七牛云, 并修改头像url
    """
    from lib.qncloud import upload_to_qiniu
    *_, avatar_url = upload_to_qiniu(filepath, filename)
    user.avatar = avatar_url
    user.save()
