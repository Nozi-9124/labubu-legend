import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ЛАБУБУ: Меню")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
font = pygame.font.SysFont(None, 60)
small_font = pygame.font.SysFont(None, 32)

# Загрузка изображения
labubu_img = pygame.image.load("assets/images/labubu_happy.png")
labubu_img = pygame.transform.scale(labubu_img, (200, 200))
labubu_rect = labubu_img.get_rect(center=(400, 200))

# Музыка
pygame.mixer.music.load("assets/audio/menu_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Кнопки
play_text = font.render("▶ Начать игру", True, (255, 255, 255))
quit_text = font.render("⏹ Выйти", True, (255, 255, 255))

play_rect = play_text.get_rect(center=(400, 400))
quit_rect = quit_text.get_rect(center=(400, 480))

def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect.inflate(40, 20))
    screen.blit(text, rect)

def show_menu():
    running = True
    while running:
        screen.fill(WHITE)

        # Заголовок
        title = font.render("ЛАБУБУ: Секрет Бу-Бу-Бу", True, (50, 50, 50))
        screen.blit(title, (150, 50))
        screen.blit(labubu_img, labubu_rect)

        # Кнопки
        draw_button(play_text, play_rect, (100, 200, 100))
        draw_button(quit_text, quit_rect, (200, 100, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    os.system("python level1.py")
                    return
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    show_menu()
