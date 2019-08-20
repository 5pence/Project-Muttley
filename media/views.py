from rest_framework import viewsets

from media.serializers import MediaSerializer
from .models import Media


class MediaViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing media instances.
    """
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
