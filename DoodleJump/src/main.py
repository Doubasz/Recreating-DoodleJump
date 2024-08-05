import time
import pygame

pygame.init()

#TODO create the window of the game
#TODO create the player and adding physics to it
#TODO making so that the player can travel between the two side of the screen
#TODO creating platform
#TODO creating different types of platforms
#TODO making the feeling of going upward endlessly
#TODO random spawn of plaforms
#TODO creating objects
#TODO using the real sprites of doodle jump
#TODO creating the score
#TODO if all is well implemented maybe train an ai to beat the game 

#creating the screen
SCREEN_WIDTH = 350
SCREEN_HEIGHT = 575

PLAYER_POSX = 160
PLAYER_POSY = 441
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 45
JUMP_HEIGHT = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect((PLAYER_POSX, PLAYER_POSY, PLAYER_WIDTH, PLAYER_HEIGHT))

run = True
colorPlayer = (11, 102, 35)
colorBgScreen = (250, 243, 221)

def deplacement(player, key):
    while (PLAYER_POSY - player.y) < JUMP_HEIGHT:
        player.y -= 1
    
    if key[pygame.K_RIGHT] == True:
        player.x += 1
        if(player.x == SCREEN_WIDTH):
            player.x = 0
    elif key[pygame.K_LEFT] == True:
        player.x -= 1
        if(player.x == 0):
            player.x = SCREEN_WIDTH

while(run):
    
    screen.fill(colorBgScreen)
    
    pygame.draw.rect(screen, colorPlayer, player)
    key = pygame.key.get_pressed()
    
    deplacement(player, key)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
    pygame.display.update()

pygame.quit()
