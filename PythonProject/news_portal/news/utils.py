from allauth.account.utils import user_username
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from news_portal.news_portal import settings


def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',{
            'username':user_username,
            'text':preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject= title,
        body='',
        from_email= settings.DEFAULT_FROM_EMAIL,
        to= subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()