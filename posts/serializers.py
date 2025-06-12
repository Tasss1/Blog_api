# posts/serializers.py
from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at']
        read_only_fields = ['author']


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'likes_count', 'comments', 'created_at', 'updated_at']

    def get_likes_count(self, obj):
        return obj.likes.count()