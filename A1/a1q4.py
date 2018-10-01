'''
Fahd Hussain
NISD: fah235
Student Num: 11140722
CMPT 317
'''

from a1q1 import Problem
from a1q1 import State
from a1q2_Parser import Parser
from a1q2_SearchNode import SearchNode
from a1q2_PriorityEntry import PriorityEntry
import queue
import time

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
    #NUMBER OF PROBLEMS, use p.counter(fileName) for all problems in file
    simple_problems = 10 # p.counter("simple_examples.txt")
    for i in range(0,simple_problems):
        args = p.parser("simple_examples.txt")#FILE
        problem = Problem()
        problem.set_goal(args[i][0])
        problem.set_values(args[i][1])
        print("\nValues: "+str(problem.values))
        print("Goal: "+ str(problem.goal))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        print("Solution: "+str(aStar(problem)))#PICK SEARCH METHOD HERE: UC,GBFS,aStar
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    t = time.clock() - t
    print("Total Runtime for "+str(simple_problems)+" problems "+str(t))
