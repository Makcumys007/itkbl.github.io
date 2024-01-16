from errno import EMLINK
from telnetlib import PRAGMA_HEARTBEAT
from wsgiref.util import request_uri
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

main_menu = ["🚨🚨🚨Номера экстренных служб",
             "💊👨‍⚕️👩‍⚕️Оказание доврачебной помощи",
             "📑📚Организация и планирования обучения",
             "📍Локация",
             "👷👷‍♂️🥽🪖СИЗ",
             "🔗🔗🔗Часто используемые ссылки",
             "Базовые требования Безопасности",
             "📚📚📚Библиотека"]

main_meny_item0 = ["Номер аварийного диспетчера🚨🚨🚨",
                   "Номера медицинского пункта KBL 🚑🚑🚑",
                   "Go Back"]


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(main_menu[0])
    markup.row(btn1)   
    btn2 = types.InlineKeyboardButton(main_menu[1])
    markup.row(btn2) 
    btn3 = types.InlineKeyboardButton(main_menu[2])
    markup.row(btn3) 
    btn4 = types.InlineKeyboardButton(main_menu[3])
    markup.row(btn4) 
    btn5 = types.InlineKeyboardButton(main_menu[4])
    markup.row(btn5) 
    btn6 = types.InlineKeyboardButton(main_menu[5])
    markup.row(btn6)               
    btn7 = types.InlineKeyboardButton(main_menu[6])
    markup.row(btn7)               
    btn8 = types.InlineKeyboardButton(main_menu[7])
    markup.row(btn8)


    text="Добро пожаловать в бот безопасности! Выберите раздел, который вас интересует:"


    time.sleep(2)
    await message.answer(text, reply_markup=markup)
    

@dp.message_handler()
async def echo(message: types.Message):
     request = message.text        
     markup = types.ReplyKeyboardMarkup()
     if request == main_menu[0]:
        btn1 = types.InlineKeyboardButton(main_meny_item0[0])
        markup.row(btn1)   
        btn2 = types.InlineKeyboardButton(main_meny_item0[1])
        markup.row(btn2) 
        btn3 = types.InlineKeyboardButton(main_meny_item0[2])
        markup.row(btn3) 
        await message.answer(request, reply_markup=markup)       

# main_meny_item0 ответы
     if request == main_meny_item0[0]:
        await message.answer("Номер аварийного диспетчера \n87015555116 \n87750158555 \nСо стационарного телефона:58555")
     elif request == main_meny_item0[1]:
         await message.answer("Номера медицинских пунктов: \n87018137003 \n87018137054 \nСо стационарного телефона:58333")
         
# go back для всех видов меню
     if request == main_meny_item0[2] :
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(main_menu[0])
        markup.row(btn1)   
        btn2 = types.InlineKeyboardButton(main_menu[1])
        markup.row(btn2) 
        btn3 = types.InlineKeyboardButton(main_menu[2])
        markup.row(btn3) 
        btn4 = types.InlineKeyboardButton(main_menu[3])
        markup.row(btn4) 
        btn5 = types.InlineKeyboardButton(main_menu[4])
        markup.row(btn5) 
        btn6 = types.InlineKeyboardButton(main_menu[5])
        markup.row(btn6)               
        btn7 = types.InlineKeyboardButton(main_menu[6])
        markup.row(btn7)               
        btn8 = types.InlineKeyboardButton(main_menu[7])
        markup.row(btn8)
        await message.answer(request, reply_markup=markup)




@dp.message_handler(commands=['sba'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Ответственный за изоляцию", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA061'))
    markup.row(btn1)  
    btn2 = types.InlineKeyboardButton("Управление подрядными организациями", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA130'))
    markup.row(btn2) 
    btn3 = types.InlineKeyboardButton("Контроль за состоянием лесов", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA143'))
    markup.row(btn3) 
    btn4 = types.InlineKeyboardButton("Ответственные лица по надзору за безопасной эксплуатацией грузоподъемных кранов, подъемников, съемных грузозахватных приспособлений и тары (Каждые 3 года)", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA106'))
    markup.row(btn4) 
    btn5 = types.InlineKeyboardButton("Ответственные лица за безопасное производство работ кранами по перемещению грузов (ежегодно)", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA107'))
    markup.row(btn5) 
    btn6 = types.InlineKeyboardButton("Ответственные лица за содержание грузоподъемных кранов, крановых путей и подъемников в исправном состоянии (Каждые 3 года)", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA108'))
    markup.row(btn6)               
    btn7 = types.InlineKeyboardButton("Работники, допущенные к управлению самоходным телескопическим подъемником и автогидроподъемником ежегодно", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA053'))
    markup.row(btn7)               
    btn8 = types.InlineKeyboardButton("Персонал, имеющий смежную профессию Стропальщик ежегодно", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA113'))
    markup.row(btn8)               
    btn9 = types.InlineKeyboardButton("Персонал, имеющий смежную профессию рабочий с правом управления грузоподъемными механизмами с пола ежегодно", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA109'))
    markup.row(btn9)               
    btn10 = types.InlineKeyboardButton("Лица, допущенные к самостоятельной работе в качестве машиниста крана  ежегодно", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA054'))
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
    btn27 = types.InlineKeyboardButton("Выявление опасных факторов", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA003'))
    markup.row(btn27) 
    
    btn28 = types.InlineKeyboardButton("Первая помощь", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA001'))
    markup.row(btn28) 
    btn29 = types.InlineKeyboardButton("Наряд-допуск", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA033'))
    markup.row(btn29) 
    

    btn30 = types.InlineKeyboardButton("Анализ безопасности работ", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA007'))
    markup.row(btn30) 
    btn31 = types.InlineKeyboardButton("ICAM факторов", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA138'))
    markup.row(btn31) 
    btn32 = types.InlineKeyboardButton("Safety Leadership", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA022'))
    markup.row(btn32)     
    btn33 = types.InlineKeyboardButton("Владелец личного замка", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA060'))
    markup.row(btn33)     
    btn34 = types.InlineKeyboardButton("Работы на высоте", web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/employeid.html?sba=SBA009'))
    markup.row(btn34) 






    time.sleep(2)
    await message.answer('Ждите...', reply_markup=markup)




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