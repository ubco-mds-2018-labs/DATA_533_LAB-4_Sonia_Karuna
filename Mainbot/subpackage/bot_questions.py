
# coding: utf-8

# In[5]:



# coding: utf-8

# In[36]:
import pandas as pd


def questions(command):

    rdata = {
            'Questions' : ["How are you",   "What do you do", "What is MDS program","Tell me more about MDS",
                       "Ok Great,I will come back to you for more details", "Bye","Bye"  ],
            'Answers' :  ["I am good, how are you doing today?", "I try to find out the answers for your questions, go ahead and ask me about MDS program",
                     "MDS stands for Master's in Data Science. It is a 10 month program",
                     "You may like to visit the webpage for more detail, please check this link: https://masterdatascience.ubc.ca/programs/okanagan",
                     "Oh sure, You are welcome","Bye, Thank you", "Bye, Thank you"]
        }
    
    # Creating Dataframe from Dictionary by Skipping 2nd Item from dict
    robo_data = pd.DataFrame(rdata, columns=['Questions', 'Answers'])
 
    ans=robo_data[robo_data.Questions == command]['Answers'].tolist()
    try:
        if ans==[]:
            return ans
        else:
            return ans[0]
    except:
        print("Error")
        

