import logging
import httpx
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

# Получаем токен и URL из .env
API_TOKEN = os.getenv("Token")
SERVER_URL = f'{os.getenv("Bot_url")}/api/users/'

if not API_TOKEN:
    raise ValueError("BOT_TOKEN не найден в .env")
if not SERVER_URL:
    raise ValueError("SERVER_URL не найден в .env")

# Логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: Message):
    user = message.from_user

    user = message.from_user

    telegram_id = user.id
    username = user.username or user.first_name or "unknown"
    full_name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name


    user_data = {
        "telegram_id": telegram_id,
        "username": username,
        "full_name": full_name
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(SERVER_URL, json=user_data)
        except Exception as e:
            pass

# Точка входа
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())