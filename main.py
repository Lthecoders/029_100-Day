import os
import time

print("\n\n\nToday's NRG news loading....\n\nPlease wait....")
time.sleep(5)  # used time module
os.system("clear")  # used os module


def color_print(color, text):
  if color == "red":
    print("\033[31m", text, sep="", end="\033[0m")
  elif color == "green":
    print("\033[32m", text, sep="", end="\033[0m")
  elif color == "yellow":
    print("\033[33m", text, sep="", end="\033[0m")
  elif color == "blue":
    print("\033[34m", text, sep="", end="\033[0m")
  elif color == "purpule":
    print("\033[35", text, sep="", end="\033[0m")
  elif color == "caen":
    print("\033[36m", text, sep="", end="\033[0m")
  else:
    print("\033[0m", text, sep="", end="\033[0m")


print("----------------TODAY'S BREAKING NEWS-----------------------")

print("\n\n\n1. Nikihl's result had arrived and he ", end="")
color_print("green", "passed the exam.")
print("\n\n2. Nikhil is planning to extend the date of his python course by ",
      end="")
color_print("red", "4 more moths")

print("\n\n3. according to today's weather ", end="")
color_print("blue", "rain is comming")

print("\n\n4. nikhil had declared replit as ", end="")
color_print("yellow", "his favourite IDE\n\n")

color_print("red", "5. decrease by 95%")
print(" Nikhil's VS code daily usage")
