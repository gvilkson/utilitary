#-*- coding: utf-8 -*-

MENU = """
       __  __    _    ____ _____ _____ ____         
  __/\__ |  \/  |  / \  / ___|_   _| ____|  _ \  __/\__
  \    / | |\/| | / _ \ \___ \ | | |  _| | |_) | \    /
  /_  _\ | |  | |/ ___ \ ___) || | | |___|  _ <  /_  _\
    
    \/   |_|  |_/_/   \_\____/ |_| |_____|_| \_\   \/  
   _____ _____ _____ _____ _____ _____ _____ _____ _____  
  |_____|_____|_____|_____|_____|_____|_____|_____|_____|
      Auxiliary | command line | HOME ******************
      """

class Dialog(object):
    def __init__(self):
        pass
            
    def head_msg(self, name):
        name = str(name)
        if name == 'menu':
            return MENU
