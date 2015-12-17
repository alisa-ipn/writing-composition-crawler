# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 19:14:43 2015

@author: Alisa
"""
import sys
import re
import digits_to_words 


FN = "E:\\Study\\SpeechRecognProject\\crawl\\corpus_lined\\www.native-english.ru_all.txt"


def convert_numbers(fname, num_rex = r'(\d+(?:[,|\.]\d)?\d*)'): 
    pat = re.compile(num_rex, re.U)     

    i = 1 
    for s in open(fname): 
        matches = pat.finditer(s)
        if matches == None: 
            print >> sys.stderr,  i , 'No matches found' 
            i+=1
        else: 
            #replacements = {}            
            for m in matches: 
                #print type(m.group())
                #print type(m.group(0))
                #print i, m.group(), m.start(), m.end(), m.span(),                 
                num_str = m.group().replace('.', '')                
                num_str = num_str.replace(',', '')
                #print num_str
                num_word = digits_to_words.Number_To_Words(int(num_str))
                ## It's better to replace first the longest matching strings
                ## and thenteh smaller ones in decreasing order. 
                ## Otherwise, we can replace, e.g.,  a digit withina longer number by mistake.  
                s = s.replace(m.group(), num_word, 1)                
                #replacements[m.group()] = num_word            
            i+=1
        print s,
        
   
convert_numbers(FN)
