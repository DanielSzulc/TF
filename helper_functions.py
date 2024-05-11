"""
Helper functions code for TensorFlow Certficate Course 
"""
import zipfile

def unzip_data(filepath):
    zip_handler = zipfile.ZipFile(filepath)
    zip_handler.extractall()
    zip_handler.close()
