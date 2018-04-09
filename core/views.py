
from apistar import http

from core import schemas
from core import models


def list_posts():
    db_posts = models.BlogPost.objects.all()
    return [schemas.BlogPost(db_post.__dict__) for db_post in db_posts]


def post(slug: str):
    try:
        db_post = models.BlogPost.objects.get(slug=slug)
    except models.BlogPost.DoesNotExist:
        return http.Response({'message': 'Post {} does not exist.'.format(slug)}, status=404)
    return schemas.BlogPost(db_post.__dict__)
