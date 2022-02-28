#-*- coding: utf-8 -*-

import os
import time

class Dialog(object):
    def __init__(self, name):
        self.name = name
        
    def make_msg(self, text):
        
        try:
            msg = open(self.name, 'w')
            msg.write(text)
            msg.close()
            
        except:
            print('Error in make msg')
            
    def head_msg(self, name):
        
        try:
            msg = open(name, 'r')
            message = msg.read()
            msg.close()
            return message
            
        except:
            print('Error open msg')