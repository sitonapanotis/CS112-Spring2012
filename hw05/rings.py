#!/usr/bin/env python

import pygame
from pygame.locals import *

## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")

## Draw
screen.fill(WHITE)

## Rings
topY = 128
botY = 256
circleBlue = pygame.draw.circle(screen, (BLUE), (160, topY), 110, THICKNESS)
circleBlack = pygame.draw.circle(screen, (BLACK), (400, topY), 110, THICKNESS)
circleRed = pygame.draw.circle(screen, (RED), (640, topY), 110, THICKNESS)
circleYellow = pygame.draw.circle(screen, (YELLOW), (280, botY), 110, THICKNESS)
circleGreen = pygame.draw.circle(screen, (GREEN), (520, botY), 110, THICKNESS)
pygame.display.update


## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
