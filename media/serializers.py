from .models import Media
from rest_framework import serializers
from user.serializers import UserSerializer
from tags.serializers import TagsSerializer


class MediaSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    tags = TagsSerializer()

    class Meta:
        model = Media
        exclude = []
