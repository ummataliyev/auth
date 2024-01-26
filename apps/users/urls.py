"""
the users-app url patterns
"""
from django.urls import path
from rest_framework_simplejwt import views

from apps.users.views import CustomTokenObtainPairView


urlpatterns = [
    path(
        route="token/get",
        view=views.TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        route="token/refresh",
        view=views.TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    path(
        route="token/verify",
        view=views.TokenVerifyView.as_view(),
        name="token_verify",
    ),
    path(
        route="login/",
        view=CustomTokenObtainPairView.as_view()
    )
]
