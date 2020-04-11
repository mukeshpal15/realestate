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
    path('agent_forgot_pass/', agent_forgot_pass),
    path('password_send_to_agent/',password_send_to_agent),
    path('openaddpropertyimages/', openaddpropertyimages),
    path('savepropertyimages/', savepropertyimages),
    path('error/', error),
    path('agentdata/', agentdata),
    path('make_active_agent/',make_active_agent),
    path('make_deactive_agent/',make_deactive_agent),
    path('openpropertycategory/',openpropertycategory),
    path('openmyaccount/',openmyaccount),
    path('propertypaginator/',propertypaginator),
    path('user_signup/',user_signup),
    path('userregistation/', userregistation),
    path('loginformuser/', loginformuser),
    path('user_login/',user_login),
    path('user_forgot_pass/', user_forgot_pass),
    path('password_send_to_user/', password_send_to_user),
    path('send_mail_by_contact/', send_mail_by_contact),
    path('Log/', Log),
    path('openmyaccount/',openmyaccount),
    path('dele/',dele),
    path('openproperty/', openproperty),
    path('openchangeaccountdetails/',openchangeaccountdetails)

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
