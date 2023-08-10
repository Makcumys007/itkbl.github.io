from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json 
import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

TOKEN = '5994379087:AAHP4nVkE9CBW1lzjliu6fLPoa57dP7R3ko'

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

@dp.message_handler(commands=['start','run'])
async def start(message: types.Message):


    global language
    language = message.from_user.language_code
    if language == 'en':
        hello = 'Welcome to the IT KBL bot!\nWe will help you solve your problems...'
        reset = 'Reset password'
        service = 'Our services'
        call = 'Call back IT Service Desk'     
        post = 'Email us'           
    else:
        hello = 'Добро пожаловать в бот IT KBL!\nМы поможем вам в решении ваших проблем... '
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
    logo = open('./img/logo.png', 'rb')
    await message.answer_photo(logo)
    await message.answer(hello)
   # time.sleep(5)
    await message.answer(service, reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):

    if language == 'en':
        sent = 'Your request has been received! Thank you!'
    else:
        sent = 'Ваше обращение получено! Спасибо!'

    result = json.loads(message.web_app_data.data) 
    name = result["name"]
    subject = result["subject"]
    text_message = result["email"]

     

    SMTP_SERVER = "smtp.office365.com"
    PORT = 587  # For starttls
    MY_ADDRESS = "itbotkbl@outlook.com"
    PASSWORD = "qz?}Y8YiP3LDKdX"

    RECIVER_ADDRESS = "maxim.abylkassov@kazminerals.com"

     # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(SMTP_SERVER,PORT)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(MY_ADDRESS, PASSWORD)

        msg = MIMEMultipart()       # create a message

        msg['From']=MY_ADDRESS
        msg['To']=RECIVER_ADDRESS
        msg['Subject']=f'{name} - {subject}'

        msg.attach(MIMEText(f'{name} \n {text_message}'))

        server.send_message(msg)


    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()



   # await message.answer(f'{name}')

    await message.answer(sent)




@dp.callback_query_handler()
async def callback(call):
    if call.data == 'call':
        await call.message.answer(f'+77750111911')
    

@dp.message_handler()
async def echo(message: types.Message):
    if message.text == 'Call back IT Service Desk' or message.text == 'Позвонить в IT Service Desk':
        await message.answer(f'+77750111911')
    else:        
        await message.answer(f'/run')

  
    






# Работает вечно
executor.start_polling(dp)

