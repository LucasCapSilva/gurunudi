#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** SUMMARY GENERATION *******************************************/
#  
#  This example shows how to query Gurunudi to summarize a given text
#  
#***************************** SUMMARY GENERATION *********************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai=AI()

response = ai.summary("<SOME_LARGE_TEXT_LIKE_AN_ARTICLE_OR_A_DOCUMENT>")
print(response)
 
#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for French text.
response = ai.summary("Emmanuel Macron est le président de la France.",lang.FRENCH)
print(response)

#For the latest updated list of languages supported by Gurunudi for summary generation visit https://guruyuga.com/languages/
