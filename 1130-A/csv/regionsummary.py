import csv
import os
import sys
from pprint import pprint as pp

if len(sys.argv) != 2:
    print("USAGE: python regionsummary.py [CSVFILE]")
    exit(1)

filename = sys.argv[1]
filename = filename.strip()

if not os.path.isfile(filename) or not filename.endswith('.csv'):
    print('INVALID FILE')
    print("USAGE: python regionsummary.py [CSVFILE]")
    exit(2)

REPDIR = 'reports'
if not os.path.isdir(REPDIR):
    os.mkdir(REPDIR)

reg_profits = {}
reg_files = {}
header_row = []

with open(filename) as fi:
    rdr = csv.reader(fi)
    for row in rdr:
        if rdr.line_num == 1:
            header_row = row
            continue

        #print(row[0], row[-1])
        region = row[0]
        region = region.strip().lower().replace(' ', '_')
        
        if region not in reg_profits:
            # NEW REGION
            # create a new subtotal variable
            reg_profits[region] = 0.0
            # open a new file
            filename = os.path.join(REPDIR, region + '.csv')
            reg_files[region] = open(filename, 'w', newline='')
            # write the header row
            wrtr = csv.writer(reg_files[region])
            wrtr.writerow(header_row[1:])
        
        try:
            profits = float(row[-1])
        except:
            continue

        reg_profits[region] += profits

        wrtr = csv.writer(reg_files[region])
        wrtr.writerow(row[1:])

for file in reg_files.values():
    file.close()

#pp(reg_profits)
print(f"{'Region':40}{'Profits':>20}")
print('=' * 60)
for region in reg_profits:
    profits = reg_profits[region]
    regstring = region.replace('_', ' ').title()
    print(f"{regstring:40}${profits:>19,.2f}")
