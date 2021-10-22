from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('price/', price, name='price'),
    path('about/', about, name='about'),
    path('team/', xodim, name='team'),
    path('qaror/', qaror, name='qaror'),
    path('xujjat/', document, name='document'),
    path('tuzilma/', tuzilma, name='tuzilma'),
    path('farmon/', farmon, name='farmon'),
    path('service/', service, name='service'),
    path('<int:pk>/', price_plan, name='price_plan'),
    path('contact/', contact, name='contact')
]
