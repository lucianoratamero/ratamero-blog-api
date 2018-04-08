
from apistar import Route

from core import views


routes = [
    Route('/posts/', 'GET', views.list_posts),
    Route('/post/{post_id}', 'GET', views.post)
]
