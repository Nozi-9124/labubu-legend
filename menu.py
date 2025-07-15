import pygame
import sys

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Окно
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ЛАБУБУ: Секрет Бу-Бу-Бу")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифт
font = pygame.font.SysFont(None, 48)
title = font.render("ЛАБУБУ: Секрет Бу-Бу-Бу", True, BLACK)

# Загрузка изображения ЛАБУБУ (замени файлом labubu_happy.png)
labubu_img = pygame.image.load("assets/images/labubu_happy.png")
labubu_img = pygame.transform.scale(labubu_img, (200, 200))
labubu_rect = labubu_img.get_rect(center=(400, 300))

# Музыка в меню (замени файлом menu_music.mp3)
pygame.mixer.music.load("assets/audio/menu_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Цикл
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
                print("ЛАБУБУ: Бу-бу-бу!")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
