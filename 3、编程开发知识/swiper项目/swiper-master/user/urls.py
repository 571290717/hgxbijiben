# -*- coding: utf-8  -*-
# @Author: ty
# @File name: urls.py 
# @IDE: PyCharm
# @Create time: 2/1/21 4:12 PM
# @Description:
from user import views
from django.conf.urls import url

# urlpatterns = [
#     # url(r'^verify_code$', views.get_verify_code),
#     url(r'^api/user/verify_code$', views.get_verify_code),
#     url(r'^api/user/login$', user.login),
#     url(r'^api/user/profile/show$', user.show_profile),
#     url(r'^api/user/profile/modify$', user.modify_profile),
#     url(r'^api/user/avatar/upload$', user.upload_avatar),
# ]

urlpatterns = [
    url(r'^verify_code$', views.get_verify_code, name='get_verify_code'),
    url(r'^login$', views.login, name='login'),
    url(r'^profile/show$', views.show_profile, name='show_profile'),
    url(r'^profile/modify$', views.modify_profile, name='modify_profile'),
    url(r'^avatar/upload$', views.upload_avatar, name='upload_avatar'),
]
