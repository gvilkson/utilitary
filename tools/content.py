# -*- coding: utf-8 -*-

import socket
import os
import subprocess
import sys
import tqdm
import subprocess
from termcolor import colored as c



class ServerLocal(object):
    CURRENT_SERVER = None

    def __init__(self, server):
        if os.path.isdir('backend_web'):
            return print('Estrutura existente no diretorio atual')
        else:
            os.system('clear')
            print('Não exite estrutura!')
            print('Criando estrutura aguarde ...')

            os.system('django-admin startproject backend_web')

    def start_server(self):
        os.system('python backend_web/manage.py runserver')
