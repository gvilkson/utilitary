#-*- coding: utf-8 -*-

from termcolor import colored

# Propriedades de cores para menu 
menu_item_01 = colored('Auxiliary', 'blue')
menu_item_02 = colored('command line', 'yellow')
menu_item_03 = colored('START', 'white')
menu_item_04 = colored('******************', 'red')

MENU = """
       __  __    _    ____ _____ _____ ____         
  __/\__ |  \/  |  / \  / ___|_   _| ____|  _ \  __/\__
  \    / | |\/| | / _ \ \___ \ | | |  _| | |_) | \    /
  /_  _\ | |  | |/ ___ \ ___) || | | |___|  _ <  /_  _\
    
    \/   |_|  |_/_/   \_\____/ |_| |_____|_| \_\   \/  
   _____ _____ _____ _____ _____ _____ _____ _____ _____  
  |_____|_____|_____|_____|_____|_____|_____|_____|_____|
      {} | {} | {} {}
      """.format(menu_item_01, menu_item_02, menu_item_03, menu_item_04)



class Dialog(object):
    def __init__(self):
        pass
            
    def head_msg(self, name):
        name = str(name)
        if name == 'menu':
            return MENU
