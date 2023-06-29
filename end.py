import pygame
from pygame import mixer
from button import Button

pygame.init()
resolution = (1280, 720)
SCREEN = pygame.display.set_mode(resolution)

mixer.music.load("assets/music.mp3")
pygame.mixer.music.set_volume(0.1)
mixer.music.play()

def end():
    run = True
    clock = 0
    backgruond = pygame.image.load("assets/win.png")
    levels = (
        Button(540, 310, "menu"),

        Button(540, 450, "quit")



    )
    while run:
        clock += pygame.time.Clock().tick(60) / 1000 # maksymalnie 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
                run = False

        for i in range(len(levels)):
            if levels[0].tick():
                run = False
            elif levels[1].tick():
                run = False
        SCREEN.blit(backgruond, (0, 0))
        for button in levels:
            button.draw(SCREEN)

        pygame.display.update()

def lose():
    run = True
    clock = 0
    backgruond = pygame.image.load("assets/Background4.png")
    levels = (
        Button(540, 310, "menu"),

        Button(540, 450, "quit")

    )
    while run:
        clock += pygame.time.Clock().tick(60) / 1000 # maksymalnie 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
                run = False

        for i in range(len(levels)):
            if levels[0].tick():
                run = False
            elif levels[1].tick():
                run = False
        SCREEN.blit(backgruond, (0, 0))
        for button in levels:
            button.draw(SCREEN)

        pygame.display.update()



if __name__ == "__main__":
    end()