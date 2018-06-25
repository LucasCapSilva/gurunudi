#!/usr/bin/env python

from gurunudi import AI,api

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("Larry Page was doing his Phd at Stanford University in 1996.")

#The AI attribute "named_entities" returns a list of named entities found in the text
#Each entry in the list is a dictionary containing a named entity's text, its label and its position in the original text
print(ai.named_entities)

#If there was any error during the attribute call, then ai.latest_error will contain the error string, else it will be None
#if ai.named_entities returns None i.e. if named entities extraction API fails, then check this value for the corresponding error message
assert(ai.latest_error==None)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for German text.
ai = AI("Emmanuel Macron est le président de la France.",gurunudi.FRENCH)

#For the latest updated list of languages supported by Gurunudi for named entities extraction visit https://gurulaghu.com/languages/
