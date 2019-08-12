from rest_framework import viewsets

from tags.serializers import TagsSerializer
from .models import Tag


class TagsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing media instances.
    """
    serializer_class = TagsSerializer
    queryset = Tag.objects.all()
