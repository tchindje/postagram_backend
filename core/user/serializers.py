from core.abstract.serializers import AbstractSerializer
from core.user.models import User


class UserSerializer(AbstractSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "is_active",
            "created",
        ]
        read_only_field = ["is_active"]
