from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_form(request):
    http_response = HttpResponse()
    return render(request, "obsah-stranky.html")

def show_about(request):
    http_response=HttpResponse()
    return render(request, "about.html")