"""moveing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,re_path,include
from moves import views
from django.views.static import serve

urlpatterns = [
    path('login/',views.login),   #登录
    path('index/',views.index),#首页

    # 上传图片显示的url，settings有配置template，media
    # 之前写在user的url里面，和现在路径一致但是不显示图片，估计是因为r'^media/(?P<path>.*)$'是包含在user后的
    # media其实和user和cms是在同一个项目文件夹下，属于同级了，下次写文件存放路径时务必注意
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": 'C:/Users/admin/PycharmProjects/moveing/media/'}),

    path('are/', views.AreList, name='AreList'),  # 地区展示

    path('cate/', views.CateList, name='CateList'),  # 类型展示

    path('add_res/', views.addRes, name='addRes'),  # 资源添加--获取新页面
    path('update_res/', views.updateRes, name='updateRes'),  # 资源添加--上传

    path('file_u/', views.fileU, name='fileU'),  #上传文件的页面--都可以上传

    path('moves/', views.MoveList, name='MoveList'),  # 资源展示
    path('detail_move/', views.detailMove, name='detailMove'),  # 资源详情

]
