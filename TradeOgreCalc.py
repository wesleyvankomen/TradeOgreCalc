#!/usr/bin/python
import sys
import csv

net = 0.0
net_amount = 0
transactions = 0


if len(sys.argv) > 1:
    market = sys.argv[1].upper()
else:
    market = 'BTC-TRTL'

if len(sys.argv) > 2:
    file_name = sys.argv[2]
else:
    file_name = 'export_trades.csv'

buy = True
price = 0.0
amount = 0
units = ['BTC', 'Satoshis']

with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
 
    for row in csv_reader:
        
        #skip unrelated transactions
        if row[1] != market:
            continue
        
        transactions += 1

        #figure out buy or sell
        if row[0].lower() == 'buy':
            buy = True
        else:
            buy = False

        #set price and amount
        price = float(row[4])
        amount = float(row[3])

        #update net
        if buy:
            net -= price * amount
            net_amount += amount
        else:
            net += price * amount
            net_amount -= amount

if market[:3] == 'LTC':
    units = ['LTC', 'Litoshis']
    
if net_amount > 0:
    print('%f net units bought' % net_amount)
    
if net_amount < 0:
    print('%f net units sold' % -net_amount)

if net_amount != 0:
    print('average unit price: %f %s' % ((-net / float(net_amount) * 100000000), units[1]))

if transactions > 0:
    print('%s %s net gain over %d transactions' % (str(net)[:10], units[0], transactions))
else:
    print('no transactions found for %s' % market)

