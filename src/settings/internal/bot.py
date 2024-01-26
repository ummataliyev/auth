"""
initialize settings
"""
from src.settings import default

default.INSTALLED_APPS.append("apps.bot")


TOKEN = default.env.str("TOKEN")
PARSE_MODE = default.env.str("PARSE_MODE")
