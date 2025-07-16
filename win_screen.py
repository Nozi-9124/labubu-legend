import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Поражение")
font = pygame.font.SysFont(None, 72)
clock = pygame.time.Clock()

text = font.render("Вы проиграли!", True, (200, 0, 0))
text_rect = text.get_rect(center=(400, 300))

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

