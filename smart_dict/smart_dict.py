'''
Created on 17 feb. 2019

@author: juan.cristobal.qg@gmail.com
'''
import smart_functions

class SmartDict(dict):
            
    def smart_update(self, other):
        smart_functions.smart_update(self, other)
        