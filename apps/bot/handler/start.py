"""
the start handler
"""
from apps.bot import bot
from apps.bot import telebot

from apps.bot.processor.storage import create_tg_user


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    """
    sends a welcome message.
    """
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
    item = telebot.types.KeyboardButton(
        text="Send Number",
        request_contact=True
    )
    markup.add(item)

    first_name = message.from_user.first_name
    text = f"Welcome <b>{first_name}</b>"

    create_tg_user(message=message)

    bot.send_message(message.chat.id, text, reply_markup=markup)
