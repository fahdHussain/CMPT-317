'''
Fahd Hussain
NISD: fah235
Student Num: 11140722
CMPT 317
'''

#Used to parse text files
class Parser:
  def parser(self,file):
      lists = []
      with open(file) as f:
          for arg_line in f:
              arg_list = arg_line.split()
              target = int(arg_list[0])
              arg_list = list(map(int,arg_list))[1:]
              pair = target,arg_list
              lists.append(pair)
      return lists


  def counter(self,file):
       num = 0
       with open(file) as f:
           for i in f:
               num += 1
       return num

#~~~~~~~~~~~~~~~~~~~~~~~~~~TESTING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    p = Parser()
    thing = p.parser("simple_examples.txt")

    print(thing[1][1])
    print(p.counter("simple_examples.txt"))
