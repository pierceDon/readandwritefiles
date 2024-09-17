import pickle

outfile = open("names_pickle_file_write.dat","ab")

names = []    
name = input("Add a name to the list: ")
names.append(name)


pickle.dump(names,outfile)

outfile.close()


