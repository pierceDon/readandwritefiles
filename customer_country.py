import csv

def main():
    file_object = open('customers.csv','r')
    csv_object = csv.reader(file_object)
    outfile = open('customer_country.csv', 'w')
    csv_outfile = csv.writer(outfile)
    next(csv_object)

    for row in csv_object:
        new_row = (row[1], row[2], row[4])
        csv_outfile.writerow(new_row)
        print(new_row)

main()


# customerlist = []

# for row in csv_object:
#     customerlist += [row] 

# for x in range(1, len(customerlist)):
#     print(customerlist[x][1], customerlist[x][2], customerlist[x][4])
    