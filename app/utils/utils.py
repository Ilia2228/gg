import datetime
from create_bot import ADMINS


ABOUT_ME='''Бот ideas

бот умеет:

-принимать контакты пользователя
-отправлять запросы на сервер по мйнкрафту
-играть с пользователем
-хранить информацию


последнее обновление: 22 марта 2025 года
'''

def create_profile_message(user: dict):
    USER_MESSAGE = "Тестовый текст"
    if user:
        USER_MESSAGE = f"""Привет, {user["name"]}! 🥋

Сейчас: {datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")} ⏳

У вас на балансе: {user["balance"]} руб 💵
    """
        if user["id"] in ADMINS:
            USER_MESSAGE += """
            
Вы обладаете правами администратора!"""
    return USER_MESSAGE