from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema  # 👈 добавлено

@extend_schema(tags=['Posts'])  # 👈 Название для Swagger
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').prefetch_related('comments', 'likes')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        if request.user in post.likes.all():
            return Response({'status': 'already liked'}, status=400)
        post.likes.add(request.user)
        return Response({'status': 'post liked'})

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        if request.user not in post.likes.all():
            return Response({'status': 'not liked yet'}, status=400)
        post.likes.remove(request.user)
        return Response({'status': 'post unliked'})


@extend_schema(tags=['Comments'])  # 👈 Название для Swagger
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs.get('post_pk')).select_related('author')

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs.get('post_pk')
        )
