import openpyxl
import datetime

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
            'SBA106': f"Ответственные лица по надзору за безопасной эксплуатацией грузоподъемных кранов, подъемников, съемных грузозахватных приспособлений и тары (Каждые 3 года/Every 3 years): Дата посл.прохождения {trim_date(self.dates[6])}, Дата след.прохождения {trim_date(self.dates[7])}",             
            'SBA107': f"Ответственные лица за безопасное производство работ кранами по перемещению грузов (ежегодно/annually): Дата посл.прохождения {trim_date(self.dates[8])}, Дата след.прохождения {trim_date(self.dates[9])}",             
            'SBA108': f"Ответственные лица за содержание грузоподъемных кранов, крановых путей и подъемников в исправном состоянии (Каждые 3 года/Every 3 years): Дата посл.прохождения {trim_date(self.dates[10])}, Дата след.прохождения {trim_date(self.dates[11])}",             
            'SBA053': f"Работники, допущенные к управлению самоходным телескопическим подъемником и автогидроподъемником ежегодно/annually: Дата посл.прохождения {trim_date(self.dates[12])}, Дата след.прохождения {trim_date(self.dates[13])}",             
            'SBA113': f"Персонал, имеющий смежную профессию Стропальщик ежегодно/annually: Дата посл.прохождения {trim_date(self.dates[14])}, Дата след.прохождения {trim_date(self.dates[15])}",             
            'SBA109': f"Персонал, имеющий смежную профессию рабочий с правом управления грузоподъемными механизмами с пола ежегодно/annually: Дата посл.прохождения {trim_date(self.dates[16])}, Дата след.прохождения {trim_date(self.dates[17])}",             
            'SBA054': f"Лица, допущенные к самостоятельной работе в качестве машиниста крана  ежегодно/annually: Дата посл.прохождения {trim_date(self.dates[18])}, Дата след.прохождения {trim_date(self.dates[19])}",             
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
            }
        return sba[course]
    
   

def trim_date(date):
    if isinstance(date, datetime.datetime):
        datetime_object = datetime.datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
        return datetime_object.date()  

def print_table(filename):
    # Открываем файл Excel
    workbook = openpyxl.load_workbook(filename)

    # Получаем лист
    sheet = workbook.active

    # Цикл по строкам
    all_rows = []
    for row in sheet.iter_rows(min_row=3):
        # Цикл по столбцам
        row_data = []
        for cell in row:
            row_data.append(cell.value)
        all_rows.append(row_data)
    employees = []
    for row in all_rows:
        employee = Employee(row[0], row[1], row[2:])       
        employees.append(employee)

    return employees

             





if __name__ == "__main__":
    filename = "//10.34.3.20/distr$/Telegram.xlsx"
    employees = print_table(filename)
    for emp in employees:
        if emp.employId == 395:
            print(emp) 
            print(emp.get_sba('SBA061'))
            print(emp.get_sba('SBA130'))
           # print(f"Ответственный за изоляцию: Дата посл.прохождения {trim_date(emp.dates[0])}, Дата след.прохождения {trim_date(emp.dates[1])}")


