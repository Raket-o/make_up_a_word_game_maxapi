"""Модуль логирования. Записывает логи в ./logs/...
Модуль настройки централизованного логирования для бота.

Настраивает логирование с выводом:
    - в консоль (stdout);
    - в файл с ротацией по времени.

Файлы логов сохраняются в директории `./logs/` в формате:
    `loging.log` + дотированные архивы (например, `loging.log.2025-04-05_12`).

Ротация:
    - Происходит каждые 10 часов (`when="H", interval=10`);
    - Хранится до 3 резервных копий (`backupCount=3`);
    - Автоматическое создание директории `logs`, если она отсутствует.

Формат сообщений:
    level: INFO | logger: utils.logging | time: YYYY-MM-DD HH:MM:SS | line №: 42 | message: Пример лога
"""

import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler

__DIR_LOGS = "logs"

if not os.path.exists(__DIR_LOGS):
    os.makedirs(__DIR_LOGS)

log_file_handler = TimedRotatingFileHandler(
    filename=f"./{__DIR_LOGS}/logging.log", when="H", interval=10, backupCount=3
)
stream_handler = logging.StreamHandler(stream=sys.stdout)

logging.basicConfig(
    format=(
        "level: %(levelname)s | "
        "logger: %(name)s | "
        "time: %(asctime)s | "
        "line №: %(lineno)s | "
        "message: %(message)s"
    ),
    level=logging.INFO,
    handlers=[stream_handler, log_file_handler],
)
