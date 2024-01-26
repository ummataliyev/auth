"""
custom login method
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom token obtain pair view to generate tokens with additional claims.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user

        refresh = RefreshToken.for_user(user)

        response_data = {
            'token': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            },
            'user_id': user.id,
            'username': user.username,
            'phone_number': user.phone_number,
        }

        return Response(response_data, status=status.HTTP_200_OK)
