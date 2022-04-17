from rest_framework import serializers

from api.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'username']


class CommentInCommentSerializer(serializers.ModelSerializer):
    answers = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'username', 'answers']


class CommentsInPostSerializer(serializers.ModelSerializer):
    answers = CommentInCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'username', "answers"]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentsInPostSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'comments']
        read_only_fields = ['id', 'comments']
