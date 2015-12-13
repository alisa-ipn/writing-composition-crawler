# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:16:51 2015

@author: Alisa
"""
import sys 

"""
FNOUT = "E://Study//SpeechRecognProject//crawl//test_data//0-9-v2.txt"
multiple_num = 5
iter_num = 2

fout = open(FNOUT, 'w')

for i in range (10):
    
    print >> fout, i 
    if i == multiple_num: 
        for j in range(iter_num):
            print >> fout, i

fout.close()    
"""

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]



FNOUT = "E://Study//SpeechRecognProject//crawl//test_data//zero-99.txt"

fout = open(FNOUT, 'w')

for i in range (100):
    if i < 10: 
        print >> fout, ones[i]
    elif i < 20: 
        remainder = i % 10        
        print >> fout, teens[remainder]
    else:    
        dec = i // 10
        remainder = i % 10
        print >> sys.stdout, remainder        
        if remainder == 0: 
            
            print >> fout, tens[dec]
        else:     
            print >> fout, tens[dec], ones[remainder]
    
    

fout.close()    