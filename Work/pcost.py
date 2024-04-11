# pcost.py
#
# Exercise 1.27

import csv
import sys #allow parsing arguments when executing

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    total_cost = 0
    #next(rows) # skip header
    headers = next(rows)
    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            nshare = int(record['shares'])
            nprice = float(record['price'])
            total_cost += nshare * nprice
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
    f.close()
    print(record)
    return(total_cost)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Die Gesamtkosten betragen: €{cost}')