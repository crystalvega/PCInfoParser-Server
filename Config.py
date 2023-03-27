from pathlib import Path
check_lines = ['ip','port','key','iv','ServerType','MySQL_User','MySQL_Password','MySQL_Host','MySQL_Port']
name = 'server.cfg'

def Parse():
    config = [None]*len(check_lines)
    if Path('.\\' + name).is_file() == False:
        default_lines = ['#ServerType можно указать только "XLSX" и "MySQL"','ip = 0.0.0.0','port = Не задан','key = Не задан','iv = Не задан','ServerType = XLSX', 'MySQL_Host = localhost', 'MySQL_Port = 3306', 'MySQL_User = Не задан', 'MySQL_Password = Не задан']
        with open('.\\' + name, "w") as file:
            for line in default_lines:
                file.write(line+'\n')
    with open('.\\' + name, "r") as file:
        for line in file:
            for index, check  in enumerate(check_lines):
                if check+' = ' in line:
                    if line != check +' = Не задан\n':
                        config[index] = line.replace(check+' = ','').replace('\n','')

    return config

def Check():
    config = Parse()
    check = True
    Return = 'Укажите в ' + name + ': '
    for index in range(0,len(config)):
        if index == 4:
            if config[index] == "XLSX":
                config[5] = 'Не нужен'
                config[6] = 'Не нужен'
                config[7] = 'Не нужен'
                config[8] = 'Не нужен'
                print('Тип БД: XLSX')
            elif config[index] == "MySQL":
                print('Тип БД: MySQL')
            else:
                config[index] = None
                config[5] = 'Не нужен'
                config[6] = 'Не нужен'
                config[7] = 'Не нужен'
                config[8] = 'Не нужен'
        if config[index] == None and Return.endswith(': '):
            Return = Return + check_lines[index]
            check = False
        elif config[index] == None:
            Return = Return + ', ' + check_lines[index]
    return check, Return, config