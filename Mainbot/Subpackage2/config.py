
# coding: utf-8

# In[2]:


try:
    
    def config(env):
        try:
            if env=='SLACK_TOKEN':
                SLACK_TOKEN='xoxb-493323995142-491822670659-tLQJy2eckXUBgFKhET9eHvO4'
                return SLACK_TOKEN
            elif env=='BOTNAME':
                botname = 'Chatbot'
                return botname    
            elif env =='BOT_ID':
                BOT_ID = 'AEFT61GF4'
                return BOT_ID
        except:
            print("Function returned nothing")
except:
    print("Configuration not defined")


        
