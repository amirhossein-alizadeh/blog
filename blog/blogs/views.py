from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def get_blog(request, blog_id):
    return HttpResponse(blog_id)


def redirect_home(request):
    return HttpResponseRedirect(reverse("home"))
