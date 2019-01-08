import csv
import datetime
import matplotlib.pyplot as pp
import numpy as np
import matplotlib.gridspec as gridspec

#讀入檔案
#輸入要讀的檔名
filename = "stocks.txt"
filehandler = open(filename, 'r', newline = '', encoding = 'utf-8', errors = "ignore") #建立filehandler
reader2 = csv.DictReader(filehandler)
####################################################################
#csv.reader被csv.DictReader來取代，dictreader的好處是可以用欄位名稱來呼叫#
###################################################################
cheader = reader2.fieldnames #這行的作用是不要管第一行（欄位名稱）



class stock:
	def __init__(self, code):
		#新建那些list, 包括date, opening, ......
		#MA(moving average)均線
		self.code = code
		self.abbreviation = stockDict_alldata[code][0] #公司簡稱
		self.date = stockDict_alldata[code][1] #日期
		self.opening = stockDict_alldata[code][2]#開盤價
		self.highest = stockDict_alldata[code][3] #最高價
		self.lowest =  stockDict_alldata[code][4] #最低價
		self.closing = stockDict_alldata[code][5] #收盤價
		self.volume = stockDict_alldata[code][6] #成交量(千股)

		#計算均線--------------------------------------------------------
		self.MA5 = [] #周線(5日線), a list
		self.MA20 = [] #月線(20日線), a list
		self.MA60 = [] #季線(60日線), a list
		self.MA120 = [] #半年線(120日線), a list

		c = 1 #counting
		for i in range(len(self.closing)):
			if c >= 5:
				self.MA5.append(sum(self.closing[(c - 5) : c]) / 5)
				if c >= 20:
					self.MA20.append(sum(self.closing[(c - 20) : c]) / 20)
					if c >= 60:
						self.MA60.append(sum(self.closing[(c - 60) : c]) / 60)
						if c >= 120:
							self.MA120.append(sum(self.closing[(c - 120) : c]) / 120)
						else:
							self.MA120.append(None)
					else:
						self.MA60.append(None)
						self.MA120.append(None)
				else:
					self.MA20.append(None)
					self.MA60.append(None)
					self.MA120.append(None)
			else:
				self.MA5.append(None)
				self.MA20.append(None)
				self.MA60.append(None)
				self.MA120.append(None)
			c += 1
		
		#計算日KD值----------------------------------------------------------
		self.K = [] 
		self.D = [] 

		#(第一個日ＫＤ值)
		self.RSV = (self.closing[0] - self.lowest[0]) / (self.highest[0] - self.lowest[0]) * 100
		self.K.append(self.RSV / 3 + 100 / 3)
		self.D.append(self.K[0] / 3 + 100 / 3)

		for i in range(1, len(self.closing)):
			if self.highest[i] != self.lowest[i]:
				self.RSV = (self.closing[i] - self.lowest[i]) / (self.highest[i] - self.lowest[i]) * 100
			else:
				self.RSV = self.K[i - 1]
			self.K.append(self.RSV / 3 + self.K[i - 1] * 2 / 3)
			self.D.append(self.K[i] / 3 + self.D[i - 1] * 2 / 3)

		#計算週KD值----------------------------------------------------------
		self.Kweek = [] 
		self.Dweek = [] 
		for i in range(4):
			self.Kweek.append(None)
			self.Dweek.append(None)

		#(第一個週ＫＤ值)
		self.RSVweek = (self.closing[0] - min(self.lowest[0 : 5])) / (max(self.highest[0 : 5]) - min(self.lowest[0 : 5])) * 100
		self.Kweek.append(self.RSVweek / 3 + 100 / 3)
		self.Dweek.append(self.Kweek[4] / 3 + 100 / 3)

		for i in range(5, len(self.closing)):
			self.RSVweek = (self.closing[i] - min(self.lowest[(i - 4) : (i + 1)])) / (max(self.highest[(i - 4) : (i + 1)]) - min(self.lowest[(i - 4) : (i + 1)])) * 100
			self.Kweek.append(self.RSVweek / 3 + self.Kweek[i - 1] * 2 / 3)
			self.Dweek.append(self.Kweek[i] / 3 + self.Dweek[i - 1] * 2 / 3)




		#計算月KD值----------------------------------------------------------
		self.Kmonth = [] 
		self.Dmonth = [] 
		for i in range(19):
			self.Kmonth.append(None)
			self.Dmonth.append(None)

		#(第一個月ＫＤ值)
		self.RSVmonth = (self.closing[0] - min(self.lowest[0 : 20])) / (max(self.highest[0 : 20]) - min(self.lowest[0 : 20])) * 100
		self.Kmonth.append(self.RSVmonth / 3 + 100 / 3)
		self.Dmonth.append(self.Kmonth[19] / 3 + 100 / 3)

		for i in range(20, len(self.closing)):
			self.RSVmonth = (self.closing[i] - min(self.lowest[(i - 19) : (i + 1)])) / (max(self.highest[(i - 19) : (i + 1)]) - min(self.lowest[(i - 19) : (i + 1)])) * 100
			self.Kmonth.append(self.RSVmonth / 3 + self.Kmonth[i - 1] * 2 / 3)
			self.Dmonth.append(self.Kmonth[i] / 3 + self.Dmonth[i - 1] * 2 / 3)



	def __str__(self):
		return self.code
	
	
stockDict_alldata = dict() #儲存一家一家的公司，key是股票代碼，value是那間公司的「歷史資料」
for line in reader2:
	#如果以「line["證券代碼"]」為key的資料不存在
		#則新增一筆資料、key是line["證券代碼"]、value是歷史資料
	#然後把這行line的每一欄位加入到以「line["證券代碼"]」為key的資料中
	allapecificdata = [] #一個大list，放下面所有小list
	
	date = [] #時間
	opening = [] #開盤價
	highest = [] #最高價
	lowest = [] #最低價
	closing = [] #收盤價
	volume = [] #成交量

	if line["證券代碼"].strip() not in stockDict_alldata.keys():
		abbreviation = line["簡稱"].strip()
		d = line["年月日"].split("/")
		date.append(datetime.date(int(d[0]), int(d[1]), int(d[2])))
		opening.append(float(line["開盤價(元)"]))
		highest.append(float(line["最高價(元)"]))
		lowest.append(float(line["最低價(元)"]))
		closing.append(float(line["收盤價(元)"]))
		volume.append(float(line["成交量(千股)"]))
		allapecificdata = [abbreviation, date, opening, highest, lowest, closing, volume]
		stockDict_alldata[line["證券代碼"].strip()] = allapecificdata
		
	else:
		d = line["年月日"].split("/")
		stockDict_alldata[line["證券代碼"].strip()][1].append(datetime.date(int(d[0]), int(d[1]), int(d[2])))
		stockDict_alldata[line["證券代碼"].strip()][2].append(float(line["開盤價(元)"]))
		stockDict_alldata[line["證券代碼"].strip()][3].append(float(line["最高價(元)"]))
		stockDict_alldata[line["證券代碼"].strip()][4].append(float(line["最低價(元)"]))
		stockDict_alldata[line["證券代碼"].strip()][5].append(float(line["收盤價(元)"]))
		stockDict_alldata[line["證券代碼"].strip()][6].append(float(line["成交量(千股)"]))
		


stockDict_stock = dict() #儲存一家一家的公司，key是股票代碼，value是那間公司的「資料」（所以新建一個「stock」class, 這個class 儲存一家公司的資料）
for key in stockDict_alldata.keys():
	stockDict_stock[key] = stock(key)
filehandler.close()


test = "2888" #inputting the code of the company
pp.figure() #creating a graph
gs1 = gridspec.GridSpec(3, 1, height_ratios=[3, 1, 1]) #setting the ratio of height to be 3:1:1

#converting lists to np.arrays
npdate = np.array(stockDict_stock[test].date)
npclosing = np.array(stockDict_stock[test].closing)
npMA20 = np.array(stockDict_stock[test].MA20)
npMA60 = np.array(stockDict_stock[test].MA60)
npMA120 = np.array(stockDict_stock[test].MA120)
npK = np.array(stockDict_stock[test].K)
npD = np.array(stockDict_stock[test].D)
npvolume = np.array(stockDict_stock[test].volume)

#the first part of graph -- price, including Moving Averages
pp.subplot(gs1[0])
pp.plot(npdate, npclosing, color = "#706666", label = "Price")
pp.plot(npdate, npMA20, color = "#2020BB", label = "Average Price in 20 Days")
pp.plot(npdate, npMA60, color = "#FF9900", label = "Average Price in 60 Days")
pp.plot(npdate, npMA120, color = "#60DD40", label = "Average Price in 120 Days")
pp.tick_params(
    axis='x',          # changes apply to the x-axis
    which='major',      # both major and minor ticks are affected
    bottom=True,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False,
    direction = "in")
pp.legend(loc = "upper left")
pp.ylabel("Price")
pp.xlim(stockDict_stock[test].date[0], stockDict_stock[test].date[-1])
pp.ylim(min(stockDict_stock[test].closing) * 0.99, max(stockDict_stock[test].closing) * 1.01) #讓上下界線看起來更寬裕一點

#the second part of graph -- KD
pp.subplot(gs1[1])
pp.plot(npdate, npK, color = "#CC4444", label = "K(Day)")
pp.plot(npdate, npD, color = "#33CC33", label = "D(Day)")
pp.tick_params(
    axis='x',          # changes apply to the x-axis
    which='major',      # both major and minor ticks are affected
    bottom=True,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False, 
    direction = "in")
pp.legend(loc = "upper left")
pp.ylabel("KD(Day)")
pp.xlim(stockDict_stock[test].date[0], stockDict_stock[test].date[-1])
pp.ylim(0, 100)

#the third part of graph -- volume
pp.subplot(gs1[2])
pp.bar(npdate, npvolume, color = "#2055AA", width = 1)
pp.tick_params(
    axis='x',          # changes apply to the x-axis
    which='major',      # both major and minor ticks are affected
    bottom=True,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelsize = 6.4)        
pp.legend(loc = "lower right")
pp.xlabel("Date")
pp.ylabel("volume\n(in 1000 stocks)")
pp.xlim(stockDict_stock[test].date[0], stockDict_stock[test].date[-1])
pp.ylim(0, max(stockDict_stock[test].volume))

pp.show()