from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.models import Post, Comment
from api.serializers import PostSerializer, CommentsForCommentsEndpointSerializer, \
    CommentsForCommentsPostEndpointSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related("comments", "comments__answers", "comments__answers__answers").all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination


class CommentsNestedViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk']).prefetch_related("answers", "answers__answers",
                                                                                       "answers__answers__answers",
                                                                                       "answers__answers__answers__answers")

    pagination_class = PageNumberPagination
    serializer_class = CommentsForCommentsPostEndpointSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={"request": request})
        serializer.is_valid(raise_exception=True)
        comment = serializer.create(serializer.validated_data, post_id=kwargs['post_pk'])

        return Response({"id": comment.id, **serializer.data})


class CommentsViewSet(viewsets.GenericViewSet):
    serializer_class = CommentsForCommentsEndpointSerializer


class CommentsNestedInCommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsForCommentsEndpointSerializer

    def get_queryset(self):
        return Comment.objects.filter(answer_to_id=self.kwargs['answer_to_pk']).prefetch_related("answers",
                                                                                                 "answers__answers",
                                                                                                 "answers__answers__answers",
                                                                                                 "answers__answers__answers__answers")

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={"request": request})
        serializer.is_valid(raise_exception=True)
        comment = serializer.create(serializer.validated_data, answer_to_pk=kwargs['answer_to_pk'])

        return Response({"id": comment.id, **serializer.data})
