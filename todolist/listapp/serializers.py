from rest_framework import serializers
from todolist.listapp.models import item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = ["title", "description", "status", "user"]