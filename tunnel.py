from pwn import *
import subprocess 
import sys
import time
import numpy as np
import codecs
import copy


def found_cycle(char):
  global start
  global location
  x = start[0]
  y = start[1]
  z = start[2]

  if char == "U":
    z += 1
  elif char == "D":
    z -=1 
  elif char == "L":
    x -= 1
  elif char == "R":
    x += 1
  elif char == "F":
    y += 1
  elif char == "B":
    y -= 1
    
  at_bounds = x == 100 or x < 0 or y == 100 or y < 0 or z == 100 or z < 0
  
  if not(at_bounds):
    if location[x][y][z]:
      print("found cycle")
      return True
    else:
      return False
    
  else:
    print("at bounds")
    return True
    
    
    
    

  

  
def update_position(char):
  global start
  if char == "U":
    start[2] += 1
  elif char == "D":
    start[2] -=1 
  elif char == "L":
    start[0] -= 1
  elif char == "R":
    start[0] += 1
  elif char == "F":
    start[1] += 1
  elif char == "B":
    start[1] -= 1
    

    
def update_location():
  global location
  global start
  location[start[0]][start[1]][start[2]] = True
  


# repeatedly send lines

# save where we go 
size = 100
location = [[[False for _ in range(size)] for _ in range(size)] for _ in range(size)]
start = [int(size/2),int(size/2),int(size/2)]

payload = ["U","D","L","R","F","B"]
quit = "Q"
potential = ""
others = []
previous_move = ""
restarting = False
index = -1
found = False
found_route = False
executable = process('./tunnel')
first = executable.readline()
#second = executable.readline()
print(first)

while True:
  print("others")
  print(len(others))
  if  len(others) != 0 and restarting:
    
    first = executable.readline()
    print(first)
    #second = executable.readline()
    print("restarting")
    location = [[[False for _ in range(size)] for _ in range(size)] for _ in range(size)]
    start = [int(size/2),int(size/2),int(size/2)]
    
    restarting = False
    potential = others[len(others)-1]
    # now need to try potential beyond
    last_char = potential[len(potential)-1]
  
    if last_char == "U":
      index = 0
    elif last_char == "D":
      index = 1
    elif last_char == "L":
      index = 2
    elif last_char == "R":
      index = 3
    elif last_char == "F":
      index = 4
    elif last_char == "B":
      # should not happen
      index = 5
    potential = potential[:-1] # remove the last char
    if len(potential) > 0:
      previous_move = potential[len(potential) - 1]
      
      
    for character in potential:
      executable.sendline(character)
      out = executable.readline()
      print("out 1: " + str(out))
      update_position(character)
      update_location()

  for ind in range(len(payload)):
    item = payload[ind]

    if index == -1: 

      if not((previous_move == "U" and item == "D") or (previous_move == "D" and item == "U") or (previous_move == "L" and item == "R") or (previous_move == "R" and item == "L") or (previous_move == "F" and item == "B") or (previous_move == "B" and item == "F")):

        executable.sendline(item) 
        
        output = executable.readline()
        output = str(output)
     
        if "Cannot move that way" in output:
          executable.readline()
     
        
        print("output: " + output + " with input: " + item)
        if not("Cannot move that way" in output) and not(found_cycle(item)):
          found_route = True
          previous_move = item 
          potential += item
          update_position(item)
          update_location()
          
          
          
          
          print("working with path: " + potential)
          if "break into the vault" in output:
            print("found flag with: " + potential)
            found = True
            break
            
          
          if item != "B":
            others.append(potential)
          break
        else: 
          if item == "B":
            restarting = True
            executable.sendline("Q")
            
            print("balls")
            executable = process('./tunnel')
            
    else:
      if index == ind:
        index = -1
  if found:
    break
      
      
      
  

