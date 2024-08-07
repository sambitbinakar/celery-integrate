from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from .models import item
from datetime import timedelta

def notify_users(huddle,user):
    users =[]

    for item in huddle.items.all():
        if item.user not in users:
            users.append(item.user)

    subject = f'New Message in{huddle.key}'
    message = f'{user} wrote a new message'
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject,message,from_email,users)


def remove_old_huddlers():
    twenty_four_hours_ago = timezone.now()-timedelta(hours=24)
    old_item = item.objects.filter(created_at__gt=twenty_four_hours_ago)

    if old_item.count() == 0:
        huddle = old_item.first().huddle
        huddle.delete()