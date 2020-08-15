from random import *
import collections
from Algorithm import *
from Board import *
from Nodes import *
from dotsandboxes import EnenmyMove, gameMoves

#global
#up-down-left-right
box1 =[]
box2 =[]
box3 =[]
box4 =[]
box5 =[]
box6 =[]
box7 =[]
box8 =[]
box9 =[]

class DotsNBoxes: # A class for managing the moves made by the human and the computer
    def __init__(self, Board_Xdim, Board_Ydim, Ply_num):
        currentState = Game([], Board_Xdim, Board_Ydim)
        currentState.Initiate()
        self.State = Thing(currentState)
        self.Ply_num = Ply_num
        self.Score = 0

    def Human(self): # Defining the Human player and his actions/Choices
        self.State.Draw()
        #global Humanmove
        Humanmove = EnenmyMove()
        global HumanX
        global HumanY
        if (Humanmove == (204, 284)):
          HumanX = 1
          HumanY = 0
          box1.append((1,0))
        if (Humanmove == (346, 283)):
          HumanX = 3
          HumanY = 0
          box2.append((3,0))
        if (Humanmove == (469, 285)):
          HumanX = 5
          HumanY = 0
          box3.append((0,5))
        if (Humanmove == (145, 349)):
          HumanX = 0
          HumanY = 1
          box1.append((0,1))
        if (Humanmove == (274, 345)):
          HumanX = 2
          HumanY = 1
          box1.append((2,1))
          box2.append((2,1))
        if (Humanmove == (404, 342)):
          HumanX = 4
          HumanY = 1
          box2.append((4,1))
          box3.append((4,1))
        if (Humanmove == (536, 348)):
          HumanX = 6
          HumanY = 1
          box3.append((6,1))
        if (Humanmove == (210, 415)):
          HumanX = 1
          HumanY = 2
          box1.append((1,2))
          box4.append((1,2))
        if (Humanmove == (343, 414)):
          HumanX = 3
          HumanY = 2
          box2.append((3,2))
          box5.append((3,2))
        if (Humanmove == (475, 414)):
          HumanX = 5
          HumanY = 2
          box3.append((5,2))
          box6.append((5,2))
        if (Humanmove == (143, 473)):
          HumanX = 0
          HumanY = 3
          box4.append((0,3))
        if (Humanmove == (274, 469)):
          HumanX = 2
          HumanY = 3
          box4.append((2,3))
          box5.append((2,3))
        if (Humanmove == (404, 476)):
          HumanX = 4
          HumanY = 3
          box5.append((4,3))
          box6.append((4,3))
        if (Humanmove == (536, 474)):
          HumanX = 6
          HumanY = 3
          box6.append((6,3))
        if (Humanmove == (211, 544)):
          HumanX = 1
          HumanY = 4
          box4.append((1,4))
          box7.append((1,4))
        if (Humanmove == (347, 546)):
          HumanX = 3
          HumanY = 4
          box5.append((3,4))
          box8.append((3,4))
        if (Humanmove == (480, 544)):
          HumanX = 5
          HumanY = 4
          box6.append((5,4))
          box9.append((5,4))
        if (Humanmove == (144, 619)):
          HumanX = 0
          HumanY = 5
          box7.append((0,5))
        if (Humanmove == (275, 604)):
          HumanX = 2
          HumanY = 5
          box7.append((2,5))
          box8.append((2,5))
        if (Humanmove == (405, 613)):
          HumanX = 4
          HumanY = 5
          box8.append((4,5))
          box9.append((4,5))
        if (Humanmove == (536, 627)):
          HumanX = 6
          HumanY = 5
          box9.append((6,5))
        if (Humanmove == (212, 676)):
          HumanX = 1
          HumanY = 6
          box7.append((1,6))
        if (Humanmove == (345, 676)):
          HumanX = 3
          HumanY = 6
          box8.append((3,6))
        if (Humanmove == (476, 676)):
          HumanX = 5
          HumanY = 6
          box9.append((5,6))

        if (HumanX, HumanY) not in self.State.children:
            self.State.Make(HumanX, HumanY, False)
            self.State = self.State.children[(HumanX, HumanY)]
        else:
            self.State = self.State.children[(HumanX, HumanY)]

        print("Current Score =====>> Your Score - AI Score = " + str(self.State.CurrentScore),end ="\n\n\n")
        if((HumanX, HumanY) in box1):
          if(len(box1)==4):
            self.Human()
          else:
            self.Computer()
        elif ((HumanX, HumanY) in box2):
          if (len(box2) == 4):
            self.Human()
          else:
            self.Computer()
        elif ((HumanX, HumanY) in box3):
          if (len(box3) == 4):
            self.Human()
          else:
            self.Computer()
        elif ((HumanX, HumanY) in box4):
          if (len(box4) == 4):
            self.Human()
          else:
            self.Computer()
        elif ((HumanX, HumanY) in box5):
          if (len(box5) == 4):
            self.Human()
          else:
            self.Computer()
        elif((HumanX, HumanY) in box6):
          if(len(box6)==4):
            self.Human()
          else:
            self.Computer()
        elif((HumanX, HumanY) in box7):
          if(len(box7)==4):
            self.Human()
          else:
            self.Computer()
        elif((HumanX, HumanY) in box8):
          if(len(box8)==4):
            self.Human()
          else:
            self.Computer()
        elif((HumanX, HumanY) in box9):
          if(len(box9)==4):
            self.Human()
          else:
            self.Computer()


    def Computer(self): # Defining the Computer player and its actions/Choices
        self.State.Draw()

        move = Algo.miniMax(self.State, self.Ply_num)

        self.State = self.State.children[(move[0], move[1])]

        print("AI selected the following coordinates to play:\n" + "(" ,str(move[0]), ", " + str(move[1]), ")", end = "\n\n")

        if ((move[0], move[1]) == (1, 0)):
          gameMoves("box1 up")
          box1.append((1, 0))
        if ((move[0], move[1]) == (3, 0)):
          gameMoves("box2 up")
          box2.append((3, 0))
        if ((move[0], move[1]) == (5, 0)):
          gameMoves("box3 up")
          box3.append((5, 0))
        if ((move[0], move[1]) == (0, 1)):
          gameMoves("box1 left")
          box1.append((0, 1))
        if ((move[0], move[1]) == (2, 1)):
          gameMoves("box2 left")
          box2.append((2, 1))
        if ((move[0], move[1]) == (4, 1)):
          gameMoves("box3 left")
          box3.append((4, 1))
        if ((move[0], move[1]) == (6, 1)):
          gameMoves("box3 right")
          box3.append((6, 1))
        if ((move[0], move[1]) == (1, 2)):
          gameMoves("box4 up")
          box4.append((1, 2))
        if ((move[0], move[1]) == (3, 2)):
          gameMoves("box5 up")
          box5.append((3, 2))
        if ((move[0], move[1]) == (5, 2)):
          gameMoves("box6 up")
          box6.append((5, 2))
        if ((move[0], move[1]) == (0, 3)):
          gameMoves("box4 left")
          box4.append((0, 3))
        if ((move[0], move[1]) == (2, 3)):
          gameMoves("box5 left")
          box5.append((2, 3))
        if ((move[0], move[1]) == (4, 3)):
          gameMoves("box6 left")
          box6.append((4, 3))
        if ((move[0], move[1]) == (6, 3)):
          gameMoves("box6 right")
          box6.append((6, 3))
        if ((move[0], move[1]) == (1, 4)):
          gameMoves("box7 up")
          box7.append((1, 4))
        if ((move[0], move[1]) == (3, 4)):
          gameMoves("box8 up")
          box8.append((3, 4))
        if ((move[0], move[1]) == (5, 4)):
          gameMoves("box9 up")
          box9.append((5, 4))
        if ((move[0], move[1]) == (0, 5)):
          gameMoves("box7 left")
          box7.append((0, 5))
        if ((move[0], move[1]) == (2, 5)):
          gameMoves("box8 left")
          box8.append((2, 5))
        if ((move[0], move[1]) == (4, 5)):
          gameMoves("box9 left")
          box9.append((4, 5))
        if ((move[0], move[1]) == (6, 5)):
          gameMoves("box9 right")
          box9.append((6, 5))
        if ((move[0], move[1]) == (1, 6)):
          gameMoves("box7 down")
          box7.append((1, 6))
        if ((move[0], move[1]) == (3, 6)):
          gameMoves("box8 down")
          box8.append((3, 6))
        if ((move[0], move[1]) == (5, 6)):
          gameMoves("box9 down")
          box9.append((5, 6))

        if len(self.State.children) == 0:
            self.State.Draw()

            return

        if ((move[0], move[1]) in box1):
          if (len(box1) == 4):
            self.Computer()
          else:
            self.Human()
        elif ((move[0], move[1]) in box2):
          if (len(box1) == 4):
            self.Computer()
          else:
            self.Human()
        elif ((move[0], move[1]) in box3):
          if (len(box1) == 4):
            self.Computer()
          else:
            self.Human()
        elif ((move[0], move[1]) in box4):
          if (len(box1) == 4):
            self.Computer()
          else:
            self.Human()
        elif ((move[0], move[1]) in box5):
          if (len(box1) == 4):
            self.Computer()
          else:
            self.Human()
        elif ((move[0], move[1]) in box6):
          if (len(box1) == 4):
            self.Computer()
          else:
            self.Human()
        elif ((move[0], move[1]) in box7):
          if (len(box1) == 4):
            self.Computer()
          else:
            self.Human()
        elif ((move[0], move[1]) in box8):
          if (len(box1) == 4):
            self.Computer()
          else:
            self.Human()
        elif ((move[0], move[1]) in box9):
          if (len(box1) == 4):
            self.Computer()
          else:
            self.Human()




    def start(self):
         self.Human()
