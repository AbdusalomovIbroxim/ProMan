

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from aiogram.types import ParseMode
from ..models import User
from dispatcher import dispatcher

scheduler = AsyncIOScheduler()


async def send_daily_message():
    users = await User.get_all()
    for user in users:
        user_id = user[0].user_id
        username = user[0].username
        try:
            await dispatcher.dis.bot.send_message(
                user_id, 
                f'Здравствуйте, @{username}, напишите пожалуйста, когда вы будете на работе и используйте команду /come, чтобы записать время.',
                parse_mode=ParseMode.MARKDOWN
            )
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю @{username}: {e}")

async def send_leave_message():
    users = await User.get_all()
    for user in users:
        user_id = user[0].user_id
        username = user[0].username
        try:
            await dispatcher.dis.bot.send_message(
                user_id, 
                f'Здравствуйте, @{username}, напишите пожалуйста, когда вы уходите с работы и используйте команду /leave, чтобы записать время.',
                parse_mode=ParseMode.MARKDOWN
            )
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю @{username}: {e}")

async def send_report_message():
    users = await User.get_all()
    for user in users:
        user_id = user[0].user_id
        username = user[0].username
        try:
            await dispatcher.dis.bot.send_message(
                user_id, 
                f'Здравствуйте, @{username}, напишите пожалуйста отчет: что готово, что вы делаете и что будете делать дальше. Используйте команду /report для отправки отчета.',
                parse_mode=ParseMode.MARKDOWN
            )
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю @{username}: {e}")


def start_scheduler():
    # scheduler.add_job(send_daily_message, 'cron', hour=10, minute=30)
    # scheduler.add_job(send_report_message, 'cron', hour=10, minute=30)
    # scheduler.add_job(send_daily_message, 'cron', hour=13, minute=30)
    # scheduler.add_job(send_daily_message, 'cron', hour=14, minute=00)
    # scheduler.add_job(send_report_message, 'cron', hour=16, minute=30)
    # scheduler.add_job(send_leave_message, 'cron', hour=17, minute=00)
    # scheduler.add_job(send_leave_message, 'cron', hour=18, minute=00)
    # scheduler.add_job(send_leave_message, 'cron', hour=18, minute=30)
    # scheduler.add_job(send_leave_message, 'cron', hour=19, minute=00)
    # scheduler.add_job(send_leave_message, 'interval', seconds=5)


    scheduler.start()
