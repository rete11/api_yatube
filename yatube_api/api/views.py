from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import AuthorPermission
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление в виде набора представлений(ModelViewSet),
    предназначенное только для чтения, для модели Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Представление в виде набора представлений(ModelViewSet)
    для модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, AuthorPermission)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Представление в виде набора представлений(ModelViewSet)
    для модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, AuthorPermission)

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get("post_id"))

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()
