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
    path('openaddpropertyimages/', openaddpropertyimages),
    path('savepropertyimages/', savepropertyimages),
    path('error/', error),
    path('agentdata/', agentdata),
    path('make_active_agent/',make_active_agent),
    path('make_deactive_agent/',make_deactive_agent),
    path('openpropertycategory/',openpropertycategory),
    path('openmyaccount/',openmyaccount),
    path('propertypaginator/',propertypaginator)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
