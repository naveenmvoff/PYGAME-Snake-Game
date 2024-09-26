import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_width, player_height = 20, 20
player = pygame.Rect(300, 250, player_width, player_height)

element_width, elemnt_height = 50, 50 # create the first element at a random position
element_x = random.randint(0, SCREEN_WIDTH - element_width)
element_y = random.randint(0, SCREEN_HEIGHT - elemnt_height)
element = pygame.Rect(element_x, element_y, element_width, elemnt_height)

run = True
element_visible = True  # To control element visibility

player_speed = 4  # Constant speed for the player
player_speed_x = player_speed  # Start movement speed along the X-axis
player_speed_y = 0  # Start movement speed along the Y-axis

clock = pygame.time.Clock()  # Clock for controlling frame rate

while run:

    screen.fill((0, 0, 102))
    
    pygame.draw.rect(screen, (255, 0, 0), player)  # Draw the player

    front_points = [
         (player.left, player.bottom),
         (player.centerx, player.top),
         (player.right, player.top)
    ]
    pygame.draw.polygon(screen, (255, 165, 0), front_points)

    if element_visible:
        pygame.draw.rect(screen, (0, 255, 0), element)

    player.move_ip(player_speed_x, player_speed_y)  # Move the player in the X and Y direction

    # Wall collision detection to prevent the player from moving outside
    if player.left <= 0:
        player.left = 0
        player_speed_x = 0
    if player.right >= SCREEN_WIDTH:
        player.right = SCREEN_WIDTH
        player_speed_x = 0
    if player.top <= 0:
        player.top = 0
        player_speed_y = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT
        player_speed_y = 0

    # Screen control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_speed_x = -player_speed  # Move left at constant speed
        player_speed_y = 0
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_speed_x = player_speed  # Move right at constant speed
        player_speed_y = 0
    elif keys[pygame.K_w] or keys[pygame.K_UP]:
        player_speed_y = -player_speed  # Move up at constant speed
        player_speed_x = 0
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_speed_y = player_speed  # Move down at constant speed
        player_speed_x = 0

    if player.colliderect(element):  # Generate a new random position for the element when collected
        element_visible = False  # Make the element disappear

        player_width += 10  # Increase player size on collecting the element
        player.size = (player_width, player_height)

        element_x = random.randint(0, SCREEN_WIDTH - element_width)  # Generate a new random element
        element_y = random.randint(0, SCREEN_HEIGHT - elemnt_height)
        element = pygame.Rect(element_x, element_y, element_width, elemnt_height)
        element_visible = True  # Make the new element visible

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
