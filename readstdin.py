import csv
import sys
import datetime
import re

def isdate(string):
    try:
        datetime.datetime.strptime(string, '%Y-%m-%d')
        return True
    except:
        return False

csvfile = csv.reader(sys.stdin, delimiter='\t')

datalist = []
for line in csvfile:
    line = iter(line)
    for field in line:
        if isdate(field):
            date = datetime.datetime.strptime(field, '%Y-%m-%d')
            desc = next(line)
            category = next(line)
            amount = float(next(line).replace(".", "").replace(",", "."))
            saldo = next(line)
            try:
                date = datetime.datetime.strptime(desc, 'Kortköp %y%m%d')
            except ValueError:
                pass
            desc = re.sub("^Kortköp [0-9]{6}", "Kortköp", desc)
            desc = re.sub("^Reservation Kortköp", "Kortköp", desc)
            datalist += [{'date': date, 'amount': amount, 'desc': desc}]
#print(sorted(datalist, key=lambda k: k['date']))
#for line in sorted(datalist, key=lambda k: k['date']):
#    print("%s\t%.2f\t%s" % (line['date'].strftime("%Y-%m-%d"), line['amount'], line['desc']))
print("=== Expenses ===")
for line in sorted(datalist, key=lambda k: k['date']):
    if line['amount'] < 0:
        print("%s\t%.2f\t%s" % (line['date'].strftime("%Y-%m-%d"), -line['amount'], line['desc']))
print()
print("=== Income ===")
for line in sorted(datalist, key=lambda k: k['date']):
    if line['amount'] > 0:
        print("%s\t%.2f\t%s" % (line['date'].strftime("%Y-%m-%d"), line['amount'], line['desc']))

