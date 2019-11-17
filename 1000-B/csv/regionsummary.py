import os
import csv
import sys
from pprint import pprint as pp

if len(sys.argv) != 2:
    print("USAGE: python regionsummary.py [CSVFILE]")
    exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename) or not filename.endswith('.csv'):
    print("INVALID FILE")
    print("USAGE: python regionsummary.py [CSVFILE]")
    exit(2)

REPDIR = 'reports'
if not os.path.isdir(REPDIR):
    os.mkdir(REPDIR)

with open(filename, 'r') as fi:
    rdr = csv.reader(fi)
    reg_profits = {}
    reg_files = {}
    header_row = []
    for row in rdr:
        if rdr.line_num == 1:
            header_row = row
            continue

        region = row[0].strip().lower().replace(' ', '_')

        if region not in reg_profits:
            reg_profits[region] = 0.0
            filename = os.path.join(REPDIR, region + '.csv')
            reg_files[region] = open(filename, 'w', newline='')
            # Write header row
            wrtr = csv.writer(reg_files[region])
            wrtr.writerow(header_row[1:])

        try:
            reg_profits[region] += float(row[-1])
        except:
            continue

        wrtr = csv.writer(reg_files[region])
        wrtr.writerow(row[1:])

for file in reg_files.values():
    file.close()

#pp(reg_profits)
print(f"{'Region':40}{'Profits':>20}")
print("=" * 60)
for reg in reg_profits:
    prof = reg_profits[reg]
    print(f"{reg:40}${prof:>19,.2f}")

