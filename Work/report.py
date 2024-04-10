# report.py
#
# Exercise 2.4
import csv
import pprint

def read_portfolio(filename):
    '''
    Turning portfolio.csv into dictionary (or tuple if uncommenting lines 17+18 and commenting lines 19-22)
    '''
    portfolio = []
    f = open(filename, 'r')
    rows = csv.reader(f)
    next(rows)
    
    for row in rows:
#        rowt = (row[0], int(row[1]), float(row[2]))
#        portfolio.append(rowt)
        rowd = {}
        rowd['name'] = row[0]
        rowd['shares'] = int(row[1])
        rowd['price'] = float(row[2])
        portfolio.append(rowd)
    
    return(portfolio)


def read_prices(filename):
    '''
    Turning prices.csv into dictionary
    '''
    prices = {}
    f = open(filename, 'r')
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        if len(row) == 0:
            continue
        prices[row[0]] = float(row[1])    
    return(prices)


def gains_losses(price, value):
    '''
    Calculating the gains/losses when comparing the portfolio.csv and prices.csv files    
    '''
    current_value = 0
    total_cost = 0
    for v in value:
        total_cost += v['shares'] * v['price']
        if v['name'] in price:
            current_value += price[v['name']] * v['shares']
    gain_loss = current_value - total_cost
    return(gain_loss)

portfolio = 'Data/portfolio.csv'
prices = 'Data/prices.csv'
retire = gains_losses(read_prices(prices), read_portfolio(portfolio))
print(f'Der Gewinn beträgt: €{retire:0.2f}')

#price = read_prices(prices)
#pprint.pp(price)

#value = read_portfolio(portfolio)
#pprint.pp(value)