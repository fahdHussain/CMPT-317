'''
Fahd Hussain
NISD: fah235
Student Num: 11140722
CMPT 317
'''

#TreeSearch
from a1q1 import Problem
from a1q1 import State
from a1q2_Parser import Parser
from a1q2_SearchNode import SearchNode
from a1q2_PriorityEntry import PriorityEntry
import queue
import time

#Breath First Search
def BFS(problem):
    c = 0 #Counter
    qSize = 0 #Largest frontier size
    t = time.clock()
    frontier = queue.Queue()
    initState = State()
    initState.set_values(problem.values)
    frontier.put(initState)

    while frontier.empty() == False:
        curState = frontier.get()
        c += 1
        if frontier.qsize() > qSize:
            qSize = frontir.qSize()
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


if __name__ == "__main__":
    t = time.clock()
    p = Parser()
    simple_problems = 10 #p.counter("simple_examples.txt")#NUMBER OF PROBLEMS
    for i in range(0,simple_problems):
        args = p.parser("simple_examples.txt")#FILE
        problem = Problem()
        problem.set_goal(args[i][0])
        problem.set_values(args[i][1])
        print("\nValues: "+str(problem.values))
        print("Goal: "+ str(problem.goal))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        print("Solution: "+str(ID(problem)))#PICK SEARCH METHOD HERE: BFS,DFS,DL,ID
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    t = time.clock() - t
    print("Total Runtime for "+str(simple_problems)+" problems "+str(t))
