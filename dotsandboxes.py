from PIL import ImageGrab, Image, ImageOps
import os
import time
import win32api, win32con
from numpy import *
#from Algorithm import *
#from DotsNBoxes import *
#from Board import *
#from Nodes import *
x_pad = 2
y_pad = 75
visited=[]

def screenGrab():
  box = (x_pad + 1, y_pad + 1, x_pad + 679, y_pad + 650)
  im = ImageGrab.grab(box)
  return im

def grab():
  box = (x_pad + 1, y_pad + 1, x_pad + 679, y_pad + 650)
  im = ImageOps.grayscale(ImageGrab.grab(box))
  a = array(im.getcolors())
  a = a.sum()
  print(a)
  return a

class RGB:
  # box1
  get_up_one=3273
  get_left_one=2184
  get_right_one=2227
  get_down_one=1734
  #box2
  get_up_two=2411
  get_left_two=2227
  get_right_two=2273
  get_down_two=2818
  #box3
  get_up_three=2762
  get_left_three=2273
  get_right_three=2187
  get_down_three=3241
  #box4
  get_up_four=1734
  get_left_four=2721
  get_right_four=1836
  get_down_four=3330
  #box5
  get_up_5=2818
  get_left_5=1836
  get_right_5=2259
  get_down_5=3127
  #box6
  get_up_6=3241
  get_left_6=2259
  get_right_6=2822
  get_down_6=3102
  #box7
  get_up_7=3330
  get_left_7=2800
  get_right_7=2676
  get_down_7=3173
  #box8
  get_up_8=3127
  get_left_8=3207
  get_right_8=2225
  get_down_8=4496
  #box9
  get_up_9=2798
  get_left_9=2106
  get_right_9=2921
  get_down_9=3492

  RGBArray = [get_up_one, get_down_one, get_left_one, get_right_one,
              get_up_two, get_down_two, get_left_two, get_right_two,
              get_up_three, get_down_three, get_left_three, get_right_three,
              get_up_four, get_down_four, get_left_four, get_right_four,
              get_up_5, get_down_5, get_left_5, get_right_5,
              get_up_6, get_down_6, get_left_6, get_right_6,
              get_up_7, get_down_7, get_left_7, get_right_7,
              get_up_8, get_down_8, get_left_8, get_right_8,
              get_up_9, get_down_9, get_left_9, get_right_9]

def get_up_one():
    box = (149, 281, 273, 293)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    return a
def get_left_one():
    box = (142, 293, 150,411)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_right_one():
    box = (273,293,281,412)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_down_one():
    box = (152, 413, 270, 420)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_up_two():
    box = (281,283,401,291)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_left_two():
    box = (273, 293, 281, 412)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_right_two():
    box = (402,293,411,411)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_down_two():
    box = (281, 413, 401, 422)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_up_three():
    box = (412,282,532,292)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_left_three():
    box = (402,293,411,411)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_right_three():
    box = (534,293,542,411)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_down_three():
    box = (410,411,534,423)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_up_four():
    box =(152, 413, 270, 420)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_left_four():
    box = (141,423, 150, 543)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_right_four():
    box = (272,424,280,542)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_down_four():
    box = (150,542,272,554)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_up_5():
    box = (281, 413, 401, 422)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_left_5():
    box = (272,424,280,542)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_right_5():
    box = (403,423,411,542)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_down_5():
    box = (281,542,403,553)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_up_6():
    box = (410,411,534,423)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_left_6():
    box = (403,423,411,542)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_right_6():
    box = (532, 423, 543, 542)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_down_6():
    box = (410,542,533,554)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_up_7():
    box =  (150,542,272,554)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_left_7():
    box = (141,553,150,673)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_right_7():
    box = (271,554,281,672)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_down_7():
    box = (150,672,271,684)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_up_8():
    box =  (281,542,403,553)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_left_8():
    box = (271,553,281,673)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_right_8():
    box = (402,553,412,672)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_down_8():
    box = (279,672,402,684)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_up_9():
    box =  (411,542,532,553)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_left_9():
    box = (402,553,411,672)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_right_9():
    box = (532,553,542,673)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_down_9():
    box = (411,672,532,683)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
   # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a

class cords:
  # box number 1
  cordup1 = (204, 284)
  corddown1 = (210, 415)
  cordleft1 = (145, 349)
  cordright1 = (274, 345)
  # box number 2
  cordup2 = (346, 283)
  corddown2 = (343, 414)
  cordleft2 = (274, 345)
  cordright2 = (404, 342)
  # box number 3
  cordup3 = (469, 285)
  corddown3 = (475, 414)
  cordleft3 = (404, 342)
  cordright3 = (536, 348)
  # box number 4
  cordup4 = (210, 415)
  corddown4 = (211, 544)
  cordleft4 = (143, 473)
  cordright4 = (274, 469)
  # box number 5
  cordup5 = (343, 414)
  corddown5 = (347, 546)
  cordleft5 = (274, 469)
  cordright5 = (404, 476)
  # box number 6
  cordup6 = (475, 414)
  corddown6 = (480, 544)
  cordleft6 = (404, 478)
  cordright6 = (536, 474)
  # box number 7
  cordup7 = (211, 544)
  corddown7 = (212, 676)
  cordleft7 = (144, 619)
  cordright7 = (275, 604)

  # box number 8
  cordup8 = (339, 536)
  corddown8 = (346, 673)
  cordleft8 = (275, 604)
  cordright8 = (405, 613)
  # box number 9
  cordup9 = (480, 544)
  corddown9 = (469, 673)
  cordleft9 = (405, 613)
  cordright9 = (536, 627)
  

global cordArray
cordArray = [cords.cordup1, cords.corddown1, cords.cordleft1, cords.cordright1,
               cords.cordup2, cords.corddown2, cords.cordleft2, cords.cordright2,
               cords.cordup3, cords.corddown3, cords.cordleft3, cords.cordright3,
               cords.cordup4, cords.corddown4, cords.cordleft4, cords.cordright4,
               cords.cordup5, cords.corddown5, cords.cordleft5, cords.cordright5,
               cords.cordup6, cords.corddown6, cords.cordleft6, cords.cordright6,
               cords.cordup7, cords.corddown7, cords.cordleft7, cords.cordright7,
               cords.cordup8, cords.corddown8, cords.cordleft8, cords.cordright8,
               cords.cordup9, cords.corddown9, cords.cordleft9, cords.cordright9]
  
def leftClick():
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
  time.sleep(.1)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
  print
  'Click.'

def mousePos(cord):
  win32api.SetCursorPos((cord[0], cord[1]))

def gameMoves(move):
  # box1
  if move == "box1 up":
    mousePos(cords.cordup1)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordup1)
  if move == "box1 left":
    mousePos(cords.cordleft1)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordleft1)
  if move == "box1 right":
    mousePos(cords.cordright1)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordright1)
  if move == "box1 down":
    mousePos(cords.corddown1)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.corddown1)
  # box2
  if move == "box2 up":
    mousePos(cords.cordup2)
    leftClick()
    time.sleep(0.5)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordup2)
  if move == "box2 left":
    mousePos(cords.cordleft2)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordleft2)
  if move == "box2 right":
    mousePos(cords.cordright2)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordright2)
  if move == "box2 down":
    mousePos(cords.corddown2)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.corddown2)
  # box3
  if move == "box3 up":
    mousePos(cords.cordup3)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordup3)
  if move == "box3 left":
    mousePos(cords.cordleft3)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordleft3)
  if move == "box3 right":
    mousePos(cords.cordright3)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordright3)
  if move == "box3 down":
    mousePos(cords.corddown3)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.corddown3)
  # box4
  if move == "box4 up":
    mousePos(cords.cordup4)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordup4)
  if move == "box4 left":
    mousePos(cords.cordleft4)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordleft4)
  if move == "box4 right":
    mousePos(cords.cordright4)
    leftClick()
    mousePos((cords.cordright4) + (1, 1))
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordright4)
  if move == "box4 down":
    mousePos(cords.corddown4)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.corddown4)
  # box5
  if move == "box5 up":
    mousePos(cords.cordup5)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordup5)
  if move == "box5 left":
    mousePos(cords.cordleft5)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordleft5)
  if move == "box5 right":
    mousePos(cords.cordright5)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordright5)
  if move == "box5 down":
    mousePos(cords.corddown5)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.corddown5)
  # box6
  if move == "box6 up":
    mousePos(cords.cordup6)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordup6)
  if move == "box6 left":
    mousePos(cords.cordleft6)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordleft6)
  if move == "box6 right":
    mousePos(cords.cordright6)
    leftClick()
    leftClick()
    mousePos(cords.cordright6 + (1, 1))
    leftClick()
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordright6)
  if move == "box6 down":
    mousePos(cords.corddown6)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.corddown6)
  # box7
  if move == "box7 up":
    mousePos(cords.cordup7)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordup7)
  if move == "box7 left":
    mousePos(cords.cordleft7)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordleft7)
  if move == "box7 right":
    mousePos(cords.cordright7)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordright7)
  if move == "box7 down":
    mousePos(cords.corddown7)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.corddown7)
  # box8
  if move == "box8 up":
    mousePos(cords.cordup8)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordup8)
  if move == "box8 left":
    mousePos(cords.cordleft8)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordleft8)
  if move == "box8 right":
    mousePos(cords.cordright8)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordright8)
  if move == "box8 down":
    mousePos(cords.corddown8)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.corddown8)
  # box9
  if move == "box9 up":
    mousePos(cords.cordup9)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordup9)
  if move == "box9 left":
    mousePos(cords.cordleft9)
    leftClick()
    time.sleep(0.5)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordleft9)
  if move == "box9 right":
    mousePos(cords.cordright9)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.cordright9)
  if move == "box9 down":
    mousePos(cords.corddown9)
    leftClick()
    time.sleep(0.5)
    visited.append(cords.corddown9)

def checkChange(move):
  #box1
  if (move == cords.cordup1):
    a = get_up_one()
    if(a==RGB.get_up_one):
      return True
    else:
      return False
  if (move == cords.corddown1):
    a = get_down_one()
    if(a==RGB.get_down_one):
      return True
    else:
      return False
  if (move == cords.cordleft1):
    a = get_left_one()
    if(a==RGB.get_left_one):
      return True
    else:
      return False
  if (move == cords.cordright1):
    a = get_right_one()
    if(a==RGB.get_right_one):
      return True
    else:
      return False
  #box2
  if (move == cords.cordup2):
    a = get_up_two()
    if (a == RGB.get_up_two):
      return True
    else:
      return False
  if (move == cords.corddown2):
    a = get_down_two()
    if (a == RGB.get_down_two):
      return True
    else:
      return False
  if (move == cords.cordleft2):
    a = get_left_two()
    if (a == RGB.get_left_two):
      return True
    else:
      return False
  if (move == cords.cordright2):
    a = get_right_two()
    if (a == RGB.get_right_two):
      return True
    else:
      return False
  #box3
  if (move == cords.cordup3):
    a = get_up_three()
    if (a == RGB.get_up_three):
      return True
    else:
      return False
  if (move == cords.corddown3):
    a = get_down_three()
    if (a == RGB.get_down_three):
      return True
    else:
      return False
  if (move == cords.cordleft3):
    a = get_left_three()
    if (a == RGB.get_left_three):
      return True
    else:
      return False
  if (move == cords.cordright3):
    a = get_right_three()
    if (a == RGB.get_right_three):
      return True
    else:
      return False
  #box4
  if (move == cords.cordup4):
    a = get_up_four()
    if (a == RGB.get_up_four):
      return True
    else:
      return False
  if (move == cords.corddown4):
    a = get_down_four()
    if (a == RGB.get_down_four):
      return True
    else:
      return False
  if (move == cords.cordleft4):
    a = get_left_four()
    if (a == RGB.get_left_four):
      return True
    else:
      return False
  if (move == cords.cordright4):
    a = get_right_four()
    if (a == RGB.get_right_four):
      return True
    else:
      return False
  #box5
  if (move == cords.cordup5):
    a = get_up_5()
    if (a == RGB.get_up_5):
      return True
    else:
      return False
  if (move == cords.corddown5):
    a = get_down_5()
    if (a == RGB.get_down_5):
      return True
    else:
      return False
  if (move == cords.cordleft5):
    a = get_left_5()
    if (a == RGB.get_left_5):
      return True
    else:
      return False
  if (move == cords.cordright5):
    a = get_right_5()
    if (a == RGB.get_right_5):
      return True
    else:
      return False
  #box6
  if (move == cords.cordup6):
    a = get_up_6()
    if (a == RGB.get_up_6):
      return True
    else:
      return False
  if (move == cords.corddown6):
    a = get_down_6()
    if (a == RGB.get_down_6):
      return True
    else:
      return False
  if (move == cords.cordleft6):
    a = get_left_6()
    if (a == RGB.get_left_6):
      return True
    else:
      return False
  if (move == cords.cordright6):
    a = get_right_6()
    if (a == RGB.get_right_6):
      return True
    else:
      return False
  #box7
  if (move == cords.cordup7):
    a = get_up_7()
    if (a == RGB.get_up_7):
      return True
    else:
      return False
  if (move == cords.corddown7):
    a = get_down_7()
    if (a == RGB.get_down_7):
      return True
    else:
      return False
  if (move == cords.cordleft7):
    a = get_left_7()
    if (a == RGB.get_left_7):
      return True
    else:
      return False
  if (move == cords.cordright7):
    a = get_right_7()
    if (a == RGB.get_right_7):
      return True
    else:
      return False
  #box8
  if (move == cords.cordup8):
    a = get_up_8()
    if (a == RGB.get_up_8):
      return True
    else:
      return False
  if (move == cords.corddown8):
    a = get_down_8()
    if (a == RGB.get_down_8):
      return True
    else:
      return False
  if (move == cords.cordleft8):
    a = get_left_8()
    if (a == RGB.get_left_8):
      return True
    else:
      return False
  if (move == cords.cordright8):
    a = get_right_8()
    if (a == RGB.get_right_8):
      return True
    else:
      return False
  #box9
  if (move == cords.cordup9):
    a = get_up_9()
    if (a == RGB.get_up_9):
      return True
    else:
      return False
  if (move == cords.corddown9):
    a = get_down_9()
    if (a == RGB.get_down_9):
      return True
    else:
      return False
  if (move == cords.cordleft9):
    a = get_left_9()
    if (a == RGB.get_left_9):
      return True
    else:
      return False
  if (move == cords.cordright9):
    a = get_right_9()
    if (a == RGB.get_right_9):
      return True
    else:
      return False

def EnenmyMove():

  for move in cordArray:
    if(move not in visited):
      if(checkChange(move) is False):
        global EnemyMoves
        EnemyMoves= move
        visited.append(move)
        break
  return EnemyMoves



