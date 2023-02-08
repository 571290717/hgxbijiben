# -*- coding: utf-8  -*-
# @Author: ty
# @File name: gunicorn_config.py.py 
# @IDE: PyCharm
# @Create time: 2/15/21 5:09 PM
# @Description: gunicorn配置
from multiprocessing import cpu_count

bind = ['127.0.0.1:8000']
daemon = True  # 是否开启守护进程模式, 后台运行
pidfile = 'logs/gunicorn.pid'

workers = cpu_count() * 2  # 工作进程数量
worker_class = 'gevent'  # 指定一个异步处理的库
worker_connections = 65535

keepalive = 60  # 服务器保持连接的时间, 能够避免频繁的建立连接过程
timeout = 30
graceful_timeout = 10  # 重启时的超时时间
forwarded_allow_ips = '*'

# 日志处理
capture_output = True
loglevel = 'info'
errorlog = 'logs/error.log'

"""
gunicorn -c swiper/gunicorn_config.py swiper.wsgi
Gunicorn 进程模型:
    master: 主进程(只负责管理子进程, 自身不接受用户请求)
    worker: 工作进程(它是fork主进程而来的, 接收并处理用户请求)
使用gunicorn代替wsgi提升django服务器性能
"""

