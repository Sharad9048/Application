from rest_framework.response import Response
from pageTest.models import Inventory
from pageTest.api.serializers import InventorySerializer
from rest_framework.views import APIView

class InventoryManager(APIView):
    def get(self, request):
        """
        @input : request
        @output : JSON response
        You will get all the inventory data in JSON format.
        """
        print(request.data)
        inventory = Inventory.objects.all() # filter(userid = request.data["filter"]["userid"])
        inventorySerial = InventorySerializer(inventory, many = True)
        return Response(inventorySerial.data)
    def put(self, request):
        """
        @input : request
        @output : JSON response
        It will accept list of dictionary data and store them into the inventory table
        """
        inventorySerial = InventorySerializer(data=request.data, many=True)
        if inventorySerial.is_valid():
            inventorySerial.save()
            return Response(inventorySerial.data)
        else:
            return Response(inventorySerial.errors)
    def post(self, request):
        """
        @input : request
        @output : JSON response
        It will accept dictionary data and store it into the inventory table.
        """
        print(request.data)
        inventorySerial = InventorySerializer(data=request.data)
        if inventorySerial.is_valid():
            inventorySerial.save()
            return Response(inventorySerial.data)
        else:
            return Response(inventorySerial.errors)
        
    def patch(self, request):
        """
        @input : request
        @output : JSON response
        It will accept data to update the inventory
        """
        pass