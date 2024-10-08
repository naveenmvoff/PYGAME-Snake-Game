import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_width, player_height = 20, 20
player = pygame.Rect(300, 250, player_width, player_height)

element_width, elemnt_height = 50, 50 #create the first element at the random position
element_x = random.randint(0, SCREEN_WIDTH - element_width)
element_y = random.randint(0, SCREEN_HEIGHT - elemnt_height)
element = pygame.Rect(element_x, element_y, element_width, elemnt_height)

run = True
element_visible = True    # To control element visibility

player_speed = 4
player_speed_x = player_speed #movement speed along with X-axis
player_speed_y = 0 #movement speed along with Y-axis


clock = pygame.time.Clock()  # Clock for controlling frame rate

while run:

    screen.fill((0, 0, 102))
    
    pygame.draw.rect(screen, (255, 0, 0), player)  # Draw the element (green rectangle) only if it's visible

    
    pygame.draw.rect(screen,(255, 0, 0), player)
    front_points = [
         (player.left, player.bottom),
         (player.centerx, player.top),
         (player.right, player.top)
    ]
    pygame.draw.polygon(screen, (255, 165, 0), front_points)

    if element_visible:
        pygame.draw.rect(screen, (0, 255, 0), element)

    player.move_ip(player_speed_x, player_speed_y)  #the player automatical move in the direction X and Y

    # FOR WALL COLLISITION AND PREVENT THE PLAYER FROM MOVING OUTSIDE
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
    
    keys = pygame.key.get_pressed()   #screen control
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_speed_x = -player_speed
        player_speed_y = 0
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_speed_x = player_speed
        player_speed_y = 0
    elif keys[pygame.K_w] or keys[pygame.K_UP]:
        player_speed_y = -player_speed
        player_speed_x = 0
    elif keys[pygame.K_s] or keys[pygame.K_DOWN] == True:
        player_speed_y = player_speed
        player_speed_x = 0


    if player.colliderect(element):    #generatethe position of the element
        element_visible = False        #Make the element disappear

        player_width += 10
        # player_height += 10
        player.size = (player_width, player_height) #update the player height

        element_x = random.randint(0, SCREEN_WIDTH - element_width)  #GENERATE THE RANDOM ELEMENT
        element_y = random.randint(0, SCREEN_HEIGHT - elemnt_height)
        element = pygame.Rect(element_x, element_y, element_width, elemnt_height)
        element_visible =True                                               #MAKE THAT VISIBLE 


    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()

    clock.tick(60) # control the frame rate, # Limit to 60 frames per second

pygame.quit()
