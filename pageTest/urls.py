from django.urls import path, include
from pageTest.views import index

urlpatterns = [
    path("", index, name = "HomePage"),
    path("data/", include("pageTest.api.urls")),
]