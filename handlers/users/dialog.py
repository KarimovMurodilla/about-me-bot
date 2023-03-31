import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons


@dp.message_handler(text="Расскажи о себе", state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(
        "Привет! Меня зовут Муродилла. Мне 20 лет. Я родился и вырос в Ташкенте, Узбекистан. "
        "Я начал программировать с 17 лет. Я изучил программирование путем самообучения. (Конечно, "
        "большое спасибо Google, YouTube и Telegram). Мой первый язык программирования это - Python. "
        "Пройдя базовый уровень, я начал делать небольшие проекты чат-ботов на Телеграме. "
        "После долгой тяжелой работы и попыток я начал набираться опыта и начал "
        "прием заказов для Telegram бота. Сейчас я изучаю Django и делаю небольшие проекты.",
        reply_markup=keyboard_buttons.cases()
    )


@dp.message_handler(text="Кейсы", state='*')
async def bot_start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pagination'] = 0

    pag = data.get('pagination')

    projects = await db.get_all_projects()

    await message.answer(
        f"Название: {projects[pag].title}\n\n"
        f"Описание:\n{projects[pag].description}\n\n"
        f"Демо: {projects[pag].demo}\n"
        f"Github: {projects[pag].github}",
        reply_markup=inline_buttons.pagination(),
        disable_web_page_preview=True
    )

    await asyncio.sleep(5) # Отправляем уведомление через 5 секунд
    await message.answer("Свяжитесь со мной", reply_markup=inline_buttons.contact())


@dp.callback_query_handler(text_contains='next')
async def next(c: types.CallbackQuery, state: FSMContext):
    await c.answer()
    projects = await db.get_all_projects()

    async with state.proxy() as data:
        old = data.get('pagination')

        if (len(projects)-1) > old:
            data['pagination'] += 1

    pag = data.get('pagination')

    await c.message.edit_text(
        f"Название: {projects[pag].title}\n\n"
        f"Описание:\n{projects[pag].description}\n\n"
        f"Демо: {projects[pag].demo}\n"
        f"Github: {projects[pag].github}",
        reply_markup=inline_buttons.pagination(),
        disable_web_page_preview=True
    )


@dp.callback_query_handler(text_contains='previous')
async def previous(c: types.CallbackQuery, state: FSMContext):
    await c.answer()
    projects = await db.get_all_projects()

    async with state.proxy() as data:
        old = data.get('pagination')

        if old > 0:
            data['pagination'] -= 1

    pag = data.get('pagination')

    await c.message.edit_text(
        f"Название: {projects[pag].title}\n\n"
        f"Описание:\n{projects[pag].description}\n\n"
        f"Демо: {projects[pag].demo}\n"
        f"Github: {projects[pag].github}",
        reply_markup=inline_buttons.pagination(),
        disable_web_page_preview=True
    )
