from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions,authentication
from .serializers import *
from .models import *

class ListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Lists to be viewed or edited.
    """
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        return List.objects.filter(owner=user)

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Items to be viewed or edited.
    """
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(list__owner=user)



