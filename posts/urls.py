from rest_framework.viewsets import ModelViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render

# Главная страница
def home(request):
    return render(request, 'home.html')

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # 👇 Название раздела для Swagger
    swagger_tags = ['Posts']


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # 👇 Название раздела для Swagger
    swagger_tags = ['Comments']
