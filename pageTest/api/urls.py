from django.urls import path
from pageTest.api.views import InventoryManager

urlpatterns = [
    path("inventory/", InventoryManager.as_view(), name = "get_all_inventiry"),
    path("inventory/add/", InventoryManager.as_view(), name = "put_inventory")
]