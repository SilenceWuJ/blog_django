"""
应用路由
"""
from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('hello/',views.Hello),
    path('index/',views.index),
    path('detail/',views.get_detail_page),
    path('detail/<int:article_id>',views.get_detail_page),
    path('login/',views.login,name = 'login'),
    path('dologin/', views.do_login,name = 'do_login'),  # 执行登录

]