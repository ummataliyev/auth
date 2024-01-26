"""
bot urlpatterns
"""
from django.urls import path

from apps.bot.views import WebhookAPIView


urlpatterns = [
    path("webhook/", WebhookAPIView.as_view())
]
