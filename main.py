"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
import pygame
import random

pygame.init()

size = (700, 500)
board_size = (700, 400)
screen = pygame.display.set_mode(size)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Returns number of alive neighboars at position
def alive_neighbors(position, board):
    rows = len(board)
    columns = len(board[0])
    x, y = position
    num_alive = 0
    neighbors = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
    		  (x - 1, y),                 (x + 1, y),
    		  (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
    for x,y in neighbors:
        if x in range(rows) and y in range(columns):
            num_alive += board[x][y]
    return num_alive
 
# Return rows x columns board with all cells dead    
def blank_board(rows, columns):
    board = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(0)
        board.append(row)
    return board

# Randomize values of board
def randomize_board(board):
    rows = len(board)
    columns = len(board[0])
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(random.randint(0,1))
        board.append(row)

def display_board(board):
    rows = len(board)
    columns = len(board[0])
    cell_width = board_size[0] / columns
    cell_height = board_size[1] / rows
    
    for r in range(rows):
        for c in range(columns):
            pygame.draw.rect(screen, pygame.Color(0, 0, 0), (r * cell_width, c * cell_height, cell_width, cell_height))
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), (r * cell_width, c * cell_height, cell_width, cell_height), 1)       
        
     

# Updates board with which cells are alive and dead after next gen
def next_gen(board):
    rows = len(board)
    columns = len(board[0])
    
    new_board = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(0)
        new_board.append(row)
    
    for r in range(rows):
        for c in range(columns):
            num_neighbors = alive_nieghbors((r, c), board)
            if num_neighbors == 3 or (num_neighbors == 2 and board[r][c] == 1):
                new_board[r][c] = 1
            else:
                new_board[r][c] = 0
    return new_board
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    board = blank_board(5, 5)
    randomize_board(board)
    display_board(board)
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
