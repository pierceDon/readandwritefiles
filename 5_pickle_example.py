# Python pickle module is used for serializing and de-serializing a Python object structure. Any object in Python can be pickled
# so that it can be saved on disk. What pickle does is that it “serializes” the object first before writing it to file.
# Pickling is a way to convert a python object (list, dict, etc.) into a character stream. The idea is that this character
# stream contains all the information necessary to reconstruct the object in another python script.

import pickle
import os

eof = False
path = 'C:/Users/johnny_bhojwani/Box Sync/MIS 4V98 - PYTHON/Scripts/Chapter 9 - Dictionaries/names_pickle_file.dat'

outfile = open("names_pickle_file.dat","ab")
infile = open("names_pickle_file.dat","rb")
print(os.path.getsize(path))
input()

if os.path.getsize(path) > 0:
    names = pickle.load(infile)
    name = input("Add a name to the list: ")
    names.append(name)
else:
    names = []    
    name = input("Add a name to the list: ")
    names.append(name)


pickle.dump(names,outfile)
outfile.close()

print(names)
