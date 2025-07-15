import pygame
import sys
from level1 import run_level_1  # ← добавь в начало

# ...

elif event.type == pygame.MOUSEBUTTONDOWN:
    if button_rect.collidepoint(event.pos):
        print("Переход на уровень 1 🚀")
        pygame.mixer.music.stop()  # выключаем музыку меню
        run_level_1()

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Экран
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ЛАБУБУ: Меню")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифт
font = pygame.font.SysFont(None, 48)

# Заголовок
title = font.render("ЛАБУБУ: Секрет Бу-Бу-Бу", True, BLACK)

# Кнопка
button_text = font.render("▶ Играть", True, (255, 255, 255))
button_rect = button_text.get_rect(center=(400, 450))

# Загрузка изображения
labubu_img = pygame.image.load("assets/images/labubu_happy.png")
labubu_img = pygame.transform.scale(labubu_img, (200, 200))
labubu_rect = labubu_img.get_rect(center=(400, 250))

# Музыка
pygame.mixer.music.load("assets/audio/menu_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Игровой цикл
running = True
while running:
    screen.fill(WHITE)
    screen.blit(title, (150, 100))
    screen.blit(labubu_img, labubu_rect)
    pygame.draw.rect(screen, (100, 100, 250), button_rect.inflate(20, 10))
    screen.blit(button_text, button_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Переход на уровень 1 🚀")
                # Здесь позже будет переход на level1
                # import level1; level1.run_level_1()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

