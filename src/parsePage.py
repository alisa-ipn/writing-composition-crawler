# -*- coding: cp1251 -*-
"""
Created on Fri Nov 20 22:44:14 2015

@author: Alisa
"""

import sys, os 
import re 
import codecs

FNAME = "E://Study//SpeechRecognProject//crawl//raw_data//abc-english-grammar.com//A._Sakharov.html"


#DIR_OUT = "E://Study//SpeechRecognProject//crawl//corpus"
DIR_OUT = "E://Study//SpeechRecognProject//crawl//corpus_v2"
DIR_IN = "E://Study//SpeechRecognProject//crawl//raw_data"


#PARAGRAPH = r">(\w\s?(?:(?:[\w\-';&]+[\s\t]*\n?)+[\.!\?,;:\%]?[\s\t]*\n?)+)"
#PARAGRAPH = r">([A-Z]\s?(?:(?:[a-zA-Z0-9\-'�;&�\"]+[\s\t]*\n?)+[\.!\?,;:�\%]?[\s\t]*\n?)+)"
#PARAGRAPH = r">([A-Z]\s?(?:(?:[a-zA-Z0-9\-'�;&�]+[\s\t]*\n?)+[\.!\?,;:�\%]?\.{0,2}[\s\t]*\n?)+)".decode('cp1251')
PARAGRAPH = r">([A-Z]\s?(?:(?:[a-zA-Z0-9\-'�;&�]+[\s\t]*\n?)+[\.!\?,;:�\%]?\.{0,2}[\s\t]*\n?)+)"

def format_and_print(paragraphs, fout=sys.stdout):
    for par in paragraphs: 
        #print par 
        #par = unicode(par)
        #print "Got here-6"  
        par = par.replace('\n', ' ')
        par = par.replace('  ', ' ')
        par = par.replace('\t', '')
        par = par.replace('&quot;', '"')
        par = par.replace('&nbsp;', ' ')    
        par = par.strip() 
        #if par[-1] not in ['.', '!', '?']:
        if len(par) < 10:
            continue
        print >>fout, par 


def main(argv):

  print "Start running"
  par_pat = re.compile(PARAGRAPH, re.I|re.M|re.U)

  for the_dir in os.listdir(DIR_IN):
        dir_path = os.path.join(DIR_IN, the_dir)
        try:
            #if os.path.isfile(file_path):
            #    os.unlink(file_path) 
            #print "Got here-1"
            if os.path.isdir(dir_path):
                #print "Got here-2"
                dir_out_name = os.path.join(DIR_OUT, the_dir)
                if not os.path.exists(dir_out_name):
                    os.mkdir(dir_out_name) 
                for the_file in os.listdir(dir_path):                    
                    file_path = os.path.join(dir_path, the_file)
                    if os.path.isfile(file_path) and the_file != "_url_list.txt":
                        print the_file   
                        fin = open(file_path, 'r')                        
                        #fin =  codecs.open(file_path, encoding = 'cp1251', errors ='replace') 
                        #fin =  codecs.open(file_path, encoding = 'cp1251', errors ='replace')                                                   
                        #print "Got here-3"                           
                        the_file = the_file[:the_file.find(".htm")]+".txt"
                        fout_nm = os.path.join(dir_out_name, the_file)                        
                        fout = open(fout_nm, 'w')
                        page = fin.read()
                        #print "Got here-4"  
                        pars = par_pat.findall(page)
                        #print "Got here-5"  
                        if pars:
                            format_and_print(pars, fout)
                
        except Exception, e:
            print e



if __name__ == "__main__":
    main(sys.argv)




