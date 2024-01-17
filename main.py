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


main_menu = ["🚨🚨🚨Номера экстренных служб",
             "💊👨‍⚕️👩‍⚕️Оказание доврачебной помощи",
             "📑📚Организация и планирования обучения",
             "📍Локация",
             "👷👷‍♂️🥽🪖СИЗ",
             "🔗🔗🔗Часто используемые ссылки",
             "Базовые требования Безопасности",
             "📚📚📚Библиотека"]

main_menu_item0 = {"Номер аварийного диспетчера🚨🚨🚨":"Номер аварийного диспетчера \n87015555116 \n87750158555 \nСо стационарного телефона:58555",
                   "Номера медицинского пункта KBL 🚑🚑🚑":"Номера медицинских пунктов: \n87018137003 \n87018137054 \nСо стационарного телефона:58333",
                   "Go Back":""}

main_menu_item1 = {"🆘🆘🆘Оперативные действия": """Лицо, оказывающее первую помощь, проводит следующие мероприятия по оценке обстановки и обеспечению безопасных условий для оказания первой помощи:
      1) определение угрожающих факторов для собственной жизни и здоровья;
      2) определение угрожающих факторов для жизни и здоровья пострадавшего;
      3) устранение угрожающих факторов для жизни и здоровья;
      4) прекращение действия повреждающих факторов на пострадавшего;
      5) оценка количества пострадавших;
      6) перемещение пострадавшего.
 
Лицо, оказывающее первую помощь, проводит оценку состояния пострадавшего по следующим критериям:
      1) определение наличия кровотечения, угрожающего жизни пострадавшего;
      2) определение сознания;
      3) определение дыхания.

Лицо, оказывающее первую помощь, вызывает бригаду скорой медицинской помощи и по необходимости другие службы экстренного реагирования и передает следующие данные со слов пострадавшего:
      1) фамилия, имя, отчество (при его наличии), возраст и пол пострадавшего;
      2) данные по состоянию пострадавшего и обстоятельства несчастного случая, травмы или заболевания;
      3) адрес и телефон, а также ориентировочные данные по проезду к месту нахождения пострадавшего.""",
                   "🚑🚑🚑Базовая реанимация":"""Базовая реанимация:
      1) при обнаружении пострадавшего без сознания, но с наличием дыхания принять меры по устранению опасности, перевести пострадавшего в восстановительное положение и вызвать экстренную службу 103 (112), контролируя состояние пострадавшего;
      2) при обнаружении пострадавшего без сознания и без дыхания принять меры по устранению опасности, вызвать экстренную службу 103 (112) и начать проводить непрямой массаж сердца непрерывно до ее прибытия;
      3) для повышения выживаемости пострадавшего и восстановления сердечной деятельности при наличии возможности применять автоматический дефибриллятор со встроенным в электроды датчиком контроля качества непрямого массажа сердца, предназначенный для лиц без медицинского образования;
      4) при восстановлении дыхания и сердечной деятельности, перевести пострадавшего в восстановительное (боковое) положение;
      5) не оставлять пострадавшего без присмотра и контролировать его состояние до прибытия экстренной службы 103 (112).""",
                   "🛏🛏🛏Расположение пострадавшего лица в восстановительном (боковом) положении":"""Расположение пострадавшего лица в восстановительном (боковом) положении:
      1) при наличии дыхания, перевести его в восстановительное (боковое) положение:
      снять очки (если он их носит);
      встать на колени рядом с пострадавшим, при этом ноги пострадавшего должны быть прямыми;
      положить его руку, находящуюся ближе к вам, под прямым углом к телу, согнуть в локте, ладонь направить вверх;
      дальнюю руку положить через грудную клетку, а тыльную сторону ладони приложить к щеке пострадавшего как можно ближе к полу (земле);
      другой рукой взять дальнюю ногу выше колена и поднять вверх, при этом стопа должна остаться на полу (на земле);
      придерживая кисть возле щеки, надавить на дальнюю ногу, чтобы перевернуть пострадавшего на бок по направлению к себе;
      поправить верхнюю часть ноги так, чтобы бедро и колено были согнуты под прямым углом;
      наклонить голову назад, чтобы дыхательные пути были открыты;
      регулярно проверять дыхание, до приезда бригады скорой медицинской помощи (далее – СМП);
      2) не оставлять пострадавшего без присмотра и контролировать его состояние до прибытия экстренной службы.""",
                   "❤️‍🩹❤️‍🩹❤️‍🩹Сердечно-легочная реанимация":"""Сердечно-легочная реанимация:
      1) при обнаружении пострадавшего без сознания и без дыхания принять меры по устранению опасности, вызвать экстренную службу и начать проводить непрямой массаж сердца непрерывно до ее прибытия;
      2) если пострадавший взрослый старше 12 лет, сделать 30 надавливаний на центр грудной клетки руками (основанием одной ладони, накрыв ее сверху второй ладонью) на глубину 5-6 см и 2 вдувания в рот (если не проводятся вдувания, то надавливать без перерыва), непрерывно продолжать надавливания и вдувания до приезда бригады СМП. Продолжать надавливания и вдувания до появления первых признаков жизни;
      3) если пострадавший ребенок (от 1 года до 12 лет), сделать 5 вдуваний, обхватив губами рот пострадавшего, продолжительность одного вдувания в рот в течение одной секунды, 30 надавливаний на центр груди на глубину 4-5 см (надавливания одной рукой) и 2 вдувания. Продолжать надавливания и вдувания до появления первых признаков жизни;
      4) если пострадавший младенец (от 0 до 12 месяцев), сделать 5 вдуваний, обхватив губами одновременно рот и нос пострадавшего, 30 надавливаний на центр груди на глубину одной трети грудной клетки двумя пальцами и 2 вдувания, обхватив губами одновременно рот и нос пострадавшего. Продолжать надавливания и вдувания до появления первых признаков жизни;""",
                   "🫁🫁🫁При наличии инородного тела в дыхательных путях":"""При наличии инородного тела в дыхательных путях:
      1) пострадавший подавился, если он может говорить (наличие кашля, плача), то следует поощрять кашель, не мешать пострадавшему, не бить по спине, контролировать состояние пострадавшего до приезда бригады СМП;
      2) если пострадавший не может говорить, присутствует кашель, плач, то необходимо нанести до пяти скользящих ударов рукой в межлопаточную область;
      3) если пострадавший - беременная женщина или человек с большим животом:
      провести пять надавливаний на центр грудной клетки руками;
      в случае если не помогает – повторить удары в межлопаточную область;
      контролировать состояние пострадавшего до приезда бригады СМП;
      встать сзади пострадавшего, обхватить его руками;
      одну из рук сжать в кулак и прижать со стороны большого пальца к животу, между пупком и грудной клеткой;
      вторую ладонь положить на кулак;
      сделать резкие сильные толчки в живот;
      пять толчков в живот, затем пять ударов по спине до появления кашля;
      4) если пострадавший потерял сознание, проводить мероприятия по базовой реанимации""",
                   "🩸🩸При наружном кровотечении":"""При наружном кровотечении:
      1) вызов экстренных служб;
      2) при кровотечении головы:
      наложить давящую повязку из подручных средств (бинт) в несколько слоев;
      усадить пострадавшего в удобное положение;
      3) при кровотечении носа:
      сдавить крылья носа пальцами в течении 10-15 минут;
      приложить холод к переносице через полотенце;
      не запрокидывать голову назад;
      нельзя высмаркиваться и ложиться;
      4) при кровотечении шеи:
      быстро прижать пальцами место кровотечения;
      наложить повязку из подручных средств (бинт) в несколько слоев, прижать ее руками;
      держать до приезда бригады СМП;
      5) при кровотечении живота, грудной клетки:
      наложить повязку из подручных средств (бинт), в несколько слоев;
      в случае если есть посторонние предметы в грудной или брюшной стенке – не трогать и не делайте попыток их извлечь;
      6) при кровотечении конечности:
      использовать в качестве жгута брючный ремень, ремень от сумки, галстук, ткань;
      наложить жгут выше места кровотечения;
      вставить под ткань короткую палку, прут и закрутить в 2-3 оборота до остановки кровотечения;
      наложить давящую повязку из подручных средств в несколько слоев.""",
                   "🦴💀При травме:":"""При травме:
      1) при безопасном местонахождении пострадавшего, если он в сознании и с дыханием вызвать экстренные службы;
      2) определить вид травмы: открытый или закрытый:
      при закрытой травме:
      1) приложить холод к месту повреждения через ткань в течении 10-15 минут;
      2) зафиксировать конечность подручными средствами;
      3) перевести пострадавшего в удобное положение;
      4) контролировать состояние пострадавшего до приезда СМП;
      при открытой травме:
      1) при кровотечении промыть рану чистой водой;
      2) наложить повязку из подручных средств (бинт), в несколько слоев;
      3) зафиксировать конечность подручными средствами;
      4) перевести пострадавшего в удобное положение;
      5) контролировать состояние пострадавшего до приезда СМП.
      При травме позвоночника необходимо зафиксировать голову на одной линии с корпусом, все время придерживая ее руками.
      В случае если есть посторонние предметы в грудной или брюшной части тела пострадавшего, при травме грудной клетки/живота - не трогать и не пытаться извлечь их.
      В случае если при травмах видны внутренние органы - закрыть влажной тканью, затем полиэтиленом, наложить тугую повязку из подручных средств.
      При продолжительном кровотечении, наложить жгут выше места кровотечения, используя подручные средства (брючный ремень, ремень от сумки, галстук, ткань).
      При наличии перелома, зафиксировать пострадавшего в исходном положении, до приезда бригады СМП""",
                   "🔥🔥🥵При термическом ожоге":"""При термическом ожоге:
      1) принять меры по устранению опасности, если невозможно – вызов экстренных служб;
      2) пострадавший в сознании, с дыханием и без сознания, без дыхания – базовая реанимация до приезда бригады СМП, вызов экстренных служб;
      3) определить повреждения на коже пострадавшего:
      при образовании на коже корочки серого или черного цвета провести:
      срезание одежды по краю ожоговой раны;
      наложение широкой, чистой и влажной повязки на рану;
      для сохранения влаги повязки использовать полиэтиленовый пакет;
      при наличии покраснения, отека и пузыря:
      охлаждение холодной водой не менее 15 минут;
      срезание одежды по краю ожоговой раны;
      наложение широкой, чистой и влажной повязки на рану;
      придать удобное положение пострадавшему;
      контролировать состояние пострадавшего до приезда СМП.""",
                   "🥶🥶🥶При обморожении":"""При обморожении:
      если пострадавший в сознании и с дыханием, осуществляется вызов экстренных служб, если отсутствуют сознание и дыхание – проводится базовая реанимация и вызов экстренных служб;
      переместить пострадавшего в теплое помещение;
      аккуратно снять одежду и обувь с пораженной области;
      дать теплое питье;
      постепенно согревать пораженную часть тела;
      наложить повязку из подручных средств на пораженные участки тела;
      контролировать состояние пострадавшего до приезда бригады СМП;
      нельзя растирать пораженные участки тела, втирать мази, масла, спирт;
      нельзя прикладывать к пораженным участкам тела горячие предметы (грелка, обогреватель и другие.);
      противопоказано употреблять алкогольные напитки.""",
                   "🤢🤮🧪При отравлении в зависимости от пути попадания яда":"""При отравлении в зависимости от пути попадания яда:
      1) если пострадавший в сознании и с дыханием осуществляется вызов экстренной службы, если отсутствуют сознание и дыхание – проводится базовая реанимация и вызов экстренной службы, контроль за состоянием пострадавшего до приезда бригады СМП;
      2) в случае попадания яда в организм пострадавшего через рот:
      дать выпить большое количество воды;
      перевести в восстановительное боковое положение (чтобы не захлебнуться рвотными массами);
      контролировать состояние пострадавшего до приезда бригады СМП;
      3) в случае попадания яда в организм пострадавшего через дыхательные пути:
      вывести пострадавшего на чистый воздух в безопасное место;
      обеспечить удобное положение;
      освободить от стесняющей одежды;
      контролировать состояние пострадавшего до приезда бригады СМП;
      4) в случае попадания яда в организм пострадавшего через кожу и слизистые поверхности:
      очистить поверхность кожи слизистой поверхности от ядовитого вещества подручными средствами (бинт);
      промыть кожу слизистую поверхность водой;
      контролировать состояние пострадавшего до приезда бригады СМП.
      Во всех случаях не вызывать рвоту и не давать слабительные средства при отравлении нефтепродуктами, кислотами, щелочью.
      При необходимости принять адсорбирующие препараты (активированный уголь и другие).""",
                   "🛌🛌🛌При обмороке":"""При обмороке:
      если пострадавший дышит, то вызвать экстренную помощь, если не дышит проводить базовую реанимацию, вызватьэкстренную помощь;
      уложить на спину и приподнять ноги;
      расстегнуть сдавливающие части одежды;
      обеспечить приток свежего воздуха;
      протереть лицо пострадавшего прохладной водой или положить мокрое полотенце на лоб;
      при наличии рвоты, повернуть голову на бок или перевести в восстановительное боковое положение (чтобы не захлебнуться рвотными массами);
      нельзя поднимать пострадавшего в вертикальное положение;
      контролировать состояние пострадавшего до приезда бригады СМП.""",
                   "😖😖😖При боли в груди":"""При боли в груди:
      если появилась сильная, жгучая, отдающая в руку или шею боль в груди:

      вызвать экстренные службы;
      в случае необходимости прекратить физическую деятельность;
      усадить пострадавшего в удобное положение;
      расстегнуть стесняющую одежду;
      контролировать состояние пострадавшего до приезда бригады СМП (при необходимости провести базовую реанимацию);""",
                   "😣😣😣При судороге":"""При судороге:
      при обнаружении пострадавшего с судорогами вызвать экстренную службу;
      не пытаться остановить приступ или насильно удерживать пострадавшего;
      убрать рядом находящиеся предметы, которые могут стать причиной травм;
      положить под голову мягкую подушку (любое подручное средство).
      В случае если судороги прекратились, пострадавший в сознании:
      не допускать резких движений со стороны пострадавшего;
      контролировать состояние пострадавшего до приезда бригады СМП.
      В случае если судороги не прекратились, пострадавший без сознания, но дышит:
      перевести в восстановительное (боковое) положение;
      контролировать состояние пострадавшего до приезда бригады СМП.
      В случае если судороги не прекратились, пострадавший без сознания и отсутствует дыхание проводится базовая реанимация до приезда бригады СМП""",
                   "🦊🪲🐍При укусе:":"""При укусе:
      1) принять меры по устранению опасности, если невозможно – вызов экстренной службы;
      2) если при обнаружении пострадавшего место безопасно для оказания первой помощи:
      пострадавший в сознании и с дыханием - вызвать экстренные службы;
      3) определить укус на теле пострадавшего;
      4) при обнаружении кровотечения: промыть рану водой, наложить давящую повязку из подручных средств (бинт), контролировать состояние пострадавшего до приезда бригады СМП;
      5) при отсутствии кровотечения: промыть рану водой, приложить холод к месту укуса, контролировать состояние пострадавшего до приезда бригады СМП;
      6) при укусах ядовитых змей нельзя отсасывать яд, делать надрез или применять жгуты;
      7) в местах укуса ос/пчел аккуратно удалить жало;
       в случае обнаружения отеков на месте укуса наложить холодный компресс.""",
                   "🚐🛻🚒Транспортировка пострадавшего":"""Транспортировка пострадавшего:
      1) если пострадавший находится в бессознательном состоянии, транспортируется в восстановительном (боковом) положении;
      2) при травме головы и шеи – на спине с валиками вокруг головы и с мягким валиком под шеей;
      3) при травме позвоночника – на твердых носилках на спине с валиками под шеей, поясницей и под коленями или на мягких носилках – на животе;
      4) при травме грудной клетки – полусидя с валиком под коленями или в восстановительном (боковом) положении на поврежденной стороне;
      5) при травме живота - в восстановительном (боковом) положении;
      6) при травме таза – на спине с валиком под коленями и слегка разведенными ногами.
      При отсутствии у пострадавшего сознания и дыхания проводятся базовые реанимационные меропрятия и обеспечивается вызов экстренных служб.""",                   
                   "Go Back":""}

main_menu_item2_video = {"Как обучиться по курсу ПромБез ИТР?":"./videos/IMG_6199.MP4",
                   "Как обучится по курсу БиОТ ИТР?": "./videos/kak_biot_itr.mp4"}


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    for item in main_menu:
             btn1 = types.InlineKeyboardButton(item)
             markup.row(item)  


    text="Добро пожаловать в бот безопасности! Выберите раздел, который вас интересует:"


    time.sleep(2)
    await message.answer(text, reply_markup=markup)
    

@dp.message_handler()
async def echo(message: types.Message):
     request = message.text        
     markup = types.ReplyKeyboardMarkup()
     if request == main_menu[0]:
        for item in main_menu_item0.keys():
             btn = types.InlineKeyboardButton(item)
             markup.row(btn)   
       
        await message.answer(request, reply_markup=markup)   
     elif request == main_menu[1]:
        for item in main_menu_item1.keys():
             btn = types.InlineKeyboardButton(item)
             markup.row(btn) 
        await message.answer(request, reply_markup=markup)  
     elif request == main_menu[2]:
        for item in main_menu_item2_video.keys():
             btn = types.InlineKeyboardButton(item)
             markup.row(btn) 
        await message.answer(request, reply_markup=markup)
     
    
 

# main_menu_item0 ответы
     if main_menu_item0.get(request): 
        await message.answer(main_menu_item0.get(request))  
        

# main_menu_item1 ответы     
     if main_menu_item1.get(request): 
        await message.answer(main_menu_item1.get(request))    

# main_menu_item2 ответы 
     if main_menu_item2_video.get(request): 
        with open(main_menu_item2_video.get(request), 'rb') as video:
            await message.answer_video(video)

# Go Back to main menu 
     if request == "Go Back":   
         markup = types.ReplyKeyboardMarkup()
         for item in main_menu:
            btn = types.InlineKeyboardButton(item)
            markup.row(btn)  
         await message.answer("Go Back", reply_markup=markup)

       




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