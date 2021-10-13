from rest_framework import serializers
from .models import Profile, Post, File, Comment, Like, Follow
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id',
                  'username',
                  'firstName',
                  'lastName',
                  'picture',
                  'createdAt',
                  'updatedAt',
                  'deletedAt',
                  'isDeleted',
                  ]

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id',
                  'url',
                  'createdAt',
                  'updatedAt',
                  'deletedAt',
                  'isDeleted',
                  ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id',
                  'text',
                  'createdAt',
                  'updatedAt',
                  'deletedAt',
                  'isDeleted',
                  ]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id',
                  'createdAt',
                  'updatedAt',
                  'deletedAt',
                  'isDeleted',
                  ]

class PostSerializer(serializers.ModelSerializer):
    files = FileSerializer(source='file_set', many=True, read_only=True)
    comments = CommentSerializer(source='comment_set', many=True, read_only=True)
    likes = LikeSerializer(source='like_set', many=True, read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'caption',
            'comments',
            'files',
            'likes',
            'createdAt',
            'updatedAt',
            'deletedAt',
            'isDeleted',
        ]

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id',
                  'createdAt',
                  'updatedAt',
                  'deletedAt',
                  'isDeleted',
                  ]

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(source='profile_set', many=True, read_only=True)
    posts = PostSerializer(source='post_set', many=True, read_only=True)
    comments = CommentSerializer(source='comment_set', many=True, read_only=True)
    likes = LikeSerializer(source='like_set', many=True, read_only=True)
    follows = FollowSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id',
                  'email',
                  'password',
                  'username',
                  'profile',
                  'posts',
                  'comments',
                  'likes',
                  'follows',
                  ]

    def get_profile(self, obj):
        return obj.profile.username