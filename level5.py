import pygame
from parametry import Player, Player2, Beam, Cash, Lawa, g1, g2, BeamG, Grad, BeamB
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
    spadanie = []
    wynik = 0
    background = pygame.image.load("tlo1.png")
    beams = [

        Beam(0, 130, 1050, 20),
        Beam(210, 260, 1050, 20),
        Beam(0, 390, 1050, 20),
        Beam(210, 520, 1050, 20),
        
        # bariery
        
        Beam(0, 0, 1280, 20),
        Beam(0, 0, 20, 720),
        Beam(1260, 0, 20, 720),
        Beam(0, 700, 1280, 20)
    ]
    # bloki grawitacyjne góra
    beams2 = [
        BeamG(120, 690, 80, 10),
        BeamG(1050, 250, 80, 10),
        BeamG(120, 380, 80, 10),
        BeamG(1050, 510, 80, 10),
    ]
    # bloki grawitacyjne boki
    beams3 = [
        BeamB(120,200,10,60),
    ]

    przeszkody = [
        Lawa(20, 150, 100, 20),
        Lawa(1180, 20, 80, 20),
        Lawa(20, 410, 100, 20),
        Lawa(1180, 280, 80, 20),

    ]
    baza1 = [
        g1(20, 120, 50, 10),

    ]
    baza2 = [
        g2(70, 120, 50, 10),
    ]

    tel = [

    ]

    pseudo = [

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
        title = pygame.font.Font.render(pygame.font.SysFont("New Times Romana", 30), "Level: 5 ", True, (55, 245, 245))
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



        if player.hitbox.colliderect(b1.hitbox) and player2.hitbox.colliderect(b2.hitbox):
            run = False
            end.end()
            open(file="end.py")




        pygame.display.update()


if __name__ == "__main__":
    main()
