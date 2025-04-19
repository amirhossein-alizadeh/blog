from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import date


all_posts = [
    {
        "id": "1",
        "title": "سلام",
        "author": "amirhossein",
        "image": "author-1.png",
        "date": date(2024, 5, 3),
        "short_description": "سلام بر تستر عزیز",
        "content": """
            asdfghjk,lkjhggredwfgtyukio;likhgfvdsftr56uik,hngvfdet5yuihjmnvc
            xfrt5u7ujkhmnvc xdfgtyujhmnvc xdergtyujmhnvbcfdrtyukjhmnvbcdfrgtyu67ilkjhmngvc       
            xzdcfghyujkmnvbcdsaSERTYJHG
        """
    },
    {
        "id": "2",
        "title": "احوال پرسی",
        "author": "amirhossein",
        "image": "author-2.png",
        "date": date(2024, 6, 3),
        "short_description": "حالت چطوره",
        "content": """
            asdfghjk,lkjhggredwfgtyukio;likhgfvdsftr56uik,hngvfdet5yuihjmnvc
            xfrt5u7ujkhmnvc xdfgtyujhmnvc xdergtyujmhnvbcfdrtyukjhmnvbcdfrgtyu67ilkjhmngvc       
            xzdcfghyujkmnvbcdsaSERTYJHG
        """
    },
    {
        "id": "3",
        "title": "شعار",
        "author": "amirhossein",
        "image": "author-3.png",
        "date": date(2024, 6, 5),
        "short_description": "هیهات من الذله",
        "content": """
            asdfghjk,lkjhggredwfgtyukio;likhgfvdsftr56uik,hngvfdet5yuihjmnvc
            xfrt5u7ujkhmnvc xdfgtyujhmnvc xdergtyujmhnvbcfdrtyukjhmnvbcdfrgtyu67ilkjhmngvc       
            xzdcfghyujkmnvbcdsaSERTYJHG
        """
    }

]


# Create your views here.
def get_date(post):
    return post["date"]


def home(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:]
    
    return render(request, "blogs/index.html", context={
        "latest_posts": latest_posts
    })

def blog_index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    return render(request, "blogs/list_blogs.html", context={
        "posts": sorted_posts
    })


def blog_detail(request, blog_id):
    context = all_posts[blog_id]
    return render(request, "blogs/blog_detail.html", context={
        "blog": context
    })
