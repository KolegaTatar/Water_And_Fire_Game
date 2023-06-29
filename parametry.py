import pygame
from random import randint
from math import floor
pygame.init()
window = pygame.display.set_mode((1280, 720))



class Physic:
    def __init__(self, x, y, width, height, acc, max_vel):
        self.x = x  # współrzędna x
        self.y = y  # współrzędna y
        self.hor_velocity = 0  # prędkość w poziomie
        self.ver_velocity = 0  # prędkość w pionie
        self.acc = acc  # przyspieszenie
        self.max_vel = max_vel  # maksymalna prędkość
        self.width = width  # szerokość
        self.height = height  # wysokość
        self.previous_x = x
        self.previous_y = y
        self.jumping = False # czy postać skacze
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def physic_tick(self, beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski,):
        self.ver_velocity += 0.9
        self.x += self.hor_velocity
        self.y += self.ver_velocity
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)  # odświeżanie hitboxa
        for beam in beams:
            if beam.hitbox.colliderect(self.hitbox):  # cofanie obiektu do miejsca z poprzedniej klatki
                if self.x + self.width >= beam.x + 1 > self.previous_x + self.width:  # kolizja z prawej
                    self.x = self.previous_x
                    self.hor_velocity = -1
                if self.x <= beam.x + beam.width - 1 < self.previous_x:  # kolizja z lewej
                    self.x = self.previous_x
                    self.hor_velocity = 1
                if self.y + self.height >= beam.y + 1 > self.previous_y:  # kolizja z dołu
                    self.y = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y <= beam.y + beam.width - 1 < self.previous_y:  # kolizja z góry
                    self.y = self.previous_y
                    self.ver_velocity = 0
                self.y = self.previous_y
                self.ver_velocity = 0

        for beamG in beams2:
            if beamG.hitbox.colliderect(self.hitbox):  # cofanie obiektu do miejsca z poprzedniej klatki
                if self.x + self.width >= beamG.x + 1 > self.previous_x + self.width:  # kolizja z prawej
                    self.x = self.previous_x
                    self.hor_velocity = -3
                if self.x <= beamG.x + beamG.width - 1 < self.previous_x:  # kolizja z lewej
                    self.x = self.previous_x
                    self.hor_velocity = 3
                if self.y + self.height >= beamG.y + 1 > self.previous_y:  # kolizja z dołu
                    self.y = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y <= beamG.y + beamG.width - 1 < self.previous_y:  # kolizja z góry
                    self.y = self.previous_y
                    self.ver_velocity = 0
                self.y = self.previous_y
                self.ver_velocity = -22

        for beamB in beams3:
            if beamB.hitbox.colliderect(self.hitbox):  # cofanie obiektu do miejsca z poprzedniej klatki
                if self.x + self.width >= beamB.x + 1 > self.previous_x + self.width:  # kolizja z prawej
                    self.x = self.previous_x
                    self.hor_velocity = -280
                if self.x <= beamB.x + beamB.width - 1 < self.previous_x:  # kolizja z lewej
                    self.x = self.previous_x
                    self.hor_velocity = 30
                if self.y + self.height >= beamB.y + 1 > self.previous_y:  # kolizja z dołu
                    self.y = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y <= beamB.y + beamB.width - 1 < self.previous_y:  # kolizja z góry
                    self.y = self.previous_y
                    self.ver_velocity = 0
                self.y = self.previous_y
                self.ver_velocity = 0

        for Lawa in przeszkody:
            if Lawa.hitbox.colliderect(self.hitbox):  # cofanie obiektu do miejsca z poprzedniej klatki
                if self.x + self.width >= Lawa.x + 1 > self.previous_x + self.width:  # kolizja z prawej
                    self.x = self.previous_x
                    self.hor_velocity = 0
                if self.x <= Lawa.x + Lawa.width - 1 < self.previous_x:  # kolizja z lewej
                    self.x = self.previous_x
                    self.hor_velocity = 0
                if self.y + self.height >= Lawa.y + 1 > self.previous_y:  # kolizja z dołu
                    self.y = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y <= Lawa.y + Lawa.width - 1 < self.previous_y:  # kolizja z góry
                    self.y = self.previous_y
                    self.ver_velocity = 0
                self.y = self.previous_y
                self.ver_velocity = 0


        for g1 in baza1:
            if g1.hitbox.colliderect(self.hitbox):  # cofanie obiektu do miejsca z poprzedniej klatki
                if self.x + self.width >= g1.x + 1 > self.previous_x + self.width:  # kolizja z prawej
                    self.x = self.previous_x
                    self.hor_velocity = 0
                if self.x <= g1.x + g1.width - 1 < self.previous_x:  # kolizja z lewej
                    self.x = self.previous_x
                    self.hor_velocity = 0
                if self.y + self.height >= g1.y + 1 > self.previous_y:  # kolizja z dołu
                    self.y = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y <= g1.y + g1.width - 1 < self.previous_y:  # kolizja z góry
                    self.y = self.previous_y
                    self.ver_velocity = 0
                self.y = self.previous_y
                self.ver_velocity = 0


        for b2 in baza2:
            if b2.hitbox.colliderect(self.hitbox):  # cofanie obiektu do miejsca z poprzedniej klatki
                if self.x + self.width >= b2.x + 1 > self.previous_x + self.width:  # kolizja z prawej
                    self.x = self.previous_x
                    self.hor_velocity = 0
                if self.x <= b2.x + b2.width - 1 < self.previous_x:  # kolizja z lewej
                    self.x = self.previous_x
                    self.hor_velocity = 0
                if self.y + self.height >= b2.y + 1 > self.previous_y:  # kolizja z dołu
                    self.y = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y <= b2.y + b2.width - 1 < self.previous_y:  # kolizja z góry
                    self.y = self.previous_y
                    self.ver_velocity = 0
                self.y = self.previous_y
                self.ver_velocity = 0

        for tep in tel:
            if tep.hitbox.colliderect(self.hitbox):  # cofanie obiektu do miejsca z poprzedniej klatki
                if self.x + self.width >= tep.x + 1 > self.previous_x + self.width:  # kolizja z prawej
                    self.x = self.previous_x
                    self.hor_velocity = 0
                if self.x <= tep.x + tep.width - 1 < self.previous_x:  # kolizja z lewej
                    self.x = self.previous_x
                    self.hor_velocity = 0
                if self.y + self.height >= tep.y + 1 > self.previous_y:  # kolizja z dołu
                    self.y = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y <= tep.y + tep.width - 1 < self.previous_y:  # kolizja z góry
                    self.y = self.previous_y
                    self.ver_velocity = 0
                self.y = self.previous_y
                self.ver_velocity = 0


        for us in pseudo:
            if us.hitbox.colliderect(self.hitbox):  # cofanie obiektu do miejsca z poprzedniej klatki
                if self.x + self.width >= us.x + 1 > self.previous_x + self.width:  # kolizja z prawej
                    self.x = self.previous_x
                    self.hor_velocity = -1
                if self.x <= us.x + us.width - 1 < self.previous_x:  # kolizja z lewej
                    self.x = self.previous_x
                    self.hor_velocity = 1
                if self.y + self.height >= us.y + 1 > self.previous_y:  # kolizja z dołu
                    self.y = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y <= us.y + us.width - 1 < self.previous_y:  # kolizja z góry
                    self.y = self.previous_y
                    self.ver_velocity = 0
                self.y = self.previous_y
                self.ver_velocity = 0

        for Btn in przyciski:
            if Btn.hitbox.colliderect(self.hitbox):  # cofanie obiektu do miejsca z poprzedniej klatki
                if self.x + self.width >= Btn.x + 1 > self.previous_x + self.width:  # kolizja z prawej
                    self.x = self.previous_x
                    self.hor_velocity = -1
                if self.x <= Btn.x + Btn.width - 1 < self.previous_x:  # kolizja z lewej
                    self.x = self.previous_x
                    self.hor_velocity = 1
                if self.y + self.height >= Btn.y + 1 > self.previous_y:  # kolizja z dołu
                    self.y = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y <= Btn.y + Btn.width - 1 < self.previous_y:  # kolizja z góry
                    self.y = self.previous_y
                    self.ver_velocity = 0
                self.y = self.previous_y
                self.ver_velocity = 0

        for tep2 in tel:
            if tep2.hitbox.colliderect(self.hitbox):  # cofanie obiektu do miejsca z poprzedniej klatki
                if self.x + self.width >= tep2.x + 1 > self.previous_x + self.width:  # kolizja z prawej
                    self.x = self.previous_x
                    self.hor_velocity = 0
                if self.x <= tep2.x + tep2.width - 1 < self.previous_x:  # kolizja z lewej
                    self.x = self.previous_x
                    self.hor_velocity = 0
                if self.y + self.height >= tep2.y + 1 > self.previous_y:  # kolizja z dołu
                    self.y = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y <= tep2.y + tep2.width - 1 < self.previous_y:  # kolizja z góry
                    self.y = self.previous_y
                    self.ver_velocity = 0
                self.y = self.previous_y
                self.ver_velocity = 0

        self.previous_x = self.x
        self.previous_y = self.y





class Player(Physic):
    def __init__(self):
        self.kierunek = False  # prawo
        self.image = pygame.image.load("dyro.png")  # wczytuje grafikę
        self.image2 = pygame.transform.flip(pygame.image.load("dyro.png"), True, False)
        self.image3 = pygame.image.load("dyro.jump.png")
        self.image4 = pygame.transform.flip(pygame.image.load("dyro.jump.png"), True, False)
        width = self.image.get_width()  # szerokość
        height = self.image.get_height()  # wysokość
        self.chodzenie_prawa = [pygame.image.load(f"ruch_d/dyro{i}.png") for i in range(1, 7)]
        self.chodzenie_lewa = [pygame.transform.flip(pygame.image.load(f"ruch_d/dyro{i}.png"), True, False) for i in range(1, 7)]
        self.chodzenie_index = 0
        super().__init__(30, 610, width, height, 0.5, 5)

    def tick(self, keys, beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski ):  # wykonuje się raz na powtórzenie pętli
        self.physic_tick(beams, beams2, beams3, przeszkody, baza1, baza2, tel, pseudo, przyciski)
        if keys[pygame.K_a] and self.hor_velocity > self.max_vel * -1:
            self.hor_velocity -= self.acc
            self.kierunek = True
        if keys[pygame.K_d] and self.hor_velocity < self.max_vel:
            self.hor_velocity += self.acc
            self.kierunek = False
        if keys[pygame.K_w] and self.jumping is False:
            self.ver_velocity -= 9.8
            self.jumping = True
            self.jump = True
        if not (keys[pygame.K_d] or keys[pygame.K_a]):
            if self.hor_velocity > 0:
                self.hor_velocity -= self.acc
            elif self.hor_velocity < 0:
                self.hor_velocity += self.acc

    def draw(self):
        if self.jumping and self.kierunek == False:
            window.blit(self.image3, (self.x, self.y))
        elif self.jumping and self.kierunek == True:
            window.blit(self.image4, (self.x, self.y))


        elif self.kierunek == True:
            if self.hor_velocity != 0:
                window.blit(self.chodzenie_lewa[floor(self.chodzenie_index)], (self.x, self.y))
                self.chodzenie_index += 0.5
                if self.chodzenie_index > 5:
                    self.chodzenie_index = 0
            else:
                window.blit(self.image2, (self.x, self.y))

        elif self.kierunek == False:
            if self.hor_velocity != 0:
                window.blit(self.chodzenie_prawa[floor(self.chodzenie_index)], (self.x, self.y))
                self.chodzenie_index += 0.4
                if self.chodzenie_index > 5:
                    self.chodzenie_index = 0
            else:
                window.blit(self.image, (self.x, self.y))



class Player2(Physic):
    def __init__(self):
        self.kierunek = False  # prawo
        self.image = pygame.image.load("p.Sz.png")  # wczytuje grafikę
        self.image2 = pygame.transform.flip(pygame.image.load("p.Sz.png"), True, False)
        self.image3 = pygame.image.load("p.sz.jump.png")
        self.image4 = pygame.transform.flip(pygame.image.load("p.sz.jump.png"), True, False)
        width = self.image.get_width()  # szerokość
        height = self.image.get_height()  # wysokość
        self.chodzenie_prawa = [pygame.image.load(f"ruch_sz/p.sz{i}.png") for i in range(1, 7)]
        self.chodzenie_lewa = [pygame.transform.flip(pygame.image.load(f"ruch_sz/p.sz{i}.png"), True, False) for i in range(1, 7)]
        self.chodzenie_index = 0
        super().__init__(1220, 610, width, height, 0.5, 5)

    def tick(self, keys, beams, beams2, beams3, przeszkody, baza1, baza2, tep, pseudo, przyciski):  # wykonuje się raz na powtórzenie pętli
        self.physic_tick(beams, beams2, beams3, przeszkody, baza1, baza2, tep, pseudo, przyciski)
        if keys[pygame.K_LEFT] and self.hor_velocity > self.max_vel * -1:
            self.hor_velocity -= self.acc
            self.kierunek = True
        if keys[pygame.K_RIGHT] and self.hor_velocity < self.max_vel:
            self.hor_velocity += self.acc
            self.kierunek = False
        if keys[pygame.K_UP] and self.jumping is False:
            self.ver_velocity -= 9.8
            self.jumping = True
        if not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            if self.hor_velocity > 0:
                self.hor_velocity -= self.acc
            elif self.hor_velocity < 0:
                self.hor_velocity += self.acc

    def draw(self):
        if self.jumping and self.kierunek == False:
            window.blit(self.image3, (self.x, self.y))
        elif self.jumping and self.kierunek == True:
            window.blit(self.image4, (self.x, self.y))


        elif self.kierunek == True:
            if self.hor_velocity != 0:
                window.blit(self.chodzenie_lewa[floor(self.chodzenie_index)], (self.x, self.y))
                self.chodzenie_index += 0.4
                if self.chodzenie_index > 5:
                    self.chodzenie_index = 0
            else:
                window.blit(self.image2, (self.x, self.y))

        elif self.kierunek == False:
            if self.hor_velocity != 0:
                window.blit(self.chodzenie_prawa[floor(self.chodzenie_index)], (self.x, self.y))
                self.chodzenie_index += 0.5
                if self.chodzenie_index > 5:
                    self.chodzenie_index = 0
            else:
                window.blit(self.image, (self.x, self.y))



class Cash:
    def __init__(self):
        self.x = randint(30,1250)
        self.y = randint(200,680)
        self.image = pygame.image.load("kolejka.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        window.blit(self.image,(self.x, self.y))


class Beam:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (255, 239, 211), self.hitbox)

class BeamG:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (25, 25, 245), self.hitbox)

class BeamB:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (170, 203, 0), self.hitbox)


class Lawa:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (255, 99, 2), self.hitbox)

class g1:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (37, 176, 141), self.hitbox)

class g2:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (100, 52, 183), self.hitbox)

class Tep:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    def tick(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (245, 25, 183), self.hitbox)

class Tep2:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    def tick(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (25, 235, 183), self.hitbox)

class Tep3:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    def tick(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (240, 200, 80), self.hitbox)


class Us:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (255, 239, 211), self.hitbox)

class Btn:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (200, 23, 21), self.hitbox)

class Meteor(Physic):
    def __init__(self):
        self.x = randint(100, 1000)
        self.y = 25
        self.image = pygame.image.load("meteor.png")
        width = self.image.get_width()
        height = self.image.get_height()
        super().__init__(self.x, self.y, width, height, 0.5, 5)

    def tick(self, keys, beams, beams2, beams3, przeszkody, baza1, baza2, tep, pseudo, przyciski):  # wykonuje się raz na powtórzenie pętli
        self.physic_tick(beams, beams2, beams3, przeszkody, baza1, baza2, tep, pseudo, przyciski)
        if not (keys[pygame.K_d] or keys[pygame.K_a]):
            if self.hor_velocity > 0:
                self.hor_velocity -= self.acc
            elif self.hor_velocity < 0:
                self.hor_velocity += self.acc

    def draw(self):
        window.blit(self.image, (self.x, self.y))

class Grad(Physic):
    def __init__(self):
        self.x = randint(420, 860)
        self.y = 210
        self.image = pygame.image.load("grad.png")
        width = self.image.get_width()
        height = self.image.get_height()
        super().__init__(self.x, self.y, width, height, 0.5, 5)

    def tick(self, keys, beams, beams2, beams3, przeszkody, baza1, baza2, tep, pseudo, przyciski):  # wykonuje się raz na powtórzenie pętli
        self.physic_tick(beams, beams2, beams3, przeszkody, baza1, baza2, tep, pseudo, przyciski)
        if not (keys[pygame.K_d] or keys[pygame.K_a]):
            if self.hor_velocity > 0:
                self.hor_velocity -= self.acc
            elif self.hor_velocity < 0:
                self.hor_velocity += self.acc

    def draw(self):
        window.blit(self.image, (self.x, self.y))

class Trofeum():
    def __init__(self):
        self.x = 612
        self.y = 430
        self.image = pygame.image.load("trofeum.png")
        width = self.image.get_width()
        height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x, self.y, width, height)


    def tick(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x, self.y))




