from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.


def contact(request):
    content = render_to_string("contact/index.html")
    return HttpResponse(content)
