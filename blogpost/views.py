import django_filters

from rest_flex_fields import FlexFieldsModelViewSet

from blogpost.serializers import BlogPostSerializer
from .models import BlogPost


class BlogPostViewSet(FlexFieldsModelViewSet):
    """
    A viewset for viewing and editing blog post instances.
    """
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
    permit_list_expands = ['category', 'user']
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['category', 'tags', 'user']
