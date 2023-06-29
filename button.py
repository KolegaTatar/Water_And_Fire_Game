import pygame

SCREEN = pygame.display.set_mode((1280, 720))

class Button():
	def __init__(self, x_pos,y_pos,file_name):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.image = pygame.image.load(f"assets/{file_name}.png")
		self.image_hovering = pygame.image.load(f"assets/{file_name}_hovering.png")
		self.hitbox = pygame.Rect(self.x_pos, self.y_pos, self.image.get_width(), self.image.get_width())

	def tick(self):
		if self.hitbox.collidepoint(pygame.mouse.get_pos()):
			if pygame.mouse.get_pressed()[0]:
				return True

	def draw(self, SCREEN):
		if self.hitbox.collidepoint(pygame.mouse.get_pos()):
			SCREEN.blit(self.image_hovering, (self.x_pos, self.y_pos))
		else:
			SCREEN.blit(self.image, (self.x_pos, self.y_pos))