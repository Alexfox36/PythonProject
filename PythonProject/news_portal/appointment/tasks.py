
from celery import shared_task
from django.core.mail import send_mail

from news.models import Categories


@shared_task
def send_m():
    for c in Categories.objects.all():
        for s in c.subscribers.all():
            send_mail(
                'Subject here',
                'Here is mesg',
                'alexph@mail.ru',
                [s.email],
                fail_silently=False,
            )




