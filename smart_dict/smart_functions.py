'''
Created on 17 feb. 2019

@author: juan.cristobal.qg@gmail.com
'''
class InnerListWrapper(object):
    def __init__(self, value = None):
        self.__content = [value] if value else []
    
    @property
    def content(self):
        return self.__content
    
    def __iter__(self):
        return self.__content.__iter__()
    
    def __next__(self):
        return self.__content.__next__()
    def append(self, value):
        self.__content.append(value)
    
    def __repr__(self):
        return self.__content.__repr__()
    
    def __len__(self):
        return self.__content.__len__()
    
def smart_update_replace(one, other):
    for other_key,other_value in other.iteritems():
        if other_key in one and isinstance(other_value,dict):
            one[other_key] = smart_update_replace(one[other_key], other_value)
        else:
            one[other_key] = other_value
    return one

def smart_update_add(one, other):
    if isinstance(one, InnerListWrapper):
        if all([not isinstance(one_element,dict) for one_element in one]):
            one.append(other) 
            return one
        for one_element in one:
            if isinstance(one_element, dict):            
                smart_update_add(one_element,other)
        return one
    
    for other_key,other_value in other.iteritems():
        if other_key in one and isinstance(other_value,dict):
            element = smart_update_add(one[other_key], other_value)
            one[other_key] = element
        else:
            if not other_key in one:
                one[other_key] = other_value
            else:
                if not isinstance(one[other_key], InnerListWrapper):
                    one[other_key] = InnerListWrapper(one[other_key])
                    one[other_key].content.append(other_value)
                else:
                    one[other_key].append(other_value)
    return one