"""
the contact handler
"""
import random

from apps.bot import bot
from apps.bot import telebot

from apps.bot.processor.storage import create_verify_code


@bot.message_handler(content_types=['contact'])
def contact(message: telebot.types.Message):
    """
    accepts contact and sends verification code.
    """
    chat_id = message.chat.id
    code = str(random.randrange(100000, 1000000))

    text = f"Your verification code - <code>{code}</code>"

    create_verify_code(message, code)

    bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=telebot.types.ReplyKeyboardRemove()
    )
