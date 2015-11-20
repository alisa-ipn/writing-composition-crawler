# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:10:01 2015

@author: Alisa
"""

import sys, os
import shutil

# deletes only files, leaves subfolders
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

## clean dir and subfolders
def clean_dir_r(folder): 
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)            
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception, e:
            print e


def print_list(a_list, fout = sys.stdout):    
    for item in a_list: 
        print >> fout, item 
        
##from cs101@udacity 
def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)
        