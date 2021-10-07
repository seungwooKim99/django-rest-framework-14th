from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    picture = models.CharField(max_length=200)
    createdAt = models.DateTimeField('createdAt')
    updatedAt = models.DateTimeField('updatedAt')

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    createdAt = models.DateTimeField('createdAt')
    updatedAt = models.DateTimeField('updatedAt')

    def __str__(self):
        return 'post_' + str(self.id)

class File(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)
    createdAt = models.DateTimeField('createdAt')
    updatedAt = models.DateTimeField('updatedAt')

    def __str__(self):
        return 'file_' + str(self.id)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    createdAt = models.DateTimeField('createdAt')
    updatedAt = models.DateTimeField('updatedAt')

    def __str__(self):
        return 'comment_' + str(self.id)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField('createdAt')
    updatedAt = models.DateTimeField('updatedAt')

    def __str__(self):
        return 'like_' + str(self.id)

class Follow(models.Model):
    follower_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    followee_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField('createdAt')
    updatedAt = models.DateTimeField('updatedAt')

    def __str__(self):
        return 'follow_' + str(self.id)