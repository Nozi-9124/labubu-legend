import pygame
import sys
import os

def pause_menu(screen, clock):
    pygame.mixer.music.set_volume(0.1)  # Приглушаем музыку на паузе

    # Настройки шрифта и текста
    font = pygame.font.SysFont("arial", 48)
    title_font = pygame.font.SysFont("arial", 64)

    paused = True

    # Текст кнопок
    title = title_font.render("⏸ Пауза", True, (255, 255, 255))
    continue_text = font.render("▶ Продолжить", True, (255, 255, 255))
    exit_text = font.render("⏹ Выйти в меню", True, (255, 255, 255))

    # Позиции
    title_rect = title.get_rect(center=(400, 180))
    continue_button = continue_text.get_rect(center=(400, 300))
    exit_button = exit_text.get_rect(center=(400, 380))

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.collidepoint(event.pos):
                    paused = False
                elif exit_button.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    os.system("python menu.py")
                    return

        # Затемнение фона
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(200)
        overlay.fill((30, 30, 30))
        screen.blit(overlay, (0, 0))

        # Кнопки
        pygame.draw.rect(screen, (80, 180, 120), continue_button.inflate(30, 15), border_radius=10)
        pygame.draw.rect(screen, (180, 80, 80), exit_button.inflate(30, 15), border_radius=10)

        # Отображение текста
        screen.blit(title, title_rect)
        screen.blit(continue_text, continue_button)
        screen.blit(exit_text, exit_button)

        pygame.display.flip()
        clock.tick(30)

    pygame.mixer.music.set_volume(0.4)  # Возвращаем громкость
