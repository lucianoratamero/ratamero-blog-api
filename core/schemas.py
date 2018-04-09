from apistar import typesystem

from core import typesystem as core_typesystem


class BlogPost(core_typesystem.Object):
    properties = {
        'title': typesystem.String,
        'tags': typesystem.String,
        'slug': typesystem.String,
        'pub_date': typesystem.String,
        'body': typesystem.String,
        'summary': typesystem.String,
        'cover_image_url': typesystem.String,
    }
