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
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 512

player_posX = 140
player_posY = 380
PLAYER_WIDTH = 42
PLAYER_HEIGHT = 55
JUMP_HEIGHT = 200
VELOCITY = 3

PLATFORM_WIDTH = 58
PLATFORM_HEIGHT = 17

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bgSurface = pygame.image.load('DoodleJump/sprites/space-bck.png').convert()

player_surf = pygame.image.load('DoodleJump/sprites/space-left.png').convert_alpha()
player_rect = pygame.Rect((player_posX, player_posY), (PLAYER_WIDTH, PLAYER_HEIGHT))

platform_surf = pygame.image.load('DoodleJump/sprites/platform.png').convert_alpha()
platform_rect = pygame.Rect((player_posX, (player_posY + PLAYER_HEIGHT)), (PLATFORM_WIDTH, PLATFORM_HEIGHT))

gravity = 0

clock = pygame.time.Clock()

run = True

colorPlayer = (11, 102, 35)
colorBgScreen = (250, 243, 221)


while(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    
    key = pygame.key.get_pressed()
    
    screen.blit(bgSurface, (0, 0))
    
    if key[pygame.K_RIGHT] == True:
        player_surf = pygame.image.load('DoodleJump/sprites/space-right.png').convert_alpha()
        player_rect.x += VELOCITY
        
        
        if(player_rect.x == SCREEN_WIDTH):
            player_rect.x = -PLAYER_WIDTH
        
    elif key[pygame.K_LEFT] == True:
        player_surf = pygame.image.load('DoodleJump/sprites/space-left.png').convert_alpha()
        player_rect.x -= VELOCITY
        
        if(player_rect.x == -PLAYER_WIDTH):
            player_rect.x = SCREEN_WIDTH
    
    if(player_rect.colliderect(platform_rect) == 1):
        gravity = -19
    
    gravity += 1
    if(player_rect.y <= SCREEN_HEIGHT - PLAYER_HEIGHT):
        player_rect.y += gravity
    
    
    pygame.draw.rect(screen, 'Black', platform_rect)
        
    screen.blit(player_surf, player_rect)
    pygame.draw.rect(screen, 'Red', player_rect)
    screen.blit(platform_surf, platform_rect)
    
    
    #deplacement(player, key)
        
    pygame.display.update()
    clock.tick(30)

pygame.quit()
