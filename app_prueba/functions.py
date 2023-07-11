from ariadne import convert_kwargs_to_snake_case

from .models import Post

def listPosts_resolver(obj, info):
    try:
        posts = [post for post in Post.objects.all()]
        payload = {
            "success": True,
            "posts": posts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        post = Post.objects.get(id=id)
        payload = {
            "success": True,
            "post": post
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Post item matching {id} not found"]
        }
    return payload
