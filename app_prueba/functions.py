from ariadne import convert_kwargs_to_snake_case
from datetime import date

from .models import Post, TipoPost

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


@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, title, description, tipo_post_id):
    try:
        today = date.today()
        tipo_post = TipoPost.objects.get(id=tipo_post_id)
        post = Post(
            title=title, 
            description=description, 
            create_at=today.strftime("%d-%m-%Y"),
            tipo_post_id = tipo_post
        )
        post.save()
        payload = {
            "success": True,
            "post": post
        }
    except Exception as e:  # date format errors
        print(e)
        payload = {
            "success": False,
            "errors": [f"{e}"]
        }
    return payload

@convert_kwargs_to_snake_case
def update_post_resolver(obj, info, id, title, description):
    try:
        post = Post.objects.get(id=id)
        if post:
            post.title = title
            post.description = description
        post.save()
        payload = {
            "success": True,
            "post": post
        }
    except Exception as e:  # todo not found
        payload = {
            "success": False,
            "errors": [f"{e}"]
        }
    return payload

@convert_kwargs_to_snake_case
def delete_post_resolver(obj, info, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        payload = {"success": True, "post": post}
    except Exception as e:
        payload = {
            "success": False,
            "errors": [f"{e}"]
        }
    return payload
