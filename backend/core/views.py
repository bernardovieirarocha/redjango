from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions,authentication
from .serializers import *
from .models import *

class ListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Lists to be viewed or edited.
    """
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


