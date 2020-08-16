"""hack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from firstapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    # url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^principal_register/$',views.principal_register,name='principal_register'),
    url(r'^teacher_register/$',views.teacher_register,name='teacher_register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^form/$',views.forma,name='form'),
    url(r'^vis/$',views.vis,name='vis'),
]