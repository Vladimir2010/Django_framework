from django.urls import path, include
from .views import *

urlpatterns = [
    path('', send, name='send_mail')
]
