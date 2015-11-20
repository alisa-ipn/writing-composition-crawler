# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:21:27 2015

@author: Alisa
"""

import urllib 
import utils

## Gets the stem of the URL, e.g., www.myurl.com from  http://www.myurl.com/1/nextpage?=etc
## @param url full URL
## @return stem_url  
def get_stem_url(url):
    start = url.find("//")+2
    end   =  url.find("/", start)
    stem_url = url[start:end]
    print stem_url        
    return stem_url
    

##from cs101@udacity 
def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""   
        
        
##from cs101@udacity 
def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

##from cs101@udacity
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

##from cs101@udacity 
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

##from cs101@udacity 
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

##from cs101@udacity 
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


##from cs101@udacity         
def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            utils.union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

index, graph = crawl_web('http://www.udacity.com/cs101x/final/multi.html')
        