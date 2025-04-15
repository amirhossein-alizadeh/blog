from django.shortcuts import render

# Create your views here.

def contact_me(request):
    return render(request, "contact_me/contact_main.html")
