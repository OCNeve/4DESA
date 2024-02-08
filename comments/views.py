from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from login.models import User, Comments, Posts
import jwt
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_comment(request):
    if request.method != "POST":
        return JsonResponse({"error": "Bad Method"}, status=405)

    try:
        token = request.headers.get("token")
        post_id = request.headers.get("post-id")
        text = request.headers.get("value")
        _id = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])["id"]
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=401)

    try:
        user = User.objects.get(pk=_id)
        post = Posts.objects.get(pk=post_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    try:
        date = datetime.now()
        comment = Comments(post=post, value=text, date=date)
        comment.save()

        return JsonResponse({"success": f"Comment added successfully with id: {comment.pk}"}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def remove_comment(request):
    pass

def edit_comment(request):
    pass
