#「技術指標」部分的運算--------------------------------------------------------------------------
    def clickBtnKD黃金交叉日(self):
        self.setclick條件Btn("KD黃金交叉(日)")
        for item in self.allcompany:
            p = stockDict_stock[item].K[-1] > stockDict_stock[item].D[-1]
            q = stockDict_stock[item].K[-2] < stockDict_stock[item].D[-2]
            if p and q:
                pass
            else:
                self.allcompany.remove(item)
    def clickBtnKD黃金交叉週(self):
        self.setclick條件Btn("KD黃金交叉(週)")
        for item in self.allcompany:
            p = stockDict_stock[item].Kweek[-1] > stockDict_stock[item].Dweek[-1]
            q = stockDict_stock[item].Kweek[-2] < stockDict_stock[item].Dweek[-2]
            if p and q:
                pass
            else:
                self.allcompany.remove(item)
    def clickBtnKD黃金交叉月(self):
        self.setclick條件Btn("KD黃金交叉(月)")
        for item in self.allcompany:
            p = stockDict_stock[item].Kmonth[-1] > stockDict_stock[item].Dmonth[-1]
            q = stockDict_stock[item].Kmonth[-2] < stockDict_stock[item].Dmonth[-2]
            if p and q:
                pass
            else:
                self.allcompany.remove(item)
    def clickBtnKD死亡交叉日(self):
        self.setclick條件Btn("KD死亡交叉(日)")
        for item in self.allcompany:
            p = stockDict_stock[item].K[-1] < stockDict_stock[item].D[-1]
            q = stockDict_stock[item].K[-2] > stockDict_stock[item].D[-2]
            if p and q:
                pass
            else:
                self.allcompany.remove(item)
    def clickBtnKD死亡交叉週(self):
        self.setclick條件Btn("KD死亡交叉(週)")
        for item in self.allcompany:
            p = stockDict_stock[item].Kweek[-1] < stockDict_stock[item].Dweek[-1]
            q = stockDict_stock[item].Kweek[-2] > stockDict_stock[item].Dweek[-2]
            if p and q:
                pass
            else:
                self.allcompany.remove(item)
    def clickBtnKD死亡交叉月(self):
        self.setclick條件Btn("KD死亡交叉(月)")
        for item in self.allcompany:
            p = stockDict_stock[item].Kmonth[-1] < stockDict_stock[item].Dmonth[-1]
            q = stockDict_stock[item].Kmonth[-2] > stockDict_stock[item].Dmonth[-2]
            if p and q:
                pass
            else:
                self.allcompany.remove(item)