'''
Fahd Hussain
NISD: fah235
Student Num: 11140722
CMPT 317
'''
#This class is used as a helper for the priority queue
class PriorityEntry():
    def __init__(self,priority,data):
        self.data = data
        self.priority = priority

    def __lt__(self,other):
        return self.priority < other.priority
