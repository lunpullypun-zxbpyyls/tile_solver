import sys
import pygame as pgm
pgm.init()

dimensions = w, h = 200,200

gamewindow = pgm.display.set_mode(dimensions)

while 1:
    for event in pgm.event.get():
        if event.type == pgm.QUIT: sys.exit()
    gamewindow.fill([0, 0, 0])
    pgm.display.flip()