from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
   class Meta:
       model = Author
       fields = ['id', 'user', 'author_rating', ]


class CategoriesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Categories
       fields = ['id', 'category_name', ]


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['id', 'username', ]

class CommentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Comment
       fields = ['id', 'comment_title', 'comment_content', 'comment_author', 'comment_rating', ]

class PostSerializer(serializers.ModelSerializer):
   class Meta:
       model = Post
       fields = ['id', 'post_author', 'post_title', 'ratint_post', 'post_content',]

