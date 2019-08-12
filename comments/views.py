from rest_framework import viewsets

from comments.serializers import CommentsSerializer
from .models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comment instances.
    """
    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()
