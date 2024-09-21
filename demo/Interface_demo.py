import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Player settings
player_width, player_height = 20, 20
player = pygame.Rect(300, 250, player_width, player_height)

# Create the first elment at a random position
element_width, element_height = 50, 50
element_x = random.randint(0, SCREEN_WIDTH - element_width)
element_y = random.randint(0, SCREEN_HEIGHT - element_height)
element = pygame.Rect(element_x, element_y, element_width, element_height)

run = True
element_visible = True  # To control element visibility

# Movement speed
player_speed = 10

clock = pygame.time.Clock()  # Clock for controlling frame rate

while run:
    
    screen.fill((0, 0, 102))

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), player)  # Body of the player

    # Create a front side for the player (triangle)
    front_points = [
        (player.centerx, player.top),  # Top point
        (player.left, player.bottom),   # Bottom left point
        (player.right, player.bottom)   # Bottom right point
    ]
    pygame.draw.polygon(screen, (255, 165, 0), front_points)  # Draw the front side (orange triangle)

    if element_visible:
        pygame.draw.rect(screen, (0, 255, 0), element)  # Draw the element (green rectangle) only if it's visible
    
    keys = pygame.key.get_pressed()   # Screen control
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if player.left > 0:
            player.move_ip(-player_speed, 0)
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if player.right < SCREEN_WIDTH:
            player.move_ip(player_speed, 0)
    elif keys[pygame.K_w] or keys[pygame.K_UP]:
        if player.top > -1:
            player.move_ip(0, -player_speed)
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if player.bottom < SCREEN_HEIGHT:
            player.move_ip(0, player_speed)

    if player.colliderect(element):  # Check for collision
        element_visible = False  # Make the element disappear
        player_width += 10
        player.size = (player_width, player_height)  # Update player size

        # Generate a new random position for the element
        element_x = random.randint(0, SCREEN_WIDTH - element_width)
        element_y = random.randint(0, SCREEN_HEIGHT - element_height)
        element = pygame.Rect(element_x, element_y, element_width, element_height)
        element_visible = True  # Make the new element visible

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()

    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
