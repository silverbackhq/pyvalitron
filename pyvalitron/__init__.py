"""
PyValitron - Python Inputs Validation Library

@author: Clivern U{hello@clivern.com}
"""

__version__ = "1.0.0"

def read_file(file_path):
    content = ""
    with open(file_path) as f:
        content = f.read()
    return content