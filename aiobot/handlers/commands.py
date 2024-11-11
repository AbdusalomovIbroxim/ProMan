from aiogram.types import Message
from aiogram.types import ParseMode
from dispatcher import dis
from aiobot.database import db
from ..models import User
# from datetime import datetime
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

# client = gspread.authorize(creds)

# sheet = client.open("Рабочий график").sheet1  

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



@dis.message_handler(commands=['come'])
async def send_welcome(message: Message):
    user_id = str(message.from_user.id)
    username = message.from_user.username

    user = await User.get(user_id)

    # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # sheet.append_row([user_id, username, "пришел на работу", current_time])
    
    await message.answer(
        f'Здравствуйте, @{username}, вы успешно отметились как на работе!',
        parse_mode=ParseMode.MARKDOWN
    )

@dis.message_handler(commands=['leave'])
async def cmd_leave(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username

    # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # sheet.append_row([user_id, username, "ушел с работы", current_time])

    # Логика для записи времени, когда сотрудник уходит с работы
    await message.answer(
        f'Здравствуйте, @{username}, вы успешно отметились как ушедший с работы!',
        parse_mode=ParseMode.MARKDOWN
    )

    # Можно добавить логику для записи времени в базу данных или другую систему


@dis.message_handler(commands=['report'])
async def cmd_report(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username

    # Спрашиваем сотрудника отчет
    await message.answer(
        f'Здравствуйте, @{username}, пожалуйста, отправьте отчет о том, что готово, что вы делаете и что будете делать дальше.',
        parse_mode=ParseMode.MARKDOWN
    )

    # Ждем, пока пользователь отправит отчет
    # @dis.message_handler()
    # async def handle_report(msg: Message):
    #     report = msg.text
    #     from datetime import datetime
    #     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # # Записываем отчет в Google Sheets
        # sheet.append_row([user_id, username, "отчет", report, current_time])

        # await msg.answer(f'Отчет для @{username} принят: {report}', parse_mode=ParseMode.MARKDOWN)
