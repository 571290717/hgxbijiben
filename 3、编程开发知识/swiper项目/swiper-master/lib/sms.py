# -*- coding: utf-8  -*-
# @Author: ty
# @File name: sms.py 
# @IDE: PyCharm
# @Create time: 2/1/21 4:55 PM
# @Description:
import random

import requests

from swiper import config
from django.core.cache import cache
from worker import call_by_worker


def gen_verify_code(length=6):
    """
    产生验证码
    """
    min_value = 10 ** (length - 1)
    max_value = 10 ** (length)
    verify_code = random.randrange(min_value, max_value)
    # print(verify_code)
    return verify_code


@call_by_worker
def send_sms(phone_num, msg):
    """发送短信"""
    # 复制一个HY_SMS_PARAMS,对其进行赋值操作,避免多人修改同一个
    params = config.HY_SMS_PARAMS.copy()
    params['mobile'] = phone_num
    params['content'] = params['content'] % msg
    response = requests.post(config.HY_SMS_URL, data=params)
    return response


def send_verify_code(phone_num):
    """
    #对接第三方的平台,发送验证码
    """
    key = 'verify_code-%s' % phone_num
    # 检查验证码是否过期, 过期了就重新发送
    if not cache.has_key(key):
        verify_code = gen_verify_code()
        # params = config.HY_SMS_PARAMS.copy()
        # params['mobile'] = phone_num
        # params['content'] = params['content'] % verify_code
        # response = requests.post(config.HY_SMS_URL, data=params)
        send_sms(phone_num, verify_code)
        # 缓存
        cache.set(key, verify_code, 180)  # timeout
        return response
    else:
        from common.code import VcodeExist
        raise VcodeExist  # 验证码未过期


# 装饰器
# @celery_app.task
# 或者
# send_verify_code = celery_app.task(send_verify_code).delay

def check_verify_code(phone_num, verify_code):
    """
    验证验证码
    """
    # 从缓存中获取验证码并进行比较
    cached_verify_code = cache.get('verify_code_%s' % phone_num)
    return cached_verify_code == verify_code
