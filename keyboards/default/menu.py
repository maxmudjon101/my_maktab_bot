from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



start_menu=ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='dars jadvali📚'),
            KeyboardButton(text="O'quvchilar ruyxati📖"),
        ],
        [

            KeyboardButton(text="sinf rahbari🥸"),
            KeyboardButton(text="Admin🤖"),
        ],

    ],

    resize_keyboard=True
)



jadval_menu=ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='Dushanba'),
            KeyboardButton(text="Seshanba"),
        ],
        [

            KeyboardButton(text="Chorshanba"),
            KeyboardButton(text="Payshanba"),
        ],
        [

            KeyboardButton(text="Juma"),
            KeyboardButton(text="SHanba"),
        ],
        [
            KeyboardButton(text="ortga"),
        ]
    ],

    resize_keyboard=True
)








