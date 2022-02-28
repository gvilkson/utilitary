#-*- coding: utf-8 -*-

import os
import time as tm
import pandas

from termcolor import colored

# Modules ---------
from tools.content import Server as S

#exeple--------------------------------------
"""
print(colored('Error Test!!!', 'red'))
print(colored('Warning Test!!!', 'yellow'))
print(colored('Success Test!!!', 'green'))
"""

class Main(object):
	_VERSAO = 'A022'
	def __init__(self):
		self.version = self._VERSAO

	def tools(self, commit):
		if commit == 'server':
			server = S()
			server.build('0.0.0.0', 5003)
			server.run()

	def methodos(self):
		pass

def main():
	obj = Main()
	obj.tools('server')
	print(obj.version)

if __name__ == '__main__':
	main()
