"""
creating a new bot instance
"""
import telebot

from src.settings.internal.bot import TOKEN
from src.settings.internal.bot import PARSE_MODE


bot = telebot.TeleBot(
    token=TOKEN,
    parse_mode=PARSE_MODE
)
