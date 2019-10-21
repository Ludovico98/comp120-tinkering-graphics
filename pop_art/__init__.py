"""Appropriation Pop Art by John 'SnugglinBunny' Rock"""

import pygame, sys, os
from pygame.locals import *

__author__ = "John Rock"
__copyright__ = "Copyright 2019, John Rock"
__license__ = "MIT"
__version__ = "1.1"
__url__ = "https://github.com/SnugglinBunny/comp120-tinkering-graphics"

pygame.init()

BASE_FILE = 'images/base.jpg'

WIDTH = 1400
HEIGHT = 932
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Generate Pop Art')
clock = pygame.time.Clock()

BLACK = (0, 0, 0)  # red, green, blue in 8-bits
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

Delay = 200
print(os.getcwd())

colourImage = pygame.image.load(BASE_FILE)
colourImage = pygame.transform.scale(colourImage, (1400, 932))

DISPLAY.blit(colourImage, (0, 0))
pygame.display.flip()


def Greyscale():
    DISPLAY.blit(colourImage, (0, 0))
    pxarray = pygame.PixelArray(DISPLAY)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b

            GREY = (RED + GREEN + BLUE) / 3

            pxarray[x, y] = (GREY, GREY, GREY)
    del pxarray


def redColour():
    DISPLAY.blit(colourImage, (0, 0))
    pxarray = pygame.PixelArray(DISPLAY)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (RED, 255 - GREEN, 255 - BLUE)


def greenColour():
    DISPLAY.blit(colourImage, (0, 0))
    pxarray = pygame.PixelArray(DISPLAY)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, GREEN, 255 - BLUE)


def blueColour():
    DISPLAY.blit(colourImage, (0, 0))
    pxarray = pygame.PixelArray(DISPLAY)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, 255 - GREEN, BLUE)


def invertColour():
    pxarray = pygame.PixelArray(DISPLAY)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, 255 - GREEN, 255 - BLUE)
    del pxarray


def BlackWhite():
    DISPLAY.blit(colourImage, (0, 0))
    pxarray = pygame.PixelArray(DISPLAY)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b

            GREY = (RED + GREEN + BLUE)
            if GREY < 400:
                pxarray[x, y] = (0, 0, 0)
            else:
                pxarray[x, y] = (255, 255, 255)

    del pxarray


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            Greyscale()
            pygame.image.save(DISPLAY, 'images/grey.jpg')
            print("Done 1/6")
            pygame.display.flip()

            redColour()
            invertColour()
            pygame.image.save(DISPLAY, 'images/red.jpg')
            print("Done 2/6")
            pygame.display.flip()

            greenColour()
            invertColour()
            pygame.image.save(DISPLAY, 'images/green.jpg')
            print("Done 3/6")
            pygame.display.flip()

            blueColour()
            invertColour()
            pygame.image.save(DISPLAY, 'images/blue.jpg')
            print("Done 4/6")
            pygame.display.flip()

            BlackWhite()
            pygame.image.save(DISPLAY, 'images/black_white.jpg')
            print("Done 5/6")
            pygame.display.flip()

            RedImage = pygame.image.load('images/red.jpg')
            RedImage = pygame.transform.scale(RedImage, (700, 466))
            GreenImage = pygame.image.load('images/green.jpg')
            GreenImage = pygame.transform.scale(GreenImage, (700, 466))
            BlueImage = pygame.image.load('images/blue.jpg')
            BlueImage = pygame.transform.scale(BlueImage, (700, 466))
            BWImage = pygame.image.load('images/black_white.jpg')
            BWImage = pygame.transform.scale(BWImage, (700, 466))

            print("Done 6/6")

            DISPLAY.blit(BWImage, (0, 0))
            pygame.display.flip()
            pygame.time.delay(Delay)
            DISPLAY.blit(RedImage, (700, 0))
            pygame.display.flip()
            pygame.time.delay(Delay)
            DISPLAY.blit(GreenImage, (0, 466))
            pygame.display.flip()
            pygame.time.delay(Delay)
            DISPLAY.blit(BlueImage, (700, 466))
            pygame.display.flip()
            pygame.time.delay(Delay)
            pygame.image.save(DISPLAY, 'images/piece_de_resistance.jpg')

    pygame.display.update()
    clock.tick(60)
