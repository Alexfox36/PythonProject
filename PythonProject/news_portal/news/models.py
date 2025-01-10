from django.core.cache import cache
from django.db import models
from django.urls import reverse
import datetime
from django.core.validators import MinValueValidator

# Create your models here.
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.user}'


class Categories(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')

    def __str__(self):
        return f'{self.category_name}'

class Comment(models.Model):
    comment_title  = models.CharField(max_length=255)
    comment_content = models.TextField(default="Оставьте ваш комментарий")
    comment_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment_date_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.FloatField(default=0.0)




class Post(models.Model):
    post = 'Pb'
    news = 'Nw'

    POSITIONS = [
        (post, 'Публикация'),
        (news, 'Новость')
    ]
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=POSITIONS, default=post)
    post_date_time = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_category = models.ManyToManyField(Categories, through='PostCategory')
    ratint_post = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.post_title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')

    def like(self):
        self.ratint_post += 1
        self.save()

    def dislike(self):
        self.ratint_post -= 1
        self.save()

    def preview(self):
        return self.post_content[:124] + '...'







class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
