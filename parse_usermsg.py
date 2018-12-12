
# coding: utf-8

# In[ ]:


import unittest
from slackclient import SlackClient
import Mainbot.Subpackage2.config as config
import Mainbot.subpackage.bot_questions as bot
import Mainbot.subpackage.ChatbotWorkings as cb
import Mainbot.Subpackage2.handler as handler

class parse_usermsg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('parse_usermsg set up class initiated')
   
    @classmethod
    def tearDownClass(cls):
        print('destroyed test parse_usermsg')
    def setUp(self):
        self.slack_events = [{'type': 'message', 'user': 'UEF9C7L73', 'text': '<@UEFQ6KQKD> hi', 
                              'client_msg_id': '5d0c761f-f4cb-4738-a756-e0b22a9ceb97', 
                              'team': 'TEH9HV946', 'channel': 'CEFN5N684', 
                              'event_ts': '1544032811.001400', 'ts': '1544032811.001400'}]
        self.slack_events1 = [{'type': 'message', 'user': 'UEF9C7L73', 'text': '<@UEFQ6KQKD> Hey', 
                              'client_msg_id': '5d0c761f-f4cb-4738-a756-e0b22a9ceb97', 
                              'team': 'TEH9HV946', 'channel': 'CEFN5N684', 
                              'event_ts': '1544032811.001400', 'ts': '1544032811.001400'}]
        self.slack_events2 = [{'type': 'message', 'user': 'UEF9C7L73', 'text': '<@UEFQ6KQKD> How are you', 
                              'client_msg_id': '5d0c761f-f4cb-4738-a756-e0b22a9ceb97', 
                              'team': 'TEH9HV946', 'channel': 'CEFN5N684', 
                              'event_ts': '1544032811.001400', 'ts': '1544032811.001400'}]
        self.slack_events3 = [{'type': 'message', 'user': 'UEF9C7L73', 'text': '<@UEFQ6KQKD> I am fine', 
                              'client_msg_id': '5d0c761f-f4cb-4738-a756-e0b22a9ceb97', 
                              'team': 'TEH9HV946', 'channel': 'CEFN5N684', 
                              'event_ts': '1544032811.001400', 'ts': '1544032811.001400'}]
        self.slack_events4 = [{'type': 'message', 'user': 'UEF9C7L73', 'text': '<@UEFQ6KQKD> What is MDS', 
                              'client_msg_id': '5d0c761f-f4cb-4738-a756-e0b22a9ceb97', 
                              'team': 'TEH9HV946', 'channel': 'CEFN5N684', 
                              'event_ts': '1544032811.001400', 'ts': '1544032811.001400'}]
        self.starterbot_id='UEFQ6KQKD'
        
    def tearDown(self):
        print('\n end of test',self.shortDescription())
    
    def testparse(self):        
        
        usermessage,channel=handler.parse_bot_commands(self.slack_events, self.starterbot_id)

        self.assertEqual(usermessage, 'hi')
    
    def testparse1(self):        
        
        usermessage,channel=handler.parse_bot_commands(self.slack_events1, self.starterbot_id)
        self.assertEqual(usermessage, 'Hey')
    
    def testparse2(self):        
        
        usermessage,channel=handler.parse_bot_commands(self.slack_events2, self.starterbot_id)
        self.assertEqual(usermessage, 'How are you')
    
    def testparse3(self):        
        
        usermessage,channel=handler.parse_bot_commands(self.slack_events3, self.starterbot_id)
        self.assertEqual(usermessage, 'I am fine')
    
    def testparse4(self):        
        
        usermessage,channel=handler.parse_bot_commands(self.slack_events4, self.starterbot_id)
        self.assertEqual(usermessage, 'What is MDS')
        


#if __name__ == '__main__':
 #   unittest.main()
unittest.main(argv=[''],verbosity=2,exit=False)

