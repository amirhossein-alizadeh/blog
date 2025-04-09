from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def get_blog(request, blog_id):
    data = {"id": blog_id, "description": "متن مقاله"}
    return render(request, "blogs/blog_view.html", context=data)


def redirect_home(request):
    return HttpResponseRedirect(reverse("home"))
