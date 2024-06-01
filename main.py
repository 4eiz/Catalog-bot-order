import asyncio
import logging

from aiogram import Dispatcher

from app import general, admin
from app.goods_list import goods_menu, monitor, mouse, keyboard
from app.services_list import services_menu, updating, cleaning, installing, repair

from config import bot


async def start():
    # Настройка логгера для записи в файл
    # logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    dp = Dispatcher()

    dp.include_routers(
        general.router,
        goods_menu.router,
        mouse.router,
        monitor.router,
        keyboard.router,
        repair.router,
        services_menu.router,
        updating.router,
        cleaning.router,
        installing.router,
        admin.router,
    )

    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())
