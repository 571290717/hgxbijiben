# -*- coding: utf-8  -*-
# @Author: ty
# @File name: forms.py 
# @IDE: PyCharm
# @Create time: 2/2/21 5:48 PM
# @Description: form表单, 将表单的验证交给django去处理
from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    """个人信息表单类"""

    class Meta:
        model = Profile  # 关联类
        fields = [
            'location', 'min_distance', 'max_distance', 'min_dating_age', 'max_dating_age', 'dating_sex', 'vibration', 'only_matche', 'auto_play'
        ]  # 约束字段

    # 验证数据的正确性
    def clean_min_distance(self):
        """检查最小距离"""
        cleaned_data = super().clean()
        if cleaned_data['min_distance'] > cleaned_data['max_distance']:
            raise forms.ValidationError('最小距离不能大于最大距离')
        return cleaned_data['min_distance']

    def clean_min_dating_age(self):
        """检查最大年龄距离"""
        cleaned_data = super().clean()
        if cleaned_data['min_dating_age'] > cleaned_data['max_dating_age']:
            raise forms.ValidationError('最小年龄不能大于最大年龄')
        return cleaned_data['min_dating_age']
