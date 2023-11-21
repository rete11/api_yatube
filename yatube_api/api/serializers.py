from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    """Данный класс используется для сериализации
    и десериализации объектов модели Post."""

    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Данный класс используется для сериализации
    и десериализации объектов модели Group."""

    class Meta:
        fields = "__all__"
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    """Данный класс используется для сериализации
    и десериализации объектов модели Comment."""

    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        fields = "__all__"
        model = Comment
        read_only_fields = ("post",)
