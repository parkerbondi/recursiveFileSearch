# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:44:34 2022
@author: Parker
"""

import os, glob
global allFilesForRecursiveSearch
allFilesForRecursiveSearch = []

def recursiveSearch(item):
    
    """
    Requires allFilesForRecursiveSearch to be a global variable
    """
    
    try:
        subItems = os.listdir(item)
        subItems = [item + "\\" + x for x in subItems]
        for subItem in subItems:
            recursiveSearch(subItem)
            b=1
    except:
        print(item)
        allFilesForRecursiveSearch.append(item)

masterFolder = r"G:\Shared drives\Animal Division  Equine\1. Design & Development\Temperature Testing"

recursiveSearch(masterFolder)
fileList = []

fileList = [file for file in allFilesForRecursiveSearch if "temp" in file.split('\\')[-1] and ".csv" in file.split('\\')[-1]]