import pygame
import sys
def main():
    pygame.init()
    SCREEN_WIDTH = 617.25
    SCREEN_HEIGHT = 700
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    background_image = pygame.transform.scale(pygame.image.load('Pictures/StartingTiles.png'), (317.25,450))
    background_rect = background_image.get_rect()
    print(background_rect.width, background_rect.height)
    running = True
    rectangle = pygame.Rect(25, 625, 30, 45)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255,255,255))
        screen.blit(background_image, (50,0))
        display_keyboard(screen, [])
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()

def display_keyboard(screen, wrong_letters):
    KEYBOARD = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    i = 0
    for letter in KEYBOARD[0]:
        rectangle = pygame.Rect((25 + (i * 36.725)), 475, 30, 45)
        pygame.draw.rect(screen, (114,114,114), rectangle)
        i += 1
    
    i = 0
    for letter in KEYBOARD[1]:
        rectangle = pygame.Rect(43.3625 + (i * 36.725), 530, 30, 45)
        pygame.draw.rect(screen, (114,114,114), rectangle)
        i += 1



if __name__ == "__main__":
    main()