# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from blog.models import Post, Tag, Comment
from .serializers import PostSerializer, CommentSerializer


class PostListView(generics.ListCreateAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
