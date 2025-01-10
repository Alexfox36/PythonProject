from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Author
       fields = ['id', 'name', 'author_rating', ]


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Categories
       fields = ['id', 'category_name', ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = User
       fields = ['id', 'name', ]

class CommentSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Comment
       fields = ['id', 'name', 'comment_title', 'comment_content', 'comment_author', 'comment_rating', ]

class PostSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Post
       fields = ['id', 'post_author', 'post_title', 'ratint_post', 'post_content',]

