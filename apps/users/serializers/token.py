"""
customizing token claims
"""
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# pylint: disable=W0223
class ObtainPairSerializer(TokenObtainPairSerializer):
    """
    the custom optain serializer.
    """
    code = serializers.IntegerField()
    password = serializers.IntegerField(allow_null=True)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username

        return token
