#!/usr/bin/env python

#***************************** CHAT ************************************/
#  
#  This example shows how to have a general conversation with Gurunudi AI
#  
#***************************** CHAT ************************************/


from gurunudi import AI,api,lang

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("capital of India?")

#The AI attribute "chat" returns a chat response to the given text
assert(ai.chat == "New Delhi is the capital of India.")

#If there was any error during the attribute call, then ai.latest_error will contain the error string, else it will be None
#if ai.chat returns None i.e. if chat API fails, then check this value for the corresponding error message
assert(ai.latest_error==None)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for French text.
ai = AI("Emmanuel Macron est le président de la France.",lang.FRENCH)

#For the latest updated list of languages supported by Gurunudi for chat visit https://gurulaghu.com/languages/
