import pygame
from parametry import Player, Player2, Beam, BeamG, Lawa, g1, g2, Cash
import end
pygame.init()
window = pygame.display.set_mode((1280, 720))


def main():
    run = True
    pause =  False
    win = False
    player = Player()
    player2 = Player2()
    clock = 0
    time = 45
    kolejki = []
    wynik = 0
    background = pygame.image.load("tlo1.png")
    
    beams = [
    #lewo
        Beam(420,400,20,350),
        Beam(370,0,20,300),

        Beam(260,400,100,20),
        
    #prawo
        Beam(840,400,20,350),

        Beam(900, 615, 100, 20),
        Beam(1100, 545, 100, 20),
        Beam(900, 465, 100, 20),
        Beam(1100, 395, 100, 20),
        Beam(880, 325, 100, 20),
        
    #środek  
        Beam(600,400,100,20),
        Beam(370,0,100,20),
        
    # bariery 
        Beam(0, 0, 1280, 20),
        Beam(0, 0, 20, 720),
        Beam(1260, 0, 20, 720),
        Beam(0, 700, 1280, 20),
        
    ]
    # bloki grawitacyjne góra
    beams2 = [
        BeamG(160, 700, 30, 10),
    ]
    # bloki grawitacyjne boki
    beams3 = [

    ]

    przeszkody = [
        Lawa(20, 600, 80, 10),
        Lawa(200, 400, 10, 300),
        Lawa(100, 400, 10, 210),
        Lawa(440, 690, 400, 10),
        Lawa(840, 390, 20, 10),
        Lawa(840, 20, 20, 205),
    ]
    baza1 = [
        g1(600, 390, 50, 10),


    ]
    baza2 = [
        g2(650, 390, 50, 10),


    ]
    tel = [
    ]

    pseudo = [
    ]

    przyciski = []
    while run:
        clock += pygame.time.Clock().tick(60) / 1000  # maksymalnie 60 fps
        if pause == True:
            time = time - 0
        else:
            time = time - 2.5 / 100
        if time < 0:
            pause = True
            run = False
            end.lose()
            open(file="end.py")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause = not pause
        keys = pygame.key.get_pressed()

        if pause:
            text = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 150), "PAUZA ", True,
                                           (245, 245, 245))
            window.blit(text, (480, 300))
            pygame.display.update()
            continue


        if win == True:
            text = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 150), "Wygrałeś ", True,
                                           (245, 245, 245))
            window.blit(text, (430, 300))
            pygame.display.update()
            continue

        player.tick(keys, beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski)
        player2.tick(keys, beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski)



        window.blit(background, (0, 0))  # rysowanie tła

        if clock >= 2:
            clock = 0
            kolejki.append(Cash())

        for banknote in kolejki:
            banknote.tick()

        for banknote in kolejki:
            if player.hitbox.colliderect(banknote.hitbox) or player2.hitbox.colliderect(banknote.hitbox):
                kolejki.remove(banknote)
                wynik += 1
            for beam in beams:
                if beam.hitbox.colliderect(banknote.hitbox):
                    if banknote in kolejki:
                        kolejki.remove(banknote)

            for lawa in przeszkody:
                if lawa.hitbox.colliderect(banknote.hitbox):
                    if banknote in kolejki:
                        kolejki.remove(banknote)
            banknote.draw()



        text = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "WYNIK: " + str(wynik), True, (55, 245, 245))
        window.blit(text, (30, 30))
        text2 = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "CZAS: " + str(round(time,1)), True, (55, 245, 245))
        window.blit(text2, (200, 30))
        title = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "Level: 4 ", True, (55, 245, 245))
        window.blit(title, (1100, 30))
        player.draw()
        player2.draw()

        for beam in beams:
            beam.draw(window)

        for beamG in beams2:
            beamG.draw(window)

        for beamB in beams3:
            beamB.draw(window)

        for lawa in przeszkody:
            if player.hitbox.colliderect(lawa.hitbox) or player2.hitbox.colliderect(lawa.hitbox):
                run = False
                end.lose()
                open(file="end.py")
            lawa.draw(window)

        for b2 in baza2:
            b2.draw(window)

        for b1 in baza1:
            b1.draw(window)



        if player.hitbox.colliderect(b1.hitbox) and player2.hitbox.colliderect(b2.hitbox):
            run = False
            end.end()
            open(file="end.py")

        pygame.display.update()



if __name__ == "__main__":
    main()
