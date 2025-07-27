from rest_framework import serializers
from .models import Item

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'completed', 'created_at', 'updated_at')