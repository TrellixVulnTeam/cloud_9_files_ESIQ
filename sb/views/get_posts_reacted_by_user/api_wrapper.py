from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from django.http import HttpResponse
from fb_post.utils import get_posts_reacted_by_user

from raven.utils import json

from django_swagger_utils.drf_server.exceptions import BadRequest

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    print()
    user = kwargs['user']
    print('user_id', user.id)
    print(kwargs)
    post_ids_list = get_posts_reacted_by_user(
            user_id=user.id
            )
    response = HttpResponse(post_ids_list,status=200)
    return response