import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Победа!")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 200, 100)

# Шрифты
font = pygame.font.SysFont(None, 72)
button_font = pygame.font.SysFont(None, 48)

# Победный текст
victory_text = font.render("🎉 Победа! Ты прошёл игру!", True, GREEN)
victory_rect = victory_text.get_rect(center=(400, 200))

# Кнопки
replay_text = button_font.render("🔁 Сыграть снова", True, WHITE)
exit_text = button_font.render("⏹ Выйти", True, WHITE)

replay_rect = replay_text.get_rect(center=(400, 350))
exit_rect = exit_text.get_rect(center=(400, 430))

def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect.inflate(40, 20), border_radius=15)
    screen.blit(text, rect)

def show_victory():
    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(victory_text, victory_rect)

        draw_button(replay_text, replay_rect, (100, 150, 255))
        draw_button(exit_text, exit_rect, (255, 100, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if replay_rect.collidepoint(event.pos):
                    os.system("python menu.py")  # Запускает игру с начала
                    return
                elif exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    show_victory()
