"""
storage database processor
"""
import logging

from apps.bot import telebot
from apps.users.models.tg_user import TGUser # noqa


logger = logging.getLogger(__name__)


def create_tg_user(message: telebot.types.Message):
    """
    create a new telegram user.
    """
    user = message.from_user

    try:
        TGUser.objects.update_or_create(
            chat_id=user.id,
            defaults={
                "username": user.username,
                "first_name": user.first_name
            }
        )
    except Exception as exc:
        logger.error("error exc: %s", exc)


def create_verify_code(message: telebot.types.Message, code: str):
    """
    create a new verification code
    """
    user = message.from_user
    contact_info = message.contact
    phone_number = contact_info.phone_number

    try:
        TGUser.objects.update_or_create(
            chat_id=user.id,
            defaults={
                "username": user.username,
                "first_name": user.first_name,
                "phone_number": phone_number,
                "code": code
            }
        )
    except Exception as exc:
        logger.error("error exc: %s", exc)
