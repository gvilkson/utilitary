# -*- coding: utf-8 -*-
import os
import platform
import subprocess
import threading

from datetime import datetime
import click
from termcolor import colored
from dialog.dialog import Dialog as msg

##########################################################################
#	 Start Funções auxiliares
#-------------------------------------------------------------------------


#-------------------------------------------------------------------------
#	 End Funções auxiliares
##########################################################################


##########################################################################
#	 Start Tratamento de processos paralelos
#-------------------------------------------------------------------------
"""
É uma má pratica parar de forma abruptamente uma thread em qualquer linguagem.

Vamos pensar A thread está com algum recurso critico que precisa ser fechado de forma correta.
 A thread tem outras threads que devem ser paradas junto com essa thread.

A melhor maneira de lidar com isso se você puder, (se você está administrando suas próprias threads) 
é ter uma flag exit_request que cada thread checa regularmente para ver se é hora de fechar.
"""
class StoppableThread(threading.Thread):
    """Thread class com metodo de stop(). A thread precisa checar 
    regularmente pela condição de stopped() ."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

"""
Há casos, no entanto, quando você realmente precisa matar uma thread.
 Um exemplo é quando você está fazendo o wrap de uma biblioteca externa que está ocupada e você deseja interrompê-la.
 A seguir permite que (com algumas restrições) lance uma exceção em uma thread do Python.

"""

def _async_raise(tid, exctype):
    '''Lanca uma excecao na threads com id tid'''
    if not inspect.isclass(exctype):
        raise TypeError("Somente tipos podem ser lancados (nao instancias)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,
                                                  ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("thread com invalido id")
    elif res != 1:
        # "Se lancar um numero maior que um, eh um problema,
        # e voce deveria chamar novamente com exc=NULL para reverter o efeito"
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemError("PyThreadState_SetAsyncExc falhou")

class ThreadWithExc(threading.Thread):
    def _get_my_tid(self):
        if not self.isAlive():
            raise threading.ThreadError("the thread is not active")

        if hasattr(self, "_thread_id"):
            return self._thread_id

        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid

        # TODO: em python 2.6, existe uma forma mais simples : self.ident

        raise AssertionError("nao pode determinar as threads com id")

    def raiseExc(self, exctype):
        _async_raise( self._get_my_tid(), exctype )

# Conforme observado, isto não é perfeito, porque se a thread estiver ocupada fora do interpretador Python, não vai pegar a interrupção.


#-------------------------------------------------------------------------
#	 End Tratamento de processos paralelos
##########################################################################


##########################################################################
#	 Start Sistema principal
#-------------------------------------------------------------------------
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

#-------------------------------------------------------------------------
#	 End Sistema principal
##########################################################################
