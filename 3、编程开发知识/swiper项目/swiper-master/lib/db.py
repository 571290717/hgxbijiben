# -*- coding: utf-8  -*-
# @Author: ty
# @File name: db.py 
# @IDE: PyCharm
# @Create time: 2/9/21 12:15 AM
# @Description:
from django.core.cache import cache


def get(cls, *args, **kwargs):
    """数据优先从缓存中获取, 缓存中获取不到,再从数据库中获取"""
    # 创建key
    pk = kwargs.get('pk') or kwargs.get('id')
    # 从缓存中获取数据
    if pk is not None:
        key = 'Model-%s-%s' % (cls.__name__, pk)
        model_obj = cache.get(key)
        if isinstance(model_obj, cls):
            return model_obj

    # 缓存中没有数据, 直接从数据库中获取
    model_obj = cls.objects.get(*args, **kwargs)
    # 写入缓存, 并设置过期时间为 一周
    key = 'Model-%s-%s' % (cls.__name__, model_obj.pk)
    cache.set(key, model_obj, 604800)
    return model_obj


def get_or_create(cls, *args, **kwargs):
    """"""
    pk = kwargs.get('pk') or kwargs.get('id')
    if pk is not None:
        key = 'Model-%s-%s' % (cls.__name__, pk)
        model_obj = cache.get(key)
        if isinstance(model_obj, cls):
            return model_obj, False

    model_obj, created = cls.objects.get_or_create(*args, **kwargs)
    key = 'Model-%s-%s' % (cls.__name__, model_obj.pk)
    cache.set(key, model_obj, 604800)
    return model_obj, created


# def save_to_cache(origin_save):
#     def wrapper(*args, **kwargs):
#         origin_save(*args, **kwargs)
#         cache.set(key, obj)
#     return wrapper


def save_with_cache(model_save_func):
    """"""

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    def save(self, *args, **kwargs):
        """存入数据库后 ,同时写入缓存"""
        # model_save_func(force_insert, force_update, using, update_fields)
        model_save_func(*args, **kwargs)
        # 添加缓存
        key = 'Model-%s-%s' % (self.__class__.__name__, self.pk)
        cache.set(key, self)

    return save


def to_dict(self, ignore_fields=()):
    """将一个model转换成一个dict"""
    attr_dict = {}
    for field in self._meta.fields:
        name = field.attrname
        if name not in ignore_fields:
            attr_dict[name] = getattr(self, name)
    return attr_dict


def patch_model():
    """动态更新Model方法"""
    # Model在django中是一个特殊的类, 如果通过继承的方式来增加或修改原有的方法,
    # django会将继承的类识别为一个普通的app.model, 所以只能通过monkey patch(猴子补丁)的方式动态修改

    # models.Model.get = get
    # models.Model.save = save

    # 动态添加一个类方法 get/get_or_create
    from django.db import models
    models.Model.get = classmethod(get)
    models.Model.get_or_create = classmethod(get_or_create)

    models.Model.save = save_with_cache(models.Model.save)
    models.Model.to_dict = to_dict
