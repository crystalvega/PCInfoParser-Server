import codecs
import pickle
import socket
from _thread import *
import asyncio

import mysql.connector
from Crypto.Cipher import AES

from GetConfiguration import API
from OutputConfiguration import MySQL
from OutputConfiguration import WorkBook as wb

ThreadCount = 0
ipport = ''
disk = []
charters = []
ServerSocket = socket.socket()
socket.setdefaulttimeout(25)
type = False
MySQL_User = ''
MySQL_Password = ''
MySQL_Host = ''
MySQL_Port = ''
key = ''
iv = ''
cnx = ''

unpad = lambda s : s[0:-ord(s[-1])]

def mysqlconnect():
    try:
        global cnx
        cnx = mysql.connector.connect(
            host=MySQL_Host,
            port=MySQL_Port,
            user=MySQL_User,
            password=MySQL_Password,
            auth_plugin='mysql_native_password',
            )
        print('Подключение к MYSQL произошло успешно')
        global cursor
        cursor = cnx.cursor()
        return 0
    except mysql.connector.errors.DatabaseError:
        print('Не удалось подключиться к MySQL')
        return 1001
    except mysql.connector.errors.InterfaceError:
        print('Не удалось подключиться к MySQL')
        return 1002


def do_decrypt(ciphertext):
    try:
        obj2 = AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
        message = obj2.decrypt(ciphertext)
        message = message.decode('utf-8')
        padmsg = unpad(message)
        return padmsg
    except UnicodeDecodeError:
        return 'Error'

def mysql_createtables(filename):
    allconfcreate, diskconfcreate = MySQL.load_tableparametras(filename)
    try:
        cursor.execute(allconfcreate)
    except mysql.connector.errors.ProgrammingError as e:
        Exception
    try:
        cursor.execute(diskconfcreate)
    except mysql.connector.errors.ProgrammingError as e:
        Exception
    cnx.commit()
        
def mysql_execute(charters, disk,filename):
    executecharters, executedisks = MySQL.load_executeparametras(charters, disk, filename)
    cursor.execute(executecharters.encode('UTF8'))
    for executedisk in executedisks:
        cursor.execute(executedisk.encode('UTF8'))
    cnx.commit()

def mysql_checkandcreatedatabase(filename):
    try:
        execute = 'CREATE DATABASE `' + filename + '`;'
        cursor.execute(execute.encode('UTF8'))
    except mysql.connector.errors.DatabaseError:
        Exception
    mysql_createtables(filename)

def wb_configuration(filename, charters, disk):
    wb.fileName = filename + ".xlsx"
    wb.allconfiguration = charters
    wb.diskconfiguration = disk
    wb.create()
    wb.wb, wb.sheet1, wb.sheet2 = wb.init()
    wb.rowinputall, wb.rowinputdisk = wb.checklastrecord()
    wb.configuration()
    rowin, rowend = wb.configurationdisk()
    wb.create_hyperlink(rowin, rowend)
    charters = []
    disk = []
    wb.close()

def takecheck(connection):
    message = b''
    while True:
        message_raw = connection.recv(4096)
        if message_raw != b'end':
            message = message + message_raw
            connection.send('1'.encode('utf-8'))
        else:
            connection.send('1'.encode('utf-8'))
            return message

def client_handler(connection, ipport):
    asyncio.run(client_handler_async(connection, ipport))

async def client_handler_async(connection, ipport):
    asyncio.create_task(run(connection, ipport))
   
async def run(connection, ipport):
    try:
        connection.send(str.encode('Вы были подключены к серверу.'))
        while True:
            dataencrypt = takecheck(connection)
            data = do_decrypt(dataencrypt)
            if data == "Error":
                        print('Подключение с ' + ipport + ' было разорвано из-за неверного ключа')
                        connection.close()
                        break
            message = pickle.loads(codecs.decode(data.encode(), "base64"))
            if message[0] == 'CONF':
                message[0] = ["Автозаполнение", "V"]
                charters = message
            if message[0] == 'FILENAME':
                filename = message[1]
                filename.title()
            if message[0] == 'DISK':
                message[0] = ["Автозаполнение", "V"]
                disk = message
            if message == 'END INFO':
                print('Сбор информации с ' + ipport + ' завершен успешно')
                if type:
                    if (cnx.is_connected()):
                        del charters[0]
                        del disk[0]
                        mysql_checkandcreatedatabase(filename)
                        mysql_execute(charters, disk, filename)
                    else:
                        print("Отсутсвует подключение к MySQL. Попытка переподключиться...")
                        error = mysqlconnect()
                        if error != 0:
                            break
                else:
                    wb_configuration(filename, charters, disk)
                print('Запись данных прошла успешно')
                break
            reply = f'Сервер: {message}'
            connection.sendall(pickle.dumps(reply))
    except WindowsError as error:
        print(error)
        print('Подключение с ' + ipport + ' было разорвано')
    connection.close()
        
def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print('Проверка подключения к ' + address[0] + ':' + str(address[1]))
    request, reason = API.Check(address[0])
    print(reason)
    if request:
        print('Подключено к ' + address[0] + ':' + str(address[1]))
        ipport = address[0] + ':' + str(address[1])
        start_new_thread(client_handler, (Client, ipport, ))
    else:
        print('Подключение с ' + address[0] + ':' + str(address[1]) + ' разорвано')

def Start(host, port):
    returnvalue = 0
    if type == True:
        returnvalue = mysqlconnect()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Сервер запущен на порте {port}')
    ServerSocket.listen()
    return returnvalue
    
def Check():
    accept_connections(ServerSocket)