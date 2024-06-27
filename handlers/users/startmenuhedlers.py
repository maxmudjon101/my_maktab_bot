from keyboards.default.menu import jadval_menu,start_menu
from loader import dp
from aiogram import types


# Admin tugmasi uchun hedler


@dp.message_handler(text="Admin🤖")
async def admin_message(message:types.Message):
    text=f"Bot egasi : Maxmudjonov Maxmudjon\n"
    text+=f"Telfon Raqami : +998991505333\n"
    text+=f"Telegram :@maxmudjon_99150\n"
    await message.answer(text)


@dp.message_handler(text="sinf rahbari🥸")
async def admin_message(message:types.Message):
    text=f" Sindarova Matluba\n"
    await message.answer(text)

@dp.message_handler(text="O'quvchilar ruyxati📖")
async def secelt_message(message: types.Message):
        text = f"Baliqqni Boshi:Ravshanova Ruxshona\n"
        text += f"Murodova Amira:\n"
        text+= f"Amir Umarkulov:\n"
        text+=f"fariza ochilova\n"
        text+= f"Daler Mrdonkulov:\n"
        text+= f"Xamidov Alijon:\n"
        text+= f"Usmonov Mirzamon:\n"
        text+= f"Axtamov Davlat:\n"
        text+= f"Teshakulova Diyora:\n"
        text+= f"Tursunov Jasur:\n"
        text+= f"Maxmudjonov Maxmudjon:\n"
        text+= f"Abdusamatov Abduali:\n"
        text+= f"Baxriev Xushnut:\n"
        text+= f"Ulmasova Zarnigor:\n"
        text+= f"Xushvaxtova Marjona:\n"

        await message.answer(text)




@dp.message_handler(text='dars jadvali📚')
async def admin_message(message:types.Message):
   text="Xfta kunini tanlang"
   await message.answer(text,reply_markup=jadval_menu)


@dp.message_handler(text="ortga")
async def admin_message(message: types.Message):
       text = "Tanlang"
       await message.answer(text,reply_markup=start_menu)



@dp.message_handler(text='Dushanba')
async def admin_message(message:types.Message):
   text="Algebra\n"
   text+="Biologia\n"
   text+="Onatili\n"
   text+="Jismoni tarbi\n"
   text+="Adabiot\n"
   text+="Tarix\n"
   await message.answer(text,reply_markup=jadval_menu)





@dp.message_handler(text="Seshanba")
async def admin_message(message:types.Message):
   text="Tarbia\n"
   text+="Fizika\n"
   text+="Algebra\n"
   text+="Rustili\n"
   text+="chizmachilik\n"
   text += "texnalogia\n"
   await message.answer(text,reply_markup=jadval_menu)








@dp.message_handler(text="Chorshanba")
async def admin_message(message:types.Message):
   text="onatili\n"
   text+="geometria\n"
   text+="jismoni tarbia\n"
   text+="tarix\n"
   text+="geografia\n"
   text+="ingilis tili\n"
   await message.answer(text,reply_markup=jadval_menu)






@dp.message_handler(text="Payshanba")
async def admin_message(message:types.Message):
   text="taix\n"
   text+="algebra\n"
   text+="kimyo\n"
   text+="ingilis tili\n"
   text+="geografia:iqtisot\n"
   text+="informatika\n"
   await message.answer(text,reply_markup=jadval_menu)





@dp.message_handler(text="Juma")
async def admin_message(message:types.Message):
   text="sinif:soati\n"
   text+="biologia\n"
   text+="onatili\n"
   text+="adabiot\n"
   text+="ingilis tili\n"

   await message.answer(text,reply_markup=jadval_menu)







@dp.message_handler(text="SHanba")
async def admin_message(message:types.Message):
   text="fizika\n"
   text+="huquq asosi\n"
   text+="geometiria"
   text+="informatika\n"
   text+="rustili\n"
   text+="kimyo\n"
   await message.answer(text,reply_markup=jadval_menu)














