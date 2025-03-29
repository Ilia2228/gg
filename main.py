import asyncio
from create_bot import bot, dp
from app.handlers.start import start_router

async def main():
    dp.include_router(start_router)
    await bot.delet_webhook(drop_pendinng_updetes=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())