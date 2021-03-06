#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame import draw
from pygame.locals import *

BACKGROUND = 80, 80, 80
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30
RED = (255,0,0)
BLUE = (0,0,255)



def turnRight(direction):
    dx, dy = direction
    if abs(dx) == 1:
        dy += dx
        dx = 0
    elif abs(dy) == 1:
        dx -= dy
        dy = 0
    return dx, dy

def turnLeft(direction):
    dx, dy = direction
    if abs(dx) == 1:
        dy -= dx
        dx = 0
    elif abs(dy) == 1:
        dx += dy
        dy = 0
    return dx, dy

def move(pos, direction):
    x, y = pos
    dx, dy = direction
    x += dx
    y += dy

    return x, y

def drawLiteBike(surf, pos, color):

    x,y = pos[0], pos[1]

    pygame.draw.rect(surf , color, (x,y,4,4))

def collision(tail1, tail2):
    win = ""
    done = False
    t1 = tail1
    t2 = tail2
    print tail1
    print t1
    front1 = t1[-1]
    front2 = t2[-1]
    print "tail2", tail2
    print front1
    #if len(t1) < 2:
     #   del t1[-1]
     #   del t2[-1]
    tailOneSelf = t1[0: -2]
    print tailOneSelf
    tailTwoSelf = t2[0: -2]
    if front1 in tail2 or front1 in tailOneSelf:
        win = "player 2 (red)"
        done = True
    if front2 in tail2 or front1 in tailTwoSelf:
        win = "player 1 (blue)"
        done = True
    print "colis", t1, front1, tailOneSelf, tail1
    return done, win, tail1

done = False
win =""
p1 = K_LEFT, K_RIGHT
p2 = K_a, K_d
pos1 = (599, 299)
pos2 = (199, 299)
dir1 = -1, 0
dir2 = 1, 0
p1tail = []
p2tail = []

#main screen turn on
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()


while not done:
    screen.fill((0,0,0))
    drawLiteBike(screen, pos1, RED)
    drawLiteBike(screen, pos2, BLUE)
    p1tail.append(pos1)
    p2tail.append(pos2)
    print p1tail
    colis1 , colis2 = p1tail, p2tail
    pos1 = move(pos1, dir1)
    pos2 = move(pos2, dir2)
    
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True
        elif evt.type == KEYDOWN and evt.key == p1[0]:
            dir1 = turnLeft(dir1)
        elif evt.type == KEYDOWN and evt.key == p1[1]:
            dir1 = turnRight(dir1)
        elif evt.type == KEYDOWN and evt.key == p2[0]:
            dir2 = turnLeft(dir2)
        elif evt.type == KEYDOWN and evt.key == p2[1]:
            dir2 = turnRight(dir2)
        
    print p1tail        
    done, win, p1tail= collision(colis1, colis2)
    pygame.display.flip()
    clock.tick(FPS)
    print done, win, p1tail

#print "s% won the game" % win
print "the end"
