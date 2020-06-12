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

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

size = (700, 500)
board_size = (700, 400)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
 
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
def randomize_board(rows, columns):
    board = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(random.randint(0,1))
        board.append(row)
    return board

def display_board(board):
    rows = len(board)
    columns = len(board[0])
    cell_width = board_size[0] / columns
    cell_height = board_size[1] / rows
    
    for r in range(rows):
        for c in range(columns):
            if board[r][c] == 1:
                pygame.draw.rect(screen, BLACK, (r * cell_width, c * cell_height, cell_width, cell_height))
                pygame.draw.rect(screen, WHITE, (r * cell_width, c * cell_height, cell_width, cell_height), 1)
            else:  
                pygame.draw.rect(screen, WHITE, (r * cell_width, c * cell_height, cell_width, cell_height))
                pygame.draw.rect(screen, BLACK, (r * cell_width, c * cell_height, cell_width, cell_height), 1)
        
def update_display(position, board):
    row = position[0]
    column = position[1]
    
    board[row][column] = (board[row][column] + 1 ) % 2    
    
    cell_width = board_size[0] / len(board)
    cell_height = board_size[1] / len(board[0])
    
    if board[row][column] == 1:
        pygame.draw.rect(screen, BLACK, (row * cell_width, column * cell_height, cell_width, cell_height))
        pygame.draw.rect(screen, WHITE, (row * cell_width, column * cell_height, cell_width, cell_height), 1)
    else:  
        pygame.draw.rect(screen, WHITE, (row * cell_width, column * cell_height, cell_width, cell_height))
        pygame.draw.rect(screen, BLACK, (row * cell_width, column * cell_height, cell_width, cell_height), 1)

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
            num_neighbors = alive_neighbors((r, c), board)
            if board[r][c] == 1 and num_neighbors not in [2, 3]:
                new_board[r][c] = 0
                update_display((r, c), board)
            elif board[r][c] == 0 and num_neighbors == 3:
                new_board[r][c] = 1
                update_display((r, c), board)
    return new_board


# -------- Main Program Loop -----------
board = blank_board(5, 5)
display_board(board)

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here
    next_gen(board)
    # --- Screen-clearing code goes here
 
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
