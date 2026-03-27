"""
Модуль конфигурации бота на основе Pydantic Settings.
Загружает переменные окружения из `.env`
"""

import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
START_MESSAGE = os.getenv("START_MESSAGE")
ADMINS_ID = set(int(i) for i in os.getenv("ADMINS_ID").split()) \
    if os.getenv("ADMINS_ID") \
    else []