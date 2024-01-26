"""
URL configuration for src project.
"""
from django.urls import path
from django.urls import include


urlpatterns = [
    path('api/v1/bot/', include('apps.bot.urls')),
    path('api/v1/users/', include('apps.users.urls'))
]
