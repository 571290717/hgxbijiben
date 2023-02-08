# -*- coding: utf-8  -*-
# @Author: ty
# @File name: orm.py 
# @IDE: PyCharm
# @Create time: 2/2/21 1:06 AM
# @Description:

class ModelMixin():
    """类似于虚拟模型类的处理方式"""

    def to_dict(self, ignore_fields=()):
        """将一个model转换为一个dict"""
        attr_dict = {}
        for field in self._meta.fields:  # 遍历所有字段
            name = field.name  # 取出字段名称
            if name not in ignore_fields:  # 检查是否是需要忽略的字段
                attr_dict[name] = getattr(self, name)  # 获取字段对应的值
        return attr_dict
