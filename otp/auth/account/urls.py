from django.urls import path,include, re_path
from django.conf.urls import url
from .views import ValidatePhoneSendOTP
app_name='account'
urlpatterns=[
    re_path(r'^validate_phone/',ValidatePhoneSendOTP.as_view()),
]