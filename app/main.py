import asyncio
from aiogram import Bot, Dispatcher
from database.models import async_main
from handlers import router


async def main():
    await async_main()
    bot = Bot(token='7729254671:AAGtL_j2ZvT6bFrqCISHng_w_V8fPlvcGAQ')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')