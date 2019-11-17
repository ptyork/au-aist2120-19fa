'''
{
    'alan.alda': [ 75, 83, 72 ],
    'benny.barker': [ 85, 100, 77], ...
}
'''

import openpyxl as xl
from sys import argv
from pprint import pprint as pp

grades = {}
filename = argv[1]

# open excel workbook
wb = xl.load_workbook(filename)

# for each sheet in the workbook
for sheet in wb.worksheets:
    #print(sheet.title)

#   for each row in sheet
    for row in sheet.rows:

#     get the id and grade (lazy without error checking)
        id = row[0].value
        grade = float(row[1].value)
        print(id, grade)

#     add or update the grade list for id
        if id in grades:
            # 'alan.alda': [ 75 ]
            ls = grades[id]   # [ 75 ]
            ls.append(grade)
        else:
            # NO ENTRY IN DICTIONARY YET
            # ls = []
            # ls.append(grade)
            # grades[id] = ls
            grades[id] = [grade]
            # 'alan.alda': [ 75 ]

wb.close()

# average and print grades for id
pp(grades)

for id in grades:
    ls = grades[id]
    avg = sum(ls) / len(ls)
    print(f"{id:40}{avg:>10.1f}")
