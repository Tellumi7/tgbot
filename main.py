import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# Загружаем токен из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Инициализация бота (новый способ для aiogram 3.7+)
bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

# Простой обработчик — эхо
@dp.message()
async def echo_message(message: types.Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except Exception:
        await message.answer("Невозможно отправить это сообщение 😅")

# Основная функция
async def main():
    print("🚀 Бот запускается...")   # <-- добавлен вывод перед стартом
    await dp.start_polling(bot)
    print("✅ Бот успешно запущен и работает!")  # <-- если polling завершится

# Точка входа
if __name__ == "__main__":
    asyncio.run(main())
