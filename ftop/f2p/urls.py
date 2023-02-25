from django.urls import path
from . import views

urlpatterns = [
    path("Form", views.index, name = "form"),
    path("card", views.card, name="card")
]