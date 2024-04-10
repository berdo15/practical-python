# pcost.py
#
# Exercise 1.27

import csv
import sys #allow parsing arguments when executing

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    total_cost = 0
    next(rows) # skip header
    for row in rows:
        total_cost += float(row[1]) * float(row[2])
    f.close()
    return(total_cost)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Die Gesamtkosten betragen: €{cost}')