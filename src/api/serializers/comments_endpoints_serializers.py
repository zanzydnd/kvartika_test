from rest_framework import serializers

from api.models import Comment
from api.serializers import CommentsInPostSerializer


class CommentsForCommentsEndpointSerializer(serializers.ModelSerializer):
    answers = CommentsInPostSerializer(many=True, read_only=True)

    def create(self, validated_data, **kwargs):
        comment = Comment(**self.validated_data, answer_to_id=kwargs['answer_to_pk'])
        comment.save()
        return comment

    class Meta:
        model = Comment
        fields = ['id', 'text', 'username', "answers"]
