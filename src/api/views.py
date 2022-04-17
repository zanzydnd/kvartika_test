from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api.models import Post
from api.serializers import PostSerializer, CommentsInPostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related("comments", "comments__answers", "comments__answers__answers").all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
