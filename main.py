# -*- coding: utf-8 -*-

import os
import time as tm
import pandas
import platform
from threading import Thread as Th
from termcolor import colored

# Modules ---------
from tools.content import Server as S
from tools.content import ServerLocal
from dialog.dialog import Dialog as msg
from modules.system.system import MainSystem

def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()


def entry():
    data = input('#'+colored('|set|', 'yellow')+'#>'+' ')
    return data


def response(data):
    return data


class Main(object):

    _MainSystem = MainSystem()

    _USUARIO = None
    _SESSION_NAME = None

    _DEBUG = False

    def __init__(self):
        pass

    def commands(self, commit):
        if commit.lower() == 'server':
            server = S()
            server.build('0.0.0.0', 5003)
            server.run()

        elif commit.lower() == 'exit':
            os.system('clear')
            print('Fechando aplicação!')
            return exit()

        elif commit.lower() == 'login':
            return print('Em desenvolvimento....')

        elif commit.lower() == 'help':
            return print('Em desenvolvimento....')

        elif commit.lower() == 'gitconfig':
            return print('Em desenvolvimento....')

        elif commit.lower() == 'herokuconfig':
            return print('Em desenvolvimento....')

        elif commit.lower() == 'server web local':
            obj = ServerLocal('teste')
            thred = Th(target=obj.start_server)
            thred.start()

        elif commit.lower() == 'hydra':
            from tools.hydra import THC_hydra
            hydra = THC_hydra()
            print('Verificando hydra no sistema Operacional...')



    def methodos(self, argv):
        triggers = {
            'commands': [

                'data',
                'server',
                'hydra',
                'help',
                'exit',
                'login',
                'gitconfig',
                'herokuconfig',
                'server web local',

            ],
        }

        # Avaliando comandos enviados ...
        for cmd in triggers['commands']:
            if argv == cmd:
                return self.commands(commit=cmd)

            if not argv in triggers['commands']:
                return print(colored('[-]', 'red'), colored('Comando não encontrado...', 'yellow'))

# Processos de lógica para manipulação ...


def builder():
    sessao = Main()

    while True:
        data = entry()
        if data:
            if data:
                sessao.methodos(data)


def main():

    # Verificação do sistema...
    so = platform.system()
    if so == 'Linux':
        print('Sistema Operacional', colored('Linux', 'green'))
        builder()

    elif so == 'Windows':
        print('Sistema Operacional', colored(' Windows', 'green'))
        print(colored('Windows not suported', 'red'))

    else:
        print('Sistema Operacional', colored(' Não Identificado', 'red'))
        print(colored('Not suported', 'red'))


if __name__ == '__main__':
    main()
