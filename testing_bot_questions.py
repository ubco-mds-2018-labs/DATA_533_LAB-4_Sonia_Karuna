
# coding: utf-8

# In[8]:



import sys
import unittest
import Mainbot.subpackage.bot_questions as bot
class TestBot(unittest.TestCase):   
    
    @classmethod
    def setUpClass(cls):
        print('set up')
   
    @classmethod
    def tearDownClass(cls):
        print('tear down cls')
    
    
    def setUp(self): 
        self.command = "How are you"
        self.command1 = "What do you do"
        self.command2 = "Hello"
        
    def tearDown(self):
        print('Tear Down')
    
   
       
    def test_questions(self):
        cmd = bot.questions(self.command)
        cmd1 = bot.questions(self.command1)
        cmd2 = bot.questions(self.command2)
        aaa=["we","are"]
        cmd3=bot.questions(aaa)
        print(self.assertEqual(cmd,"I am good, how are you doing today?"))
        print(self.assertTrue(cmd,"I am good, how are you doing today?"))
        print(self.assertEqual(cmd1,"I try to find out the answers for your questions, go ahead and ask me about MDS program"))
        print(self.assertTrue(cmd1,"I try to find out the answers for your questions, go ahead and ask me about MDS program"))
        print(self.assertNotEqual(cmd2,"I am good, how are you doing today?"))
        print(self.assertNotEqual(cmd3,"I am good, how are you doing today?"))
        
unittest.main(argv=[''], verbosity=2, exit=False)

