from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, db
from states.reg import RegProject


@dp.message_handler(chat_id=ADMINS, commands='new_project', state='*')
async def add_project(message: types.Message, state: FSMContext):
    await message.answer("Отправьте название проекта")
    await RegProject.get_title.set()


@dp.message_handler(state=RegProject.get_title)
async def add_project(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text

    await message.answer("Отправьте описание проекта")
    await RegProject.next()


@dp.message_handler(state=RegProject.get_description)
async def add_project(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text

    await message.answer("Отправьте демо версии проекта")
    await RegProject.next()


@dp.message_handler(state=RegProject.get_demo)
async def add_project(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['demo'] = message.text

    await message.answer("Отправьте исходный код (github) проекта")
    await RegProject.next()


@dp.message_handler(state=RegProject.get_github)
async def add_project(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        title = data.get('title')
        description = data.get('description')
        demo = data.get('demo')
        github = message.text

    await db.reg_project(title, description, demo, github)
    await message.answer("Готово ✅")
    await state.finish()
