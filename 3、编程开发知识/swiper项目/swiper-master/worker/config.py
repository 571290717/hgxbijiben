# -*- coding: utf-8  -*-
# @Author: ty
# @File name: config.py 
# @IDE: PyCharm
# @Create time: 2/2/21 12:02 AM
# @Description: Celery配置

broker_url = 'redis://127.0.0.1: 6379/0'
broker_pool_limit = 100  # Broker 连接池, 默认是 10

timezone = 'Asia/Shanghai'
accept_content = ['pickle', 'json']

task_serializer = 'pickle'
result_expires = 3600

result_backend = 'redis://127.0.0.1: 6379/0'
result_serializer = 'pickle'
result_cache_max = 10240  # 任务结果对大缓存数量

worker_redirect_stdouts_level = 'INFO'
