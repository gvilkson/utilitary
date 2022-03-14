# -*- coding: utf-8 -*-
import os
import platform
import subprocess
from threading import Thread as th

from datetime import datetime
import click
from termcolor import colored
from dialog.dialog import Dialog as msg

def loader(args):
    with click.progressbar(range(int(args))) as bar:
            for i in bar:
                pass

class MainSystem(object):
	versao = None
	plataforma = None
	data = None

	_BASE_DIR = '/home/'
	_PATH_LOCAL = []
	_ARQ_LOCAL_PATH = []

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
		print(colored('Finalizado!', 'yellow'))
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

		os.system('clear')
		hydra = THC_hydra()

		banner_msg = msg()
		print(banner_msg.head_msg('hydra'))

		chaves = [chave for chave, valor in sorted(hydra._target.items(), reverse=True)]
		args_target = {}

		for chave in chaves:
			print(colored('Implemente', 'yellow'), colored('{}'.format(chave), 'green'))
			enty = input(colored('>>> ', 'blue'))
			args_target[chave] = enty
			print(args_target)

			print(colored('______________________________', 'blue'), '\n')

		hydra.target(
			host=str(args_target['host']),
			port=args_target['porta_web'],
			list_name=args_target['list_name'],
			list_password=args_target['list_password'],
			protocolo=args_target['protocolo'],
			local_page_login=args_target['local_page_login'],
			request=args_target['request'],
			message=args_target['message'],
			)
		hydra.atack_web()




	# Comandos basicos do sistema ---------------------------------------------######################################
	def cmd_ls(self):
		self._ARQ_LOCAL_PATH = []
		self._PATH_LOCAL = []
		data = os.listdir()
		indice = 0

		print(colored('<<<<<<<<<<<<<<<< Pastas >>>>>>>>>>>>>>>>>', 'white'))
		for i in data:
			if not "." in i:
				self._PATH_LOCAL.append(i)
				path_size = os.path.getsize(i)

				if self._PATH_LOCAL[indice] == indice:
					indice = indice + 1

				else:

					vl = len(i)

					self._PATH_LOCAL[indice] = self._PATH_LOCAL[indice] + '[{}]'.format(indice)
					if vl <= 10:
						print(colored(self._PATH_LOCAL[indice][-3:].strip('[').strip(']'), 'white'), colored(self._PATH_LOCAL[indice][:-3], 'green'), '| BT/'+str(path_size))
					
					if vl >= 10:
						print(colored(self._PATH_LOCAL[indice][-3:].strip('[').strip(']'), 'white'), colored(self._PATH_LOCAL[indice][:-3], 'green'), '| BT/'+str(path_size))

					indice = indice + 1

		print(colored('<<<<<<<<<<<<<<<< Arquivos >>>>>>>>>>>>>>>>>', 'white'))
		for i in data:
			if "." in i:
				if not "." in i[0]:
					self._ARQ_LOCAL_PATH.append(i)
					arq_size = os.path.getsize(i)
					print(colored(i, 'white'), '| BT/'+str(arq_size))

		print(colored('___________________________________________________________ _ _', 'green'))
		print(colored('|========================  End  =============================>>>', 'white'))


	def cmd_clear(self):
		return os.system('clear')

	def cmd_cd(self, commit):
		try:
			return os.chdir(path=commit)
		except:
			print(colored('Diretório não encontrado!', 'red'))

	def cmd_cat(self, commit):
		return subprocess.call(['cat', commit])

	# Comandos sobre redes -------------------------------------
	def cmd_ping(self, commit):
		return subprocess.call(['ping', commit])
