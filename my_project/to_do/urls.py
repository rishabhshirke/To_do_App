from django.urls import path
from .views import *


# urlpatterns = [
#     path("", views.create_task, name="create"),
# ]

urlpatterns = [
    path("", TodoList.as_view()),
    path("<int:pk>/", TodoDetail.as_view()),
    path("create", TodoCreate.as_view()),
    path("delete/<int:pk>", TodoDelete.as_view()),
]
