from django.conf.urls import url

from vip import views

urlpatterns = [
    url(r'/', views.index, name='index'),
    url(r'^show_vip_permissions', views.show_vip_permissions, name='show_vip_permissions'),
]
