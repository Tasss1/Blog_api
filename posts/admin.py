# posts/admin.py
from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'likes_count')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content')
    filter_horizontal = ('likes',)
    readonly_fields = ('created_at', 'updated_at')

    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = 'Likes'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('text',)
    raw_id_fields = ('post',)
    readonly_fields = ('created_at',)