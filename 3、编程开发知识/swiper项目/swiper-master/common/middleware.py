# -*- coding: utf-8  -*-
# @Author: ty
# @File name: middleware.py 
# @IDE: PyCharm
# @Create time: 2/2/21 11:19 AM
# @Description: 自定义中间件
import logging

from django.utils.deprecation import MiddlewareMixin
from common import code
from user.models import User
from lib.http import render_json

logger = logging.getLogger('err')


class AuthMiddleware(MiddlewareMixin):
    """用户验证中间件"""
    # 白名单
    white_list = [
        '/api/user/verify_code',
        '/api/user/login',
        '/api/user/avatar/upload',  # 本身不需要添加到白名单中, 只是为了方便调试
    ]

    def process_request(self, request):
        """
        所有请求处理之前都要进行此中间件的处理
        """
        # 检查当前path是否在白名单内
        if request.path in self.white_list:
            return

        # 用户登录验证
        # 获取用户信息
        uid = request.session.get['uid']
        # 验证用户信息
        if uid is None:
            return render_json(None, code.LoginRequire.code)
        else:
            try:
                user = User.objects.get(id=uid)
            # 用户不存在
            except User.DoesNotExist:
                logger.error('{} does not exist'.format(user))
                return render_json(None, code.UserNotExist.code)
            else:
                # 最终将user对象附到request上
                request.user = user


class LogicErrorMiddleware(MiddlewareMixin):
    """代码中逻辑错误处理中间件"""

    def process_exception(self, request, exception):
        """异常处理"""
        if isinstance(exception, code.LogicError):
            # 处理逻辑错误
            logger.error(f'LogicError: {exception}')
            return render_json(None, exception.code)
        # else:
        #     # 处理程序错误
        #     error_info = format_exception(*exc_info())
        #     error_log.error(''.join(error_info))  # 将异常信息输出到错误日志
        #     return render_json(error=code.InternalError)  # 程序错误统一使用 InternalError
