from aiogram import executor

from loader import dp,db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    try:
        db.create_table_users()
    except Exception as err:
        print(err)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if name == 'main':
    executor.start_polling(dp, on_startup=on_startup)
