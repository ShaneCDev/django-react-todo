from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import TodoItemSerializer


# Create your views here.

class TodoItemView(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset = Item.objects.all()