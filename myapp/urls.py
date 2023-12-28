from django.urls import path
from .views import *

urlpatterns = [
   path("",todo_list, name="todo_list"),
   path("todo_detail/<int:id>/",todo_detail, name="todo_detail"),
]