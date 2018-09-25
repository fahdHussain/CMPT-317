from State import State
#Contains is_goal(state),actions(state),result(state)
class Problem:

    def __init__(self):
        self.goal = 0
        self.values = []

    def set_goal(self,num):
        #Sets goal to given value
        self.goal = num

    def set_values(self,list):
        #Creates a list of all the values
        self.values = list

    def is_goal(self,state):
        #Checks if current state evaluates to goal value
        if state.val == self.goal:
            return True
        else:
            return False


    def actions(self,state):
        #List all possible actions that can be acted upon at this state
        if len(state.values) == 0:
            return ["NA"]
        else:
            return ["add","sub","mul","div"]

    def result(self,state,action,num):
        #Return new state after performing action
        #Every number can be +,-,*,//(besides 0 for div)
        newState = State()
        newState.values = state.values
        newState.removeVal(num)

        if action == "NA":
            return None

        elif action == "add":
            newState.exp = "(" + state.exp + "+" + str(num) + ")"
            newState.val = eval(newState.exp)
            return newState

        elif action == "sub":
            newState.exp = "(" + state.exp + "-" + str(num) + ")"
            newState.val = eval(newState.exp)
            return newState

        elif action == "mul":
            newState.exp = "(" + state.exp + "*" + str(num) + ")"
            newState.val = eval(newState.exp)

        elif action == "div":
            if num == 0:
                return None
            else:
                newState.exp = "(" + state.exp + "//" + str(num) + ")"
                newState.val = eval(newState.exp)
                return newState

if __name__ == "__main__":
    initState = State()
    myList = [1,2,3,4,5]
    problem = Problem()

    problem.set_goal(7)
    problem.set_values(myList)

    initState.set_values(myList)

    print("Checking if init is goal:"+str(problem.is_goal(initState)))
    print("Available actions from init: "+str(problem.actions(initState)))

    nextState = problem.result(initState,"add",5)

    print("Adding 5: "+str(nextState.curExp()))
