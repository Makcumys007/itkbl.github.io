import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json 
import os

from exchangelib import Credentials, Configuration, Account, DELEGATE
from exchangelib import Message, Mailbox
from dotenv import load_dotenv 
import os

load_dotenv()


def send_email_to_recipients(subject, body):

    LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")
    LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
    LOGIN_USER = os.getenv("LOGIN_USER")    
    SMTP_SERVER = os.getenv("SMTP_SERVER") 
    RECEPIENT_EMAIL = os.getenv("RECEPIENT_EMAIL")

    credentials = Credentials(username=LOGIN_USER, password=LOGIN_PASSWORD)
    config = Configuration(server=SMTP_SERVER, credentials=credentials)

    account = Account(
        primary_smtp_address=LOGIN_EMAIL,
        config=config,
        autodiscover=True,
        access_type=DELEGATE,
    )

    m = Message(
        account=account,
        folder= account.sent,
        subject=subject,
        body=body,
        to_recipients=[Mailbox(email_address=RECEPIENT_EMAIL)],
    )
    m.send_and_save()




TOKEN = os.getenv("TOKEN")
IMG_FOLDER_PATH = os.getenv("IMG_FOLDER_PATH")
print(TOKEN)

bot = Bot(TOKEN)

dp = Dispatcher(bot)

language = None


hello = ''
reset = ''
service = ''
call = ''
post = ''
name =''
subject = ''
sent = ''
start_run = ''

@dp.message_handler(commands=['start','run'])
async def start(message: types.Message):


    global language
    language = message.from_user.language_code
    print(language)
    if language == 'en':
        hello = 'Welcome to IT KBL bot!\nWe are glad to help you...'
        reset = 'Reset password'
        service = 'Our services'
        call = 'Call IT Service Desk'     
        post = 'Write us'   
    elif language == 'kk':
        hello = 'IT KBL ботына қош келдіңіз!\n Біз сізге көмектесуге қуаныштымыз...'   
        reset = 'Парольды өзгерту' 
        service = 'Біздің қызметтер'    
        call = 'IT Service Desk\'ке қоңырау шалу' 
        post = 'Бізге жазу'   
    else:
        hello = 'Добро пожаловать в бот IT KBL!\nМы рады вам помочь... '
        reset = 'Сбросить пароль'
        service = 'Наши сервисы'
        call = 'Позвонить в IT Service Desk'
        post = 'Написать нам'

   # markup = types.InlineKeyboardMarkup()
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(reset, web_app=WebAppInfo(url='https://passwordreset.microsoftonline.com/'))
    markup.row(btn1)    
    btn2 = types.InlineKeyboardButton(call, callback_data='call')
  #  btn2 = types.InlineKeyboardButton(call, web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/phone.html'))
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton(post, web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/index.html'))
    markup.row(btn3)
    
    

    logo = open(f'{IMG_FOLDER_PATH}logo_bot.png', 'rb')
    await message.answer_photo(logo)
    await message.answer(hello)
    time.sleep(2)
    await message.answer(service, reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):

    if language == 'en':
        sent = 'Your request has been received! Thank you!'
    elif language == 'kk':
        sent = 'Сіздің өтінішіңіз қабылданды! Рахмет!'
    else:
        sent = 'Ваше обращение получено! Спасибо!'

    result = json.loads(message.web_app_data.data) 
    name = result["name"]
    subject = result["subject"]
    text_message = result["email"]

     
    send_email_to_recipients(f"{name} - {subject}", f"{name} \n {subject} \n {text_message}")
    

   
    await message.answer(sent)




@dp.callback_query_handler()
async def callback(call):
    if call.data == 'call':
        await call.message.answer(f'+77750111911')
    

@dp.message_handler()
async def echo(message: types.Message):


    if language == 'en':
        start_run = 'To get the menu, press /start'     
    elif language == 'kk':
        start_run = 'Мәзірге өту үшін /start батырмасын басыңыз.'
    else:
        start_run = 'Для получения меню, нажмите /start'  


    if message.text == 'Call IT Service Desk' or message.text == 'Позвонить в IT Service Desk' or message.text == 'IT Service Desk\'ке қоңырау шалу':
        await message.answer(f'+77750111911')
    else:        
        await message.answer(f'{start_run}')

  
    






# Работает вечно
executor.start_polling(dp)

