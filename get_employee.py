import pandas
import datetime
import os


class Employee:
    dict_SBA = {}
    dates = []
    def __init__(self, employId, fullname, dates):
        self.employId = employId
        self.fullname = fullname
        self.dates = dates
        
    def __str__(self):
        return f"Таб №: {self.employId}, ФИО: {self.fullname}"
    
    def get_sba(self, course):
        sba = {
            'SBA061': f"Ответственный за изоляцию: Дата посл.прохождения {trim_date(self.dates[0])}, Дата след.прохождения {trim_date(self.dates[1])}",            
            'SBA130': f"Управление подрядными организациями: Дата посл.прохождения {trim_date(self.dates[2])}, Дата след.прохождения {trim_date(self.dates[3])}",             
            'SBA143': f"Контроль за состоянием лесов: Дата посл.прохождения {trim_date(self.dates[4])}, Дата след.прохождения {trim_date(self.dates[5])}",             
            'SBA106': f"Ответственные лица по надзору за безопасной эксплуатацией грузоподъемных кранов, подъемников, съемных грузозахватных приспособлений и тары (Каждые 3 года): Дата посл.прохождения {trim_date(self.dates[6])}, Дата след.прохождения {trim_date(self.dates[7])}",             
            'SBA107': f"Ответственные лица за безопасное производство работ кранами по перемещению грузов (ежегодно): Дата посл.прохождения {trim_date(self.dates[8])}, Дата след.прохождения {trim_date(self.dates[9])}",             
            'SBA108': f"Ответственные лица за содержание грузоподъемных кранов, крановых путей и подъемников в исправном состоянии (Каждые 3 года): Дата посл.прохождения {trim_date(self.dates[10])}, Дата след.прохождения {trim_date(self.dates[11])}",             
            'SBA053': f"Работники, допущенные к управлению самоходным телескопическим подъемником и автогидроподъемником ежегодно: Дата посл.прохождения {trim_date(self.dates[12])}, Дата след.прохождения {trim_date(self.dates[13])}",             
            'SBA113': f"Персонал, имеющий смежную профессию Стропальщик ежегодно: Дата посл.прохождения {trim_date(self.dates[14])}, Дата след.прохождения {trim_date(self.dates[15])}",             
            'SBA109': f"Персонал, имеющий смежную профессию рабочий с правом управления грузоподъемными механизмами с пола ежегодно: Дата посл.прохождения {trim_date(self.dates[16])}, Дата след.прохождения {trim_date(self.dates[17])}",             
            'SBA054': f"Лица, допущенные к самостоятельной работе в качестве машиниста крана  ежегодно: Дата посл.прохождения {trim_date(self.dates[18])}, Дата след.прохождения {trim_date(self.dates[19])}",             
            'SBA055': f"Работники, допущенные к управлению вилочным погрузчиком: Дата посл.прохождения {trim_date(self.dates[20])}, Дата след.прохождения {trim_date(self.dates[21])}",             
            'SBA137': f"ИТР, ответственный по надзору за техническим состоянием и эксплуатацией сосудов: Дата посл.прохождения {trim_date(self.dates[22])}, Дата след.прохождения {trim_date(self.dates[23])}",             
            'SBA147': f"ИТР, ответственный по надзору за безопасной эксплуатаций КС и СРД: Дата посл.прохождения {trim_date(self.dates[24])}, Дата след.прохождения {trim_date(self.dates[25])}",             
            'SBA029_1': f"ИТР Ответственные за исправное состояние и безопасное действие сосудов: Дата посл.прохождения {trim_date(self.dates[26])}, Дата след.прохождения {trim_date(self.dates[27])}",             
            'SBA146': f"ИТР Ответственный за исправное состояние КС и СРД: Дата посл.прохождения {trim_date(self.dates[28])}, Дата след.прохождения {trim_date(self.dates[29])}",             
            'SBA116_1': f"Ответственные за исп. сост. и безопасную эксплуатацию котлов: Дата посл.прохождения {trim_date(self.dates[30])}, Дата след.прохождения {trim_date(self.dates[31])}",             
            'SBA029': f"Ответственные за исп. сост. и безопасную экспл-ю трубопроводов: Дата посл.прохождения {trim_date(self.dates[32])}, Дата след.прохождения {trim_date(self.dates[33])}",             
            'SBA045': f"Лица, из числа обслуж.персонала с правом обслуживания сосудов и трубопроводов: Дата посл.прохождения {trim_date(self.dates[34])}, Дата след.прохождения {trim_date(self.dates[35])}",             
            'SBA114': f"Лица, допущенные к самостоятельному обслуж. КУ: Дата посл.прохождения {trim_date(self.dates[36])}, Дата след.прохождения {trim_date(self.dates[37])}",             
            'SBA116': f"Лица по обслуживанию котлов: Дата посл.прохождения {trim_date(self.dates[38])}, Дата след.прохождения {trim_date(self.dates[39])}",             
            'SBA023': f"ПромБез для работников: Дата посл.прохождения {trim_date(self.dates[40])}, Дата след.прохождения {trim_date(self.dates[41])}",             
            'SBA024': f"ПромБез для ИТР: Дата посл.прохождения {trim_date(self.dates[42])}, Дата след.прохождения {trim_date(self.dates[43])}",             
            'SBA034': f"БиОТ для ИТР: Дата посл.прохождения {trim_date(self.dates[44])}, Дата след.прохождения {trim_date(self.dates[45])}",             
            'SBA035': f"БиОТ для рабочих: Дата посл.прохождения {trim_date(self.dates[46])}, Дата след.прохождения {trim_date(self.dates[47])}",             
            'SBA036': f"ПТМ ежегодно: Дата посл.прохождения {trim_date(self.dates[48])}, Дата след.прохождения {trim_date(self.dates[49])}",             
            'SBA077': f"ПТМ один раз в три года: Дата посл.прохождения {trim_date(self.dates[50])}, Дата след.прохождения {trim_date(self.dates[51])}",  
            
            'SBA003': f"Выявление опасных факторов: Дата посл.прохождения {trim_date(self.dates[52])}, Дата след.прохождения {trim_date(self.dates[53])}",
            'SBA001': f"Первая помощь: Дата посл.прохождения {trim_date(self.dates[54])}, Дата след.прохождения {trim_date(self.dates[55])}",
            'SBA033': f"Наряд-допуск: Дата посл.прохождения {trim_date(self.dates[56])}, Дата след.прохождения {trim_date(self.dates[57])}",
            'SBA007': f"Анализ безопасности работ: Дата посл.прохождения {trim_date(self.dates[58])}, Дата след.прохождения {trim_date(self.dates[59])}",            
            'SBA138': f"ICAM факторов: Дата посл.прохождения {trim_date(self.dates[60])}, Дата след.прохождения {trim_date(self.dates[61])}",
            'SBA022': f"Safety Leadership: Дата посл.прохождения {trim_date(self.dates[62])}, Дата след.прохождения {trim_date(self.dates[63])}",            
            'SBA060': f"Владелец личного замка: Дата посл.прохождения {trim_date(self.dates[64])}, Дата след.прохождения {trim_date(self.dates[65])}",            
            'SBA009': f"Работы на высоте: Дата посл.прохождения {trim_date(self.dates[66])}, Дата след.прохождения {trim_date(self.dates[67])}",
            
            'EL01': f"Электробез 1 группа {trim_date(self.dates[68])}, Дата след.прохождения {trim_date(self.dates[69])}",
            'EL02': f"Электробез 2 группа {trim_date(self.dates[70])}, Дата след.прохождения {trim_date(self.dates[71])}",
            'EL03': f"Электробез 3 группа {trim_date(self.dates[72])}, Дата след.прохождения {trim_date(self.dates[73])}",
            'EL04': f"Электробез 4 группа {trim_date(self.dates[74])}, Дата след.прохождения {trim_date(self.dates[75])}",
            'EL05': f"Электробез 5 группа {trim_date(self.dates[76])}, Дата след.прохождения {trim_date(self.dates[77])}",
            
            'DRV': f"Право на вождение по сайту {trim_date(self.dates[78])}, Дата след.прохождения {trim_date(self.dates[79])}",
            'DRVM': f"Допуск в карьер {trim_date(self.dates[80])}, Дата след.прохождения {trim_date(self.dates[81])}",
            'ABC': f"Антикоррупционные политики {trim_date(self.dates[80])}, Дата след.прохождения {trim_date(self.dates[81])}",

            }
        return sba[course]
    
   

def trim_date(date):
    if isinstance(date, datetime.datetime):
        datetime_object = datetime.datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
        return datetime_object.date().strftime("%d.%m.%Y")
    return date

def print_table(filename):
    df = pandas.read_excel(filename, sheet_name='ПромБеЗ общие курсы')
        # Поместить данные первой строки в массив
    sheet = df.to_numpy()
    all_rows = []
    for row in sheet[1:]:
        # Цикл по столбцам
        row_data = []
        for cell in row:
            row_data.append(cell)
        all_rows.append(row_data)
    employees = []
    for row in all_rows:
        employee = Employee(row[0], row[1], row[2:])       
        employees.append(employee)
    return employees

             





if __name__ == "__main__":
   # filename = "//10.34.3.20/distr$/Telegram.xlsx"
    
    filename = "//10.34.3.176/T&D$/04 - HSE Training - Обучение ОТиТБ/04-20 Reports/Отчеты по внутренним курсам/Telegram.xlsx"
    if os.path.exists(filename) and os.path.isfile(filename):        
        employees = print_table(filename)
        for emp in employees:
            if emp.employId == 7833:
                print(emp) 
                print(emp.get_sba('SBA061'))
  


