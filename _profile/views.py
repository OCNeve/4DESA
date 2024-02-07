from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import jwt
from DESA.customMessage import CustomMessage, CustomResponse
from django.contrib.auth.models import User
from django.conf import settings
from login.models import Profile
from django.views.decorators.csrf import csrf_exempt


def serialize_user(user):
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }


@csrf_exempt
def set_privacy(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Bad method")

    token = request.headers.get("token")
    privacy_choice = request.headers.get("privacy-choice")

    try:
        _id = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])["id"]
        user = User.objects.get(pk=_id)
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.is_public = bool(privacy_choice.capitalize())
        profile.save()
        return JsonResponse(CustomMessage.get("successful",
                f"profile is public setting is set to: {privacy_choice} for user with id: {user.pk}"))
    except:
        return JsonResponse(CustomMessage.get("unsuccessful","unvalid bearer token"))



def show(request):
    if request.method != "GET":
        return JsonResponse(CustomMessage.get("unsuccessful","Bad Method"))
    try:
        user_id = int(request.headers.get("user-id"))
    except:
        return JsonResponse(CustomMessage.get("unsuccessful","you must provide a user-id as a header variable"))

    try:
        user = User.objects.get(pk=user_id)
    except:
        return JsonResponse(CustomMessage.get("unsuccessful", "invalid user-id"))

    profile, _ = Profile.objects.get_or_create(user=user)
    if profile.is_public:
        return JsonResponse(CustomMessage.get("successful", None, data=serialize_user(user)), safe=False)
    else:
        return JsonResponse(CustomMessage.get("unsuccessful", "requested profile is private"))
