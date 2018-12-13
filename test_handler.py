
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
        self.command = "How are you"
        self.command1 = "What do you do"
        self.command2 = "Hello"
        self.channel = 'DEFQ6KR5H'
        self.slack_client = SlackClient(config.config('SLACK_TOKEN'))
        self.command3='I am fine'
        self.command4='What is MDS program'
        self.slack_events6='hi'
        self.slack_events7 = [{'type': 'chan', 'user': 'UEF9C7L73', 'text': '<@UEFQ6KQKD> do', 
                              'client_msg_id': '5d0c761f-f4cb-4738-a756-e0b22a9ceb97', 
                              'team': 'TEH9HV946', 'channel': 'CEFN5N684', 
                              'event_ts': '1544032811.001400', 'ts': '1544032811.001400'}]


    def tearDown(self):
        print('\n end of test Test_handler')
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
    def testparse5(self):
        usermessage=handler.parse_bot_commands(self.slack_events7, self.starterbot_id)
        self.assertNotEqual(usermessage, 'What is MDS')
       
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
    def test_config(self):
        slack_token=config.config('SLACK_TOKEN')
        slack_id=config.config('BOT_ID')
        bot_name=config.config('BOTNAME')
        botname=config.config('botname_id')
        self.assertTrue(slack_token,'xoxb-493323995142-491822670659-tLQJy2eckXUBgFKhET9eHvO4')
        self.assertTrue(slack_id,'AEFT61GF4')
        self.assertTrue(bot_name,'Chatbot')
        self.assertTrue(botname,None)
    def testhandler(self):
        slack_client='aaqqwtttttttttt'
        response=handler.handle_command(self.command, self.channel,slack_client)
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
    def testhandler6(self):  
        response,channel=handler.handle_command('do', self.channel,self.slack_client)
        self.assertNotEqual(response, 'I am good, how are you doing today?')
    def testhandler4(self):
        slack_client='nnnnnn'
        channel="nnnnnnnnn"
        command4="hi"
        response=handler.handle_command(command4, channel,slack_client)
        self.assertEqual(response,'No events')
    def testhandler5(self):
        usermessage1=handler.parse_bot_commands('hi', self.starterbot_id)
        self.assertEqual(usermessage1, 'No events found')
    def test_workings(self):
        a = ['hi'] 
        
        robo = cb.Greet(a)
        response = robo.greeting()
        self.assertIn(response, ["'sup bro", "hey", "sasriakaal", "hi", "namastey", "awesome girl if you are"])
    def test_workings2(self):
        a = ['hhhhhh'] 
        
        robo = cb.AbortGreet(a)
        response = robo.greeting()
        self.assertNotIn(response, ["'sup bro", "hey", "sasriakaal", "hi", "namastey", "awesome girl if you are"])
    def test_workings3(self):
        a=[int(5)]
        a1=cb.Greet(a)
        response=a1.greeting()
        self.assertEqual(response, 'Please pass alist of greeting')
    def test_workings4(self):
        a=[int(5)]
        a2=cb.AbortGreet(a)
        response=a2.greeting()
        self.assertEqual(response, 'Bot insist for retry')

        
        

       
unittest.main(argv=[''],verbosity=2,exit=False)

