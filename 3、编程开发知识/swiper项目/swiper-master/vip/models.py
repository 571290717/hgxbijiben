from django.db import models

# from lib.orm import ModelMixin


# Create your models here.
# class Vip(models.Model, ModelMixin):
class Vip(models.Model):
    """VIP表"""
    name = models.CharField(max_length=32, unique=True)
    level = models.IntegerField(unique=True)
    price = models.FloatField()

    # @property
    def permissions(self):
        """查询关联的权限信息, 当前VIP具有的所有权限"""
        relations = VipPermissionRelation.objects.filter(vip_id=self.id)
        permission_id_list = [r.permission_id for r in relations]
        return Permission.objects.filter(id__in=permission_id_list)

    def has_permission(self, permission_name):
        """检查该等级VIP是否具有某个权限"""
        try:
            permission = Permission.objects.get(name=permission_name)
        except Permission.DoesNotExist:
            return False
        else:
            return VipPermissionRelation.objects.filter(vip_id=self.id, permission_id=permission.id).exist()

    class Meta:
        db_table = 'db_vip'
        ordering = ['level']
        verbose_name = 'vip'
        verbose_name_plural = verbose_name


# class Permission(models.Model, ModelMixin):
class Permission(models.Model):
    """权限表"""
    name = models.CharField(max_length=32, unique=True)
    desc = models.TextField()

    class Meta:
        db_table = 'db_permission'
        ordering = ['name']
        verbose_name = 'permission'
        verbose_name_plural = verbose_name


# class VipPermissionRelation(models.Model, ModelMixin):
class VipPermissionRelation(models.Model):
    """vip和权限关联表"""
    vip_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        db_table = 'db_vip_permission'
