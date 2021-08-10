from django.urls import path,include
from .views import home,contact,profile



app_name = 'Home'

urlpatterns = [
    path('home/',home,name='home'),
    path('contact/',contact,name='contact'),
    path('profile/',profile,name='profile'),
]

