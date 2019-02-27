'''
Created on 17 feb. 2019

@author: juan.cristobal.qg@gmail.com
'''
import smart_functions

class SmartDict(dict):
    
    def smart_set_add(self,*args):
    
        try:
            next_element = args[-1]
            cur_element = args[-2]
        except:
            return
        new_args = list(args)
        
        new_args.pop(-1)
        new_args.pop(-1)
        
        o = {}
        o[cur_element] = next_element
        
        if new_args:
            new_args.append(o)
            self.smart_set_add(*new_args)
        else:
            self.smart_update_add(o)
    
    def smart_set_replace(self,*args):
    
        try:
            next_element = args[-1]
            cur_element = args[-2]
        except:
            return
        new_args = list(args)
        
        new_args.pop(-1)
        new_args.pop(-1)
        
        o = {}
        o[cur_element] = next_element
        
        if new_args:
            new_args.append(o)
            self.smart_set_replace(*new_args)
        else:
            self.smart_update_replace(o)
    
    def smart_update_add(self, other):
        smart_functions.smart_update_add(self, other)
    
    def smart_update_replace(self, other):
        smart_functions.smart_update_replace(self, other)
        