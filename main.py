import pygame
from render import render

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
canvas = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

render(WIDTH, HEIGHT, canvas)

while running:
	mouse_down = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KSCAN_ESCAPE:
			pygame.quit()

	screen.blit(canvas, (0, 0))
	pygame.display.flip()
	clock.tick(60)

pygame.quit()

