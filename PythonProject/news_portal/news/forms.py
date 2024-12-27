from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_author',
            'post_type',
            'post_title',
            'post_content',
            'post_category',
            'ratint_post',
        ]

    def clean(self):
        cleaned_data = super().clean()
        post_content = cleaned_data.get("post_title")

        if post_content is not None and len(post_content) < 10:
            raise ValidationError({
                "post_content": "Описание не может быть менее 10 символов."
            })

        name = cleaned_data.get("post_content")
        if name is None:
            raise ValidationError(
                "Описание не может быть пустым."
            )

        return cleaned_data

