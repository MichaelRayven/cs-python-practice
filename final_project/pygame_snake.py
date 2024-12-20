import pygame
from sys import exit

pygame.init()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
# font = pygame.font.Font("*.ttf", 50)
font = pygame.font.Font(None, 50)

surface = pygame.Surface((200, 400))
# surface.fill('red')
# surface = pygame.image.load("path")
text_surface = font.render("Hey", True, 'green')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(surface, (0,0))
    screen.blit(text_surface, (0,0))

    pygame.display.update()
    clock.tick(60)