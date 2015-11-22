# -*- coding: utf-8 -*-
"""

@author: Alisa
"""

import os
import utils, urlutils

URL1 = "http://en365.ru/topic.htm"
URL_BASE =  "http://en365.ru/"
PREFIX = "E://Study//SpeechRecognProject//crawl//raw_data//"


    
def get_next_target(page):
    start_link = page.find('<td><a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)    
    url = URL_BASE + page[start_quote + 1:end_quote]
    print url        
    content = urlutils.get_page(url)    
    write_file(content, page, end_quote)
        
    return url, end_quote



def write_file(content, page, end_quote): 
    
    name = get_file_name(page, end_quote)
    #fname0 = os.path.join(dir_name, name) 
    fname0 = dir_name + "//" + name
    fname = fname0    
    i = 0 
    while (os.path.isfile(fname)): 
        i+=1        
        fname =  fname0[:-5]+"-"+str(i)+'.html'
                                   
    fout = open(fname, 'w')
    print fname
    fout.write(content)


def get_target_urls(content): 
    links = []  
    while True: 
        url, endpos = get_next_target(content)
        if url:
            links.append(url)
            content = content[endpos:]
        else:
            break
    return links
        

def get_file_name(page, end_quote): 

    start_name = page.find(">", end_quote)+1
    end_name = page.find("<", start_name)
    if page.find("/", start_name, end_name) > -1 :
        start_name = page.find("/", start_name)+1
    
    fname = page[start_name:end_name]
    fname = fname.strip()
    fname = fname.replace(" ", "_")
    fname = fname.replace("/", "_")
    fname = fname.replace("?", "_")    
    fname = fname.replace("!", "_")
    fname = fname.replace("'", "_")
    fname = fname.replace("’", "_")    
    print fname
    
    return fname + ".html" 
    
       
def crawl_url(seed): # returns list of crawled links
    
    crawled = []    
    content = urlutils.get_page(seed)    
    crawled = get_target_urls(content) 

    return crawled


# create a directory with the name of the URL if it does not exist
# if it exists, clean the files from the directory 
dir_name = urlutils.get_stem_url(URL1)
dir_name = PREFIX+dir_name 
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
utils.clean_dir(dir_name)

#crawl urls 
crawled = crawl_url(URL1)
fout = open(dir_name+"//_url_list.txt",'w')    
utils.print_list(crawled, fout)    
fout.close()
