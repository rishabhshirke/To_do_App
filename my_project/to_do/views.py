from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.
# def create_task(request):
#     return render(request, "create.html")


class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoCreate(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDelete(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
