import pygame
import sys
import wordleSolver
def main():
    
    pygame.init()
    pygame.font.init()
    SCREEN_WIDTH = 617.25
    SCREEN_HEIGHT = 700
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    background_image = pygame.transform.scale(pygame.image.load('Pictures/StartingTiles.png'), (317.25,450))
    background_rect = background_image.get_rect()
    print(background_rect.width, background_rect.height)
    running = True
    rectangle = pygame.Rect(25, 625, 30, 45)
    wrong_letters = []
    current_guess = []
    yellow_letters = []
    green_letters =[]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if (len(current_guess) < 5):
                    current_guess.append(chr(event.key))
            elif (event.type == pygame.K_RETURN):
                if len(current_guess) == 5:
                    #check guess
            
            
        screen.fill((255,255,255))
        screen.blit(background_image, (50,0))
        display_keyboard(screen,wrong_letters)
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()
def check_guess()
def display_keyboard(screen, wrong_letters):
    font = pygame.font.Font(None, 36)
    KEYBOARD = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    i = 0
    WHITE = (255,255,255)
    GREY = (114,114,114)
    BLACK = (0,0,0)
    box_color = WHITE
    letter_color = BLACK
    for letter in KEYBOARD[0]:
        if (letter in wrong_letters):
            box_color = GREY
            letter_color = WHITE
        else:
            box_color = WHITE
            letter_color = BLACK
        rectangle = pygame.Rect((25 + (i * 36.725)), 475, 30, 45)
        pygame.draw.rect(screen, box_color, rectangle)
        pygame.draw.rect(screen, BLACK, rectangle, 3)
        text_surface = font.render(letter, True, letter_color)
        text_rect = text_surface.get_rect(center=rectangle.center)
        screen.blit(text_surface, text_rect)
        i += 1
    
    i = 0
    for letter in KEYBOARD[1]:
        if (letter in wrong_letters):
            box_color = GREY
            letter_color = WHITE
        else:
            box_color = WHITE
            letter_color = BLACK
        rectangle = pygame.Rect(43.3625 + (i * 36.725), 530, 30, 45)
        pygame.draw.rect(screen, box_color, rectangle)
        pygame.draw.rect(screen,BLACK, rectangle, 3)
        text_surface = font.render(letter, True, letter_color)
        text_rect = text_surface.get_rect(center=rectangle.center)
        screen.blit(text_surface, text_rect)
        i += 1
    i = 0
    for letter in KEYBOARD[2]:
        if (letter in wrong_letters):
            box_color = GREY
            letter_color = WHITE
        else:
            box_color = WHITE
            letter_color = BLACK
        rectangle = pygame.Rect(80.0875 + (i * 36.725), 585, 30, 45)
        pygame.draw.rect(screen, box_color, rectangle)
        pygame.draw.rect(screen, BLACK, rectangle, 3)
        text_surface = font.render(letter, True, letter_color)
        text_rect = text_surface.get_rect(center=rectangle.center)
        screen.blit(text_surface, text_rect)
        i += 1



if __name__ == "__main__":
    main()