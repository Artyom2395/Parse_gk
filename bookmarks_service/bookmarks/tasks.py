import requests

from django.core.files.base import ContentFile
from huey.contrib.djhuey import db_task
from .models import Bookmark
from django.contrib.auth.models import User
from bookmarks.parser import parse_link



@db_task()
def parse_and_save_link(url, user_id):
    user = User.objects.get(id=user_id)
    title, description, favicon = parse_link(url)
    bookmark = Bookmark(user=user, url=url, title=title, description=description)
    if favicon:  # Если favicon доступен
        
        response = requests.get(favicon)
        if response.status_code == 200:
            bookmark.favicon.save(f'{title}.ico', ContentFile(response.content), save=False)
    bookmark.save()