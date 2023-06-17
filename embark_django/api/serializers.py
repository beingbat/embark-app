from rest_framework.serializers import ModelSerializer

from .models import UserInformation


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserInformation
        fields = "__all__"
