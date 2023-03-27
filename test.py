def gen_execute_disk(List, tablename):
    execute_charters = []
    disknumbs = 0
    defpar1 = ['']*3
    defpar2 = ['']*3
    disknumbs = len(List)-4
    for i in range(0,3):
        defpar1[i] = List[i][0]
        defpar2[i] = List[i][1]
    List = List[3:]
    for i in range(0,disknumbs+1):
        execute_charters.append("INSERT INTO `" + tablename + "`(`")
        values_charters = ""
        for i2 in defpar1:
                execute_charters[i] = execute_charters[i] + str(i2) +  "`, `"
        for i2 in defpar2:
                values_charters = values_charters + "'" + str(i2) + "', "
    
    for i in range(0,disknumbs+1):
        values_charters = ""
        for params in List:
            for par in params:
                execute_charters[i] = execute_charters[i] + str(par[0]) +  "`, `"
                values_charters = values_charters + "'" + str(par[1]) + "', "
            values_charters = values_charters[:-2] + ");"
        execute_charters[i] = execute_charters[i][:-3] + ") VALUES (" + values_charters
    return execute_charters

def gen_execute_params(List, tablename):
    execute_charters = "INSERT INTO `" + tablename + "`(`"
    values_charters = ""
    for params in List:
            execute_charters = execute_charters + str(params[0]) +  "`, `"
            values_charters = values_charters + "'" + str(params[1]) + "', "
    values_charters = values_charters[:-2] + ");"
    execute_charters = execute_charters[:-3] + ") VALUES (" + values_charters
    return execute_charters


disk = [('Автозаполнение', 'V'), ('Кабинет', '27'), ('ФИО', 'Мальцев Василий Юдофеевич'), (('Диск', 1), ('Наименование', 'WDC WD5000LPCX-21VHAT0'), ('Прошивка', '01.01A01'), ('Размер', '500,1 GB'), ('Время работы', '3805 Часов'), ('Включён', '724 Раз'), ('Состояние', 'Good')), (('Диск', 2), ('Наименование', 'AMD R5SL240G'), ('Прошивка', 'V0718B0'), ('Размер', '240,0 GB'), ('Время работы', '2373 Часов'), ('Включён', '8 Раз'), ('Состояние', 'Good (100 %)')), (('Диск', 3), ('Наименование', 'Corsair Force GT'), ('Прошивка', '5.02'), ('Размер', '90,0 GB'), ('Время работы', '42954 Часов'), ('Включён', '1627 Раз'), ('Состояние', 'Good (95 %)'))]
conf = [('Автозаполнение', 'V'), ('Кабинет', 'Серверная'), ('LAN', '172.16.85.202'), ('ФИО', 'Бельтюков Дмитрий Михайлович'), ('Монитор', 'Acer Technologies EK220Q'), ('Диагональ', 21.5), ('Тип принтера', 'МФУ'), ('Модель принтера', 'WorkCentre 5020/DN'), ('ПК', 'ПК'), ('Материнская плата', 'Micro-Star International Co., Ltd. PRO H610M-E DDR4 (MS-7D48)'), ('Процессор', '12th Gen Intel(R) Core(TM) i3-12100'), ('Частота процессора', '3300 МГц'), ('Баллы Passmark', 14297), ('Дата выпуска', 2022), ('Тип ОЗУ', 'DDR4'), ('ОЗУ, 1 Планка', '8 ГБ'), ('ОЗУ, 2 Планка', '8 ГБ'), ('ОЗУ, 3 Планка', ''), ('ОЗУ, 4 Планка', ''), ('Сокет', 'LGA1700'), ['Диск 1', 'Patriot Burst Elite 480GB'], ['Состояние диска 1', 'Good (100 %)'], ['Диск 2', ''], ['Состояние диска 2', ''], ['Диск 3', ''], ['Состояние диска 3', ''], ['Диск 4', ''], ['Состояние диска 4', ''], ('Операционная система', 'Майкрософт Windows 11 Pro'), ('Антивирус', 'Windows Defender  '), ('CPU Под замену', 'Intel Core i9-13900KF'), ('Все CPU под сокет', 'Intel Core i3-12100F, Intel Core i3-12300, Intel Core i5-12400T, Intel Core i5-12600T, Intel Core i5-12500T, Intel Core i5-12500TE, Intel Core i5-12400, Intel Core i5-12400F, Intel Core i5-12500, Intel Core i7-12700TE, Intel Core i5-12490F, Intel Core i5-12600, Intel Core i7-12700T, Intel Core i5-12600KF, Intel Core i5-12600K, Intel Core i7-12700E, Intel Core i7-12700, Intel Core i7-12700F, Intel Core i9-12900E, Intel Core i9-12900T, Intel Core i7-12700KF, Intel Core i7-12700K, Intel Core i9-12900, Intel Core i9-12900F, Intel Core i5-13600KF, Intel Core i5-13600K, Intel Core i9-12900KF, Intel Core i9-12900K, Intel Core i9-12900KS, Intel Core i7-13700KF, Intel Core i7-13700K, Intel Core i9-13900K, Intel Core i9-13900KF')]

params = gen_execute_params(conf, 'configuration')
disk = gen_execute_disk(disk, 'configuration')
print(1)