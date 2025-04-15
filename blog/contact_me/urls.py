from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.contact_me, name='contact_me'),
]