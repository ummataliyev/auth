"""
the echo handler
"""
from apps.bot import bot
from apps.bot import telebot


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    """
    sends echo message.
    """
    bot.send_message(
        chat_id=message.chat.id,
        text=message.text,
        reply_markup=telebot.types.ReplyKeyboardRemove()
    )
