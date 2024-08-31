from django.urls import path

from . import views

urlpatterns = [
    path("", views.app, name="app"),
    path("add-expenses/", views.add_expense, name="add_expense")
]