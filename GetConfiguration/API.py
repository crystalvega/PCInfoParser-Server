import json
import socket
import urllib.request

from GetConfiguration import Whitelist

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localip = s.getsockname()[0]
localip = localip.split('.')
localip = localip[0] + '.' + localip[1] + '.' + localip[2] + '.'

def LocalCheck(ip):
    if localip in ip or ip == "127.0.0.1":
        return True
    else:
        return False

def Get(ip):
    response = urllib.request.urlopen('http://ipwho.is/' + ip)
    whoisJSON = json.load(response)
    whoisData = whoisJSON.items()
    whoisList = list(whoisData)
    if not "country" in whoisList:
        whoisList.append(("country",None))
    return whoisList


def Check(ip):
    clientinfo = Get(ip)
    for item in clientinfo:
        if item[0] == "country":
            country = item[1]
            break
    wlcheck = Whitelist.Check(ip)
    localcheck = LocalCheck(ip)
    if wlcheck == True:
        return True, "IP в Whitelist"
    elif localcheck:
        return True, "Подключение из локальной сети"
    elif country == "Russia":
        return True, "Подключение с России"
    elif country == None:
        return False, "Не удалось определить страну. Если вы подключаетесь с локальной сети, пожалуйста, добавьте ваш локальный IP в Whitelist"
    else:
        return False, "Подключение разорвано. IP нет в Whitelist и он не из России"
    