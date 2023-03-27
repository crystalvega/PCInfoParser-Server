def load_tableparametras():
    create_allconf_table = """
    CREATE TABLE `all configuration` 
    (
        `Кабинет`	VARCHAR(512),
        `LAN`	VARCHAR(512),
        `ФИО`	VARCHAR(512),
        `Монитор`	VARCHAR(512),
        `Диагональ`	VARCHAR(512),
        `Тип принтера`	VARCHAR(512),
        `Модель принтера`	VARCHAR(512),
        `ПК`	VARCHAR(512),
        `Материнская плата`	VARCHAR(512),
        `Процессор`	VARCHAR(512),
        `Частота процессора`	VARCHAR(512),
        `Баллы Passmark`	VARCHAR(512),
        `Дата выпуска`	VARCHAR(512),
        `Тип ОЗУ`	VARCHAR(512),
        `ОЗУ, 1 Планка`	VARCHAR(512),
        `ОЗУ, 2 Планка`	VARCHAR(512),
        `ОЗУ, 3 Планка`	VARCHAR(512),
        `ОЗУ, 4 Планка`	VARCHAR(512),
        `Сокет`	VARCHAR(512),
        `Диск 1`	VARCHAR(512),
        `Состояние диска 1`	VARCHAR(512),
        `Диск 2`	VARCHAR(512),
        `Состояние диска 2`	VARCHAR(512),
        `Диск 3`	VARCHAR(512),
        `Состояние диска 3`	VARCHAR(512),
        `Диск 4`	VARCHAR(512),
        `Состояние диска 4`	VARCHAR(512),
        `Операционная система`	VARCHAR(512),
        `Антивирус`	VARCHAR(512),
        `CPU Под замену`	VARCHAR(512),
        `Все CPU под сокет`	LONGTEXT
    );
    """
    
    create_diskconf_table = """
    CREATE TABLE `disk configuration` 
    (
        `Кабинет`	VARCHAR(512),
        `LAN`	VARCHAR(512),
        `ФИО`	VARCHAR(512),
        `Диск`	VARCHAR(512),
        `Наименование`	VARCHAR(512),
        `Прошивка`	VARCHAR(512),
        `Размер`	VARCHAR(512),
        `Время работы`	VARCHAR(512),
        `Включён`	VARCHAR(512),
        `Состояние`	VARCHAR(512)
    );
    """
    return create_allconf_table, create_diskconf_table

def gen_execute_disk(List, tablename):
    #List = (('Автозаполнение', 'V'), ('Кабинет', '27'), ('LAN', '172.16.85.215'), ('ФИО', 'Мальцев Василий Юдофеевич'), (('Диск', 1), ('Наименование', 'WDC WD5000LPCX-21VHAT0'), ('Прошивка', '01.01A01'), ('Размер', '500,1 GB'), ('Время работы', '3805 Часов'), ('Включён', '724 Раз'), ('Состояние', 'Good')), (('Диск', 2), ('Наименование', 'AMD R5SL240G'), ('Прошивка', 'V0718B0'), ('Размер', '240,0 GB'), ('Время работы', '2373 Часов'), ('Включён', '8 Раз'), ('Состояние', 'Good (100 %)')), (('Диск', 3), ('Наименование', 'Corsair Force GT'), ('Прошивка', '5.02'), ('Размер', '90,0 GB'), ('Время работы', '42954 Часов'), ('Включён', '1627 Раз'), ('Состояние', 'Good (95 %)')))
    execute_charters = []
    defpar1 = ['']*3
    defpar2 = ['']*3
    disknumbs = len(List)-3
    for i in range(0,3):
        defpar1[i] = List[i][0]
        defpar2[i] = List[i][1]
    List = List[3:]
    for i in range(0,disknumbs):
        execute_charters.append("INSERT INTO `" + tablename + "`(`")
        values_charters_set = ""
        for i2 in defpar1:
                execute_charters[i] = execute_charters[i] + str(i2) +  "`, `"
        for i2 in defpar2:
                values_charters_set = values_charters_set + "'" + str(i2) + "', "
    
    for i in range(0,disknumbs):
        values_charters = values_charters_set
        for par in List[i]:
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

def load_executeparametras(charters, disk):
    execute_charters = gen_execute_params(charters, "all configuration")
    execute_disk = gen_execute_disk(disk, "disk configuration")
    return execute_charters, execute_disk