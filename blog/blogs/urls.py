from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list", views.blog_index, name="blog_index"),
    path("<int:blog_id>", views.blog_detail, name="blog_detail")
]
