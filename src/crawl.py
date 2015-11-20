# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:49:22 2015

@author: Alisa
"""

import urllib
import sys 
import os, shutil


URL1 = "http://abc-english-grammar.com/1/sochinenia_po_angliiskomu_yaziku.htm"
str_to_look = "<a href=\"http://abc-english-grammar.com/1/sochinenia_po_angliiskomu_yaziku"

URL2 = "http://en365.ru/topic.htm"
URL3 = "http://www.native-english.ru/topics"
URL4 = "http://iloveenglish.ru/topics"
URL5 = "http://www.alleng.ru/english/top_08.htm" 


PREFIX = "E://Study//SpeechRecognProject//crawl//raw_data//"

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""

    
def get_next_target(page):
    start_link = page.find(str_to_look)
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)    
    url = page[start_quote + 1:end_quote]    
    
    content = get_page(url)
    
    #start_name = page.find(">", end_quote)+1
    #end_name = page.find("<", start_name)
    
    write_file(content, page, end_quote)
        
    return url, end_quote


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


##from original 
def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

##from original 
def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

##from original         
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

##from original 
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

        

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
    


def get_dir_name(url):
    start = url.find("//")+2
    end   =  url.find("/", start)
    dir_name = url[start:end]
    print dir_name
    
    
    return dir_name 

    
def crawl_url(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    '''   
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    
    '''
    
    content = get_page(seed)    
    crawled = get_target_urls(content) 
    #for link in crawled: 
    #    print link 
        
    return crawled


def clean_dir(folder): 
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # uncomment to delete subdirs             
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception, e:
            print e



# create  adirectory with teh name of the file if it does not exist
# if it exists, clean the files from the directory 
dir_name = get_dir_name(URL1)
dir_name = PREFIX+dir_name 
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
clean_dir(dir_name)

#crawl urls 
crawled = crawl_url(URL1)
