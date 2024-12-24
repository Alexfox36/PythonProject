import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal.settings')

app = Celery('news_portal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'mail_send':{
        'task': 'appointment.tasks.send_mail',
        'schedule': crontab(day_of_week='1'),
    },
}

app.autodiscover_tasks()