# from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer
from .models import UserInformation


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            "Endpoint": "/api",
            "method": "GET",
            "description": "authentication",
        },
    ]
    return Response(routes)


# url: http://127.0.0.1:8000/info/
# {
#     method: 'GET',
#     headers:{
#         'Content-Type':'application/json',
#         'Authorization':'Bearer ' + access_token
#     }
# }


@api_view(["GET"])
@permission_classes(
    [
        IsAuthenticated,
    ]
)
def getUserInfo(request):
    user = request.user
    userInfo = user.user_information
    serializer = UserSerializer(userInfo, many=False)
    return Response(serializer.data)
