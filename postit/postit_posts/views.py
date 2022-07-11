from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from . import models, serializers


# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def put(self, request, *args, **kwargs):
        post = models.Post.objects.filter(pk=kwargs['pk'], user=request.user)
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_("you cant edit a post that is no yours!!!"))

    def delete(self, request, *args, **kwargs):
        post = models.Post.objects.filter(pk=kwargs['pk'], user=request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_("you cant delete a post that is no yours!!!"))



class CommentList(generics.ListCreateAPIView):
    # queryset = models.Comments.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        post = models.Post.objects.get(pk=self.kwargs['pk'])
        return models.Comments.objects.filter(post=post)

    def perform_create(self, serializer):
        post = models.Post.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, post=post)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.Post.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def put(self, request, *args, **kwargs):
        post = models.Comments.objects.filter(pk=kwargs['pk'], user=request.user)
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_("you cant edit a comment that is no yours!!!"))

    def delete(self, request, *args, **kwargs):
        post = models.Comments.objects.filter(pk=kwargs['pk'], user=request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_("you cant delete a comment that is no yours!!!"))

