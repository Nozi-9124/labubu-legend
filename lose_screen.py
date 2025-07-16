import pygame
import sys

def lose_screen():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("💀 Вы проиграли")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 72)
    small_font = pygame.font.SysFont(None, 36)

    text = font.render("Вы проиграли 💀", True, (200, 0, 0))
    text_rect = text.get_rect(center=(400, 250))

    hint = small_font.render("Нажмите любую клавишу, чтобы выйти", True, (50, 50, 50))
    hint_rect = hint.get_rect(center=(400, 350))

    # Музыка поражения
    pygame.mixer.music.load("assets/audio/fail.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play()

    running = True
    while running:
        screen.fill((255, 255, 255))
        screen.blit(text, text_rect)
        screen.blit(hint, hint_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(30)
