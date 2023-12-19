from django.urls import path
from pageTest.api.views import InventoryManager, UserData

urlpatterns = [
    path("inventory/", InventoryManager.as_view(), name = "get_all_inventiry"),
    path("inventory/add/", InventoryManager.as_view(), name = "put_inventory"),
    path("user/", UserData.as_view(), name = "users")
]