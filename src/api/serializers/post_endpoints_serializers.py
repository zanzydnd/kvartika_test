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


class CommentsForCommentsPostEndpointSerializer(serializers.ModelSerializer):
    answers = CommentsInPostSerializer(many=True, read_only=True)

    def create(self, validated_data, **kwargs):
        comment = Comment(**self.validated_data, post_id=kwargs['post_id'])
        comment.save()
        return comment

    class Meta:
        model = Comment
        fields = ['id', 'text', 'username', "answers"]
