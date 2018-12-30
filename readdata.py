import csv


#讀入檔案
#輸入要讀的檔名
filename = input()
filehandler = open(filename, 'r', newline = '', encoding = 'utf-8', errors = "ignore") #建立filehandler
cheader = filehandler.readline() #這行的作用是不要管第一行（欄位名稱）
reader2 = csv.reader(filehandler, delimiter = ",")

shares code = []
Abbreviation = []
date = []
opening price = []
highest = []
lowest = []
closing price = []
volume = []
for i in range(1730):
	listdata = next(reader2)
	shares code.append(listdata[0])
	Abbreviation.append(listdata[1])
	date.append(listdata[2])
	opening price.append(float(listdata[3]))
	highest.append(float(listdata[4]))
	lowest.append(float(listdata[5]))
	closing price.append(float(listdata[6]))
	volume .append(int(listdata[7]))



filehandler.close()