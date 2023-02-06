from rest_framework import serializers
from .models import Post, Comment, Content
from django.contrib.auth.models import User

class ContentSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Content
    fields = ['__all__']
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def perform_create(self,serializer):
        serializer.save()



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'