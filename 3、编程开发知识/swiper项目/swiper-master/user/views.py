from django.core.cache import cache
from django.shortcuts import render
from lib.http import render_json
from common import code
from lib.sms import check_verify_code, send_verify_code
from social.helper import pre_rcmd
from user.models import User
from user.helper import save_upload_file
from lib.qncloud import async_upload_to_qiniu


# Create your views here.
def get_verify_code(request):
    """
    获取验证码
    """
    # 获取手机号
    phone_num = request.GET.get('phone_num', '')

    # 产生验证码
    # 对接第三方短信平台发送短信验证码
    send_verify_code(phone_num)
    # 异步调用方式
    send_verify_code.delay(phone_num)
    """
    send_verify_code = celery_app.task(send_verify_code).delay
    """
    # return render_json(data, 200)
    # return render_json(None, code.OK)
    return render_json(None)


def login(request):
    """
    登录
    """
    # 获取参数
    phone_num = request.POST.get('phone_num', '')
    verify_code = request.POST.get('verify_code', '')
    # 验证参数
    if not check_verify_code(phone_num, verify_code):
        # 验证成功
        # pass
        # try:
        #     user = User.objects.get()
        # except User.DoesNotExist:
        #     User.objects.create()
        user, created = User.objects.get_or_create(phone_num=phone_num)
        # 缓存user id
        request.session['uid'] = user.id
        # return render_json(user.to_dict(), code.OK)
        return render_json(user.to_dict())
    else:
        # 验证失败, 返回错误的验证码
        # return render_json(None, code.VcodeError.code)
        raise code.VcodeError


def user_back(request):
    user = request.user
    # 推荐算法预处理
    pre_rcmd(user)
    return render_json(None)


def show_profile(request):
    """展示个人信息"""
    # 获取用户
    # uid = request.session['uid']
    # user = User.objects.get(uid)
    # 用户验证
    # 封装请求中间件进行用户信息的获取和用户信息的验证
    user = request.user
    # 将profile私有化为user类的一个属性
    # 增加缓存处理
    key = f'Profile-{user.id}'
    result = cache.get(key)  # 获取缓存
    if result is None:
        result = user.profile.to_dict()
        cache.set(key, result)  # 添加缓存
    return render_json(result)


def modify_profile(request):
    """
    编辑个人信息
    """
    from user.forms import ProfileForm
    # 表单数据获取
    form = ProfileForm(request.POST)
    # 表单数据验证
    if form.is_valid():
        # 创建对象的时候先封装出来, 不提交, 等额外构建完之后再提交
        profile = form.save(commit=False)
        profile.id = request.user.id
        profile.save()
        # return render_json(profile.to_dict())

        result = profile.to_dict()
        # 添加缓存
        cache.set(f'Profile-{profile.id}', result)
        return render_json(result)
    else:
        return render_json(form.errors, code.ProfileError.code)


def upload_avatar(request):
    """
    上传头像
    """
    # 获取需要上传的头像
    avatar = request.FILES.get('avatar')  # 类型为InMemoryUploadedFile对象
    # 上传的文件保存到本地
    filepath, filename = save_upload_file(request.user, avatar)
    # 再将本地文件上传到七牛云, 但是直接上传的话,效率比较低下, 采用异步上传的方式处理
    # upload_to_qiniu(filepath, filename)
    # 异步上传
    # async_upload_to_qiniu(filepath, filename)
    # 异步上传, 并修改头像url
    from user.helper import upload_avatar_to_qiniu
    upload_avatar_to_qiniu(request.user, filepath, filename)
    return render_json(None)

