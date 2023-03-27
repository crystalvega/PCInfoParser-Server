import os

from command_runner.elevate import elevate
from mysql.connector.locales.eng import client_error

import Config
from GetConfiguration import Server


def main():
    check, error, config = Config.Check()
    if check:
        if config[4] == 'MySQL':
            Server.type = True
            Server.MySQL_User = config[5]
            Server.MySQL_Password = config[6]
            Server.MySQL_Host = config[7]
            Server.MySQL_Port = int(config[8])
        elif config[4] == 'XLSX':
            Server.type = False
        Server.key = config[2]
        Server.iv = config[3]
        backcode = Server.Start(config[0], int(config[1]))
        while True and backcode == 0:
            Server.Check()
    else:
        print(error)
    os.system("pause")
    
if __name__ == "__main__":
    elevate(main)