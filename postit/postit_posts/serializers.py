from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source="post.id")
    
    class Meta:
        model = models.Comments
        fields = ('id', 'post', 'content', 'user', 'user_id', 'created_at', 'updated_at',)


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comments = CommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return models.Comments.objects.filter(post=obj).count()

    class Meta:
        model = models.Post
        fields = ('id', 'title', 'content', 'comments', 'comment_count', 'user', 'user_id', 'created_at', 'updated_at',)
