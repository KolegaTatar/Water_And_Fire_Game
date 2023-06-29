import pygame
from parametry import Player, Player2, Beam, Cash, Btn, Lawa, Us, g1, g2, BeamG, Tep, Tep2, Grad, BeamB
import end
pygame.init()
window = pygame.display.set_mode((1280, 720))


def main():
    run = True
    pause = False
    win = False
    player = Player()
    player2 = Player2()
    clock = 0
    time = 90
    kolejki = []
    spadanie = []
    wynik = 0
    background = pygame.image.load("tlo1.png")
    beams = [

        Beam(20, 580, 300, 20),
        Beam(960, 580, 300, 20),
        Beam(400, 580, 20, 150),
        Beam(860, 580, 20, 150),

        Beam(560, 180, 160, 20),
        Beam(635, 20, 10, 160),
        Beam(130, 320, 20, 180),
        Beam(280, 70, 20, 250),
        Beam(20, 150, 70, 20),
        Beam(180, 160, 20, 10),

        Beam(1100, 460, 160, 20),
        Beam(300, 180, 70, 20),
        Beam(450, 180, 50, 20),

        Beam(1000, 380, 50, 20),
        Beam(900, 300, 50, 20),
        Beam(1000, 220, 50, 20),
        Beam(1100, 130, 160, 20),
        Beam(800, 145, 90, 10),




        # bariery
        Beam(0, 0, 1280, 20),
        Beam(0, 0, 20, 720),
        Beam(1260, 0, 20, 720),
        Beam(0, 700, 1280, 20)
    ]
    # bloki grawitacyjne góra
    beams2 = [
        BeamG(20, 570, 50, 10),
    ]
    # bloki grawitacyjne boki
    beams3 = [
        BeamB(1200, 570, 60, 10),
        BeamB(1200, 120, 60, 10)
    ]

    przeszkody = [
        Lawa(420, 690, 440, 10)

    ]
    baza1 = [
        g1(655, 175, 40, 5),

    ]
    baza2 = [
        g2(585, 175, 40, 5),
    ]

    tel = [
        Tep(130, 300, 150, 20),
        Tep2(20, 60, 5, 70),

    ]

    pseudo = [
        Us(320, 580, 80, 20),
        Us(880, 580, 80, 20),

    ]
    przyciski = [
        Btn(1250, 600, 10, 10),
        Btn(20, 600, 10, 10)
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

        player.tick(keys, beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski)
        player2.tick(keys, beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski)

        window.blit(background, (0, 0))  # rysowanie tła

        if clock >= 2:
            clock = 0
            kolejki.append(Cash())
        if clock > 1:
            spadanie.append(Grad())


        for grad in spadanie:
            grad.tick(keys, beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski)

        for grad in spadanie:
            if player.hitbox.colliderect(grad.hitbox) or player2.hitbox.colliderect(grad.hitbox):
                run = False
                end.lose()
                open(file="end.py")
            for beam in beams:
                if beam.hitbox.colliderect(grad.hitbox):
                    if grad in spadanie:
                        spadanie.remove(grad)
            for us in pseudo:
                if us.hitbox.colliderect(grad.hitbox):
                    if grad in spadanie:
                        spadanie.remove(grad)
            grad.draw()


        for tep in tel:
            for beamB in beams3:
                if player2.hitbox.colliderect(beamB.hitbox):
                    tel.remove(tep)
            tep.draw(window)

        for tep2 in tel:
            if player2.hitbox.colliderect(tep2.hitbox):
                player2.x = 310
                player2.y = 100
            tep2.draw(window)
        for tep3 in tel:
            tep3.draw(window)

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
        title = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "Level: 9 ", True, (55, 245, 245))
        window.blit(title, (1100, 30))
        player.draw()
        player2.draw()

        for beam in beams:
            beam.draw(window)

        for beamG in beams2:
            beamG.draw(window)

        for beamB in beams3:
            beamB.draw(window)

        for btn in przyciski:
            if player2.hitbox.colliderect(btn.hitbox):
                for us in pseudo:
                    pseudo.remove(us)
            btn.draw(window)


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


        if wynik == 2:
            player.x = 1100
            player.y = 300

        if player.hitbox.colliderect(b1.hitbox) and player2.hitbox.colliderect(b2.hitbox):
            run = False
            end.end()
            open(file="end.py")




        pygame.display.update()


if __name__ == "__main__":
    main()
