import pygame
from parametry import Player, Player2, Beam, Cash, Lawa, Us, g1, g2, BeamG, Tep, Trofeum, BeamB

import end

pygame.init()
window = pygame.display.set_mode((1280, 720))




def main():
    run = True
    pause = False
    win = False
    nagroda = False
    player = Player()
    player2 = Player2()
    trof = Trofeum()
    clock = 0
    time = 90
    kolejki = []
    spadanie = []
    wynik = 0
    background = pygame.image.load("tlo1.png")
    beams = [

        Beam(20, 130, 100, 20),
        Beam(1160, 130, 100, 20),

        Beam(20, 590, 200, 20),
        Beam(1060, 590, 200, 20),


        Beam(515, 140, 20, 560),
        Beam(745, 140, 20, 560),

        Beam(610, 500, 60, 20),

        Beam(1010, 300, 60, 20),
        Beam(210, 300, 60, 20),
        Beam(210, 300, 60, 20),

        Beam(360, 350, 60, 20),
        Beam(860, 350, 60, 20),


        Beam(900, 630, 60, 20),
        Beam(320, 630, 60, 20),
        Beam(820, 200, 60, 20),
        Beam(1150, 550, 5, 5),
        Beam(120, 550, 5, 5),

        Beam(20, 410, 500, 20),
        Beam(765, 410, 500, 20),



        # bariery
        Beam(0, 0, 1280, 20),
        Beam(0, 0, 20, 720),
        Beam(1260, 0, 20, 720),
        Beam(0, 700, 1280, 20)
    ]
    # bloki grawitacyjne góra
    beams2 = [
        BeamG(1010, 295, 60, 5),
        BeamG(210, 295, 60, 5),
        BeamG(610, 495, 60, 5),
    ]
    # bloki grawitacyjne boki
    beams3 = [
        BeamB(515, 120, 250, 20),
    ]

    przeszkody = [
        Lawa(50, 590, 120, 10),
        Lawa(1110, 590, 120, 10),
        Lawa(535, 685, 210, 15)

    ]
    baza1 = [
        g1(1200, 125, 60, 5),

    ]
    baza2 = [
        g2(20, 125, 60, 5),
    ]

    tel = [
        Tep(20, 490, 10, 80),
        Tep(1250, 490, 10, 80)

    ]

    pseudo = [
        Us(200, 610, 20, 90),
        Us(1060, 610, 20, 90),

    ]
    przyciski = [

    ]


    while run:
        clock += pygame.time.Clock().tick(60) / 1000 # maksymalnie 60 fps
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

        if nagroda == True:
            text = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "Zebrano Trofeum ZSK", True,
                                          (245, 245, 245))
            window.blit(text, (530, 30))
            pygame.display.update()

        player.tick(keys, beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski)
        player2.tick(keys, beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski)

        window.blit(background, (0, 0))  # rysowanie tła

        if clock >= 2:
            clock = 0
            kolejki.append(Cash())




        for tep in tel:
            if player2.hitbox.colliderect(tep.hitbox):
                player2.x = 40
                player2.y = 180
            if player.hitbox.colliderect(tep.hitbox):
                player.x = 1200
                player.y = 180
            tep.draw(window)


        for banknote in kolejki:
            banknote.tick()

        for beam in beams:
            beam.tick()

        for banknote in kolejki:
            if player.hitbox.colliderect(banknote.hitbox) or player2.hitbox.colliderect(banknote.hitbox):
                kolejki.remove(banknote)
                wynik += 1
            for beam in beams:
                if beam.hitbox.colliderect(banknote.hitbox):
                    if banknote in kolejki:
                        kolejki.remove(banknote)
            banknote.draw()

        text = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "WYNIK: " + str(wynik), True,
                                       (55, 245, 245))
        window.blit(text, (30, 30))
        text2 = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "CZAS: " + str(round(time, 1)),
                                        True, (55, 245, 245))
        window.blit(text2, (200, 30))
        title = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "Level: 10 ", True, (55, 245, 245))
        window.blit(title, (1100, 30))
        player.draw()
        player2.draw()
        trof.draw()




        for beam in beams:
            beam.draw(window)

        for beamG in beams2:
            beamG.draw(window)

        for beamB in beams3:
            beamB.draw(window)

        for beamB in beams3:
            if time < 35:
                beams3.remove(beamB)


        for us in pseudo:
            if time < 75:
                pseudo.remove(us)

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

        for us in pseudo:
            us.draw(window)

        if player.hitbox.colliderect(trof.hitbox):
            nagroda = True

        if player.hitbox.colliderect(b1.hitbox) and player2.hitbox.colliderect(b2.hitbox) and nagroda == True:
            run = False
            end.end()
            open(file="end.py")

        pygame.display.update()


if __name__ == "__main__":
    main()




