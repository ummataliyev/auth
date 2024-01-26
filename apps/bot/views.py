"""
webhook
"""
import telebot

from rest_framework import views
from rest_framework import response

from apps.bot.instance import bot


class WebhookAPIView(views.APIView):
    """
    Webhook view that can handle Telegram updates
    """
    def post(self, request):
        """
        Handle incoming POST requests (Telegram updates)
        """
        update = telebot.types.Update.de_json(request.data)
        bot.process_new_updates([update])

        return response.Response()
