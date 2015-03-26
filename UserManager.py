# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:41:12 2015

@author: nerc
"""
import user
class UserManager():
    
    def set_library_controller(self, library_controller):
        self.library_controller = library_controller    
    
    def create_user(self,user_id):

        NewUser=user.User()
        NewUser.set_identification(user_id)
        self.library_controller.add_user(NewUser)
 #       NewUser._identification = str()
 #       NewUser._first_name = str()
 #       NewUser._last_name = str()

        

#    LibraryController.AddUser(NewUser)
        
    
    
