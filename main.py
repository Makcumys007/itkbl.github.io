from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

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

@dp.message_handler(commands=['start','run'])
async def start(message: types.Message):


    global language
    language = message.from_user.language_code
    if language == 'en':
        hello = 'Welcome to the IT KBL bot!\nWe will help you solve your problems...'
        reset = 'Reset password'
        service = 'Our services'
        call = 'Call back'     
        post = 'Email us'   
    else:
        hello = 'Добро пожаловать в бот IT KBL!\nМы поможем вам в решении ваших проблем... '
        reset = 'Сбросить пароль'
        service = 'Наши сервисы'
        call = 'Позвонить нам'
        post = 'Написать нам'

    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(reset, url='https://passwordreset.microsoftonline.com/')
    markup.row(btn1)    
    btn2 = types.InlineKeyboardButton(call, callback_data='call')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton(post, web_app=WebAppInfo(url='https://makcumys007.github.io/itkbl.github.io/'))
    markup.row(btn3)
    logo = open('logo.png', 'rb')
    await message.answer_photo(logo)
    await message.answer(hello)
   # time.sleep(5)
    await message.answer(service, reply_markup=markup)


@dp.callback_query_handler()
async def callback(call):
    if call.data == 'call':
        await call.message.answer(f'+77750111911')
  
    






# Работает вечно
executor.start_polling(dp)

