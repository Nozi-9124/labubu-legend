import pygame
import sys

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Окно
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ЛАБУБУ: Секрет Бу-Бу-Бу")
clock = pygame.time.Clock()

# Цвет
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Фон и шрифт
font = pygame.font.SysFont(None, 48)
title = font.render("ЛАБУБУ: Секрет Бу-Бу-Бу", True, BLACK)

# Загрузка изображения
labubu_img = pygame.image.load("assets/images/labubu_happy.png")
labubu_img = pygame.transform.scale(labubu_img, (200, 200))
labubu_rect = labubu_img.get_rect(center=(400, 280))

# Загрузка музыки
try:
    pygame.mixer.music.load("assets/audio/menu_music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print("⚠️ Ошибка загрузки музыки:", e)

# Кнопка
def draw_button(text, center):
    button_font = pygame.font.SysFont(None, 36)
    text_render = button_font.render(text, True, WHITE)
    text_rect = text_render.get_rect(center=center)
    pygame.draw.rect(screen, (50, 50, 200), text_rect.inflate(20, 10), border_radius=10)
    screen.blit(text_render, text_rect)
    return text_rect

# Цикл
running = True
while running:
    screen.fill((240, 240, 255))
    screen.blit(title, (150, 100))
    screen.blit(labubu_img, labubu_rect)

    play_button = draw_button("Играть", (400, 500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                print("▶ Переход к первому уровню...")  # здесь позже будет запуск уровня

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

