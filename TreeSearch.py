#TreeSearch
from Problem import Problem
from State import State
from Queue import Queue

def treeSearch(problem):
    frontier = Queue()
    initState = State()
    initState.set_values(problem.values)

    frontier.put(initState)

    while frontier.empty() == False:
        curState = frontier.get()
        if problem.is_goal(curState):
            print("reached is_goal")
            return curState.curExp()
        else:
            print(curState.curExp())
            actions = problem.actions(curState)
            print(actions)
            print(str(frontier.qsize()))
            if actions is not None:
                for i in actions:
                    print("i:"+str(i)+", "+curState.curExp())
                    addState = problem.result(curState,"add",i)
                    subState = problem.result(curState,"sub",i)
                    mulState = problem.result(curState,"mul",i)
                    divState = problem.result(curState,"div",i)

                    frontier.put(addState)
                    frontier.put(subState)
                    frontier.put(mulState)
                    frontier.put(divState)

    return "No Solution"

if __name__ == "__main__":
    goal_1 = 50
    list_1 = [55,32,18,17,10,11,54]
    problem_1 = Problem()
    problem_1.set_values(list_1)
    problem_1.set_goal(goal_1)

    goal_2 = -52
    list_2 = [29,26,68,41,40,12,52]
    problem_2 = Problem()
    problem_2.set_values(list_2)
    problem_2.set_goal(goal_2)

    goal_3 = 59
    list_3 = [45,41,19,14,18,53]
    problem_3 = Problem()
    problem_3.set_values(list_3)
    problem_3.set_goal(goal_3)

    print(treeSearch(problem_2))
