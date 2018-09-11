from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "email", "login", "first_name", "last_name")
