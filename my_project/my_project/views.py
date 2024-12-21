from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, World, This is the Check process")
    return render(request, "index.html")


def about(request):
    return HttpResponse("This is the about page")
