# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:13:31 2015

@author: nerc
"""


class UserIdError(Exception):
    def __init__(self, message):
        self.message = message

    def __del__(self):
        pass
        
    def __str__(self):
        return repr(self.message)