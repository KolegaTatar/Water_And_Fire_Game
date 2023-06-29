import pygame
from pygame import mixer
from button import Button
import level1, level2, level3, level4, level5, level6, level7, level8, level9, level10

pygame.init()
resolution = (1280, 720)
SCREEN = pygame.display.set_mode(resolution)

mixer.music.load("assets/music.mp3")
pygame.mixer.music.set_volume(0.1)
mixer.music.play()

def levels():
    run = True
    clock = 0
    backgruond = pygame.image.load("assets/Background2.png")
    levels = (
        Button(200, 170, "level1"),
        Button(200, 280, "level2"),
        Button(200, 390, "level3"),
        Button(200, 500, "level4"),
        Button(200, 610, "level5"),

        Button(880, 170, "level6"),
        Button(880, 280, "level7"),
        Button(880, 390, "level8"),
        Button(880, 500, "level9"),
        Button(880, 610, "level10"),

        Button(540, 450, "quit")



    )
    while run:
        clock += pygame.time.Clock().tick(60) / 1000 # maksymalnie 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
                run = False

        for i in range(len(levels)):
            if levels[0].tick():
                level1.main()
                open(file="level1.py")
            elif levels[1].tick():
                level2.main()
                open(file="level2.py")
            elif levels[2].tick():
                level3.main()
                open(file="level3.py")
            elif levels[3].tick():
                level4.main()
                open(file="level4.py")
            elif levels[4].tick():
                level5.main()
                open(file="level5.py")
            elif levels[5].tick():
                level6.main()
                open(file="level6.py")
            elif levels[6].tick():
                level7.main()
                open(file="level7.py")
            elif levels[7].tick():
                level8.main()
                open(file="level8.py")
            elif levels[8].tick():
                level9.main()
                open(file="level9.py")
            elif levels[9].tick():
                level10.main()
                open(file="level10.py")

            elif levels[10].tick():
                run = False
        SCREEN.blit(backgruond, (0, 0))
        for button in levels:
            button.draw(SCREEN)

        pygame.display.update()


def main_menu():
    run = True
    clock = 0
    backgruond = pygame.image.load("assets/Background.png")
    player1 = pygame.image.load("dyroG.png")
    player2 =pygame.transform.flip(pygame.image.load("p.szG.png"), True, False)
    buttons = (
        Button(540, 306, "play"),
        Button(540, 450, "quit")
    )

    while run:
        clock += pygame.time.Clock().tick(60) / 1000 # maksymalnie 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
                run = False

        for i in range(len(buttons)):
            if buttons[0].tick():
                levels()
            if buttons[1].tick():
                run = False

        SCREEN.blit(backgruond, (0, 0))
        SCREEN.blit(player1, (20, 300))
        SCREEN.blit(player2, (1040, 300))

        for button in buttons:
            button.draw(SCREEN)
        pygame.display.update()


if __name__ == "__main__":
    main_menu()