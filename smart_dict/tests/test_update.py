'''
Created on 17 feb. 2019

@author: juan.cristobal.qg@gmail.com
'''
import unittest
from ..smart_dict import SmartDict

class TestSmartDict(unittest.TestCase):
    
    def testBasicTypesUpdate(self):
        dict1 = {'1' : { 'hello' : 'man'},
                 '2' : { '2' : { '3' : {'3' : '4'} }},
                 3 : { 3 : 3.3333}}
        dict2 = {'1' : {'goodbye' : 'girl'},
                 '2' : { '2' : { '3' : {'5' : '6'}}},
                 3 : { 4: 4.44444}}
    
        smd1 = SmartDict(dict1)
        smd2 = SmartDict(dict2)
    
        smd1.smart_update(smd2)
        
        self.assertTrue(len(smd1['1'].keys()) == 2)
        self.assertTrue(len(smd1['2']['2']['3'].keys())==2)
        self.assertTrue(len(smd1[3].keys())==2)
        import pprint
        pprint.pprint(smd1)
        

if __name__ == '__main__':
    unittest.main()