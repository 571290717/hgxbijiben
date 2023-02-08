# -*- coding: utf-8  -*-
# @Author: ty
# @File name: config.py 
# @IDE: PyCharm
# @Create time: 2/1/21 5:02 PM
# @Description: 其他配置

# 互亿无线短信平台对接配置
HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': '',
    'password': '',
    'content': '您的验证 码是: %s, 为了您的帐号安全, 请勿泄露您的验证码.',
    'mobile': None,
    'format': 'json',
}

# 七牛云配置
QN_BUCKET = 'testswiper'  # 空间名称
QN_BASE_URL = 'http://qnxshht1r.hn-bkt.clouddn.com'  # 域名
# 密钥
QN_ACCESS_KEY = 'rAl8TwaBg3dzgBZx2qyEV9ap9UbVy7k5vioqRBKR'  # AK
QN_SECRET_KEY = 'Yy0AfVCsdM4hvvu3Wa1mpWtDv7-IEvEcY0BE8uyJ'  # SK

# 日志配置
# 使用python默认的日志模块实现
# import logging
#
# # 设置日志格式
# fmt = '%(asctime)s %(levelname) %(funcName)s: %(message)s'
# # 格式化器
# formatter = logging.Formatter(fmt, datefmt='%Y-%m-%d %H:%M:%S')
#
# # 处理器handler
# handler = logging.handlers.TimeRotatingFileHandler('logs.log', when='D', backupCount=30)  # 日志按照天分割, 备份数量为30份
# # setFormatter
# handler.setFormatter(formatter)
#
# # 定义logging对象
# logging = logging.getLogger('Log')
# logging.addHandler(handler)
# logging.setLevel(logging.info)
