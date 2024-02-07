from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
import jwt
from django.contrib.auth.models import User
from DESA.customMessage import CustomMessage, CustomResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Bad method")

    username = request.headers.get("username")
    password = request.headers.get("password")

    try:
        user = User.objects.get(username=username, password=password)
    except:
        return JsonResponse(CustomMessage.get("unsucessful", "username and password do not match"))

    return JsonResponse(CustomResponse.get(jwt.encode({"id": user.pk}, settings.SECRET_KEY, algorithm="HS256")))