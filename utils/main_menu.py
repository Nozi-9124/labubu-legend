import pygame
import sys
import os
from utils import load_image, load_sound, load_music, draw_scaled_button

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ЛАБУБУ: Меню")
clock = pygame.time.Clock()

# === Цвета ===
WHITE = (255, 255, 255)

# === Звук клика ===
click_sound = load_sound("assets/audio/click.wav", volume=0.3)

# === Фон и Лабубу ===
background = load_image("assets/images/menu_background.png")
labubu_img = load_image("assets/images/labubu_happy.png", size=(200, 200))
labubu_rect = labubu_img.get_rect(center=(400, 150))

# === Кнопки ===
buttons = {
    "play": "play_button.png",
    "music": "music_button.png",
    "settings": "settings_button.png",
    "shop": "shop_button.png",
    "records": "records_button.png",
    "exit": "exit_button.png"
}

button_images = {}
button_rects = {}
hover_states = {}

# === Позиции кнопок ===
positions = {
    "play": (400, 290),
    "music": (250, 360),
    "settings": (550, 360),
    "shop": (250, 430),
    "records": (550, 430),
    "exit": (400, 500)
}

for key, filename in buttons.items():
    img = load_image(f"assets/images/{filename}", size=(200, 50))
    button_images[key] = img
    hover_states[key] = False
    button_rects[key] = img.get_rect(center=positions[key])

# === Музыка ===
load_music("assets/audio/menu_music.mp3", volume=0.5)

def show_menu():
    running = True
    while running:
        screen.blit(background, (0, 0))
        screen.blit(labubu_img, labubu_rect)

        mouse_pos = pygame.mouse.get_pos()

        # Проверка наведения
        for key in button_rects:
            hover_states[key] = button_rects[key].collidepoint(mouse_pos)

        # Отображение кнопок
        for key in button_images:
            rect = draw_scaled_button(screen, button_images[key], positions[key], hover=hover_states[key])
            button_rects[key] = rect

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for key, rect in button_rects.items():
                    if rect.collidepoint(event.pos):
                        click_sound.play()
                        if key == "play":
                            pygame.mixer.music.stop()
                            os.system("python level1.py")
                            return
                        elif key == "music":
                            print("Музыка: вкл/выкл")
                        elif key == "settings":
                            print("Настройки")
                        elif key == "shop":
                            print("Магазин")
                        elif key == "records":
                            print("Рекорды")
                        elif key == "exit":
                            pygame.quit()
                            sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    show_menu()
