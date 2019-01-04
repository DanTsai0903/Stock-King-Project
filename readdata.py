import csv
import datetime

#讀入檔案
#輸入要讀的檔名
filename = input()
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
		self.opening = stockDict_alldata[code][2][-1] #今日開盤價
		self.highest = stockDict_alldata[code][3][-1] #今日最高價
		self.lowest =  stockDict_alldata[code][4][-1] #今日最低價
		self.closing = stockDict_alldata[code][5][-1] #今日收盤價
		self.volume = stockDict_alldata[code][6][-1] #今日成交量(千股)
		self.MA5 = sum(stockDict_alldata[code][5][-5 : -1]) / 5 #周線(5日線)
		self.MA20 = sum(stockDict_alldata[code][5][-20 : -1]) / 20 #月線(20日線)
		self.MA60 = sum(stockDict_alldata[code][5][-60 : -1]) / 60 #季線(60日線)
		
		#計算KD值----------------------------------------------------------
		self.initialK = 50 #初始K
		self.initialD = 50 #初始D
		for i in range(200):
			preday = 200 - i #因為是從兩百天前開始算，所以要用200去減
			
			#未成熟隨機值
			self.RSV = (stockDict_alldata[code][5][-preday] - min(stockDict_alldata[code][5][-preday-9 : -preday])) / (max(stockDict_alldata[code][5][-preday-9 : -preday]) - min(stockDict_alldata[code][5][-preday-9 : -preday])) * 100
			
			self.K = self.initialK * (2/3) + self.RSV * (1 / 3)#當日k值
			self.D = self.initialD * (2/3) + self.K * (1 / 3)#當日d值
			
			#將今日k值變成昨日k值,d值也一樣
			self.initialK = self.K
			self.initialD = self.D

		self.K = self.initialK
		self.D = self.initialD
		

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
		date.append(line["年月日"])
		opening.append(float(line["開盤價(元)"]))
		highest.append(float(line["最高價(元)"]))
		lowest.append(float(line["最低價(元)"]))
		closing.append(float(line["收盤價(元)"]))
		volume.append(float(line["成交量(千股)"]))
		allapecificdata = [abbreviation, date, opening, highest, lowest, closing, volume]
		stockDict_alldata[line["證券代碼"].strip()] = allapecificdata
		
	else:
		stockDict_alldata[line["證券代碼"].strip()][1].append(line["年月日"])
		stockDict_alldata[line["證券代碼"].strip()][2].append(float(line["開盤價(元)"]))
		stockDict_alldata[line["證券代碼"].strip()][3].append(float(line["最高價(元)"]))
		stockDict_alldata[line["證券代碼"].strip()][4].append(float(line["最低價(元)"]))
		stockDict_alldata[line["證券代碼"].strip()][5].append(float(line["收盤價(元)"]))
		stockDict_alldata[line["證券代碼"].strip()][6].append(float(line["成交量(千股)"]))
		


stockDict_stock = dict() #儲存一家一家的公司，key是股票代碼，value是那間公司的「資料」（所以新建一個「stock」class, 這個class 儲存一家公司的資料）
for key in stockDict_alldata.keys():
	stockDict_stock[key] = stock(key)


filehandler.close()