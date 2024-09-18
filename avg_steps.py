import csv

file_object = open('steps.csv', 'r')
csv_object = csv.reader(file_object)
next(csv_object)

month_with_steps = {}
month_num = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
}

for row in csv_object:
    month = int(row[0])
    step = int(row[1])
    if month in month_with_steps:
        month_with_steps[month].append(step)
    else:
        month_with_steps[month] = [step]

for key, value in month_with_steps.items():
    step_avg = sum(value) / len(value)
    print(f'''
{month_num[key]} - {round(step_avg,2):,}
''')





