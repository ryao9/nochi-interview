import pygame,sys, random

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Simulation")
BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
clock = pygame.time.Clock()

#colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

BoardLength = 6;
size = 80;


def main():
    global gen, genButton
    gameExit = False
    board = randomize_Board()

    gen, genButton = makeText('Generate', WHITE, BLUE, 600,500)





    while not gameExit:


        drawBoard(board)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #board = update_Board(board)
                    board = randomize_Board()
                    drawBoard(board)

        pygame.display.flip()
        clock.tick(60)











def drawBoard(board):
    counter = 0
    for i in range(1, BoardLength + 1):
        for j in range(1, BoardLength + 1):
            # check if current loop value is even
            if board[i-1][j-1] == 0:
                pygame.draw.rect(gameDisplay, BLACK, [size * j, size * i, size, size])
            else:
                pygame.draw.rect(gameDisplay, BLUE, [size * j, size * i, size, size])
            counter += 1
        # since theres an even number of squares go back one value
        counter -= 1

    pygame.draw.rect(gameDisplay, WHITE, [size, size, BoardLength * size, BoardLength * size], 1)


def randomize_Board():
    board = []
    counter = 1
    for r in range(0, BoardLength):
        column = []
        for c in range(0, BoardLength):
            i = random.randint(0,1)
            column.append(i)
            counter += BoardLength
        board.append(column)
        counter -= BoardLength * (BoardLength - 1) + BoardLength - 1

    return board

def update_Board(board):
    for r in range(0, BoardLength):
        for c in range(0, BoardLength):
            if(num >=2 & num <= 3):
                board[r][c] = 1 - board[r][c];


def makeText(text, color, bgcolor, top, left):
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)





if __name__ == "__main__":
    main()