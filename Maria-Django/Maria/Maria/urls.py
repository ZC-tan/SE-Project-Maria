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
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('modify_user_info/',modify_user_info,name='modify_user_info'),
    path('show_user_info/',show_user_info,name='show_user_info'),
    path('mydocs/',my_docslist,name='my_docslist'),
    path('createdoc/',create_doc,name='createdoc'),
    path('editdoc/',edit_doc,name='editdoc'),
    path('admin/', admin.site.urls),
]
