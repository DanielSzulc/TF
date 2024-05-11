"""
Helper functions code for TensorFlow Certficate Course 
"""
import zipfile
import os

def unzip_data(filepath):
    zip_handler = zipfile.ZipFile(filepath)
    zip_handler.extractall()
    zip_handler.close()

def walk_through_dir(path_to_dir):
    for dirpath, dirnames, filenames in os.walk(path_to_dir):
        print(f"There is {len(dirnames)} dirs and {len(filenames)} in '{dirpath}'."
    
