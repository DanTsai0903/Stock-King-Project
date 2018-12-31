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



stockDict = Dict() #儲存一家一家的公司，key是股票代碼，value是那間公司的「資料」（所以新建一個「stock」class, 這個class 儲存一家公司的資料）
class stock():
	def __init__(self):
		#新建那些list, 包括date, opening, ......
	def calculate(self):
		#算出5日線，20日線 ......


for line in reader2:
	#如果以「line["證券代碼"]」為key的資料不存在
		#則新增一筆資料、key是line["證券代碼"]、value是stock()
	#然後把這行line的每一欄位加入到以「line["證券代碼"]」為key的資料中



###############################################################	

	#這些要在for迴圈裡，我改了一些變數名稱
	#然後運算的方法稍有不同
	#舉個例子，應該是stockDict["2801"].opening.append(15.00)之類的

	code.append(listdata[0])
	abbreviation.append(listdata[1])
	date.append(listdata[2])
	opening.append(float(listdata[3]))
	highest.append(float(listdata[4]))
	lowest.append(float(listdata[5]))
	closing.append(float(listdata[6]))
	volume.append(int(listdata[7]))
###############################################################



##############################################################

#這些應該在__init__這個function裡面

code = [] #股票代碼(變數名稱不要包含空白)
abbreviation = [] #公司簡稱
date = [] #日期, 用datetime物件，所以要import datetime
opening = [] #開盤價
highest = [] #最高價
lowest = [] #最低價
closing = [] #收盤價
volume = [] #成交量(千股)
##############################################################



filehandler.close()