import os
from pathlib import Path
import easygui as g

def start(fileName):
    checking = False
    fileObj = Path(fileName)
    checking = fileObj.is_file()
    fin = []
    if checking == False:
        list1 = ["ФИО", "Кабинет(номер)", "Принтер(принтер, МФУ, копир)", "Устройство(ПК, ноутбук, моноблок)"]
        fin = g.multenterbox("Введите ФИО, номер кабинета, тип принтера(Принтер, МФУ, Копир) и устройство(ПК, Ноутбук, Моноблок)",title = 'Ввод данных о пользователе',fields = (list1), )
        if fin is None:
            fin = ['None', 'None', 'None', 'None']
        else:
            os.mkdir("C:\Program Files\ConfigNKU")
            with open(fileName, "w") as file:
                    print("\n".join(map(str, fin)), file=file)
    else:
        i = 0
        fileopen = open(fileName, 'r')
        for line in fileopen:
            fin.append(line)
    for index, line  in enumerate(fin):
        fin[index] = line.rstrip('\n')
    return fin

def success():
    g.msgbox("Операция завершена успешно!","Оповещение")
    
def Error():
    g.msgbox("Операция не может быть совершена из-за открытого Excel документа!","Оповещение")