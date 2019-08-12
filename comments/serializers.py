from rest_framework import serializers

from comments.models import Comment
from user.serializers import UserSerializer



class CommentsSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Comment
        exclude = []