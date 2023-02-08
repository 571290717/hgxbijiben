from django.db import models

from django.db.models import Q


# Create your models here.
class Swiped(models.Model):
    """滑动记录表"""
    FLAGS = (
        ('superlike', '上滑'),
        ('like', '右滑'),
        ('dislike', '左滑'),
    )
    uid = models.IntegerField(verbose_name='滑动者的ID')
    sid = models.IntegerField(verbose_name='被滑动者的ID')
    flag = models.CharField(max_length=10, choices=FLAGS)  # 滑动标志
    date_time = models.DateTimeField(auto_now=True)  # 滑动的时间

    class Meta:
        db_table = 'db_swiped'
        get_latest_by = 'date_time'
        ordering = ['-date_time']  # 按照那个字段排序
    #     permissions = (())  # 权限限制
        verbose_name = 'swiped'
        verbose_name_plural = 'swipeds'

    @classmethod
    def like(cls, uid, sid):
        obj = cls.objects.create(uid=uid, sid=sid, flag='like')
        return obj

    @classmethod
    def dislike(cls, uid, sid):
        obj = cls.objects.create(uid=uid, sid=sid, flag='dislike')
        return obj

    @classmethod
    def superlike(cls, uid, sid):
        obj = cls.objects.create(uid=uid, sid=sid, flag='superlike')
        return obj

    @classmethod
    def regret(cls, uid):
        cls.objects.filter(uid=uid).latest().delete()

    @classmethod
    def is_liked(cls, uid, sid):
        # 检查是否存在
        return cls.objects.filter(uid=uid, sid=sid, flag__in=['like', 'superlike']).exists()

    @classmethod
    def liked_me(cls, uid):
        cls.objects.filter(sid=uid, flag__in=['like', 'superlike'])


class Friend(models.Model):
    """好友关系表"""
    # 好友关系是相互的
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    class Meta:
        db_table = 'db_friend'
        ordering = ['uid1']  # 按照那个字段排序
        # permissions = (())  # 权限限制
        verbose_name = 'friend'
        verbose_name_plural = 'friends'

    @classmethod
    def make_friend(cls, uid1, uid2):
        uid1, uid2 = sorted([uid1, uid2])  # 排序
        cls.objects.get_or_create(uid1=uid1, uid2=uid2)

    @classmethod
    def is_friends(cls, uid1, uid2):
        # 检查两个人是否是好友
        # 排序
        uid1, uid2 = sorted([uid1, uid2])
        return cls.objects.get_or_create(uid1=uid1, uid2=uid2).exists()

    @classmethod
    def break_off(cls, uid1, uid2):
        """断开好友关系"""
        uid1, uid2 = sorted([uid1, uid2])
        cls.objects.filter(uid1=uid1, uid2=uid2).delete()

    @classmethod
    def friend_id_list(cls, uid):
        """获取所有好友id列表"""
        # 查询我的好友
        condition = Q(uid1=uid) | Q(uid2=uid)
        relations = cls.objects.filter(condition)
        # 筛选好友的uid
        id_list = []
        for relation in relations:
            friend_id = relation.uid2 if relation.uid1 == uid else relation.uid1
            id_list.append(friend_id)
        return id_list
