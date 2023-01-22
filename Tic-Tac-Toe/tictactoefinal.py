"""
Tic Tac Toe game by AC
"""
import pygame

# Initialize pygame and music
pygame.init()
pygame.mixer.init()

# Set window size and title
size = (750, 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe by AC")

# Load player images
playerX_img = pygame.image.load("X1.png")
playerO_img = pygame.image.load("O1.png")

# Load sound effect
place_sound = pygame.mixer.Sound("sound.wav")

# Create a 3x3 grid
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Set current player
current_player = "X"

# Set players score counter
playerX_score = 0
playerO_score = 0


def check_winner():
    """
    Function checks the rows, columns and diagonals
    in order to determine if there is a winner
    """
    # Check rows
    for row in grid:
        if row.count(row[0]) == len(row) and row[0] != 0:
            return row[0]
    # Check columns
    for col in range(len(grid)):
        check = []
        for row in grid:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            return check[0]
    # Check diagonals
    diags = []
    for idx in range(len(grid)):
        diags.append(grid[idx][idx])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        return diags[0]
    diags = []
    for idx in range(len(grid)):
        diags.append(grid[idx][len(grid) - 1 - idx])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        return diags[0]
    return 0


def check_draw():
    """
    Function checks if there is a draw,
    by determing if the matrix is full.
    """
    for row in grid:
        if 0 in row:
            return False
    return True


if __name__ == "__main__":

    # Game loop
    running = True
    game_over = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the x and y coordinates of the click
                pos = pygame.mouse.get_pos()
                x = pos[0] // 250
                y = pos[1] // 250

                # Check if the spot is empty
                if grid[y][x] == 0:
                    # Fill in the spot with the current player's symbol
                    grid[y][x] = current_player
                    place_sound.play()

                    # Check for winner
                    winner = check_winner()
                    if winner:
                        running = False
                        game_over = True
                        winner_player = winner
                    else:
                        draw = check_draw()
                        if draw:
                            running = False
                            game_over = True
                            winner_player = "Draw"
                        else:
                            # Switch current player
                            if current_player == "X":
                                current_player = "O"
                            else:
                                current_player = "X"

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the grid lines
        for i in range(1, 3):
            pygame.draw.line(screen, (255, 255, 255),
                             (i * 250, 0), (i * 250, 750))
            pygame.draw.line(screen, (255, 255, 255),
                             (0, i * 250), (750, i * 250))

        # Draw the symbols
        for y in range(3):
            for x in range(3):
                if grid[y][x] == "X":
                    screen.blit(playerX_img, (x * 250, y * 250))
                elif grid[y][x] == "O":
                    screen.blit(playerO_img, (x * 250, y * 250))

        # Display the scores
        font = pygame.font.SysFont("Comic sans", 20)
        text = font.render("Player X: " + str(playerX_score) +
                           "  Player O: " + str(playerO_score),
                           True, (255, 255, 255))
        screen.blit(text, (15, 700))

        # Display the current player
        font = pygame.font.SysFont("Comic sans", 20)
        text = font.render("Current player: " + str(current_player),
                           True, (255, 255, 255))
        screen.blit(text, (570, 700))

        # Update the display
        pygame.display.flip()

        if game_over:
            font = pygame.font.SysFont("Comic sans", 35)
            if winner_player == "Draw":
                text = font.render("Draw!", True, (255, 255, 255))
                screen.blit(text, (330, 346))
            else:
                text = font.render("Player " + str(winner_player) + " wins!",
                                   True, (255, 255, 255))
                screen.blit(text, (255, 346))
            if winner_player == "X":
                playerX_score += 1
            elif winner_player == "O":
                playerO_score += 1
            pygame.display.flip()
            pygame.time.wait(3000)

            # Run the game again
            grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            current_player = "X"
            game_over = False
            running = True

# Quit pygame
pygame.mixer.stop()
pygame.quit()
