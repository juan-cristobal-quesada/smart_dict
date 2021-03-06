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
    
        smd1.smart_update_replace(smd2)
        
        self.assertTrue(len(smd1['1'].keys()) == 2)
        self.assertTrue(len(smd1['2']['2']['3'].keys())==2)
        self.assertTrue(len(smd1[3].keys())==2)
        import pprint
        pprint.pprint(smd1)
        
    def testBasicTypesUpdateReplace(self):
        dict1 = {'1' : { 'hello' : 'man'},
                 '2' : { '2' : { '3' : {'3' : '4'} }},
                 3 : { 3 : 3.3333}}
        dict2 = {'1' : {'goodbye' : 'girl'},
                 '2' : { '2' : { '3' : {'5' : '6'}}},
                 3 : { 4: 4.44444}}
    
        dict3 = {3 : {4 : 5.5555}}
        smd1 = SmartDict(dict1)
        smd2 = SmartDict(dict2)
        smd3 = SmartDict(dict3)
        
        smd1.smart_update_add(smd2)
        self.assertTrue(len(smd1['1'].keys()) == 2)
        self.assertTrue(len(smd1['2']['2']['3'].keys())==2)
        self.assertTrue(len(smd1[3].keys())==2)
        import pprint
        pprint.pprint(smd1)
        
        smd1.smart_update_add(smd3)
        self.assertTrue(len(smd1[3][4]) == 2)
        pprint.pprint(smd1)
    
    def testBasicTypesSetReplace(self):
        smd1 = SmartDict()
        smd1.smart_set_replace('hello','girl','bye')
        smd1.smart_set_replace('hello','girl','good')
        smd1.smart_set_replace('hello','girl', 'boy', ['fine'])
        smd1.smart_set_replace('hello','girl', 'boy', 'just')
        import pprint
        pprint.pprint(smd1)
        smd1.smart_set_replace('hello','girl', 'boy', ['arrghh'])
        pprint.pprint(smd1)
        smd1.smart_set_replace('hello','girl','boy', {'some' : 'stuff'})
        pprint.pprint(smd1)
        smd1.smart_set_replace('hello','girl','boy', {'some' : 'new_stuff'})
        pprint.pprint(smd1)
if __name__ == '__main__':
    unittest.main()