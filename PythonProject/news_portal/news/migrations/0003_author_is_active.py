# Generated by Django 5.1.4 on 2025-01-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_categories_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
