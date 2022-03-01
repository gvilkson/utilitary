# -*- coding: utf-8 -*-
import platform
from datetime import datetime

class MainSystem(object):
	versao = None
	plataforma = None
	data = None

	def __init__(self):
		self.plataforma = platform.platform()
		self.versao = platform.python_version()
		self.data = datetime.now()


	def get_info(self, argv):
		if argv == 'data':
			data = str(self.data.day)+'/'+str(self.data.month)+'/'+str(self.data.year)
			return data