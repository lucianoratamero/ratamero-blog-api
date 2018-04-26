
from apistar import http
from django.core.paginator import Paginator, EmptyPage

from core import schemas
from core import models


def list_posts(page: http.QueryParam):
    db_posts = models.BlogPost.objects.all()
    page_count = 1
    if page:
        paginator = Paginator(db_posts, 5)
        page_count = paginator.count
        try:
            db_posts = paginator.page(int(page))
        except EmptyPage:
            db_posts = []
    return {
        'page_count': page_count,
        'posts': [schemas.BlogPost(db_post.__dict__) for db_post in db_posts]
    }


def post(slug: str):
    try:
        db_post = models.BlogPost.objects.get(slug=slug)
    except models.BlogPost.DoesNotExist:
        return http.Response({'message': 'Post {} does not exist.'.format(slug)}, status=404)
    return schemas.BlogPost(db_post.__dict__)
