import openpyxl
import datetime

class Employee:
    dict_SBA = {}

    def __init__(self, employId, fullname):
        self.employId = employId
        self.fullname = fullname

    def __str__(self):
        return f"Employee ID: {self.employId}, Fullname: {self.fullname}"

    
    def set_SBA(self, course, title, last, next):
        if isinstance(last, datetime.datetime):
            datetime_object = datetime.datetime.strptime(str(last), "%Y-%m-%d %H:%M:%S")
            last = datetime_object.date()
        if isinstance(next, datetime.datetime):
            datetime_object = datetime.datetime.strptime(str(next), "%Y-%m-%d %H:%M:%S")
            next = datetime_object.date()
      
        self.dict_SBA[course] = [title, last, next]
        
    def get_SBA(self, course):
        return f"{self.dict_SBA.get(course)[0]}: Дата посл.прохождения/Last comp.date {self.dict_SBA.get(course)[1]}, Дата след.прохождения/Next comp.date {self.dict_SBA.get(course)[2]}"

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
        employee = Employee(row[0], row[1])
        employee.set_SBA('SBA061', 'Ответственный за изоляцию', row[2], row[3])
        employee.set_SBA('SBA130', 'Управление подрядными организациями', row[4], row[5])
        employee.set_SBA('SBA143', 'Контроль за состоянием лесов', row[6], row[7])
        employee.set_SBA('SBA106', 'Ответственные лица по надзору за безопасной эксплуатацией грузоподъемных кранов, подъемников, съемных грузозахватных приспособлений и тары (Каждые 3 года/Every 3 years)', row[8], row[9])
        employee.set_SBA('SBA107', 'Ответственные лица за безопасное производство работ кранами по перемещению грузов (ежегодно/annually)', row[10], row[11])
        employee.set_SBA('SBA108', 'Ответственные лица за содержание грузоподъемных кранов, крановых путей и подъемников в исправном состоянии (Каждые 3 года/Every 3 years)', row[12], row[13])
        employee.set_SBA('SBA053', 'Работники, допущенные к управлению самоходным телескопическим подъемником и автогидроподъемником ежегодно/annually', row[14], row[15])
        employee.set_SBA('SBA113', 'Персонал, имеющий смежную профессию Стропальщик ежегодно/annually', row[16], row[17])
        employee.set_SBA('SBA109', 'Персонал, имеющий смежную профессию рабочий с правом управления грузоподъемными механизмами с пола ежегодно/annually', row[18], row[19])
        employee.set_SBA('SBA054', 'Лица, допущенные к самостоятельной работе в качестве машиниста крана  ежегодно/annually', row[20], row[21])
        employee.set_SBA('SBA055', 'Работники, допущенные к управлению вилочным погрузчиком', row[22], row[23])
        employee.set_SBA('SBA137', 'ИТР, ответственный по надзору за техническим состоянием и эксплуатацией сосудов', row[24], row[25])
        employee.set_SBA('SBA147', 'ИТР, ответственный по надзору за безопасной эксплуатаций КС и СРД', row[26], row[27])
        employee.set_SBA('SBA029_1', 'ИТР Ответственные за исправное состояние и безопасное действие сосудов', row[28], row[29])
        employee.set_SBA('SBA146', 'ИТР Ответственный за исправное состояние КС и СРД', row[30], row[31])
        employee.set_SBA('SBA116_1', 'Ответственные за исп. сост. и безопасную эксплуатацию котлов', row[32], row[33])
        employee.set_SBA('SBA029', 'Ответственные за исп. сост. и безопасную экспл-ю трубопроводов', row[34], row[35])
        employee.set_SBA('SBA045', 'Лица, из числа обслуж.персонала с правом обслуживания сосудов и трубопроводов', row[36], row[37])
        employee.set_SBA('SBA114', 'Лица, допущенные к самостоятельному обслуж. КУ', row[38], row[39])
        employee.set_SBA('SBA116', 'Лица по обслуживанию котлов', row[40], row[41])
        employee.set_SBA('SBA023', 'ПромБез для работников', row[42], row[43])
        employee.set_SBA('SBA024', 'ПромБез для ИТР', row[44], row[45])
        employee.set_SBA('SBA034', 'БиОТ для ИТР', row[46], row[47])
        employee.set_SBA('SBA035', 'БиОТ для рабочих', row[48], row[49])
        employee.set_SBA('SBA036', 'ПТМ ежегодно', row[50], row[51])
        employee.set_SBA('SBA077', 'ПТМ один раз в три года', row[52], row[53])
        employees.append(employee)

    return employees

             





if __name__ == "__main__":
    filename = "//10.34.3.20/distr$/Telegram.xlsx"
    employees = print_table(filename)
    for emp in employees:
        if emp.employId == 11797:
            print(emp)
            print(emp.get_SBA('SBA061'))                                                                               
            print(emp.get_SBA('SBA130'))                                                                              
            print(emp.get_SBA('SBA143'))                                                                              
            print(emp.get_SBA('SBA106'))     
            print(emp.get_SBA('SBA107'))                                                                             
            print(emp.get_SBA('SBA108'))                                                                              
            print(emp.get_SBA('SBA053'))                                                                               
            print(emp.get_SBA('SBA113'))                                                                               
            print(emp.get_SBA('SBA109'))                                                                              
            print(emp.get_SBA('SBA054'))
            print(emp.get_SBA('SBA055'))  
            print(emp.get_SBA('SBA137'))  
            print(emp.get_SBA('SBA147'))  
            print(emp.get_SBA('SBA029_1'))                                                                            
            print(emp.get_SBA('SBA146'))                                                                          
            print(emp.get_SBA('SBA116_1'))                                                                             
            print(emp.get_SBA('SBA029'))                                                                           
            print(emp.get_SBA('SBA045'))                                                                             
            print(emp.get_SBA('SBA114'))                                                                               
            print(emp.get_SBA('SBA116'))                                                                               
            print(emp.get_SBA('SBA023'))           
            print(emp.get_SBA('SBA024'))    
            print(emp.get_SBA('SBA034')) 
            print(emp.get_SBA('SBA035'))     
            print(emp.get_SBA('SBA036')) 
            print(emp.get_SBA('SBA077'))  


