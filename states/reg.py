from aiogram.dispatcher.filters.state import State, StatesGroup


class RegProject(StatesGroup):
	get_title = State()
	get_description = State()
	get_demo = State()
	get_github = State()