from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import ItemSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Item
# Create your views here.
class create(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ItemSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class delete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        item = get_object_or_404(Item, pk=id)
        if request.user == item.author:
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)

class update(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, id):
        item = get_object_or_404(Item, pk=id)
        if request.user == item.author:
            serializer = ItemSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
