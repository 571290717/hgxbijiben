import datetime
from django.db import models
# from lib.orm import ModelMixin

from social.models import Friend
from vip.models import Vip


# Create your models here.
# class User(models.Model, ModelMixin):
class User(models.Model):
    """用户模型类"""
    SEX = (
        ('0', '男性'),
        ('1', '女性'),
    )
    nickname = models.CharField(max_length=32, unique=True)
    phone_num = models.CharField(max_length=16, unique=True)
    sex = models.CharField(max_length=8, choices=SEX)
    # 出生年月日
    birth_year = models.IntegerField(default=1998, verbose_name='出生年')
    birth_month = models.IntegerField(default=1, verbose_name='出生月')
    birth_day = models.IntegerField(default=1, verbose_name='出生日')

    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=32, verbose_name='常居地')

    vip_id = models.IntegerField(default=1, verbose_name='VIP ID')

    @property
    def age(self):
        """
        用户年龄
        """
        today = datetime.date.today()
        birth_time = datetime.date(self.birth_year, self.birth_month, self.birth_day)

        # 把函数变为了类的私有属性, 相当于每次都进行类一次数据库的查询操作,效率地下
        # print(self.profile.dating_sex)
        # print(self.profile.location)
        # print(self.profile.vibration)
        # 只进行一次数据库的操作, 有一个中间的保存过程
        # profile = self.profile
        # print(profile.dating_sex)
        # print(profile.location)
        # print(profile.vibration)

        return (today - birth_time).days // 365

    # 用户和用户信息之间建立关联(拥有相同的id)

    @property
    def profile(self):
        # 每次先检查是否有_profile这一属性, 没有就先创建出这一属性, 将该属性保持住self.profile, 并返回避免每次都要进行数据库的查询, 懒加载的机制
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile

    @property
    def vip(self):
        if not hasattr(self, '_vip'):
            self._vip = Vip.objects.get(id=self.vip_id)
        return self._vip

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'nickname': self.nickname,
    #         'phone_num': self.phone_num,
    #         'age': self.age,
    #         'sex': self.sex,
    #         'avatar': self.avatar,
    #         'location': self.location,
    #     }

    def friends(self):
        friend_id_list = Friend.friend_id_list(self.id)
        return User.objects.filter(id__in=friend_id_list)

    class Meta:
        db_table = 'db_user'
        ordering = ['nickname']
        # permissions = (())
        verbose_name = 'user'
        verbose_name_plural = 'users'


# class Profile(models.Model, ModelMixin):
class Profile(models.Model):
    """个人配置数据"""
    SEX = (
        ('0', '男'),
        ('1', '女'),
    )
    location = models.CharField(max_length=32, verbose_name='目标城市')
    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=60, verbose_name='最大交友年龄')
    dating_sex = models.CharField(max_length=8, choices=SEX, verbose_name='匹配性别')
    vibration = models.CharField(max_length=8, default=True, verbose_name='开启提示')
    only_matche = models.CharField(max_length=8, default=True, verbose_name='不让未匹配的人看我的相册')
    auto_play = models.CharField(max_length=8, default=True, verbose_name='自动播放视频')

    class Meta:
        db_table = 'db_profile'
        # ordering = ['']
        verbose_name = 'user_info'
        verbose_name_plural = verbose_name
