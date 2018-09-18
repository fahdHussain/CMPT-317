from State import State

class Action:

    def add(num, aState):
        newState = State()
        if aState.exp == "":
            newState.exp = str(num)
            newState.val = num
            return newState
        else:
            newState.exp = aState.exp + "+" + str(num)
            newState.val = eval(newState.exp)
            return newState

    def sub(num, aState):
        newState = State()
        if aState.exp == "":
            newState.exp = str(num)
            newState.val = num
            return newState
        else:
            newState.exp = aState.exp + "-" + str(num)
            newState.val = eval(newState.exp)
            return newState

    def mul(num, aState):
        if aState.exp == "":
            newState.exp = str(num)
            newState.val = num
            return newState
        else:
            newState = State()
            newState.exp = aState.exp + "*" + str(num)
            newState.val = eval(newState.exp)
            return newState

    def div(num, aState):
        if aState.exp == "":
            newState.exp = str(num)
            newState.val = num
            return newState
        else:
            newState = State()
            newState.exp = aState.exp + "//" + str(num)
            newState.val = eval(newState.exp)
            return newState

if __name__ == "__main__":
    action = Action()
    curExp = State()
    curExp = action.add(10, curExp)
    print(curExp.val)
    print(curExp.exp)
