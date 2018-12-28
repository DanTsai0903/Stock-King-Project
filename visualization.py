import tkinter as tk
import tkinter.font as tkFont


class BigFrame(tk.Frame):
    全選股條件line = []#放入每個條件line

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.條件list = []#以選的條件放進list
        self.條件數量n = 0#以選的條件數量
        
    
    def createWidgets(self):
        #創每個種類-----------------------------------------------------------------------------------------------------
        f = tkFont.Font(size = 14 , family = "Courier New")
                
        self.Btn突破 = tk.Button(self,text = "突破",width = 8,command = self.clickBtn突破,font = f)
        self.Btn乖離 = tk.Button(self,text = "乖離",width = 8,command = self.clickBtn乖離,font = f)
        self.Btn趨勢 = tk.Button(self,text = "趨勢",width = 8,command = self.clickBtn趨勢,font = f)
        self.Btn技術指標 = tk.Button(self,text = "技術指標",width = 8,command = self.clickBtn技術指標,font = f)
        
        self.Btn今日盤中突破5日新高 = tk.Button(self,text = "今日盤中突破5日新高",command = self.clickBtn今日盤中突破5日新高,width = 32,font = f)
        self.Btn今日收盤突破月線 = tk.Button(self,text = "今日收盤突破月線",command = self.clickBtn今日收盤突破月線,width = 32,font = f)
        self.Btn今日收盤突破季線 = tk.Button(self,text = "今日收盤突破季線",command = self.clickBtn今日收盤突破季線,width = 32,font = f)
        self.Btn今日收盤跌破月線 = tk.Button(self,text = "今日收盤跌破月線",command = self.clickBtn今日收盤跌破月線,width = 32,font = f)
        self.Btn今日收盤跌破季線 = tk.Button(self,text = "今日收盤跌破季線",command = self.clickBtn今日收盤跌破季線,width = 32,font = f)
        self.Lbl空行 = tk.Label(self,width = 32,font = f)
        
        
        self.lbl選股條件 = tk.Label(self,text = "選股條件",relief = "ridge",height = 1,width = 32,font = f)
        self.lbl選股條件line1 = tk.Label(self,anchor = 'w',height = 1,width = 40 ,font = f,background = 'white')
        self.lbl選股條件line2 = tk.Label(self,anchor = 'w',height = 1,width = 40 ,font = f,background = 'white')
        self.lbl選股條件line3 = tk.Label(self,anchor = 'w',height = 1,width = 40 ,font = f,background = 'white')
        self.lbl選股條件line4 = tk.Label(self,anchor = 'w',height = 1,width = 40 ,font = f,background = 'white')
        self.lbl選股條件line5 = tk.Label(self,anchor = 'w',height = 1,width = 40 ,font = f,background = 'white')
        self.lbl選股條件line6 = tk.Label(self,anchor = 'w',height = 1,width = 40 ,font = f,background = 'white')
        
        self.lbl符合廠商 = tk.Label(self,text = "符合廠商",height = 1,width = 32,font = f)
        self.lbl符合廠商列 = tk.Label(self,height = 5,width = 40 ,font = f,background='white')
        
        self.Btn開始選股 = tk.Button(self,text = "開始選股",height = 1,width = 16,font = f,background = 'blue')
        self.Btn重設條件 = tk.Button(self,text = "重設條件",command = self.clickDelBtn,height = 1,width = 16,font = f,background = 'pink')
       
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
        self.lbl符合廠商.grid(row = 18,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.lbl符合廠商列.grid(row = 19,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)

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
        self.Btn今日盤中突破5日新高 = tk.Button(self,text = "今日盤中突破5日新高",command = self.clickBtn今日盤中突破5日新高,width = 32,font = f)
        self.Btn今日收盤突破月線 = tk.Button(self,text = "今日收盤突破月線",command = self.clickBtn今日收盤突破月線,width = 32,font = f)
        self.Btn今日收盤突破季線 = tk.Button(self,text = "今日收盤突破季線",command = self.clickBtn今日收盤突破季線,width = 32,font = f)
        self.Btn今日收盤跌破月線 = tk.Button(self,text = "今日收盤跌破月線",command = self.clickBtn今日收盤跌破月線,width = 32,font = f)
        self.Btn今日收盤跌破季線 = tk.Button(self,text = "今日收盤跌破季線",command = self.clickBtn今日收盤跌破季線,width = 32,font = f)
        self.Lbl空行 = tk.Label(self,width = 32,font = f)
        
        self.Btn今日盤中突破5日新高.grid(row = 1,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.Btn今日收盤突破月線.grid(row = 2,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.Btn今日收盤突破季線.grid(row = 3,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.Btn今日收盤跌破月線.grid(row = 4,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.Btn今日收盤跌破季線.grid(row = 5,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.Lbl空行.grid(row = 6,column = 0,rowspan = 2,columnspan = 12,sticky = tk.NE + tk.SW)
        
        
    def clickBtn乖離(self):
        f = tkFont.Font(self,size = 14 , family = "Courier New")
                
        self.Btn股價大於周線 = tk.Button(self,text = "股價大於周線5%",command = self.clickBtn股價大於周線,width = 32,font = f)
        self.Btn股價大於月線 = tk.Button(self,text = "股價大於月線10%",command = self.clickBtn股價大於月線,width = 32,font = f)
        self.Btn股價大於季線 = tk.Button(self,text = "股價大於季線20%",command = self.clickBtn股價大於季線,width = 32,font = f)
        self.Lbl空行 = tk.Label(self,width = 32,font = f)
         
        self.Btn股價大於周線.grid(row = 1,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.Btn股價大於月線.grid(row = 2,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.Btn股價大於季線.grid(row = 3,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.Lbl空行.grid(row = 4,column = 0,rowspan = 4,columnspan = 12,sticky = tk.NE + tk.SW)
        
        
    def clickBtn趨勢(self):
        f = tkFont.Font(self,size = 14 , family = "Courier New")
                
        self.Btn均線多頭排列 = tk.Button(self,text = "均線多頭排列",command = self.clickBtn均線多頭排列,width = 32,font = f)
        self.Btn均線空頭排列 = tk.Button(self,text = "均線空頭排列",command = self.clickBtn均線空頭排列,width = 32,font = f)
        self.Btn週線大於月線 = tk.Button(self,text = "週線大於月線",command = self.clickBtn週線大於月線,width = 32,font = f)
        self.Btn月線大於季線 = tk.Button(self,text = "月線大於季線",command = self.clickBtn月線大於季線,width = 32,font = f)
        self.Btn週收盤連兩周上漲 = tk.Button(self,text = "週收盤連兩周上漲",command = self.clickBtn週收盤連兩周上漲,width = 32,font = f)
        self.Btn月收盤連兩周上漲 = tk.Button(self,text = "月收盤連兩周上漲",command = self.clickBtn月收盤連兩周上漲,width = 32,font = f)
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
        
        self.BtnKD黃金交叉日 = tk.Button(self,text = "KD黃金交叉(日)",command = self.clickBtnKD黃金交叉日,width = 32,font = f)
        self.BtnKD黃金交叉週 = tk.Button(self,text = "KD黃金交叉(週)",command = self.clickBtnKD黃金交叉週,width = 32,font = f)
        self.BtnKD黃金交叉月 = tk.Button(self,text = "KD黃金交叉(月)",command = self.clickBtnKD黃金交叉月,width = 32,font = f)
        self.BtnKD死亡交叉日 = tk.Button(self,text = "KD死亡交叉(日)",command = self.clickBtnKD死亡交叉日,width = 32,font = f)
        self.BtnKD死亡交叉週 = tk.Button(self,text = "KD死亡交叉(週)",command = self.clickBtnKD死亡交叉週,width = 32,font = f)
        self.BtnKD死亡交叉月 = tk.Button(self,text = "KD死亡交叉(月)",command = self.clickBtnKD死亡交叉月,width = 32,font = f)
        self.Lbl空行 = tk.Label(self,width = 32,font = f)
        
        self.BtnKD黃金交叉日.grid(row = 1,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.BtnKD黃金交叉週.grid(row = 2,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.BtnKD黃金交叉月.grid(row = 3,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.BtnKD死亡交叉日.grid(row = 4,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.BtnKD死亡交叉週.grid(row = 5,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.BtnKD死亡交叉月.grid(row = 6,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
        self.Lbl空行.grid(row = 7,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)
    #end---------------------------------------------------------------------------

    def create條件LabelWidges(self,line):
        self.lbl = tk.Label(self,height = 1,width = 40 ,font = f,background = 'white')
        self.lbl.grid(row = line + 5,column = 0,columnspan = 12,sticky = tk.NE + tk.SW)

    #創每個category的條件-------------------------------------------------------
    def setclick條件Btn(self,條件):
        self.條件list.append(條件)
        self.全選股條件line[self.條件數量n].configure(text = str(條件))
        self.條件數量n += 1
        
    #選擇突破選項------------------------------------------------------------------------------
    
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

    #選擇乖離選項-----------------------------------------------------------------------------
    
    def clickBtn股價大於周線(self):
        self.setclick條件Btn("股價大於周線5%")
    def clickBtn股價大於月線(self):
        self.setclick條件Btn("股價大於月線10%")
    def clickBtn股價大於季線(self):
        self.setclick條件Btn("股價大於季線20%")
        
    #選擇趨勢選項-----------------------------------------------------------------------------
	
    def clickBtn均線多頭排列(self):
        self.setclick條件Btn("均線多頭排列")
    def clickBtn均線空頭排列(self):
        self.setclick條件Btn("均線空頭排列")
    def clickBtn週線大於月線(self):
        self.setclick條件Btn("週線大於月線")
    def clickBtn月線大於季線(self):
        self.setclick條件Btn("月線大於季線")
    def clickBtn週收盤連兩周上漲(self):
        self.setclick條件Btn("週收盤連兩周上漲")
    def clickBtn月收盤連兩周上漲(self):
        self.setclick條件Btn("月收盤連兩周上漲")
        
    #選擇技術指標選項--------------------------------------------------------------------------
    
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
        self.條件list = []
    
        

cal = BigFrame()
cal.master.title("選股好簡單")
cal.mainloop()  