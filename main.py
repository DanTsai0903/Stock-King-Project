import csv
import matplotlib.pyplot as pp
import datetime

#讀入檔案
#輸入要讀的檔名
filename = input()
filehandler = open(filename, 'r', newline = '', encoding = 'utf-8', errors = "ignore") #建立filehandler
inf = csv.DictReader(filehandler) #把所有資訊一行一行存在inf這個變數裡
chead2801 = inf.fieldnames #這行的作用是不要管第一行（欄位名稱）


#建立 日期、價格、5日平均價格清單
date = []
price = []
avgprice5 = [] #這個是5日線、也就是五日均價的意思
price5 = [] #這個list用來暫存最近5日的股價、每讀一行都會變一次
today = datetime.date(2000, 1, 1) #創立一個暫時的datetime變數，用來暫存當日日期
y, m, d = int(), int(), int() #用來暫存當天的 年、月、日

#從inf裡面一行一行地讀資料
for line in inf:

	#把所有數字(開盤價(元),最高價(元),最低價(元),收盤價(元),成交量(千股))轉成float跟int
	#(雖然有些好像是多餘的
	line["開盤價(元)"] = float(line["開盤價(元)"])
	line["最高價(元)"] = float(line["最高價(元)"])
	line["最低價(元)"] = float(line["最低價(元)"])
	line["收盤價(元)"] = float(line["收盤價(元)"])
	line["成交量(千股)"] = int(line["成交量(千股)"])

	#接下來把日期、價格、五日平均價寫入list裡面

	y, m, d = line["年月日"].split("/")
	today = datetime.date(int(y), int(m), int(d))
	date.append(today) #日期的部分

	price.append(line["收盤價(元)"]) #收盤價的部分

	price5.append(line["收盤價(元)"])
	sumPrice5 = 0
	if len(price5) > 5:
		del price5[0]
	if len(price5) == 5:
		for i in range(5):
			sumPrice5 += price5[i]
		avgprice5.append(sumPrice5 / 5)
	else:
		avgprice5.append(None) #5日線的部分


#簡單繪圖
#這只是拿來測試用
#不屬於我們的管轄範圍
pp.plot(date, price, label = "Price")
pp.plot(date, avgprice5, label = "Average Price in 5 Days")
pp.legend(loc = "lower right")
pp.xlabel("Date")
pp.ylabel("Price")
pp.xlim(date[0], date[-1])
pp.ylim(min(price) - 1, max(price) + 1) #讓上下界線看起來更寬裕一點
pp.show()


filehandler.close()