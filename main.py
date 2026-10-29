import asyncio
from aiogram import Bot, Dispatcher
from aiogram.exceptions import (
    TelegramNetworkError,
)
from config.settings import BOT_TOKEN
from handlers.users.start import rt as start
from handlers.users.test import rt as test

dp = Dispatcher()
async def main():
    bot = Bot(BOT_TOKEN)
    dp.include_router(start)

    dp.include_router(test)

    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("bot ishga tushdi")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot to'xtatildi")
    except TelegramNetworkError:
        print("internetga ulang")
