import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Настройки")
clock = pygame.time.Clock()

# === Цвета и шрифты ===
WHITE = (255, 255, 255)
BG_COLOR = (30, 30, 60)
font = pygame.font.SysFont(None, 60)
small_font = pygame.font.SysFont(None, 36)

# === Звук клика (если есть файл) ===
try:
    click_sound = pygame.mixer.Sound("assets/audio/click.wav")
except:
    click_sound = None

# === Кнопка "Назад" ===
back_text = small_font.render("← Назад в меню", True, WHITE)
back_rect = back_text.get_rect(center=(400, 500))


def show_settings():
    running = True
    while running:
        screen.fill(BG_COLOR)

        title = font.render("Настройки", True, WHITE)
        screen.blit(title, (280, 100))

        pygame.draw.rect(screen, (60, 60, 120), back_rect.inflate(30, 15), border_radius=12)
        screen.blit(back_text, back_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    if click_sound:
                        click_sound.play()
                    running = False

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    show_settings()
