from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from unicodedata import category

from news_portal.news.models import PostCategory
from news_portal.news.views import subscribe
from utils import send_notifications

@receiver(m2m_changed, sender=PostCategory)
def notify_new_post(sender, instance, **kwargs):
    if kwargs['action']=='post_add':
        categories = isinstance.category.all()
        subscribers_email= []

        for cat in categories:
            subscribers = cat.subscribers,all()
            subscribers_email += [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers_email)