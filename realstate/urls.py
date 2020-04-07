"""realstate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from realstateapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('about/', about),
    path('property_detail/', property_detail),
    path('blog/', blog),
    path('properties/', properties),
    path('contact/', contact),
    path('registration/', registration),
    path('login/', login),
    path('adminlogin/', adminlogin),
    path('adminlogincheck/', adminlogincheck),
    path('openaddproperty/', openaddproperty),
    path('saveproperty/', saveproperty),
    path('openaddpropertycategory/', openaddpropertycategory),
    path('savepropertycategory/', savepropertycategory),
    path('agent_signup/',agent_signup),
    path('agentdata/', agentdata),
    path('make_active_agent/',make_active_agent),
    path('make_deactive_agent/',make_deactive_agent),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
