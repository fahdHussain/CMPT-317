from State import State

class SearchNode:

    def __init__(self,state,depth,action,parent,step_cost=1):
        self.state = state
        self.depth = depth
        self.action = action
        self.parent = parent
        self.step_cost = step_cost

    def display(self):
        print("State: "+(self.state.curExp())+"\nDepth: "+str(self.depth)+
        "\nActions: "+(self.action)+"\nParent: "+(self.parent.curExp())+
        "\nStep Cost: "+str(self.step_cost))


if __name__ == "__main__":
    newState = State()
    newState.exp = "55 + 3"
    newerState = State()
    newerState.exp = "55"
    newNode = SearchNode(newState,5,"add",newerState)
    newNode.display()
