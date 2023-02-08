import os

from celery import Celery

from . import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')

# 创建celery实例
celery_app = Celery('swiper')
# 配置
celery_app.config_from_object(config)
# 自动搜索项目中的任务
celery_app.autodiscover_tasks()


def call_by_worker(func):
    """
    将被装饰的函数,直接变成一个异步任务
    """
    task = celery_app.task(func).delay
    return task

"""
启动celery任务:
celery worker -A --loglevel=info 
"""