'''
{
    'alan.alda': [ 72.0, 82.0, 100.0 ],
    'bob.barker': [ 72.0, 82.0, 100.0 ],
}
'''

import openpyxl as xl
from sys import argv
from pprint import pprint as pp

filename = argv[1]

grades = {}

# open the excel file
wb = xl.load_workbook(filename)

# for every worksheet
for ws in wb.worksheets:

#    for every row
    for row in ws.rows:

#        add or update a student in the dictionary
        id = row[0].value
        grade = float(row[1].value)

        if id in grades:
            # { 'alan.alda': [ 10 ] }
            ls = grades[id]
            ls.append(grade)
            # { 'alan.alda': [ 10, 20 ] }
        else:
            # {}
            grades[id] = [grade]
            # { 'alan.alda': [ 10 ] }

wb.close()

pp(grades)
# print averages

for id in grades:
    ls = grades[id]
    # option 1
    # tot = 0
    # for gr in ls:
    #     tot += gr
    # avg = tot / len(ls)

    # option 2
    # import statistics
    # avg = statistics.mean(ls)

    # option 3
    avg = sum(ls) / len(ls)
    print(f"{id:40}{avg:>10.1f}")
