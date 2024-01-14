from errno import EMLINK
from telnetlib import PRAGMA_HEARTBEAT
from dotenv import load_dotenv 
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json 
import os
import get_employee
# Путь к файлу env.env
dotenv_path = "env.env"

# Загружаем переменные окружения
load_dotenv(dotenv_path)
TOKEN = os.getenv("TOKEN2")
EXCEL_FILE = os.getenv("EXCEL_FILE")

employees = get_employee.print_table(EXCEL_FILE)

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['sba003'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Табельный номер", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=sba003'))
    markup.row(btn1)  
    time.sleep(2)
    await message.answer('service', reply_markup=markup)

# # Обработчик для всех остальных сообщений
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.reply(message.text)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    result = json.loads(message.web_app_data.data) 
    employeId = result["employeId"]
    if employeId.isdigit():
         for emp in employees:
            if emp.employId == 11797:
                print(emp)
                print(emp.get_SBA('SBA061'))  
    await message.reply(employeId)


# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)