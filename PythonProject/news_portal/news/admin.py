from django.contrib import admin

# Register your models here.
from .models import Author, Post, Comment, Categories, PostCategory

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Categories)
admin.site.register(PostCategory)