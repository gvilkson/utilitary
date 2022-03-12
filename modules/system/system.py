# -*- coding: utf-8 -*-
import os
import platform
import subprocess
from threading import Thread as th

from datetime import datetime
import click

def loader(args):
    with click.progressbar(range(int(args))) as bar:
            for i in bar:
                pass

class MainSystem(object):
	versao = None
	plataforma = None
	data = None

	_BASE_DIR = '/home/'

	def __init__(self):
		self.plataforma = platform.platform()
		self.versao = platform.python_version()
		self.data = datetime.now()


	def get_info(self, argv):
		if argv == 'data':
			data = str(self.data.day)+'/'+str(self.data.month)+'/'+str(self.data.year)
			return data

	def cmd_exit(self):
		os.system('clear')
		print('Fechando aplicação!')
		return exit()

	def cmd_login(self):
		return print('Em desenvolvimento....')

	def cmd_gitconfig(self):
		return print('Em desenvolvimento....')

	def cmd_help(self):
		return print('Em desenvolvimento....')

	def cmd_herokuconfig(self):
		return print('Em desenvolvimento....')

	def cmd_server_web_local(self):
		from tools.content import ServerLocal
		obj = ServerLocal('teste')
		thred = th(target=obj.start_server)
		thred.start()

	def cmd_hydra(self):
		from tools.hydra import THC_hydra
		hydra = THC_hydra()
		print('Verificando hydra no sistema Operacional...')
		loader(10000)

	# Comandos basicos do sistema ---------------------------------------------
	def cmd_ls(self):
		return print(os.listdir())

	def cmd_clear(self):
		return os.system('clear')

	def cmd_cd(self, commit):
		try:
			return os.chdir(path=commit)
		except:
			print('Diretório não encontrado!')