from rest_framework import serializers

from api.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text']
        read_only_fields = ['id']
