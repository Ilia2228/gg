from aiogram import Router, F
from aiogram.types import Message

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(messeage: Message):
    await messeage.answer('Запуск сообщения по' + \
        'комвнде /start используя фильтр CommandStart()')
    
@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск по сообщения start_2 используя фильтр Command()')