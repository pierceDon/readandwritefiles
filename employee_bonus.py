import csv

file_object = open('employee_data.csv', 'r')
csv_object = csv.reader(file_object)
next(csv_object)


for row in csv_object:
    name = row[1]
    salary = float(row[3])
    bonus_percent = float(row[7])
    bonus_dollar = bonus_percent * salary
    pay = salary + bonus_dollar
    salary = str(salary)
    bonus_dollar = str(bonus_dollar)
    pay = str(pay)
    print(f'''
Name: {name}
Salary: $  {str(salary[:2])},{str(salary[2:])}0
Bonus: $  {str(bonus_dollar[:1])},{str(bonus_dollar[1:])}0
Pay: $  {str(pay[:2])},{str(pay[2:])}0
''')