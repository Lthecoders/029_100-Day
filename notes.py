# for i in range(0, 100):
#   print(i, end=" ")
# """
#   what print function actualy does is that after evey print statemet get's over it press
#   enter and new line is created. and from that line furthter printing is done

#   \n creates a new line
#   \t create a tab
#   \v create a vertical tab
#   \b create a backspace
#   \r create a carriage return
#   \f create a form feed
#   \o oo create a octal value
#   \x hh create a hex value
#   \N{name} create a unicode character
#   \
# """

# name="nikhil"
# sname="akhil"

# print("my name is",name,"my brother name is ", end=sname)
# #after end we cannot inter further data in print statement
# "by adding end means we are offically ending this print funcion"

# print("If you put")
# print("\033[33m", end="") #yellow
# print("nothing as the")
# print("\033[35m", end="") #purple
# print("end character")
# print("\033[32m", end="") #green
# print("then you don't")
# print("\033[0m", end="") #default
# print("get odd gaps")

# print("If you put", "\033[33m", "nothing as the", "\033[35m", "end character", "\033[32m", "then you don't", "\033[0m", "get odd gaps", end="")

# print()
# print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")

# import os, time
# print('\033[?25l', end="")
# for i in range(1, 101):
#   print(i)
#   time.sleep(0.1)
#   os.system("clear")

# import os, time

# for i in range(1, 101):
#   print(i)
#   time.sleep(0.5)
#   # os.system("clear")

# name = input("what is your name ? ")
# print('\033[?25l',
#       end="")  # by doing this we cannot interact with the console or terminal
# print("hello", name)
# print('\033[?25h',
#       end="")  # by doing this we cannot interact with the console or terminal


def super_subroutine(text2, text):
  # text = ""
  # text2 = ""
  # color =
  print('LET TRY\n',
        "\033[35m",
        text2,
        "\033[32m",
        text,
        sep="",
        end="\033[0m")
  print(" get the normal color back")


# print(su)
super_subroutine(
    "now we have to level up or else i will no become mythos pro ",
    "let's hope for positive one day i can become. ")
