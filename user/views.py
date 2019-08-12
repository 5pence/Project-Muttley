from rest_framework import viewsets

from user.serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
