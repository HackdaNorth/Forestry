import pygame
pygame.init()

# Set your grid size and cell size
grid_width = 128
grid_height = 128
cell_size = 8

# Create the game window
screen = pygame.display.set_mode((grid_width * cell_size, grid_height * cell_size))
pygame.display.set_caption("AI Village Game")

# Set the game clock
clock = pygame.time.Clock()

def create_grid():
    grid = [[' ' for _ in range(grid_width)] for _ in range(grid_height)]
    return grid

grid = create_grid()

# Define player
player_x, player_y = grid_width // 2, grid_height // 2  # Starting position
player_size = 2  # Double the size of the trees

# Generate houses and trees
import random

num_houses = 5
num_trees = 20

def generate_random_objects():
    for _ in range(num_houses):
        x, y = random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)
        grid[y][x] = 'H'  # 'H' represents a house

    for _ in range(num_trees):
        x, y = random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)
        grid[y][x] = 'T'  # 'T' represents a tree

generate_random_objects()

# Legend data
legend_data = {
    'H': ('House', (255, 0, 0)),
    'T': ('Tree', (0, 255, 0)),
}

# Initialize the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player movement controls
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_y -= 1
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_y += 1
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_x -= 1
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_x += 1

    # Check for collisions with trees
    if grid[player_y][player_x] == 'T':
        # If there's a tree at the player's position, reset the player's position
        player_x, player_y = grid_width // 2, grid_height // 2

    # Clear the screen
    screen.fill((0, 0, 0))

    # Redraw the grid and player
    for y in range(grid_height):
        for x in range(grid_width):
            if grid[y][x] in legend_data:
                # Get the cell data and draw a colored rectangle
                name, color = legend_data[grid[y][x]]
                pygame.draw.rect(screen, color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))

    # Draw the player
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(player_x * cell_size, player_y * cell_size, player_size * cell_size, player_size * cell_size))

    # Draw the legend
    legend_x, legend_y = 10, 10
    for symbol, (name, color) in legend_data.items():
        pygame.draw.rect(screen, color, pygame.Rect(legend_x, legend_y, cell_size, cell_size))
        font = pygame.font.Font(None, 36)
        legend_text = font.render(f"{symbol}: {name}", True, (0, 0, 255))
        screen.blit(legend_text, (legend_x + cell_size + 5, legend_y))
        legend_y += cell_size + 5

    # Add player icon to the legend
    legend_x += 5
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(legend_x, legend_y, cell_size, cell_size))
    legend_text = font.render("Player", True, (0, 0, 255))
    screen.blit(legend_text, (legend_x + cell_size + 5, legend_y))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
