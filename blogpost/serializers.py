from blogpost.models import BlogPost
from rest_framework import serializers
from user.serializers import UserSerializer
from category.serializers import CategorySerializer
from comments.serializers import CommentsSerializer
from tags.serializers import TagsSerializer

from rest_flex_fields import FlexFieldsModelSerializer


class BlogPostSerializer(FlexFieldsModelSerializer):
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = BlogPost
        exclude = []

    expandable_fields = {
        'category': (CategorySerializer, {}),
        'comments': (CommentsSerializer, {'many': True, 'source': 'comment_set'}),
        'tags': (TagsSerializer, {'many': True}),
        'user': (UserSerializer, {})
    }
