from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def contact(request):
    return HttpResponse("""
                        Amirhossein Alizadeh
                        email: amirhosseinalizadeh992@gmail.com
                        phone: (+98) 9927063067""")
