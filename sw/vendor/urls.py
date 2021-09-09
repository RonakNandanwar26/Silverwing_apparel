from django.urls import path
from .views import register,please_verify,confirm_email,home,login

app_name= 'Vendor'

urlpatterns = [
    path('register/',register,name='register'),
    path('please_verify/',please_verify,name='please_verify'),
    path('confirm_email/',confirm_email,name='confirm_emails'),
    path('home/',home,name='home'),
    path('login/',login,name='login'),
]
