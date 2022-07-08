#Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

#Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.
class Podracer:
    def __init__(price,max_speed,condition,self):
      self.max_speed = max_speed,
      self.condition =condition,
      self.price = price
#Podracer defines the class-(4)
    def repair(self):
      self.condition = "repaired"
#connects repair() that changes the condition of the class Podracer 
class AnakinsPod(Podracer):
#newclass introduced (racer) as well as a method to gain speed by using boost 
  def __init__(price,max_speed,condition,self):
      super.init(condition,max_speed,price)
  def boost(self):
    self.max_speed *=2
#newclass(secondracer)SebulsPod
#similarly to the first class but with a defined method to flame_jet as well as the conidtion of the second vector 
class SebulbasPod(Podracer):
  def __init__(self,max_speed,condition,price):
    super.init(condition,price,max_speed);
  def flame_jet(other,self):
    other.condition = "trashed"
    #How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    
    #1..the encapsulation of each class with its own method to run each array within the method()
    #2 the abstraction is another pillar that the class/method make it simplistic and entirely focused on those arrangements without including other programs nor directives 
    # each program has its own method of inheritance just like sri py uses the class/subclass(def) as well as the arrays that come within the inhertance similar to cause and effort.
    #. Each  Class/subclass  can provide its own independent implementation of polymorphism interface. Each performing its own job to combine together into engaging interface interaction .
#https://replit.com/@Kaleab007/Reflecting-on-Coding-Paradigms?v=1
