# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:16:30 2015

@author: Alisa
"""

import sys, os
from bs4 import BeautifulSoup

DIR_OUT = "E://Study//SpeechRecognProject//crawl//corpus_v2//www.native-english.ru-v2"
DIR_IN = "E://Study//SpeechRecognProject//crawl//raw_data//www.native-english.ru"
TAG = 'p'

def format_and_print(par, fout=sys.stdout): 
    if len(par) < 100: 
        return  False
    par = par.replace('\n', ' ')
    par = par.replace('  ', ' ')
    par = par.replace('\t', '')        
    par = par.replace('&quot;', '"')
    par = par.replace('&nbsp;', ' ')
    par = par.replace('&amp;', '&')
    par = par.replace('&#039;', "'")
    par = par.replace('&ldquo;', '"')
    par = par.replace('&rdquo;', '"')
    par = par.strip() 
    print "Got here-6"     
    print >> fout, par 
    return True

    
def main(argv):

  print "Start running"  

  for the_dir in os.listdir(DIR_IN):
        dir_path = os.path.join(DIR_IN, the_dir)
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
                        fin = open(file_path, 'r')
                        file_name = the_file[:the_file.rfind(".")]+".txt"
                        fout_nm = os.path.join(dir_out_name, file_name)                        
                        fout = open(fout_nm, 'a')
                        page = fin.read()
                        
                        print "Got here-3" 
                        soup = BeautifulSoup(page, "lxml")
                        print "Got here-4" 
                        tags = soup(TAG)
                        print "Got here-5" 
                        for tag in tags: 
                            if len(tag.contents) > 0:
                                par = tag.contents[0]                                                                                                                                                      
                                format_and_print(par, fout)
                        fout.close()
        except Exception, e:
            print e



if __name__ == "__main__":
    main(sys.argv)

