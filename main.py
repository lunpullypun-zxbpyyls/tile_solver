import sys
import pygame as pgm
pgm.init() # initialise pygame components

dimensions = w, h = 200,200

gamewindow = pgm.display.set_mode(dimensions) #create window with specified dimensions


# Run game:
while 1:
    for event in pgm.event.get(): # listen for events
        if event.type == pgm.QUIT: sys.exit() # close window if titlebar button pressed
    gamewindow.fill([0, 0, 0]) # background color of the window
    pgm.display.flip() # update the *entire* window