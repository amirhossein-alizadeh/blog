from django.urls import path
from . import views

urlpatterns = [
    path("<int:blog_id>", views.get_blog),
    path("", views.redirect_home),
]
