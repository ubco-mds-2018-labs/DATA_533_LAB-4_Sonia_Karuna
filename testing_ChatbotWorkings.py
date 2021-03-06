
# coding: utf-8

# In[10]:



import sys
import unittest
import Mainbot.subpackage.ChatbotWorkings as cw
 
class TestMyBot(unittest.TestCase):   
    
    @classmethod
    def setUpClass(cls):
        print('set up')
   
    @classmethod
    def tearDownClass(cls):
        print('tear down cls')
    
    
    def setUp(self): 
        a = ["hello"]
        a1= [ "hi"]
        a2= ["greetings"]
        a3= ['ROFL']
        self.cw = cw.AbortGreet(a)
        self.cw1 = cw.AbortGreet(a1)
        self.cw2 = cw.AbortGreet(a2)
        self.cw3 = cw.AbortGreet(a3)
        a4=[int(444)]
        self.cw5 = cw.AbortGreet(a4)
        
        self.cw4 = cw.Greet(a4)
        
        
    def tearDown(self):
        print('Tear Down')
    
   
    def test_greeting(self):
        cmd = self.cw.greeting()
        cmd1 = self.cw1.greeting()
        cmd2 = self.cw2.greeting()
        cmd3 = self.cw3.greeting()
        cmd4=self.cw4.greeting()
        cmd5=self.cw5.greeting()
        print(self.assertIn(cmd,["'sup bro", "hey", "sasriakaal", "hi", "namastey", "awesome girl if you are"]))
        print(self.assertIn(cmd1,["'sup bro", "hey", "sasriakaal", "hi", "namastey", "awesome girl if you are"]))
        print(self.assertIn(cmd2,["'sup bro", "hey", "sasriakaal", "hi", "namastey", "awesome girl if you are"]))
        print(self.assertNotIn(cmd3,["'sup bro", "hey", "sasriakaal", "hi", "namastey", "awesome girl if you are"]))
        print(self.assertIn(cmd3,["Bhaag ja padaku", "Sorry, I did not get you", "I am listening, keep trying", " Better luck next time", "Attempts over", " Good bye", " Invalid Password, go try again"]))
        print(self.assertEqual(cmd4,"Please pass alist of greeting"))
        print(self.assertEqual(cmd5,"Test2"))
unittest.main(argv=[''], verbosity=2, exit=False)

