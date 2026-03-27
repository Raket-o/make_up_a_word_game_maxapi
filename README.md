<div style="text-align: center">
    <img src="./images_readme/logo.jpg" width="450"/>
</div>

# Инструкция телеграм-бота.
## Краткое описание:
Бот составляет слова из предложенных ему букв. 

<div style="text-align: center">
    <img src="./images_readme/main_screen.png" width="380"/>
</div>

### Стек:
* python
* aiogram

---

### <img src="images_readme/instruc.jpg" width="50" alt="instruc"/>
Для начальной настройки бота, Вам необходимо создать виртуальное окружение. 
Поместить токен-бота и указать URL веб приложения (файл .env). 
Далее запускаем бота в файле main.py. Для отслеживания функционирования бота и возможных ошибок,
ведётся логирования, путём записи данных в файлы (logs/loging.log) 
Параметры логирования можно изменить в файле utils/logging.py. 

---

### <img src="images_readme/terminal_logo.png" width="45" alt="terminal_logo"/>
### Запуск на Windows (при установленном python):
Открываем терминал, переходим в корневую папку с ботом
1. Создаём окружение ```python -m venv venv```
2. Активируем окружение ```venv\Scripts\activate.bat```
3. Устанавливаем зависимости ```FOR /F %x IN (requirements.txt) DO ( IF NOT # == %x ( pip install %x ) )```
4. Переименовываем файл .env.template в .env
5. Заполняем поля токен-бота и URL веб приложения
6. Запускаем командой из терминала ```python aiogram_bot/main.py```

### Запуск на Linux (при установленном python):
Открываем терминал, переходим в корневую папку с ботом
1. Создаём окружение ```python3 -m venv venv```   
2. Активируем окружение source ```source venv/bin/activate```
3. Устанавливаем зависимости ```pip install -r requirements.txt```
4. Переименовываем файл .env.template в .env
5. Заполняем поля токен-бота и URL веб приложения
6. Запускаем командой из терминала ```python3 aiogram_bot/main.py```

---

### <img src="images_readme/pep8.jpg" width="50" alt="pep8"/>
Проверено линтерами (black, isort, flake8, mypy).

---

### <img src="images_readme/licentie.jpg" width="45" alt="licentie"/>
Проект распространяется под лицензией MIT.

---
