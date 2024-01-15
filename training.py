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
from get_employee import print_table, trim_date
# Путь к файлу env.env
dotenv_path = "env.env"

# Загружаем переменные окружения
load_dotenv(dotenv_path)
TOKEN = os.getenv("TOKEN2")
EXCEL_FILE = os.getenv("EXCEL_FILE")

employees = print_table(EXCEL_FILE)

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['sba'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Ответственный за изоляцию", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA061'))
    markup.row(btn1)  
    btn2 = types.InlineKeyboardButton("Управление подрядными организациями", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA130'))
    markup.row(btn2) 
    btn3 = types.InlineKeyboardButton("Контроль за состоянием лесов", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA143'))
    markup.row(btn3) 
    btn4 = types.InlineKeyboardButton("Ответственные лица по надзору за безопасной эксплуатацией грузоподъемных кранов, подъемников, съемных грузозахватных приспособлений и тары (Каждые 3 года/Every 3 years)", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA106'))
    markup.row(btn4) 
    btn5 = types.InlineKeyboardButton("Ответственные лица за безопасное производство работ кранами по перемещению грузов (ежегодно/annually)", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA107'))
    markup.row(btn5) 
    btn6 = types.InlineKeyboardButton("Ответственные лица за содержание грузоподъемных кранов, крановых путей и подъемников в исправном состоянии (Каждые 3 года/Every 3 years)", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA108'))
    markup.row(btn6)               
    btn7 = types.InlineKeyboardButton("Работники, допущенные к управлению самоходным телескопическим подъемником и автогидроподъемником ежегодно/annually", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA053'))
    markup.row(btn7)               
    btn8 = types.InlineKeyboardButton("Персонал, имеющий смежную профессию Стропальщик ежегодно/annually", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA113'))
    markup.row(btn8)               
    btn9 = types.InlineKeyboardButton("Персонал, имеющий смежную профессию рабочий с правом управления грузоподъемными механизмами с пола ежегодно/annually", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA109'))
    markup.row(btn9)               
    btn10 = types.InlineKeyboardButton("Лица, допущенные к самостоятельной работе в качестве машиниста крана  ежегодно/annually", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA054'))
    markup.row(btn10)               
    btn11 = types.InlineKeyboardButton("Работники, допущенные к управлению вилочным погрузчиком", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA055'))
    markup.row(btn11)               
    btn12 = types.InlineKeyboardButton("ИТР, ответственный по надзору за техническим состоянием и эксплуатацией сосудов", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA137'))
    markup.row(btn12)               
    btn13 = types.InlineKeyboardButton("ИТР, ответственный по надзору за безопасной эксплуатаций КС и СРД", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA147'))
    markup.row(btn13)               
    btn14 = types.InlineKeyboardButton("ИТР Ответственные за исправное состояние и безопасное действие сосудов", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA029_1'))
    markup.row(btn14)               
    btn15 = types.InlineKeyboardButton("ИТР Ответственный за исправное состояние КС и СРД", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA146'))
    markup.row(btn15)               
    btn16 = types.InlineKeyboardButton("Ответственные за исп. сост. и безопасную эксплуатацию котлов", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA116_1'))
    markup.row(btn16)               
    btn17 = types.InlineKeyboardButton("Ответственные за исп. сост. и безопасную экспл-ю трубопроводов", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA029'))
    markup.row(btn17)               
    btn18 = types.InlineKeyboardButton("Лица, из числа обслуж.персонала с правом обслуживания сосудов и трубопроводов", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA045'))
    markup.row(btn18)               
    btn19 = types.InlineKeyboardButton("Лица, допущенные к самостоятельному обслуж. КУ", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA114'))
    markup.row(btn19)               
    btn20 = types.InlineKeyboardButton("Лица по обслуживанию котлов", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA116'))
    markup.row(btn20)               
    btn21 = types.InlineKeyboardButton("ПромБез для работников", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA023'))
    markup.row(btn21)               
    btn22 = types.InlineKeyboardButton("ПромБез для ИТР", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA024'))
    markup.row(btn22)               
    btn23 = types.InlineKeyboardButton("БиОТ для ИТР", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA034'))
    markup.row(btn23)               
    btn24 = types.InlineKeyboardButton("БиОТ для рабочих", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA035'))
    markup.row(btn24)               
    btn25 = types.InlineKeyboardButton("ПТМ ежегодно", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA036'))
    markup.row(btn25)               
    btn26 = types.InlineKeyboardButton("ПТМ один раз в три года", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA077'))
    markup.row(btn26)  
    time.sleep(2)
    await message.answer('Ждите...', reply_markup=markup)

# # Обработчик для всех остальных сообщений
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.reply(message.text)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    result = json.loads(message.web_app_data.data) 
    employeId = result["employeId"]
    sba = result["sba"]
    print(sba)
    if employeId.isdigit():
         employeId = int(employeId) 
         for emp in employees:
            if emp.employId == employeId:                
                await message.reply(emp)
                await message.reply(emp.get_sba(sba))


# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)