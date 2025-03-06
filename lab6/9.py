#File handing.
#Last exercise: Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os
first_file = "C:/Users/user/niam/PP2/Lab 6/txt1.file"
if os.path.exists(first_file):
    if os.access(first_file, os.W_OK):
        os.remove(first_file)
        print("File deleted")
    else:
        print("We cannot delete this file.")
else: 
    print("File not found")
