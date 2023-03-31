from aiogram import types


def about_me():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Расскажи о себе")
    menu.add(btn1)

    return menu


def cases():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Кейсы")
    menu.add(btn1)

    return menu