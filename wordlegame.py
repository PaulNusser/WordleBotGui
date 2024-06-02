import pygame
import sys
pygame.init()
SCREEN_WIDTH = 623
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background_image = pygame.image.load('Pictures/StartingTiles.png')
background_rect = background_image.get_rect()
print(background_rect.width, background_rect.height)
running = True
center_x = (SCREEN_WIDTH - background_rect.width) / 2
center_y = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    screen.blit(background_image, (center_x,center_y))
    pygame.display.flip()
pygame.quit()
sys.exit()
