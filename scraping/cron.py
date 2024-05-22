from django.core.mail import send_mail
from .models import Subscriber

def send_weekly_email():
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        send_mail(
            'Weekly Update from Rohit Ojha',
            'Hi, this email is coming from Django as a weekly update.',
            'rohitojha9720@gmail.com',
            [subscriber.email],
            fail_silently=False
        )