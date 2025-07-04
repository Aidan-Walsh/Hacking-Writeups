from pwn import *
import subprocess 
import sys
import time
import numpy as np
import codecs



# repeatedly send lines

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
  print("reenter")
  for ind in range(len(payload)):
    item = payload[ind]
    print("here" + item)
    if index == -1: 
      print("2")
      if not(previous_move == "U" and item == "D") or (previous_move == "D" and item == "U") or (previous_move == "L" and item == "R") or (previous_move == "R" and item == "L") or (previous_move == "F" and item == "B") or (previous_move == "B" and item == "F"):
        print("reent here")
        executable.sendline(item) 
        print("balls")
        output = executable.readline()
        output = str(output)
        print("balls 1" + str(output))
        if "Cannot move that way" in output:
          executable.readline()
        print("balls 2")
        
        print("output: " + output + " with input: " + item)
        if not("Cannot move that way" in output):
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
      
      
      
  

