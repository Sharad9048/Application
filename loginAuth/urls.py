from django.urls import path
from loginAuth.views import index
urlpatterns = [
    path("", index, name = "User Login"),
]