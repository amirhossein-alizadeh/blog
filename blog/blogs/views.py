from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


blogs = {
    1: "سلام بر تستر عزیز",
    2: "حالت چطوره ",
    3: "هیهات من الذله",
    4: "حال من امروز بهتر از این نمیشه",
    5: "یادت نره این سایت روزی قراره همه ببیننش",
    6: "ستاره آی ستاره",
    733: None,
}


# Create your views here.



def home(request):
    return render(request, "blogs/index.html")

def blog_index(request):
    blogs_list = list(blogs.keys())
    data = {"blogs": blogs_list}
    return render(request, "blogs/list_blogs.html", data)


def get_blog(request, blog_id):
    description = blogs[blog_id]
    data = {"id": blog_id, "description": description}
    return render(request, "blogs/blog_view.html", context=data)
