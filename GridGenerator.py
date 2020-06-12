import pygame
pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Simulation")



#colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

BoardLength = 6;
size = 80;


def main():
    gameExit = False




    while not gameExit:

        drawBoard()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True










def drawBoard():
    counter = 0
    for i in range(1, BoardLength + 1):
        for j in range(1, BoardLength + 1):
            # check if current loop value is even
            if counter % 2 == 0:
                pygame.draw.rect(gameDisplay, BLACK, [size * j, size * i, size, size])
            else:
                pygame.draw.rect(gameDisplay, BLUE, [size * j, size * i, size, size])
            counter += 1
        # since theres an even number of squares go back one value
        counter -= 1

    pygame.draw.rect(gameDisplay, WHITE, [size, size, BoardLength * size, BoardLength * size], 1)









if __name__ == "__main__":
    main()