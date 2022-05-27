from datetime import timedelta, date
from .models import Post
from celery import shared_task

# Не смог сделать рассылку в модуле D6, тут только заглушки


def get_subscribers(category):
    pass


def send_emails(*args, **kwargs):
    pass


@shared_task
def weekly_digest():
    week = timedelta(days=7)
    posts = Post.objects.all()
    past_week_posts = []

    for post in posts:
        time_delta = date.today() - post.dateCreation.date()
        if time_delta < week:
            past_week_posts.append(post)
