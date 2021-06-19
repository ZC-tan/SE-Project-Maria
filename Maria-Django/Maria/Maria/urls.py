"""Maria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from entity.views import *

urlpatterns = [
    #基本
    path('',home,name='home'),
    #注册，登录，个人信息
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('modify_user_info/',modify_user_info,name='modify_user_info'),
    path('show_user_info/',show_user_info,name='show_user_info'),
    #文档
    path('mydocs/',my_docslist,name='my_docslist'),
    path('createdoc/',create_doc,name='createdoc'),
    path('editdoc/',edit_doc,name='editdoc'),
    path('recycledoc/',recycle_doc,name='recycledoc'),
    path('show_recycled_doc/',show_recycled_doc,name='show_recycled_doc'),
    path('del_recycled_doc/',del_recycled_doc,name='del_recycled_doc'),
    path('restore_recycled_doc/',restore_recycled_doc,name='restore_recycled_doc'),
    #团队
    path('invite_to_group/',invite_to_group,name='invite_to_group'),
    path('kick_group_member/',kick_group_member,name='kick_group_member'),
    path('creategroup/',creategroup,name='creategroup'),
    path('mygroup/',mygroup,name='mygroup'),
    path('show_group_info/',show_group_info,name='show_group_info'),
    path('show_group_member/',show_group_member,name='show_group_member'),
    path('show_group_info/show_group_doc/',show_group_doc,name='show_group_doc'),
    path('create_group_doc/',create_group_doc,name='create_group_doc'),
    path('edit_group_doc/',edit_group_doc,name='edit_group_doc'),
    #邀请
    path('myinvitations/',myinvitations,name='myinvitations'),
    path('accept_invites/',accept_invites,name='accept_invites'),
    path('decline_invites/',decline_invites,name='decline_invites'),
    #admin
    path('admin/', admin.site.urls),
]

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', TemplateView.as_view(template_name="index.html")),
#     url(r'^api/', include('backend.urls', namespace='api'))
# ]
