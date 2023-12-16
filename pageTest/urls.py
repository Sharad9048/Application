from django.urls import path
from pageTest import views

urlpatterns = [
    path("", views.index, name = "HomePage"),
]