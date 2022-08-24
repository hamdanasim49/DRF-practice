from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from todolist.listapp.serializers import ItemSerializer
from todolist.listapp.models import item

# Create your views here.
class TodoListViewSet(viewsets.ModelViewSet):
    queryset = item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]