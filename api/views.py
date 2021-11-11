from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Profile, Post, Follow, File, Comment, Like
from .serializers import UserSerializer, ProfileSerializer, PostSerializer, FollowSerializer, FileSerializer, CommentSerializer, LikeSerializer

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            #serializer.save()
            print(serializer.data)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class PostDetail(APIView):
    def get(self, request, id, format=None):
        post = Post.objects.filter(id=id)
        serializer = PostSerializer(post, many=True)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        post = Post.objects.filter(id=id)
        post.delete()
        return Response({"message: delete success"},)



"""
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
"""