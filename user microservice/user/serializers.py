from rest_framework import serializers

from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _

from .models import User




class UserSerializer(serializers.ModelSerializer):
    """
    Serializers class to User
    """
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
        error_messages={
            "blank": _("Password cannot be empty."),
            "min_length": _("This password is too short. It must be at least 8 characters long."),
        },
    )


    class Meta:
        model = User
        fields = (
            'id',
            'guid',
            'username',
            'password',
        )

    def create(self, validated_data):
        """
        Create user successfully
        """
        validated_data['password'] = make_password(
            validated_data.get('password'))
        auth_user = User.objects.create_user(**validated_data)
        return auth_user