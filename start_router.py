from aiogram import Router, F
from aiogram.types import Message
from app.utils.utils import ABOUT_ME
start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(messeage: Message):
    await messeage.answer('Запуск сообщения по' + \
        'комвнде /start используя фильтр CommandStart()')
    
@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск по сообщения start_2 используя фильтр Command()')











@start_router.message(F.text =="О нас")
async def print_about_me_message(message: Message):
    await message.answer(ABOUT_ME)