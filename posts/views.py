from django.shortcuts import render
from django.contrib.auth.models import User
from DESA.customMessage import CustomMessage
from django.http import JsonResponse
from login.models import Profile, Posts, Comments, Images, Videos
import jwt
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from storage_account_access.saa import SAA
import os


def get_posts_data(user):
    user_data = {"user_id": user.id, "posts": []}

    user_posts = Posts.objects.filter(creator=user)

    for post in user_posts:
        post_data = {
            "date": post.date.strftime("%Y-%m-%d"),
            "images": [],
            "videos": [],
            "comments": []
        }
        post_images = Images.objects.filter(post_id=post)
        for image in post_images:
            post_data["images"].append({"path": image.path})

        # Gather videos related to the post
        post_videos = Videos.objects.filter(post_id=post)
        for video in post_videos:
            post_data["videos"].append({"path": video.path})

        # Gather comments related to the post
        post_comments = Comments.objects.filter(post=post)
        for comment in post_comments:
            post_data["comments"].append({
                "date": comment.date.strftime("%Y-%m-%d"),
                "value": comment.value
            })

        user_data["posts"].append(post_data)

    return user_data


@csrf_exempt
def see_posts(request):
    if request.method != "GET":
        return JsonResponse(CustomMessage.get("unsuccessful", "Bad Method"))
    try:
        user_id = int(request.headers.get("user-id"))
    except:
        return JsonResponse(CustomMessage.get("unsuccessful", "you must provide a user-id as a header variable"))

    try:
        user = User.objects.get(pk=user_id)
    except:
        return JsonResponse(CustomMessage.get("unsuccessful", "invalid user-id"))

    profile, _ = Profile.objects.get_or_create(user=user)
    if profile.is_public:
        data = get_posts_data(user)
        return JsonResponse(CustomMessage.get("successful", None, data=data), safe=False)
    else:
        return JsonResponse(CustomMessage.get("unsuccessful", "requested profile is private"))


@csrf_exempt
def delete_posts(request):
    if request.method != "DELETE":
        return JsonResponse(CustomMessage.get("unsuccessful", "Bad Method"))
    try:
        post_id = int(request.headers.get("post-id"))
    except:
        return JsonResponse(CustomMessage.get("unsuccessful", "you must provide a user-id as a header variable"))
    try:
        user_id = int(request.headers.get("user-id"))
    except:
        return JsonResponse(CustomMessage.get("unsuccessful", "you must provide a user-id as a header variable"))
    try:
        user = User.objects.get(pk=user_id)
    except:
        return JsonResponse(CustomMessage.get("unsuccessful", "invalid user-id"))

    try:
        post = Posts.objects.get(pk=post_id)
    except:
        return JsonResponse(CustomMessage.get("unsuccessful", "invalid post-id"))

    if post.creator == user:
        post.delete()
        return JsonResponse(CustomMessage.get("successful", None))
    else:
        return JsonResponse(CustomMessage.get("unsuccessful", "you can't delete a post that does not belong to you"))

@csrf_exempt
def add_posts(request):
    if request.method != "POST":
        return JsonResponse({"error": "Bad Method"}, status=405)

    try:
        token = request.headers.get("token")
        _id = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])["id"]
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=401)

    try:
        user = User.objects.get(pk=_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    try:
        date = datetime.now()

        try:
            with open(str(request.FILES['video'].name), "wb") as video_file:
                for chunk in request.FILES['video'].chunks():
                    video_file.write(chunk)

            with open(str(request.FILES['image'].name), "wb") as image_file:
                for chunk in request.FILES['image'].chunks():
                    image_file.write(chunk)

            saa = SAA()
            video_url = saa.uploadFile(str(request.FILES['video']), user.username)
            image_url = saa.uploadFile(str(request.FILES['image']), user.username)

            os.remove(str(request.FILES['video'].name))
            os.remove(str(request.FILES['image'].name))

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

        post_text = request.headers.get("post-text")
        post = Posts.objects.create(creator=user, date=date, text=post_text)
        image = Images.objects.create(post=post, path=video_url)
        video = Videos.objects.create(post=post, path=image_url)
        post.save()
        image.save()
        video.save()

        return JsonResponse({"success": f"Post added successfully with id: {post.pk}"}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def add_comment(request):

    if request.method != "POST":
        return JsonResponse(CustomMessage.get("unsuccessful", "Bad Method"))
    try:
        token = request.headers.get("token")
    except:
        return JsonResponse(CustomMessage.get("unsuccessful", "you must provide a token as a header variable"))

    try:
        _id = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])["id"]
    except:
        return JsonResponse(CustomMessage.get("unsuccessful", "invalid token"))

    profile, _ = Profile.objects.get_or_create(user=user)
    if profile.is_public:

        return JsonResponse(CustomMessage.get("successful", None, data=data), safe=False)
    else:
        return JsonResponse(CustomMessage.get("unsuccessful", "requested profile is private"))
