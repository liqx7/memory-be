from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from rest_framework import viewsets
from .serializers import ItemSerializer

# Create your views here.


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Item.objects.all().order_by("-create_time__joined")
    serializer_class = ItemSerializer

