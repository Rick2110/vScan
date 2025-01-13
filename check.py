#!/usr/bin/python3

import sys
import shodan
try:
    flag = sys.argv[1]
    arg2 = sys.argv[2]
except:
    a = 0

def menuHelp():
    print("API Shodan vScan help menu!\n\n          -h or --help = menu to commands and flags\n          -a or --api = Specify a single api for check\n          -f or --file = Select a file with list of APIs for check\n\nExample: ./check.py -a <Key>\n")

def checkApi(a):
    api = shodan.Shodan(a)
    conta = api.info()
    print(conta)
    if conta['plan'] == 'oss':
        print("Sua API faz parte de um plano gratuito! plano: "+conta['plan'])
    else:
        print("Sua API faz parte de um plano pago! plano: "+conta['plan'])
        with open("api.key","a") as apifile:
            apifile.write(a+"\n")

def checkFile(b):
    with open(b,'rb') as file:
        linhas = file.readlines()
    for i in linhas:
            token = i.decode('utf-8').strip()
            api = shodan.Shodan(token)
            try:
                conta = api.info()
            except shodan.exception.APIError:
                print("API invalida")
            if conta['plan'] != 'oss':
                print(f"API de conta paga {token}")
                with open(b,"a") as ler:
                    ler.write(token+"\n")

match flag:
    case "--help":
        menuHelp()
    case "-h":
        menuHelp()
    case "-a":
        checkApi(arg2)
    case "--api":
        checkApi(arg2)
    case "-f":
        checkFile(arg2)
    case "--file":
        checkFile(arg2)
    case _:
        print("Formato invalido")
        menuHelp()


