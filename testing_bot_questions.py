
# coding: utf-8

# In[8]:


import Mainbot.subpackage.bot_questions as bt
import sys

 
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
        
    def tearDown(self):
        print('Tear Down')
    
   
    def test_questions(self):
        cmd = bt.questions(self.command)
        cmd1 = bt.questions(self.command1)
        print(self.assertEqual(cmd,"I am good, how are you doing today?"))
        print(self.assertTrue(cmd,"I am good, how are you doing today?"))
        print(self.assertEqual(cmd1,"I try to find out the answers for your questions, go ahead and ask me about MDS program"))
        print(self.assertTrue(cmd1,"I try to find out the answers for your questions, go ahead and ask me about MDS program"))
        print(self.assertNotEqual(cmd1,"I am good, how are you doing today?"))
        #print(self.assertNotEqual(cmd1,"I try to find out the answers for your questions, go ahead and ask me about MDS program"))
 #other than the last print statement, it passes test for rest all, last one is written for fail intentionally.
unittest.main(argv=[''], verbosity=2, exit=False)

