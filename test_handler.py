
# coding: utf-8

# In[ ]:
import unittest

from slackclient import SlackClient
import Mainbot.Subpackage2.config as config
import Mainbot.subpackage.bot_questions as bot
import Mainbot.subpackage.ChatbotWorkings as cb
import Mainbot.Subpackage2.handler as handler

class Test_handler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Test_handler set up class initiated')
   
    @classmethod
    def tearDownClass(cls):
        print('destroyed test Test_handler')
    def setUp(self):
        self.command = 'Hi'
        self.channel = 'DEFQ6KR5H'
        self.slack_client = SlackClient(config.config('SLACK_TOKEN'))
        self.command1='Hello'
        self.command2='nice'
        self.command3='How are you'
        self.command4='What is MDS program'
        
        
    def tearDown(self):
        print('\n end of test')

    def testhandler(self):
        response,channel=handler.handle_command(self.command, self.channel,self.slack_client)
        self.assertIn(response, ["'sup bro", "hey", "sasriakaal", "hi", "namastey", "awesome girl if you are"])
    
    def testhandler1(self):
        response,channel=handler.handle_command(self.command1, self.channel,self.slack_client)
        self.assertIn(response, ["'sup bro", "hey", "sasriakaal", "hi", "namastey", "awesome girl if you are"])
    def testhandler2(self):  
        response,channel=handler.handle_command(self.command2, self.channel,self.slack_client)
        self.assertNotIn(response, ["'sup bro", "hey", "sasriakaal", "hi", "namastey", "awesome girl if you are"])
    def testhandler3(self):  
        response,channel=handler.handle_command(self.command3, self.channel,self.slack_client)
        self.assertEqual(response, 'I am good, how are you doing today?')
    def testhandler4(self):  
        response,channel=handler.handle_command(self.command4, self.channel,self.slack_client)
        self.assertEqual(response, 'MDS stands for Master\'s in Data Science. It is a 10 month program')
        


#if __name__ == '__main__':
 #   unittest.main()
unittest.main(argv=[''],verbosity=2,exit=False)

