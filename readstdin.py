import csv
import sys
import datetime

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
            amount = next(line)
            saldo = next(line)
            datalist += [[date, amount, desc]]
print(datalist)
