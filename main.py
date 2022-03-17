# -*- coding: utf-8 -*-

import os
import click
import time
import pandas
import platform

import subprocess

from threading import Thread as th
from termcolor import colored

# Modules ---------
from dialog.dialog import Dialog as msg
from modules.system.system import MainSystem

# Função para receber a entradada de dados do usuário
def entry():
    data = input('{} #'.format(colored(os.getcwd(), 'white'))+colored('|set|', 'yellow')+'#>'+' ')
    return data


def response(data):
    return data

def loader(args):
    with click.progressbar(range(int(args))) as bar:
            for i in bar:
                pass


class Main(object):

    _MainSystem = MainSystem()
    _USUARIO = None
    _SESSION_NAME = None
    _DEBUG = False
    _CACHE = []

    triggers = {
            'commands': [

                'data',
                'hydra',
                'help',
                'exit',
                'login',
                'gitconfig',
                'herokuconfig',
                'server web local',

                # Comandos nativos --------
                'ls',
                'clear',
                'cd',
                'cat',
                # redes -------------------
                'ping',
                # hydra ======

            ],
        }

    def __init__(self):
        th(target=loader(10000))
        os.system('clear')
        menu_msg = msg()
        print(menu_msg.head_msg('menu'))



    def commands(self, commit):

        for cmd in self.triggers['commands']:
            if commit == cmd:
                self._CACHE.append(cmd)
                print(self._CACHE)


        if commit.lower() == 'exit':
            self._MainSystem.cmd_exit()

        elif commit.lower() == 'login':
            self._MainSystem.cmd_login()

        elif commit.lower() == 'help':
            self._MainSystem.cmd_help()

        elif commit.lower() == 'gitconfig':
            self._MainSystem.cmd_gitconfig()

        elif commit.lower() == 'herokuconfig':
            self._MainSystem.cmd_herokuconfig()

        elif commit.lower() == 'server web local':
            self._MainSystem.cmd_server_web_local()

        elif commit.lower() == 'hydra':
            self._MainSystem.cmd_hydra()

        ################################################################
        # Comandos basicos do sistema ----------------------
        ################################################################
        elif commit.lower() == 'ls':
            self._MainSystem.cmd_ls()

        elif commit.lower() == 'clear':
            self._MainSystem.cmd_clear()

        elif 'cd' in commit.lower():
            print('Commit =>', commit[:1])
            self._MainSystem.cmd_cd(commit=commit[3:])

        elif 'cat' in commit.lower():
            self._MainSystem.cmd_cat(commit=commit[4:])

        elif 'ping' in commit.lower():
            th(target=self._MainSystem.cmd_ping(commit=commit[5:])).start()

        ################################################################
        # End Comandos basicos do sistema ----------------------          <<------------------------
        ################################################################


    def methodos(self, argv):
        # Avaliando comandos enviados ...
        for cmd in self.triggers['commands']:
            if argv == cmd:
                return self.commands(commit=cmd)

            # Condições para tratar argumentos de comandos ------------------
            elif argv[:3] == 'cd ':
                self._CACHE.append(argv[:3])
                return self.commands(commit=argv)
            elif argv[:4] == 'cat ':
                self._CACHE.append(argv[:4])
                print(argv)
                return self.commands(commit=argv)
            elif argv[:5] == 'ping ':
                self._CACHE.append(argv[:5])
                print(argv)
                return self.commands(commit=argv)

            if not argv in self.triggers['commands']:
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
