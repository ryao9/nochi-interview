import pygame, sys, random
from pygame.locals import*


BOARDWIDTH = 5
BOARDHEIGHT = 5
WINDOWWIDTH = 640;
WINDOWHEIGHT = 480;

#colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


TEXTCOLOR = BLUE
TILEALIVECOLOR = WHITE
TILEDEADCOLOR = BLUE

def main():
    pygame.init()

    FPSCLOCK = pygame.ime.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Zero_Player Simulation')

    #Menu Buttons
    NEW_SURF, NEW_RECT = makeText('Start', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 60)

    BOARD = drawStartingBoard()


def terminate():
    pygame.quit()
    sys.exit()


def drawStartingBoard():
    counter = 1
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(counter)
            counter += BOARDWIDTH
        board.append(column)
        counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1

    board[BOARDWIDTH-1][BOARDHEIGHT-1] = None
    return board