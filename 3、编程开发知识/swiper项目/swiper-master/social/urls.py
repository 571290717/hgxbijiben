# -*- coding: utf-8  -*-
# @Author: ty
# @File name: urls.py 
# @IDE: PyCharm
# @Create time: 2/4/21 3:41 PM
# @Description:
from django.conf.urls import url

from social import views

urlpatterns = [
    url(r'/', views.index, name='index'),
    url(r'^get_recommend_users', views.get_recommend_users, name='get_recommend_users'),
    url(r'^new_recommend_users', views.new_recommend_users, name='new_recommend_users'),  # 使用redis缓存的推荐
    url(r'^get_friends', views.get_friends, name='get_friends'),
    url(r'^like', views.like, name='like'),
    url(r'^dislike', views.dislike, name='dislike'),
    url(r'^super_like', views.super_like, name='super_like'),
    url(r'^regret', views.regret, name='regret'),
    url(r'^show_liked_me', views.show_liked_me, name='show_liked_me'),
    url(r'^get_friends', views.get_friends, name='get_friends'),
    url(r'^hot_swiped', views.hot_swiped, name='hot_swiped'),
]
