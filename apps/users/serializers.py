from rest_framework.serializers import ModelSerializer

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel

    fields = (
        'id', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_ad', 'updated_at'
    )
    read_only_fieds = (
        'id', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at', 'updated_at'
    )
    extra_kwargs = {
        'password': {
            'write_only': True
        }
    }
