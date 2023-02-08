# -*- coding: utf-8  -*-
# @Author: ty
# @File name: status_code.py 
# @IDE: PyCharm
# @Create time: 2/1/21 7:05 PM
# @Description: 状态码常量

# 成功
OK = 200

# 验证码错误
# VCODE_ERROR = 1000
#
# # 用户登录异常
# LOGIN_REQUIRE = 1001
#
# # 用户不存在
# USER_NOT_EXIST = 1002
#
# # 个人信息数据验证不合法异常
# PROFILE_ERROR = 1003


class LogicError(Exception):  # BaseException基类异常
    """程序运行过程中出现一些逻辑上的异常, 返回对应的状态码"""
    code = 0

    def __str__(self):
        return self.__class__.__name__


def generate_logic_error(name, code):
    """
    生成逻辑异常类, 通过函数创建类
    """
    base_cls = (LogicError,)  # 继承自 LogicError
    # 通过type创建类
    # type(name, base, dict) -> a new  type
    #     name: 需要创建的类的名称
    #     base: 需要继承的基类
    #     dict: 处理成一个属性字典
    return type(name, base_cls, {'code': code})


# 验证码错误
VcodeError = generate_logic_error('VcodeError', 1000)

# 验证码未过期
VcodeExist = generate_logic_error('VcodeExist', 1001)

# 帐号未登录
LoginRequire = generate_logic_error('LoginRequire', 1002)

# 用户不存在
UserNotExist = generate_logic_error('UserNotExist', 1003)

# 个人信息错误
ProfileError = generate_logic_error('ProfileError', 1004)

# 没有相关权限
NotHasPermission = generate_logic_error('NotHasPermission', 1005)
