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

# exeple--------------------------------------
"""
print(colored('Error Test!!!', 'red'))
print(colored('Warning Test!!!', 'yellow'))
print(colored('Success Test!!!', 'green'))
"""

# Funções de classes ---


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

        elif commit.lower() == 'data':
            data = self._MainSystem.get_info('data')
            return print(data)

    def methodos(self, argv):
        triggers = {
            'commands': [

                'data',
                'server',
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
                return print(colored('[-]', 'red'), colored('Comando não encontrado...', 'red'))

# Processos de lógica para manipulação ...


def builder():
    print('Sistema Operacional', colored(' Windows', 'green'))
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
        builder()

    elif so == 'Windows':
        print('Sistema Operacional', colored(' Windows', 'green'))
        print(colored('Windows not suported', 'red'))

    else:
        print('Sistema Operacional', colored(' Não Identificado', 'red'))
        print(colored('Not suported', 'red'))


if __name__ == '__main__':
    main()
