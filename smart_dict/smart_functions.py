'''
Created on 17 feb. 2019

@author: juan.cristobal.qg@gmail.com
'''

def smart_update(one, other):
    for other_key,other_value in other.iteritems():
        if other_key in one and isinstance(other_value,dict):
            one[other_key] = smart_update(one[other_key], other_value)
        else:
            one[other_key] = other_value
    return one