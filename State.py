
class State:
    def __init__(self):
        self.exp = ""
        self.val = 0

    def curVal():
        return self.val

    def curExp():
        return self.exp

    def add(self, num):
        newState = State()
        if self.exp == "":
            newState.exp = str(num)
            newState.val = num
            return newState
        else:
            newState.exp = "(" + self.exp + "+" + str(num) + ")"
            newState.val = eval(newState.exp)
            return newState

    def sub(self, num):
        newState = State()
        if self.exp == "":
            newState.exp = str(num)
            newState.val = num
            return newState
        else:
            newState.exp = "(" + self.exp + "-" + str(num) + ")"
            newState.val = eval(newState.exp)
            return newState

    def mul(self, num):
        if self.exp == "":
            newState.exp = str(num)
            newState.val = num
            return newState
        else:
            newState = State()
            newState.exp = "(" + self.exp + "*" + str(num) + ")"
            newState.val = eval(newState.exp)
            return newState

    def div(self, num):
        if self.exp == "":
            newState.exp = str(num)
            newState.val = num
            return newState
        else:
            newState = State()
            newState.exp = "(" + self.exp + "//" + str(num) + ")"
            newState.val = eval(newState.exp)
            return newState

if __name__ == "__main__":
    aState = State()
    print(aState.val)
    print(aState.exp)
    nextState = aState.add(12)
    print(nextState.val)
    nnState = nextState.add(5)
    print(nnState.val)
    print(nnState.exp)
    nnnState = nnState.add(8)
    print(nnnState.val)
    print(nnnState.exp)
