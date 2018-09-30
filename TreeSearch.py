#TreeSearch
from Problem import Problem
from State import State
from Parser import Parser
from SearchNode import SearchNode
from PriorityEntry import PriorityEntry
import queue
import time

#Breath First Search
def BFS(problem):
    t = time.clock()
    frontier = queue.Queue()
    initState = State()
    initState.set_values(problem.values)
    frontier.put(initState)

    while frontier.empty() == False:
        curState = frontier.get()
        if problem.is_goal(curState):
            t = time.clock() - t
            print("Runtime: "+str(t))
            return curState.curExp()
        else:
            actions = problem.actions(curState)
            if actions is not None:
                for i in actions:
                    if curState.curExp() == "":
                        levelTwoState = problem.result(curState,"add",i)
                        frontier.put(levelTwoState)
                    else:
                        addState = problem.result(curState,"add",i)
                        #print(addState.get_values())
                        subState = problem.result(curState,"sub",i)
                        mulState = problem.result(curState,"mul",i)
                        divState = problem.result(curState,"div",i)

                        frontier.put(addState)
                        frontier.put(subState)
                        frontier.put(mulState)
                        frontier.put(divState)

    return "No Solution"

#Depth First Search
def DFS(problem):
    t = time.clock()
    frontier = []
    initState = State()
    initState.set_values(problem.values)
    frontier.append(initState)

    while len(frontier) != 0:
        curState = frontier.pop()
        if problem.is_goal(curState):
            t = time.clock() - t
            print("Runtime: "+str(t))
            return curState.curExp()
        else:
            actions = problem.actions(curState)
            if actions is not None:
                for i in actions:
                    if curState.curExp() == "":
                        levelTwoState = problem.result(curState,"add",i)
                        frontier.append(levelTwoState)
                    else:
                        addState = problem.result(curState,"add",i)
                        subState = problem.result(curState,"sub",i)
                        mulState = problem.result(curState,"mul",i)
                        divState = problem.result(curState,"div",i)

                        frontier.append(addState)
                        frontier.append(subState)
                        frontier.append(mulState)
                        frontier.append(divState)

    return "No Solution"


#Depth Limited Search
def DL(problem, limit):
    frontier = []
    initState = State()
    initState.set_values(problem.values)
    initNode = SearchNode(initState,0,"Initialization",None)
    frontier.append(initNode)
    t = time.clock()
    success = False
    cutoff = False

    while len(frontier) != 0:
        curNode = frontier.pop()
        if problem.is_goal(curNode.state):
            t = time.clock() - t
            print("Runtime: "+str(t))
            return [curNode.state.curExp(),"Success"]
        else:
            if curNode.depth < limit:
                actions = problem.actions(curNode.state)
                if actions is not None:
                    for i in actions:
                        if curNode.state.curExp() == "":
                            firstState = problem.result(curNode.state,"add",i)
                            firstNode = SearchNode(firstState,0,"FirstNum",i)
                            frontier.append(firstNode)
                        else:
                            addState = problem.result(curNode.state,"add",i)
                            subState = problem.result(curNode.state,"sub",i)
                            mulState = problem.result(curNode.state,"mul",i)
                            divState = problem.result(curNode.state,"div",i)

                            addNode = SearchNode(addState,(curNode.depth+1),"add",curNode)
                            subNode = SearchNode(subState,(curNode.depth+1),"sub",curNode)
                            mulNode = SearchNode(mulState,(curNode.depth+1),"mul",curNode)
                            divNode = SearchNode(divState,(curNode.depth+1),"div",curNode)

                            frontier.append(addNode)
                            frontier.append(subNode)
                            frontier.append(mulNode)
                            frontier.append(divNode)
            else:
                cutoff = True
    if cutoff == True:
        return "Not Found"
    else:
        return "No Solution"

#Iterative Deepening
def ID(problem):
    limit = 0
    while True:
        result = DL(problem,limit)
        if result[1] == "Success":
            return result[0]
        elif result[1] == "Not Found":
            return "Not Found"
        elif result[1] == "No Solution":
            return "No Solution"
        limit = limit + 1

#Uniform Cost Search
def UC(problem):
    t = time.clock()
    frontier = queue.PriorityQueue()
    initState = State()
    initState.set_values(problem.values)
    initNode = SearchNode(initState,0,"Initialization",None)
    initEntry = PriorityEntry(problem.goal,initNode)
    frontier.put(initEntry)

    while frontier.empty() == False:
        temp = frontier.get()
        #print(temp.data)
        curNode = temp.data
        if problem.is_goal(curNode.state):
            t = time.clock() - t
            print("Runtime: "+str(t))
            return curNode.state.curExp()
        else:
            actions = problem.actions(curNode.state)
            if actions is not None:
                for i in actions:
                    if curNode.state.curExp() == "":
                        firstState = problem.result(curNode.state,"add",i)
                        firstNode = SearchNode(firstState,0,"First Node",None)
                        levelTwoEntry = PriorityEntry(curNode.depth,firstNode)
                        frontier.put(levelTwoEntry)
                    else:
                        addState = problem.result(curNode.state,"add",i)
                        subState = problem.result(curNode.state,"sub",i)
                        mulState = problem.result(curNode.state,"mul",i)
                        divState = problem.result(curNode.state,"div",i)

                        addNode = SearchNode(addState,(curNode.depth+1),"add",curNode)
                        subNode = SearchNode(subState,(curNode.depth+1),"sub",curNode)
                        mulNode = SearchNode(mulState,(curNode.depth+1),"mul",curNode)
                        divNode = SearchNode(divState,(curNode.depth+1),"div",curNode)

                        addEntry = PriorityEntry(addNode.depth,addNode)
                        frontier.put(addEntry)

                        subEntry = PriorityEntry(subNode.depth,subNode)
                        frontier.put(subEntry)

                        mulEntry = PriorityEntry(mulNode.depth,mulNode)
                        frontier.put(mulEntry)

                        divEntry = PriorityEntry(divNode.depth,divNode)
                        frontier.put(divEntry)

    return "No Solution"


#Greedy Breath First Search
def GBFS(problem):
    t = time.clock()
    frontier = queue.PriorityQueue()
    initState = State()
    initState.set_values(problem.values)
    initEntry = PriorityEntry(problem.goal,initState)
    frontier.put(initEntry)

    while frontier.empty() == False:
        temp = frontier.get()
        curState = temp.data
        if problem.is_goal(curState):
            t = time.clock() - t
            print("Runtime: "+str(t))
            return curState.curExp()
        else:
            actions = problem.actions(curState)
            if actions is not None:
                for i in actions:
                    if curState.curExp() == "":
                        levelTwoState = problem.result(curState,"add",i)
                        levelTwoEntry = PriorityEntry(heuristic(levelTwoState,problem.goal),levelTwoState)
                        frontier.put(levelTwoEntry)
                    else:
                        addState = problem.result(curState,"add",i)
                        subState = problem.result(curState,"sub",i)
                        mulState = problem.result(curState,"mul",i)
                        divState = problem.result(curState,"div",i)

                        addEntry = PriorityEntry(heuristic(addState,problem.goal),addState)
                        frontier.put(addEntry)

                        subEntry = PriorityEntry(heuristic(subState,problem.goal),subState)
                        frontier.put(subEntry)

                        mulEntry = PriorityEntry(heuristic(mulState,problem.goal),mulState)
                        frontier.put(mulEntry)

                        divEntry = PriorityEntry(heuristic(divState,problem.goal),divState)
                        frontier.put(divEntry)

    return "No Solution"

#aStar Search
def aStar(problem):
    t = time.clock()
    frontier = queue.PriorityQueue()
    initState = State()
    initState.set_values(problem.values)
    initNode = SearchNode(initState,0,"Initialization",None)
    initEntry = PriorityEntry(problem.goal,initNode)
    frontier.put(initEntry)

    while frontier.empty() == False:
        temp = frontier.get()
        #print(temp.data)
        curNode = temp.data
        if problem.is_goal(curNode.state):
            t = time.clock() - t
            print("Runtime: "+str(t))
            return curNode.state.curExp()
        else:
            actions = problem.actions(curNode.state)
            if actions is not None:
                for i in actions:
                    if curNode.state.curExp() == "":
                        firstState = problem.result(curNode.state,"add",i)
                        firstNode = SearchNode(firstState,0,"First Node",None)
                        levelTwoEntry = PriorityEntry((curNode.depth + heuristic(firstNode.state,problem.goal)),firstNode)
                        frontier.put(levelTwoEntry)
                    else:
                        addState = problem.result(curNode.state,"add",i)
                        subState = problem.result(curNode.state,"sub",i)
                        mulState = problem.result(curNode.state,"mul",i)
                        divState = problem.result(curNode.state,"div",i)

                        addNode = SearchNode(addState,(curNode.depth+1),"add",curNode)
                        subNode = SearchNode(subState,(curNode.depth+1),"sub",curNode)
                        mulNode = SearchNode(mulState,(curNode.depth+1),"mul",curNode)
                        divNode = SearchNode(divState,(curNode.depth+1),"div",curNode)

                        addEntry = PriorityEntry(addNode.depth + heuristic(addState,problem.goal),addNode)
                        frontier.put(addEntry)

                        subEntry = PriorityEntry(subNode.depth + heuristic(subState,problem.goal),subNode)
                        frontier.put(subEntry)

                        mulEntry = PriorityEntry(mulNode.depth + heuristic(mulState,problem.goal),mulNode)
                        frontier.put(mulEntry)

                        divEntry = PriorityEntry(divNode.depth + + heuristic(divState,problem.goal),divNode)
                        frontier.put(divEntry)

    return "No Solution"


#Simple Hueristic
def heuristic(curState,goalState):
    if curState.values:
        i = abs(goalState - curState.val)//(len(curState.values))
    else:
        i = abs(goalState - curState.val)
    return i


if __name__ == "__main__":
    t = time.clock()
    p = Parser()
    simple_problems = 5 #p.counter("simple_examples.txt")
    for i in range(0,simple_problems):
        args = p.parser("harder_examples.txt")
        problem = Problem()
        problem.set_goal(args[i][0])
        problem.set_values(args[i][1])
        print("\nValues: "+str(problem.values))
        print("Goal: "+ str(problem.goal))
        print(GBFS(problem))
    t = time.clock() - t
    print("Total Runtime for "+str(simple_problems)+" problems "+str(t))
