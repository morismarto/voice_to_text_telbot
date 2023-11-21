from aiogram import types

def get_kb():
    buttons = [
        [types.KeyboardButton(text="tiny")],
        [types.KeyboardButton(text="base")],
        [types.KeyboardButton(text="small")],
        [types.KeyboardButton(text="medium")],
        [types.KeyboardButton(text="large")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Название модели"
    )
    return keyboard