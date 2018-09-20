#State class stores expression and value of that expression
class State:
    def __init__(self):
        self.exp = ""
        self.val = 0
        self.values = []

    def curVal(self):
        return str(self.val)

    def curExp(self):
        return self.exp

    def set_values(self,list):
        self.values = list

    def removeVal(self,num):
        i = self.values.index(num)
        self.values.pop(i)
