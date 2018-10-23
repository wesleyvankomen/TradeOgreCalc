#!/usr/bin/python
import sys
import csv

net = 0.0
net_amount = 0


if len(sys.argv) > 1:
    market = sys.argv[1]
else:
    market = 'BTC-GRFT'


if len(sys.argv) > 2:
    file_name = sys.argv[2]
else:
    file_name = 'export_trades.csv'

buy = True
price = 0.0
amount = 0

with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
 
    for row in csv_reader:
        
        #skip unrelated transactions
        if row[1] !=  market:
            continue
        
        #figure out buy or sell
        if row[0] == 'BUY':
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

if net_amount != 0:
    print('%s net units sold' % str(-net_amount))
    print('average unit price: %s Satoshis' % str((-net / float(net_amount) * 100000000)))

print('%s BTC net gain' % str(net)[:10])
