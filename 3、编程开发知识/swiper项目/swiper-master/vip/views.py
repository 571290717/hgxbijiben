import logging

from django.core.cache import cache
from django.shortcuts import render

from lib.http import render_json

from vip.models import Vip

logger = logging.getLogger('inf')


# Create your views here.
def index(request):
    return render_json(None)


def show_vip_permissions(request):
    """展示VIP所拥有的权限"""
    key = 'VipPermissions'
    # 先从缓存中获取数据, 没有再进行数据库操作
    vip_permissions = cache.get(key, [])
    logger.info(f'get from cache: {vip_permissions}')
    if not vip_permissions:
        # vip_permissions = []
        # vips = Vip.objects.filter(level__gte=1)  # 普通用户的等级为1
        for vip in Vip.objects.filter(level__gte=1):
            vip_info = vip.to_dict()
            permission_info = []
            for permission in vip.permissions():
                permission_info.append(permission.to_dict())
            vip_info['permission_info'] = permission_info
            vip_permissions.append(vip_info)
            logger.info(f'get from db: {vip_permissions}')
        # 数据库操作完之后还要将数据进行缓存, 以便下一次获取
        cache.set(key, vip_permissions)
        logger.info('set to cache')
    return render_json(vip_permissions)
