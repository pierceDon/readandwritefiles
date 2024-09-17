import csv

file_object = open('customers.csv','r')

csv_object = csv.reader(file_object)

x = 0

for line in csv_object:
    x += 1
    if x > 1:
        print(line[1])

