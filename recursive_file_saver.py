# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:13:55 2022
@author: Parker
"""
import os, glob, shutil
global all_files_for_recursive_search
all_files_for_recursive_search = []
global all_folders_for_recursive_search
all_folders_for_recursive_search = []

def recursive_folder_search(item):
    
    """
    Requires all_folders_for_recursive_search to be a global variable
    """
    # print(item)
    try:
        sub_items = os.listdir(item)
        sub_items = [item + "\\" + x for x in sub_items]
        for sub_item in sub_items:
            recursive_folder_search(sub_item)
    except:
        # print(item)
        all_folders_for_recursive_search.append(item.split(item.split('\\')[-1])[0])
                
def recursive_file_search(item):
    
    """
    Requires all_files_for_recursive_search to be a global variable
    """
    
    try:
        sub_items = os.listdir(item)
        sub_items = [item + "\\" + x for x in sub_items]
        for sub_item in sub_items:
            recursive_file_search(sub_item)
    except:
        print(item)
        all_files_for_recursive_search.append(item)

def file_to_copy(source, destination):
    if 'data_with_features' in source:
        a=1
    try:
        shutil.copy(source, destination)
        # print(destination + " copied successfully.")
     
    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
     
    # If there is any permission issue
    except PermissionError:
        print("Permission denied.")
     
    # For other errors
    except:
        print(source + " Error occurred while copying file.")


######## Manual Method ########
# master_path = r"G:\My Drive\AFE4960P EVM Evaluation\PPG Testing\LED Current Test Multiple Subjects\Settings - TS 01"
# new_path = r"G:\Shared drives\QDesign-HW\Gen 2.0 Biometrics\Testing\PPG Testing\LED Current Test Multiple Subjects"


######## Continuous Automatic Method ########
print('Copy and paste the location where you want to save your folders:')
new_path = input()

master_path = ''
while master_path != 'stop':
    print('Copy and paste the path to the folder you wish to copy (including the folder). If you are done type "stop":')
    master_path = input()
    master_folder = master_path.split('\\')[-1]
    
    recursive_folder_search(master_path)
    all_folder_paths = list(dict.fromkeys(all_folders_for_recursive_search))
    all_folder_paths.sort()
    
    for path in all_folder_paths:
        # print(path)
        additional_path = path.split(master_folder)[-1]
        # print(additional_path)
        try:
            os.mkdir(new_path + '\\' + master_folder + '\\' + additional_path)
        except FileExistsError:
            continue
    
    recursive_file_search(master_path)
    file_lst = [file for file in all_files_for_recursive_search if "desktop" not in file]
    
    for file in file_lst:
        try:
            file_to_copy(file, new_path + '\\' + master_folder + '\\' + file.split(master_folder)[-1])
        except:
            continue
    # a=1
