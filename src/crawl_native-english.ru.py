# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 20:36:14 2015

@author: Alisa
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:49:22 2015

@author: Alisa
"""

import os
import utils, urlutils



URL1 = "http://www.native-english.ru/topics"
str_to_look = "<a href=\"/topics/category/"
URL_BASE = "http://www.native-english.ru"
str_to_look_in_topics = "<a href=\"/topics/"
PAGE_NUMS = ["/2", "/3", "/4", "/5", "/6", "/7"] 

URL4 = "http://iloveenglish.ru/topics"
URL5 = "http://www.alleng.ru/english/top_08.htm" 


PREFIX = "E://Study//SpeechRecognProject//crawl//raw_data//"


def get_file_name(page, end_quote): 

    start_name = page.find(">", end_quote)+1
    end_name = page.find("<", start_name)
    if page.find("-", start_name, end_name) > -1 :
        end_name = page.find("-", start_name)
    
    fname = page[start_name:end_name]
    fname = fname.strip()
    fname = fname.replace(" ", "_")
    fname = fname.replace("/", "_")
    fname = fname.replace("?", "_")    
    fname = fname.replace("!", "_")
    fname = fname.replace("'", "_")
    print fname
    
    return fname + ".html" 

def write_file(content, page, end_quote): 
    
    name = get_file_name(page, end_quote)
    fname0 = dir_name + "//" + name
    fname = fname0    
    i = 0 
    while (os.path.isfile(fname)): 
        i+=1        
        fname =  fname0[:-5]+"-"+str(i)+'.html'
                                   
    fout = open(fname, 'w')
    print fname
    fout.write(content)
    
 
def get_file_name_from_url(url): 
    return url[url.rfind("/")+1:] +".html"
 
 
def write_file2(content, url, param_dir_name): 
    write_dir_name = param_dir_name
    #print "Write dir: ", write_dir_name
    name = get_file_name_from_url(url)
    #fname = os.path.join(write_dir_name, name)
    fname = write_dir_name+"//"+ name                                   
                                       
    fout = open(fname, 'w')
    print  fname
    fout.write(content) 
        
   
def get_next_target(page, param_str_to_look = "<a href="):
    str_to_look = param_str_to_look
    start_link = page.find(str_to_look)
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)    
    url = URL_BASE + page[start_quote + 1:end_quote]        
        
    return url, end_quote


def get_target_urls(content, param_str_to_look = "<a href="): 
    links = []    
    str_to_look = param_str_to_look     
    while True: 
        url, endpos = get_next_target(content,  str_to_look)
        if url:         
            if url[-2:] in PAGE_NUMS and url[-2:] not in visited:                
                    print "Intermediate url: ", url                
                    visited.append(url[-2:])                 
                    urls = crawl_url(url, str_to_look)
                    links+=urls
            else:
                print "Crawled url: ", url                  
                links.append(url)
                content = content[endpos:]
        else:
            break
    return links
               
def crawl_url(seed, param_str_to_look = "<a href="): # returns list of crawled links    
    str_to_look = param_str_to_look           
    crawled = []    
    content = urlutils.get_page(seed)    
    crawled = get_target_urls(content, str_to_look) 

    return crawled


# create a directory with the name of the URL if it does not exist
# if it exists, clean the files from the directory 
dir_name = urlutils.get_stem_url(URL1)
dir_name = PREFIX+dir_name 
print dir_name
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
utils.clean_dir(dir_name)


#crawl urls 
crawled = crawl_url(URL1, str_to_look)
fout = open(dir_name+"//_url_list.txt",'w')    
utils.print_list(crawled, fout)    
fout.close()


for url in crawled: 
    crawled_topic = []     
    visited = []
    subdir_name = url[url.rfind("/")+1:]
    subdir_name = dir_name+"//"+subdir_name
    
    if not os.path.exists(subdir_name):
        os.mkdir(subdir_name)
    utils.clean_dir(subdir_name)
    
    crawled_topic = crawl_url(url, str_to_look_in_topics)    
    print "Crawled a topic!"
    print "Subdir name: ", subdir_name    
    for composition_url in crawled_topic:   
        #print "Extracting from url: ", composition_url
        content = urlutils.get_page(composition_url)    
        write_file2(content, composition_url, subdir_name)    
    
    fout = open(subdir_name+"//_url_list.txt",'w')    
    utils.print_list(crawled_topic, fout)    
    fout.close()
