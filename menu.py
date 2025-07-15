import pygame
import sys
import os

# Инициализация
pygame.init()
pygame.mixer.init()

# Окно
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ЛАБУБУ: Секрет Бу-Бу-Бу")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифт и заголовок
font = pygame.font.SysFont(None, 48)
title = font.render("ЛАБУБУ: Секрет Бу-Бу-Бу", True, BLACK)

# Загрузка изображения ЛАБУБУ
labubu_img = pygame.image.load("assets/images/labubu_happy.png")
labubu_img = pygame.transform.scale(labubu_img, (200, 200))
labubu_rect = labubu_img.get_rect(center=(400, 300))

# Основной цикл
running = True
while running:
    screen.fill(WHITE)
    screen.blit(title, (150, 100))
    screen.blit(labubu_img, labubu_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if labubu_rect.collidepoint(event.pos):
                print("ЛАБУБУ: Бу-бу-бу!")  # Здесь будет звук

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
