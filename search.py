#!/usr/bin/python3

import shodan
import sys

token = 'pHHlgpFt8Ka3Stb5UlTxcaEwciOeF2QM'
def mainSearch(a):
    api = shodan.Shodan(a)
    resultado = api.search("windows OR linux OR GNU/linux")
    a = 1

    for resultados in resultado['matches']:
        print(resultados['ip_str'])
        if resultados['os'] == None:
            print("Sistema Operacional não foi encontrado")
        else:print(resultados['os'])
        print("")

        if a == 10:
            break
        a = a + 1

try:
    flag = sys.argv[1]
    match flag:
        case '-h' | '--help':
            menuHelp()
        case _:
            print("Formato inválido!")
            menuHelp()
except:
    mainSearch(token)
