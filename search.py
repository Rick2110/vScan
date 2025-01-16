#!/usr/bin/python3

import shodan
import sys

token = 'pHHlgpFt8Ka3Stb5UlTxcaEwciOeF2QM'
def mainSearch(a):
    api = shodan.Shodan(a)
    resultado = api.search("windows OR linux OR GNU/linux")
    a = 0
    portas = [22,80,443,21,23,25,110,143,3306,3389,53,445]

    for resultados in resultado['matches']:
        if resultados['port'] in portas:
            print(resultados['ip_str'])
            if resultados['os'] == None:
                print("Sistema Operacional não foi encontrado")
            else:print(resultados['os'])
            a = a + 1
            print("")
        if a == 10:
            break


def search(t,value):
    api = shodan.Shodan(t)
    resultado = api.search(value)
    a = 1
    quant = len(value)

    for resultados in resultado['matches']:
        if resultados['os'][:quant + 1] == value:
            print(resultados['ip_str'])
            print(resultados['os'])
            print("")
            a = a + 1
        if a == 10:
            break
try:
    flag = sys.argv[1]
    arg2 = sys.argv[2]
    match flag:
        case '-h' | '--help':
            menuHelp()
        case '-s' | '--search':
            print("Fazendo a busca, aguarde...")
            search(token,arg2)
        case _:
            print("Formato inválido!")
            menuHelp()
except:
    mainSearch(token)
