#rock-paper-scissor.m
#code by @mnk17arts

def rockPaperScissor(system,you):
  if system == you:
    return 
  elif system == 1 and you == 2: return True
  elif system == 1 and you == 3: return False
  elif system == 2 and you == 1: return False
  elif system == 2 and you == 3: return True
  elif system == 3 and you == 1: return True 
  elif system == 3 and you == 2: return False
  else : return 4
    
import random
import time
#system = random.randint(1,3)
#print(system)
from random import randrange

end = 1  
while end != 0:
  system= randrange(1,3)
  you=int(input('''choose(enter) 
  Rock    (1) 
  Paper   (2) 
  Scissor (3)\n '''))
  time.sleep(0.5)
  print("------------------------------------------")
  time.sleep(0.2)
  print(f"system chosen {system}")
  time.sleep(0.1)
  print(f"you chosen {you}")
  time.sleep(0.2)
  print("------------------------------------------")
  result=rockPaperScissor(system,you)
  time.sleep(0.5)
  if result == None :
   print("it's a tie!") 
  elif result == True :
   print("Congo! you won")
  elif result == False : 
   print ("system won! better luck next time")
  else : print("oops! you have entered invalid choice")
  print("------------------------------------------")
  time.sleep(0.5)
  end =(int(input("if you don't want to play again, enter 0 ")))