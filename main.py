import csv

filename = input()
filehandler1 = open(filename, 'r', newline = '', encoding = 'utf-8', errors = "ignore")
csv2801 = csv.DictReader(filehandler1)
chead2801 = csv2801.fieldnames
######print(chead2801)