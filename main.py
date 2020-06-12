"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

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

def randomize_grid(rows, columns, board):
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(randint(0,1))
        board.append(row)
        
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
    screen.fill((255, 0, 255))
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
