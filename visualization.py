import tkinter as tk
import tkinter.font as tkFont


class BigFrame(tk.Frame):
	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.createWidgets()
	
	#創每個種類
	def createWidgets(self):
		f = tkFont.Font(size = 28 , family = "Courier New")
				
		self.Btn突破 = tk.Button(self,text = "突破",width = 8,command = self.clickBtn突破,font = f)
		self.Btn乖離 = tk.Button(self,text = "乖離",width = 8,command = self.clickBtn乖離,font = f)
		self.Btn趨勢 = tk.Button(self,text = "趨勢",width = 8,command = self.clickBtn趨勢,font = f)
		self.Btn技術指標 = tk.Button(self,text = "技術指標",width = 8,command = self.clickBtn技術指標,font = f)
		
		self.lbl選股條件 = tk.Label(self,text = "選股條件",height = 1,width = 32,font = f)
		self.txt選股條件 = tk.Text(self,height = 5,width = 40 ,font = f)
		
		self.lbl符合廠商 = tk.Label(self,text = "符合廠商",height = 1,width = 32,font = f)
		self.txt符合廠商 = tk.Text(self,height = 5,width = 40 ,font = f)
		
		self.Btn突破.grid(row = 0,column = 0,columnspan = 3,sticky = tk.NE + tk.SW)
		self.Btn乖離.grid(row = 0,column = 3,columnspan = 3,sticky = tk.NE + tk.SW)
		self.Btn趨勢.grid(row = 0,column = 6,columnspan = 3,sticky = tk.NE + tk.SW)
		self.Btn技術指標.grid(row = 0,column = 9,columnspan = 3,sticky = tk.NE + tk.SW)
		self.lbl選股條件.grid(row = 5,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.txt選股條件.grid(row = 6,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.lbl符合廠商.grid(row = 7,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.txt符合廠商.grid(row = 8,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)

	#創間每個category的條件-------------------------------------------------------
	def clickBtn突破(self):
		f = tkFont.Font(self,size = 28 , family = "Courier New")
				
		self.Btntest1 = tk.Button(self,text = "test1",width = 32,font = f)
		self.Btntest2 = tk.Button(self,text = "test2",width = 32,font = f)

		self.Btntest1.grid(row = 1,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btntest2.grid(row = 2,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
	
	def clickBtn乖離(self):
		f = tkFont.Font(self,size = 28 , family = "Courier New")
				
		self.Btntest3 = tk.Button(self,text = "test3",width = 32,font = f)
		self.Btntest4 = tk.Button(self,text = "test4",width = 32,font = f)

		self.Btntest3.grid(row = 1,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btntest4.grid(row = 2,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)

	def clickBtn趨勢(self):
		f = tkFont.Font(self,size = 28 , family = "Courier New")
				
		self.Btntest5 = tk.Button(self,text = "test5",width = 32,font = f)
		self.Btntest6 = tk.Button(self,text = "test6",width = 32,font = f)

		self.Btntest5.grid(row = 1,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btntest6.grid(row = 2,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)

	def clickBtn技術指標(self):
		f = tkFont.Font(self,size = 28 , family = "Courier New")
				
		self.Btntest7 = tk.Button(self,text = "test7",width = 32,font = f)
		self.Btntest8 = tk.Button(self,text = "test8",width = 32,font = f)

		self.Btntest7.grid(row = 1,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
		self.Btntest8.grid(row = 2,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
	#-----------------------------------------------------
cal = BigFrame()
cal.master.title("選股好簡單")
cal.mainloop()	