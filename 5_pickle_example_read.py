import pickle

infile = open("names_pickle_file.dat","rb")

names = pickle.load(infile)

print(type(names))

print(names)

name = input("Add a name to the list: ")
names.append(name)

print(names)
