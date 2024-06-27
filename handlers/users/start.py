# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
# from keyboards.default.menu import start_menu
# from loader import dp
#
#
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     text=f"Assalomu alaykum \n"
#     text+=f"52-maktab botiga xush kelibsiz \n"
#     text+=f"quyidagilardan birini tanlang \n"
#     await message.answer_photo("https://i.pinimg.com/236x/0a/e2/74/0ae2746ce96c23dc9546a194fd869ca8.jpg",caption=text,reply_markup=start_menu)
import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    text="Assalomu alaykum xush kelibsizвє\n\n"
    text+="<b>Instagram, TikTok, Threads, Linkedin  \n\n"
    text+="Twitter, Facebook, Pinterest, Snapchat</b>\n\n"
    text+="Platformalaridan rasm va videolarni \n"
    text+="tezkorlik bilan yuklab olishingiz mumkin \n"
    text+="Video havolasini botga yuboringв¤µ\n"

    await message.answer(text)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)