
# coding: utf-8

# In[6]:




##from __future__ import print_function, unicode_literals
import random



# Sentences we'll respond with if the user greeted us
class Greet:
    def __init__(self, sentence):
        self.sentence = sentence 

        self.GREET_KEYWORD = ("hello", "hi", "greetings", "sup", "what's up", "morning", "namastey", "hey", "sasria")

        self.GREET_RESPONSE = ["'sup bro", "hey", "sasriakaal", "hi", "namastey", "awesome girl if you are"]

    def greeting(self):
        """If any of the words in the user's input was a greeting, return a greeting response"""
        try:
            for word in self.sentence:
                if word.lower() in self.GREET_KEYWORD:
                    return random.choice(self.GREET_RESPONSE)
        except:
            print("Retry")
class AbortGreet(Greet):
    def __init__(self, sentence):
        Greet.__init__(self, sentence)
        self.KEYWORD = ("hello", "hi", "greetings", "sup", "what's up", "morning", "namastey", "hey", "sasria")
        self.RESPONSE = ["Bhaag ja padaku", "Sorry, I did not get you", "I am listening, keep trying", " Better luck next time", "Attempts over", " Good bye", " Invalid Password, go try again"]
           
    def greeting(self):
        """If any of the words in the user's input was not a greeting, return a abort greeting response"""
        try:
            for word in self.sentence:
                try:
                    if word.lower() not in self.KEYWORD:
                        return random.choice(self.RESPONSE)
                    else:
                        return Greet.greeting(self)
                except:
                        print("MemoryError")
        except:
            print("Bot insist for retry")

