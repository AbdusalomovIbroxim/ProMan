from aiogram.types import Message
from dispatcher import dis
from ..models import User


@dis.message_handler(commands=['start'])
async def send_welcome(message: Message):
    user_id = str(message.from_user.id)
    username = message.from_user.username

    user = await User.get(user_id)

    if not user:
        await User.create(user_id, username)
        await message.answer(f'Привет, @{username}! Ты был зарегистрирован.')
    else:
        await message.answer(f'Привет, @{username}! Ты уже зарегистрирован.')
