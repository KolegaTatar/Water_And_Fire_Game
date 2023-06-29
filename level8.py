import pygame
from parametry import Player, Player2, Beam, g1, g2, Cash, Tep, Us, Meteor, Lawa, Tep2, BeamB, Tep3
import end
from random import randint
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

        Beam(670, 600, 20, 100),
        Beam(100, 580, 800, 20),
        Beam(210, 600, 20, 100),
        Beam(300, 450, 720, 20),
        Beam(1000, 470, 20, 250),


        Beam(250,410,50,40),
        Beam(200, 370, 50, 40),
        Beam(150, 330, 50, 40),
        Beam(100, 290, 50, 40),
        Beam(50, 250, 50, 40),
        Beam(0, 210, 50, 40),

        Beam(1100, 130, 160, 20),

        Beam(200, 200, 40, 15),
        Beam(380, 200, 40, 15),
        Beam(470, 270, 40, 15),
        Beam(650, 270, 40, 15),
        Beam(740, 200, 40, 15),
        Beam(830, 270, 40, 15),
        Beam(1020, 180, 40, 15),
        Beam(940, 240, 40, 15),

        Beam(35, 550, 50, 15),




        # bariery
        Beam(0, 0, 1280, 20),
        Beam(0, 0, 20, 720),
        Beam(1260, 0, 20, 720),
        Beam(0, 700, 1280, 20)
    ]
    # bloki grawitacyjne góra
    beams2 = [
        Beam(1020, 690, 80, 10),

    ]
    # bloki grawitacyjne boki
    beams3 = [
        BeamB(220, 580, 70, 10)

    ]

    przeszkody = [
        Lawa(990, 470, 10, 230),
    ]
    baza1 = [
        g1(690, 695, 60, 5),
    ]
    baza2 = [
        g2(610, 695, 60, 5),
    ]

    tel = [
        Tep(200, 600, 10, 100),
        Tep(230, 600, 10, 100),
        Tep2(20, 100, 5, 100),
        Tep3(1250, 30, 10, 90),

    ]

    pseudo = [
        Us(1020,640,80,20),
        Us(1180, 580, 80, 20),
        Us(1020, 500, 80, 20),

        Us(290, 270, 40, 15),
        Us(560, 200, 40, 15),
        Us(920, 200, 40, 15),
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
        elif clock > 1.9:
            spadanie.append(Meteor())



        for meteor in spadanie:
            meteor.tick(keys, beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski)

        for meteor in spadanie:
            if player.hitbox.colliderect(meteor.hitbox) or player2.hitbox.colliderect(meteor.hitbox):
                run = False
                end.lose()
                open(file="end.py")
            for beam in beams:
                if beam.hitbox.colliderect(meteor.hitbox):
                    if meteor in spadanie:
                        spadanie.remove(meteor)
            for us in pseudo:
                if us.hitbox.colliderect(meteor.hitbox):
                    if meteor in spadanie:
                        spadanie.remove(meteor)
            meteor.draw()

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
        title = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "Level: 8 ", True, (55, 245, 245))
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
            if player.hitbox.colliderect(tep.hitbox):
                player.x = randint(21, 1259)
                player.y = randint(200, 680)
            tep.draw(window)

        for tep2 in tel:
            if player2.hitbox.colliderect(tep2.hitbox):
                player2.x = randint(150, 400)
                player2.y = 500
            tep2.draw(window)

        for tep3 in tel:
            if player2.hitbox.colliderect(tep3.hitbox):
                player2.x = randint(220,400)
                player2.y = 600
            tep3.draw(window)


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


        if player.hitbox.colliderect(b1.hitbox) and player2.hitbox.colliderect(b2.hitbox) and wynik >= 10:
            run = False
            end.end()
            open(file="end.py")





        pygame.display.update()


if __name__ == "__main__":
    main()

