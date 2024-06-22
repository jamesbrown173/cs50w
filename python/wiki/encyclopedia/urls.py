from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addentry", views.add_entry, name="add_entry"),
    path("<str:name>", views.show_entry, name="show_entry"),
]
