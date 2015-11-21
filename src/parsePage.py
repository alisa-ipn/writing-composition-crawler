# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:44:14 2015

@author: Alisa
"""

import sys, os 
import re 

FNAME = "E://Study//SpeechRecognProject//crawl//raw_data//abc-english-grammar.com//A._Sakharov.html"


DIR_OUT = "E://Study//SpeechRecognProject//crawl//corpus"
DIR_IN = "E://Study//SpeechRecognProject//crawl//raw_data"

#PARAGRAPH = r">(\w\s?(?:(?:[\w\-';&]+[\s\t]*\n?)+[\.!\?,;:\%]?[\s\t]*\n?)+)"
PARAGRAPH = r">([A-Z]\s?(?:(?:[a-zA-Z0-9\-'’;&]+[\s\t]*\n?)+[\.!\?,;:—\%]?[\s\t]*\n?)+)"



def format_and_print(paragraphs, fout=sys.stdout):
    for par in paragraphs: 
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
  par_pat = re.compile(PARAGRAPH, re.I|re.M)

  for the_dir in os.listdir(DIR_IN):
        dir_path = os.path.join(DIR_IN, the_dir)
        try:
            #if os.path.isfile(file_path):
            #    os.unlink(file_path) 
            print "Got here-1"
            if os.path.isdir(dir_path):
                print "Got here-2"
                dir_out_name = os.path.join(DIR_OUT, the_dir)
                if not os.path.exists(dir_out_name):
                    os.mkdir(dir_out_name) 
                for the_file in os.listdir(dir_path):
                    print the_file
                    file_path = os.path.join(dir_path, the_file)
                    if os.path.isfile(file_path) and the_file != "_url_list.txt":
                        fin = open(file_path)
                        fout_nm = os.path.join(dir_out_name, the_file)                        
                        fout = open(fout_nm, 'w')
                        page = fin.read()
                        pars = par_pat.findall(page)
                        if pars:
                            format_and_print(pars, fout)
                
        except Exception, e:
            print e



if __name__ == "__main__":
    main(sys.argv)




