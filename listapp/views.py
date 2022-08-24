from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from listapp.serializers import ItemSerializer
from listapp.models import item

# Create your views here.
class TodoListViewSet(viewsets.ModelViewSet):
    queryset = item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset
