from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
import jwt
from django.contrib.auth.models import User
from DESA.customMessage import CustomMessage, CustomResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

@csrf_exempt
def register(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Bad method")

    if User.objects.filter(Q(email=request.headers.get("email")) |
                    Q(username=request.headers.get("username"))).exists():
        return JsonResponse(CustomMessage.get("unsucessful", "username or email already in use"))


    user = User.objects.create(
        username=request.headers.get("username"),
        password=request.headers.get("password"),
        email=request.headers.get("email")
    )
    return JsonResponse(CustomResponse.get(jwt.encode({"id": user.pk}, settings.SECRET_KEY, algorithm="HS256")))