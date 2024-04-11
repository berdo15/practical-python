# report.py
#
# Exercise 2.4
import csv
import pprint

def read_portfolio(filename):
    '''
    Turning portfolio.csv into list of dictionaries (or tuple if uncommenting lines 17+18 and commenting lines 19-22)
    '''
    portfolio = []
    f = open(filename, 'r')
    rows = csv.reader(f)
    headers = next(rows)

    for rowno, row in enumerate(rows, start=1):
#        rowt = (row[0], int(row[1]), float(row[2]))
#        portfolio.append(rowt)
#        rowd = {}
#        rowd['name'] = row[0]
#        rowd['shares'] = int(row[1])
#        rowd['price'] = float(row[2])
        report = dict(zip(headers, row))
        reportd = {}
        try:
            reportd['name'] = report['name']
            reportd['shares'] = int(report['shares'])
            reportd['price'] = float(report['price'])

        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
        portfolio.append(reportd)

    return(portfolio)


def read_prices(filename):
    '''
    Turning prices.csv into dictionary
    '''
    prices = {}
    f = open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        if len(row) == 0:
            continue
        prices[row[0]] = float(row[1])    
    return(prices)


def gains_losses(portfolio, price):
    '''
    Calculating the gains/losses when comparing the portfolio.csv and prices.csv files    
    '''
    current_value = 0
    total_cost = 0
    for c in portfolio:
        total_cost += int(c['shares']) * float(c['price'])
        if c['name'] in price:
            current_value += price[c['name']] * int(c['shares'])
    gain_loss = current_value - total_cost
    return(gain_loss)

portfolio = 'Data/portfolio.csv'
prices = 'Data/prices.csv'
retire = gains_losses(read_portfolio(portfolio), read_prices(prices))
print(f'Der Gewinn beträgt: €{retire:0.2f}')

#price = read_prices(prices)
#pprint.pp(price)

#value = read_portfolio(portfolio)
#pprint.pp(value)