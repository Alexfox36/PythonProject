
from celery import shared_task
import time
from django.core.mail import send_mail
from news.model import Categories


@shared_task
def send_m():
    for x in Categories.objects.all():
        for s in s.subscribers.all():
            send_mail(
                'Subject here',
                'Here is mesg',
                'alexph@mail.ru',
                ['s.mail'],
                fail_silently=False,
            )




