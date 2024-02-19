"""
URL configuration for pr2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app1.views import *
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('ChirednClass/',ChirednClass.as_   view({'get': 'list', 'post': 'create'}),name='ChirednClass'),
    path('LoginDetails/',LoginDetails,name='LoginDetails'),
    path('ProductDetails/',ProductDetails,name='ProductDetails'),
    path('OrderDetails/',OrderDetails,name='OrderDetails'),
    path('ProfileDetails/',ProfileDetails,name='ProfileDeatils'),
    # path('RatingSerializer/',RatingDetails,name='RatingDetails'),
    path('CustamerDetails/',CustamerDetails,name='CustamerDetails'),
    # path('AddCardDetails/',AddCardDetails,name='AddCardDetails'),
    path('UserDetails/', UserDetails,name=' UserDetails'),
    path('ImageDetails/',ImageDetails,name='ImageDetails'),
    # path('UserCheckDetails/',UserCheckDetails,name='UserCheckDetails')
    path('UserCheck/',UserCheckDetails,name='UserCHeck'),
    path('ProductDispalyView/',ProductDispalyView,name='ProductDispalyView'),
    path('AddCardDetails/',AddCardDetails,name='AddCardDetails')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
