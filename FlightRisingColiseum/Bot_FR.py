import os 
from PIL import ImageGrab
import time 
import win32api, win32con
from PIL import ImageOps
from numpy import *
import pyautogui
import random

from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()
#some sort of DPS problem unrelated to project
#this stops the images from being cut off while using screengrab


# ------------------


 
x_pad = 475   #These pads is so it works for different resolutions. Instead of
y_pad = 699   #changing all the coordinates, other users of the bot would just
              #have to adjust the pads using screenGrab() defined further below

class Cord: #All important coordinates that are checked often are stored here
             
    mainmenu = (835, 893)
    attack = (922, 806)
    scratch = (1106, 835)
    shred = (919, 950)
    attacker1 = (974, 177)
    hpattacker1 = (924, 13)
    attacker2 = (1091, 331)
    hpattacker2 = (1044, 147)
    attacker3 = (1223, 477)
    hpattacker3 = (1164, 305)
    attacker4 = (1031, 265)
    hpattacker4 = (984, 67)
    attacker5 = (1145, 433)
    hpattacker5 = (1104, 227)
    boss = (1007, 292)
    hpboss = (893, 67)
    
def screenGrab(): #Originally used as a tool to get x_pad and y_pad
                  #Currently used to scan the for RGB values in startGame(). See previous versions in journal
    
    box = (x_pad+1,y_pad+1,x_pad+1371,y_pad+1220)
    im = ImageGrab.grab(box)
    hm = im.getpixel(Cord.hpboss) #put any coordinate u want
    print(hm)
    
    return im
 
def leftClick(): #just for clicking
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #Press left click
    time.sleep(.1) #delays
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)   #Release left click
    print('Click')

def mousePos(cord): #Moves the mouse to the given coordinates. This changed a lot, see previous versions in journal
    
    pyautogui.moveTo(x_pad + cord[0] + random.randint(0, 20), y_pad + cord[1] + random.randint(0, 20), duration=0.25)
    #Receives coordinates given in startGame(), goes to location taking into account the pads
    #random.randint(0,20) randomizes the coordinates a bit to avoid bot detection

                       
def get_cords(): #Tool that was used to get the coordinates of all the buttons and attackers in the game.
                 #No longer used now that the bot is completed
    
    x,y = win32api.GetCursorPos()
    x = x - x_pad   #Takes into account pads, like all the other functions
    y = y - y_pad
    print(x,y)



# ------------------



def startGame(): #Start of the main function

  wait = 0 #Used and explained further below

  while x_pad == 475: #Just needed this to loop forever so picked random variable

    #location of first menu
    mousePos((257, 559))
    leftClick()
    leftClick()
    time.sleep(1.5)
     
    #location of second menu
    mousePos((489, 771))
    leftClick()
    time.sleep(3.5)

   
    while x_pad == 475: #Loop for the actual game once past menus

      x = round(random.uniform(0, 0.2),2)  #Generates random float that'll be added to randomize wait intervals

      screenGrab()
      s = screenGrab() #Takes picture of the screen and assigns it to s

      if s.getpixel((205, 57)) == (93, 94, 134): #Checks if bot got past the menu, good for checking 'camping' (explained in journal)
        wait = 0  #Resets the counter for amount of times 'waiting', used farther below
      
      if s.getpixel(Cord.mainmenu) == (222, 214, 202):
      #Checks if coordinates of mainmenu match RGB value. If so, that means this menu popped up, and level is complete
      #The coordinates & RGB values are from using get_cords() & screenGrab() as tools. Check journal for how
          print('level complete')
          mousePos((811, 822))    #Goes to the button that sends us back to the mainmenu
          leftClick()
          time.sleep(1.4 + x)      #Pauses after clicking for 1.4 + (randomized number) seconds
          break          #Breaks out of this loop to go back to the menu loop


      #All the other if statements have the same idea as the above if statement


      if s.getpixel(Cord.attack) == (236, 234, 231):
        wait=0
        print('attacking')
        mousePos(Cord.attack)
        leftClick()
        time.sleep(0.1 + x)
        
        screenGrab() 
        s = screenGrab() #Important screen change here, picture of screen taken again
        
        if s.getpixel(Cord.shred) == (214, 172, 99): #Special attack option
           mousePos(Cord.shred)
           leftClick()
           time.sleep(0.4 + x)
        else:
           mousePos(Cord.scratch)   #Normal attack option
           leftClick()
           time.sleep(0.4 + x)
           
        if s.getpixel(Cord.hpattacker1) == (49, 61, 48):
           mousePos(Cord.attacker1)
           leftClick()
           time.sleep(1.2+ x)
        elif s.getpixel(Cord.hpattacker2) == (49, 61, 48):
           mousePos(Cord.attacker2)
           leftClick()
           time.sleep(1.2 + x)
        elif s.getpixel(Cord.hpattacker3) == (49, 61, 48):
           mousePos(Cord.attacker3)
           leftClick()
           time.sleep(1.2 + x)
        elif s.getpixel(Cord.hpattacker4) == (49, 61, 48):
           mousePos(Cord.attacker4)
           leftClick()
           time.sleep(1.2 + x)
        elif s.getpixel(Cord.hpattacker5) == (49, 61, 48):
           mousePos(Cord.attacker5)
           leftClick()
           time.sleep(1.2 + x)
        elif s.getpixel(Cord.hpboss) == (10, 10, 13):
           mousePos(Cord.boss)
           leftClick()
           time.sleep(1.2 + x)


      else: #If no hp bars or attack buttons are detected, page is probably loading or enemies are attacking
          
        wait = wait+1 #Wait counter goes up 1 every loop
        print('waiting')
        if wait == 15: #If computer waited 15 consecutive times, something must've went wrong. So, program exits
          exit()    
        time.sleep(2) #Pauses for 2 seconds to wait, then loops back to recheck if they're hp bars or attack buttons



   
