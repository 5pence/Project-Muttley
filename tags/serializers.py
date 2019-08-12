from .models import Tag
from rest_framework import serializers


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        exclude = []
