import pygame
from parametry import Player, Player2, Beam, BeamG, Lawa, g1, g2, Cash, Tep, Us
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
    time = 60
    kolejki = []
    banknote = []
    wynik = 0
    background = pygame.image.load("tlo1.png")
    beams = [
        Beam(20, 680, 200, 20),  # podwyższenie po lewo
        Beam(1090, 680, 200, 20),  # podwyższenie po prawo
        Beam(200, 250, 20, 550),  # belka pionowa po lewo


        Beam(20, 570, 100, 20),

        Beam(300, 380, 1020, 20),

        Beam(220, 550, 40, 20),
        Beam(340, 550, 80, 20),
        Beam(550, 550, 80, 20),
        Beam(750, 550, 80, 20),
        Beam(940, 550, 80, 20),
        Beam(1120, 550, 150, 20),

        Beam(20, 180, 110, 20),
        Beam(1150, 560, 20, 120),






        # bariery
        Beam(0, 0, 1280, 20),
        Beam(0, 0, 20, 720),
        Beam(1260, 0, 20, 720),
        Beam(0, 700, 1280, 20)
    ]
    # bloki grawitacyjne góra
    beams2 = [
        BeamG(220, 540, 40, 10),
        BeamG(1200,370,60,10)



    ]
    # bloki grawitacyjne boki
    beams3 = [


    ]

    przeszkody = [
        Lawa(220, 690, 870, 10),

    ]
    baza1 = [
        g1(20, 170, 60, 10),
    ]
    baza2 = [
        g2(20, 680, 60, 10),
    ]

    tel = [
        Tep(20, 490, 10, 80),

    ]

    pseudo = [
        Us(200, 180, 50, 20),
        Us(300, 180, 50, 20),
        Us(400, 180, 50, 20),
        Us(500, 180, 50, 20),
        Us(600, 180, 50, 20),
        Us(700, 180, 50, 20),
        Us(800, 180, 50, 20),
        Us(900, 180, 50, 20),
        Us(1000, 180, 50, 20),
        Us(1100, 180, 50, 20),
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

        player.tick(keys, beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski)
        player2.tick(keys, beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski)

        window.blit(background, (0, 0))  # rysowanie tła

        if clock >= 2:
            clock = 0
            kolejki.append(Cash())

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
                        print(beam.x,beam.y, beam.width, beam.height)
            banknote.draw()



        text = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "WYNIK: " + str(wynik), True,
                                       (55, 245, 245))
        window.blit(text, (30, 30))
        text2 = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "CZAS: " + str(round(time, 1)),
                                        True, (55, 245, 245))
        window.blit(text2, (200, 30))
        title = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "Level: 7 ", True, (55, 245, 245))
        window.blit(title, (1100, 30))
        player.draw()
        player2.draw()

        for beam in beams:
            beam.draw(window)

        for beamG in beams2:
            beamG.draw(window)

        for beamB in beams3:
            beamB.draw(window)

        for tep in tel:
            if player.hitbox.colliderect(tep.hitbox) or player2.hitbox.colliderect(tep.hitbox):
                player.x = +1180
                player.y = 480
            tep.draw(window)

        if wynik == 3:
            player2.x = +1180
            player2.y = 480

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
            if player.hitbox.colliderect(us.hitbox):
                if not clock == clock -0.1 *clock:
                    pseudo.remove(us)
            us.draw(window)


        if player.hitbox.colliderect(b1.hitbox) and player2.hitbox.colliderect(b2.hitbox):
            run = False
            end.end()
            open(file="end.py")





        pygame.display.update()


if __name__ == "__main__":
    main()

