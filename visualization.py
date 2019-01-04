import tkinter as tk
import tkinter.font as tkFont
import csv
import datetime


class stock:
	def __init__(self, code):
		#新建那些list, 包括date, opening, ......
		#MA(moving average)均線
		self.code = code
		self.abbreviation = stockDict_alldata[code][0] #公司簡稱
		self.opening = stockDict_alldata[code][2] #今日開盤價
		self.highest = stockDict_alldata[code][3] #今日最高價
		self.lowest =  stockDict_alldata[code][4] #今日最低價
		self.closing = stockDict_alldata[code][5] #今日收盤價
		self.volume = stockDict_alldata[code][6] #今日成交量(千股)

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
		


class BigFrame(tk.Frame):
	全選股條件line = []#放入每個條件line

	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.createWidgets()
		self.條件list = []#以選的條件放進list
		self.條件數量n = 0#以選的條件數量
		
		self.allcompany = []
		for company in stockDict_stock.keys():
			self.allcompany.append(company)
	
	def createWidgets(self):
		#創每個種類-----------------------------------------------------------------------------------------------------
		f = tkFont.Font(size = 14 , family = "Courier New")
				
		self.Btn突破 = tk.Button(self,text = "突破",width = 8,command = self.clickBtn突破,font = f,bg = "Navajowhite")
		self.Btn乖離 = tk.Button(self,text = "乖離",width = 8,command = self.clickBtn乖離,font = f,bg = "Beige")
		self.Btn趨勢 = tk.Button(self,text = "趨勢",width = 8,command = self.clickBtn趨勢,font = f,bg = "Beige")
		self.Btn技術指標 = tk.Button(self,text = "技術指標",width = 8,command = self.clickBtn技術指標,font = f,bg = "Beige")
		
		self.Btn今日盤中突破5日新高 = tk.Button(self,text = "今日盤中突破5日新高",command = self.clickBtn今日盤中突破5日新高,width = 32,font = f,bg = "Antiquewhite")
		self.Btn今日收盤突破月線 = tk.Button(self,text = "今日收盤突破月線",command = self.clickBtn今日收盤突破月線,width = 32,font = f,bg = "Antiquewhite")
		self.Btn今日收盤突破季線 = tk.Button(self,text = "今日收盤突破季線",command = self.clickBtn今日收盤突破季線,width = 32,font = f,bg = "Antiquewhite")
		self.Btn今日收盤跌破月線 = tk.Button(self,text = "今日收盤跌破月線",command = self.clickBtn今日收盤跌破月線,width = 32,font = f,bg = "Antiquewhite")
		self.Btn今日收盤跌破季線 = tk.Button(self,text = "今日收盤跌破季線",command = self.clickBtn今日收盤跌破季線,width = 32,font = f,bg = "Antiquewhite")
		self.Lbl空行 = tk.Label(self,width = 32,font = f)
		
		
		self.lbl選股條件 = tk.Label(self,text = "選股條件",relief = "ridge",height = 1,width = 32,font = f)
		self.lbl選股條件line1 = tk.Label(self,anchor = 'w',height = 1,width = 40 ,font = f,background = 'Beige')
		self.lbl選股條件line2 = tk.Label(self,anchor = 'w',height = 1,width = 40 ,font = f,background = 'snow')
		self.lbl選股條件line3 = tk.Label(self,anchor = 'w',height = 1,width = 40 ,font = f,background = 'snow')
		self.lbl選股條件line4 = tk.Label(self,anchor = 'w',height = 1,width = 40 ,font = f,background = 'snow')
		self.lbl選股條件line5 = tk.Label(self,anchor = 'w',height = 1,width = 40 ,font = f,background = 'snow')
		self.lbl選股條件line6 = tk.Label(self,anchor = 'w',height = 1,width = 40 ,font = f,background = 'snow')
		
		
		self.Btn開始選股 = tk.Button(self,text = "開始選股",height = 1,width = 16,font = f,background = 'BurlyWood')
		self.Btn重設條件 = tk.Button(self,text = "重設條件",command = self.clickDelBtn,height = 1,width = 16,font = f,background = 'BurlyWood')
		self.BtnQuit = tk.Button(self,text = "Quit!",command = self.quit,height = 1,width = 16,font = f,background = 'BurlyWood')
	   #設定位置------------------------------------------------------------------------------------
		self.Btn突破.grid(row = 0,column = 0,columnspan = 3,sticky = tk.NE + tk.SW)
		self.Btn乖離.grid(row = 0,column = 3,columnspan = 3,sticky = tk.NE + tk.SW)
		self.Btn趨勢.grid(row = 0,column = 6,columnspan = 3,sticky = tk.NE + tk.SW)
		self.Btn技術指標.grid(row = 0,column = 9,columnspan = 3,sticky = tk.NE + tk.SW)
		
		self.Btn今日盤中突破5日新高.grid(row = 1,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn今日收盤突破月線.grid(row = 2,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn今日收盤突破季線.grid(row = 3,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn今日收盤跌破月線.grid(row = 4,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn今日收盤跌破季線.grid(row = 5,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Lbl空行.grid(row = 6,column = 0,rowspan = 2,columnspan = 12,sticky = tk.NE + tk.SW)
		
		
		self.lbl選股條件.grid(row = 10,column = 0,columnspan = 12,sticky = tk.E + tk.SW)
		self.lbl選股條件line1.grid(row = 11,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.lbl選股條件line2.grid(row = 12,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.lbl選股條件line3.grid(row = 13,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.lbl選股條件line4.grid(row = 14,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.lbl選股條件line5.grid(row = 15,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.lbl選股條件line6.grid(row = 16,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		
		self.Btn開始選股.grid(row = 17,column = 0,columnspan = 6,sticky = tk.NE + tk.SW)
		self.Btn重設條件.grid(row = 17,column = 6,columnspan = 6,sticky = tk.NE + tk.SW)
		self.BtnQuit.grid(row = 18,column = 6,columnspan = 6,sticky = tk.NE + tk.SW)

		self.全選股條件line.append(self.lbl選股條件line1)
		self.全選股條件line.append(self.lbl選股條件line2)
		self.全選股條件line.append(self.lbl選股條件line3)
		self.全選股條件line.append(self.lbl選股條件line4)
		self.全選股條件line.append(self.lbl選股條件line5)
		self.全選股條件line.append(self.lbl選股條件line6)
		
		#-----------------------------------------------------------------------------------------
		
		
	#創每個category的條件-------------------------------------------------------
	def clickBtn突破(self):
		f = tkFont.Font(self,size = 14 , family = "Courier New")
		
		self.Btn突破.configure(bg = "Navajowhite")
		self.Btn乖離.configure(bg = "Beige")
		self.Btn趨勢.configure(bg = "Beige")
		self.Btn技術指標.configure(bg = "Beige")
		
		self.Btn今日盤中突破5日新高 = tk.Button(self,text = "今日盤中突破5日新高",command = self.clickBtn今日盤中突破5日新高,width = 32,font = f,bg = "Antiquewhite")
		self.Btn今日收盤突破月線 = tk.Button(self,text = "今日收盤突破月線",command = self.clickBtn今日收盤突破月線,width = 32,font = f,bg = "Antiquewhite")
		self.Btn今日收盤突破季線 = tk.Button(self,text = "今日收盤突破季線",command = self.clickBtn今日收盤突破季線,width = 32,font = f,bg = "Antiquewhite")
		self.Btn今日收盤跌破月線 = tk.Button(self,text = "今日收盤跌破月線",command = self.clickBtn今日收盤跌破月線,width = 32,font = f,bg = "Antiquewhite")
		self.Btn今日收盤跌破季線 = tk.Button(self,text = "今日收盤跌破季線",command = self.clickBtn今日收盤跌破季線,width = 32,font = f,bg = "Antiquewhite")
		self.Lbl空行 = tk.Label(self,width = 32,font = f)
		
		self.Btn今日盤中突破5日新高.grid(row = 1,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn今日收盤突破月線.grid(row = 2,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn今日收盤突破季線.grid(row = 3,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn今日收盤跌破月線.grid(row = 4,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn今日收盤跌破季線.grid(row = 5,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Lbl空行.grid(row = 6,column = 0,rowspan = 2,columnspan = 12,sticky = tk.NE + tk.SW)
		
		
	def clickBtn乖離(self):
		f = tkFont.Font(self,size = 14 , family = "Courier New")
				
		self.Btn突破.configure(bg = "Beige")
		self.Btn乖離.configure(bg = "Navajowhite")
		self.Btn趨勢.configure(bg = "Beige")
		self.Btn技術指標.configure(bg = "Beige")
		
		self.Btn股價大於周線 = tk.Button(self,text = "股價大於周線5%",command = self.clickBtn股價大於周線,width = 32,font = f,bg = "Antiquewhite")
		self.Btn股價大於月線 = tk.Button(self,text = "股價大於月線10%",command = self.clickBtn股價大於月線,width = 32,font = f,bg = "Antiquewhite")
		self.Btn股價大於季線 = tk.Button(self,text = "股價大於季線20%",command = self.clickBtn股價大於季線,width = 32,font = f,bg = "Antiquewhite")
		self.Lbl空行 = tk.Label(self,width = 32,font = f)
		 
		self.Btn股價大於周線.grid(row = 1,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn股價大於月線.grid(row = 2,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn股價大於季線.grid(row = 3,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Lbl空行.grid(row = 4,column = 0,rowspan = 4,columnspan = 12,sticky = tk.NE + tk.SW)
		
		
	def clickBtn趨勢(self):
		f = tkFont.Font(self,size = 14 , family = "Courier New")
		
		self.Btn突破.configure(bg = "Beige")
		self.Btn乖離.configure(bg = "Beige")
		self.Btn趨勢.configure(bg = "Navajowhite")
		self.Btn技術指標.configure(bg = "Beige")
				
		self.Btn均線多頭排列 = tk.Button(self,text = "均線多頭排列",command = self.clickBtn均線多頭排列,width = 32,font = f,bg = "Antiquewhite")
		self.Btn均線空頭排列 = tk.Button(self,text = "均線空頭排列",command = self.clickBtn均線空頭排列,width = 32,font = f,bg = "Antiquewhite")
		self.Btn週線大於月線 = tk.Button(self,text = "週線大於月線",command = self.clickBtn週線大於月線,width = 32,font = f,bg = "Antiquewhite")
		self.Btn月線大於季線 = tk.Button(self,text = "月線大於季線",command = self.clickBtn月線大於季線,width = 32,font = f,bg = "Antiquewhite")
		self.Btn週收盤連兩周上漲 = tk.Button(self,text = "週收盤連兩周上漲",command = self.clickBtn週收盤連兩周上漲,width = 32,font = f,bg = "Antiquewhite")
		self.Btn月收盤連兩周上漲 = tk.Button(self,text = "月收盤連兩周上漲",command = self.clickBtn月收盤連兩周上漲,width = 32,font = f,bg = "Antiquewhite")
		self.Lbl空行 = tk.Label(self,width = 32,font = f)
		
		self.Btn均線多頭排列.grid(row = 1,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn均線空頭排列.grid(row = 2,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn週線大於月線.grid(row = 3,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn月線大於季線.grid(row = 4,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn週收盤連兩周上漲.grid(row = 5,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btn月收盤連兩周上漲.grid(row = 6,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Lbl空行.grid(row = 7,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)

	def clickBtn技術指標(self):
		f = tkFont.Font(self,size = 14 , family = "Courier New")
		
		self.Btn突破.configure(bg = "Beige")
		self.Btn乖離.configure(bg = "Beige")
		self.Btn趨勢.configure(bg = "Beige")
		self.Btn技術指標.configure(bg = "Navajowhite")
		
		self.BtnKD黃金交叉日 = tk.Button(self,text = "KD黃金交叉(日)",command = self.clickBtnKD黃金交叉日,width = 32,font = f,bg = "Antiquewhite")
		self.BtnKD黃金交叉週 = tk.Button(self,text = "KD黃金交叉(週)",command = self.clickBtnKD黃金交叉週,width = 32,font = f,bg = "Antiquewhite")
		self.BtnKD黃金交叉月 = tk.Button(self,text = "KD黃金交叉(月)",command = self.clickBtnKD黃金交叉月,width = 32,font = f,bg = "Antiquewhite")
		self.BtnKD死亡交叉日 = tk.Button(self,text = "KD死亡交叉(日)",command = self.clickBtnKD死亡交叉日,width = 32,font = f,bg = "Antiquewhite")
		self.BtnKD死亡交叉週 = tk.Button(self,text = "KD死亡交叉(週)",command = self.clickBtnKD死亡交叉週,width = 32,font = f,bg = "Antiquewhite")
		self.BtnKD死亡交叉月 = tk.Button(self,text = "KD死亡交叉(月)",command = self.clickBtnKD死亡交叉月,width = 32,font = f,bg = "Antiquewhite")
		self.Lbl空行 = tk.Label(self,width = 32,font = f)
		
		self.BtnKD黃金交叉日.grid(row = 1,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.BtnKD黃金交叉週.grid(row = 2,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.BtnKD黃金交叉月.grid(row = 3,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.BtnKD死亡交叉日.grid(row = 4,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.BtnKD死亡交叉週.grid(row = 5,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.BtnKD死亡交叉月.grid(row = 6,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Lbl空行.grid(row = 7,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
	#end---------------------------------------------------------------------------



	#創每個category的條件----------------------------------------------------------
	def setclick條件Btn(self,條件):
		self.全選股條件line[self.條件數量n].configure(text = str(條件))
		self.條件數量n += 1
		
	#選擇突破選項並顯示於以選條件-------------------------------------------------------------------
	def clickBtn今日盤中突破5日新高(self):
		self.setclick條件Btn("今日盤中突破5日新高")
	def clickBtn今日收盤突破月線(self):
		self.setclick條件Btn("今日收盤突破月線")
	def clickBtn今日收盤突破季線(self):
		self.setclick條件Btn("今日收盤突破季線")
	def clickBtn今日收盤跌破月線(self):
		self.setclick條件Btn("今日收盤跌破月線")
	def clickBtn今日收盤跌破季線(self):
		self.setclick條件Btn("今日收盤跌破季線")

	#選擇乖離選項並顯示於以選條件-----------------------------------------------------------------------------
	
	def clickBtn股價大於周線(self):
		self.setclick條件Btn("股價大於周線5%")
	def clickBtn股價大於月線(self):
		self.setclick條件Btn("股價大於月線10%")
	def clickBtn股價大於季線(self):
		self.setclick條件Btn("股價大於季線20%")
		
	#選擇趨勢選項並顯示於以選條件-----------------------------------------------------------------------------
	
	def clickBtn均線多頭排列(self):
		self.setclick條件Btn("均線多頭排列")
		for item in self.allcompany:
			if stockDict_stock[item].MA5[-1] <= stostockDict_stock[item].MA20[-1] or stockDict_stock[item].MA20[-1] <= stostockDict_stock[item].MA120[-1]:
				self.allcompany.remove(item)

	def clickBtn均線空頭排列(self):
		self.setclick條件Btn("均線空頭排列")
		for item in self.allcompany:
			if stockDict_stock[item].MA5[-1] >= stostockDict_stock[item].MA20[-1] or stockDict_stock[item].MA20[-1] >= stostockDict_stock[item].MA120[-1]:
				self.allcompany.remove(item)

	def clickBtn週線大於月線(self):
		self.setclick條件Btn("週線大於月線")
		for item in self.allcompany:
			if stockDict_stock[item].MA5[-1] <= stostockDict_stock[item].MA20[-1]:
				self.allcompany.remove(item)

	def clickBtn月線大於季線(self):
		self.setclick條件Btn("月線大於季線")
		for item in self.allcompany:
			if stockDict_stock[item].MA20[-1] <= stostockDict_stock[item].MA60[-1]:
				self.allcompany.remove(item)
	def clickBtn週收盤連兩周上漲(self):
		self.setclick條件Btn("週收盤連兩周上漲")
	def clickBtn月收盤連兩周上漲(self):
		self.setclick條件Btn("月收盤連兩周上漲")

	#選擇技術指標選項並顯示於以選條件--------------------------------------------------------------------------
	
	def clickBtnKD黃金交叉日(self):
		self.setclick條件Btn("KD黃金交叉(日)")
	def clickBtnKD黃金交叉週(self):
		self.setclick條件Btn("KD黃金交叉(週)")
	def clickBtnKD黃金交叉月(self):
		self.setclick條件Btn("KD黃金交叉(月)")
	def clickBtnKD死亡交叉日(self):
		self.setclick條件Btn("KD死亡交叉(日)")
	def clickBtnKD死亡交叉週(self):
		self.setclick條件Btn("KD死亡交叉(週)")
	def clickBtnKD死亡交叉月(self):
		self.setclick條件Btn("KD死亡交叉(月)")

	#刪除條件的函數--------------------------------------------------------------
	def clickDelBtn(self):
		for 條件 in self.全選股條件line:
			條件.configure(text = "")
		self.條件數量n = 0
	
		self.allcompany = []
		for company in stockDict_stock.keys():
			self.allcompany.append(company)
			

			


#讀入檔案
#輸入要讀的檔名
filename = input()
filehandler = open(filename, 'r', newline = '', encoding = 'utf-8', errors = "ignore") #建立filehandler
reader2 = csv.DictReader(filehandler)
####################################################################
#csv.reader被csv.DictReader來取代，dictreader的好處是可以用欄位名稱來呼叫#
###################################################################
cheader = reader2.fieldnames #這行的作用是不要管第一行（欄位名稱）
	
	
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

cal = BigFrame()
cal.master.title("選股好簡單")
cal.mainloop() 
filehandler.close()