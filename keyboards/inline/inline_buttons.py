from aiogram import types


def pagination():
    menu = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="◀️", callback_data="previous")
    btn2 = types.InlineKeyboardButton(text="▶️", callback_data="next")
    menu.add(btn1, btn2)

    return menu


def contact():
    menu = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Контакты", url='https://t.me/MurodillaKarimov')
    menu.add(btn1)

    return menu