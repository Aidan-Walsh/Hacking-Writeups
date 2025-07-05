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
  copy_start = copy.deepcopy(start)
  if char == "U":
    copy_start[2] += 1
  elif char == "D":
    copy_start[2] -=1 
  elif char == "L":
    copy_start[0] -= 1
  elif char == "R":
    copy_start[0] += 1
  elif char == "F":
    copy_start[1] += 1
  elif char == "B":
    copy_start[1] -= 1
    
  if location[copy_start[0]][copy_start[1]][copy_start[2]]:
    print("found cycle")
  
  return location[copy_start[0]][copy_start[1]][copy_start[2]]
  
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
    
  print("statistics: ")
  print(start)
  print(location[start[0]][start[1]][start[2]])
    
def update_location():
  global location
  global start
  location[start[0]][start[1]][start[2]] = True

# repeatedly send lines

# save where we go 
size = 100
location = [[[False] * size] * size] * size
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
while True:
  if not(found_route):
    executable = process('./tunnel')
    location = [[[False] * size] * size] * size
    first = executable.readline()
    second = executable.readline
    print(str(first))
    print(str(second))
    found_route = False
  if  len(others) != 0 and restarting:
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
    else:
      if index == ind:
        index = -1
  if found:
    break
      
      
      
  

