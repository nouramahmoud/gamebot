from Algorithm import *
from DotsNBoxes import *
from Board import *
from Nodes import *

def main():
    while True:

      print("\t\tWelcome to the game of Dots and Boxes \n\n ")

      x = input("Press 1 to start the game or press 2 to escape \n\n")
      if x == "1":
        Match = DotsNBoxes(7, 7, 2)
        Match.start()
      else:
        print("\n\nEscape it is!")
        exit()



if __name__ == "__main__":
    main()
