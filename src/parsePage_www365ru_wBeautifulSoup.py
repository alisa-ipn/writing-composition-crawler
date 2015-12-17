# -*- coding: cp1251 -*-
"""
Created on Wed Dec 16 22:45:28 2015

@author: Alisa
"""

import sys, os
from bs4 import BeautifulSoup
import codecs 

DIR_OUT = "E://Study//SpeechRecognProject//crawl//corpus//corpus_v3//"
DIR_IN = "E://Study//SpeechRecognProject//crawl//raw_data//en365.ru"
TAG = 'td'

def erase_tags(par): 
    print "Got here-6"     
    while par.find("<") > -1: 
        start = par.find("<")
        end = par.find(">")        
        par = par[:start]+" "+par[end+1:]
        par = par.strip()
        print "Got here-7" 
        print par
    return par     
        
        

def format_and_print(par, fout=sys.stdout): 
    
    par = erase_tags(par)    
    
    par = par.replace('\n', ' ')
    par = par.replace('  ', ' ')
    par = par.replace('\t', '')        
    par = par.replace('&quot;', '"')
    par = par.replace('&nbsp;', ' ')
    par = par.replace('&amp;', '&')
    par = par.replace('&#039;', "'")
    par = par.replace('&ldquo;', '"')
    par = par.replace('&rdquo;', '"')
    
            
    #print par 
    print "Got here-8"     
    print >> fout, unicode(par) 
    return True

    
def main(argv):

        print "Start running"  

  #for the_dir in os.listdir(DIR_IN):
        #dir_path = os.path.join(DIR_IN, the_dir)
        dir_path = DIR_IN
        the_dir = os.path.basename(dir_path)
        try: 
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
                        #fin = open(file_path, 'r')
                        fin =  codecs.open(file_path, encoding = 'cp1251', errors ='replace') 
                        
                        file_name = the_file[:the_file.rfind(".")]+".txt"
                        fout_nm = os.path.join(dir_out_name, file_name)                        
                        #fout = open(fout_nm, 'a')
                        fout = codecs.open(fout_nm, encoding = 'utf-8', mode = 'w') 
                        
                        page = fin.read()
                        
                        print "Got here-3" 
                        soup = BeautifulSoup(page, "lxml")
                        print "Got here-4" 
                        tags = soup(TAG)
                        print "Got here-5" 
                        for tag in tags: 
                            if len(tag.contents) > 0:
                                #par = tag.contents[0]                                   
                                par = unicode(tag) 
                                print len(par) 
                                #checking length of the paragraph and presence of cyrillic letter 
                                longpar = False 
                                for p in tag.contents: 
                                    if len(p) > 100 :
                                        longpar = True
                                if longpar and par.find('the') != -1: 
                                    print par 
                                    format_and_print(par, fout)
                        fout.close()
        except Exception, e:
            print e



if __name__ == "__main__":
    main(sys.argv)

