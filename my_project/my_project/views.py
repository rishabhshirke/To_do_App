from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("This is the First Api write create/ or delete/ or api/")
    # return render(request, "index.html")


def about(request):
    return HttpResponse("This is the about page")
