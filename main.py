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
    
#https://replit.com/@Kaleab007/Reflecting-on-Coding-Paradigms?v=1
