from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addentry", views.add_entry, name="add_entry"),
    path("edit/<str:name>", views.edit, name="edit_entry"),
    path("random", views.random, name="random"),
    path("<str:name>", views.show_entry, name="show_entry"),
]
