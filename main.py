import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ЛАБУБУ: Меню")
clock = pygame.time.Clock()

# === Цвета ===
WHITE = (255, 255, 255)
HIGHLIGHT_COLOR = (255, 255, 0)

# === Звук клика ===
click_sound = pygame.mixer.Sound("assets/audio/click.wav")
click_sound.set_volume(0.3)

# === Фон и Лабубу ===
background = pygame.image.load("assets/images/menu_background.png")
labubu_img = pygame.image.load("assets/images/labubu_happy.png")
labubu_img = pygame.transform.scale(labubu_img, (200, 200))
labubu_rect = labubu_img.get_rect(center=(400, 150))

# === Кнопки (изображения) ===
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

for key, filename in buttons.items():
    img = pygame.image.load(f"assets/images/{filename}")
    img = pygame.transform.scale(img, (200, 50))
    button_images[key] = img
    hover_states[key] = False  # по умолчанию не наведено

# === Позиции кнопок ===
positions = {
    "play": (400, 290),
    "music": (250, 360),
    "settings": (550, 360),
    "shop": (250, 430),
    "records": (550, 430),
    "exit": (400, 500)
}

for key in buttons:
    button_rects[key] = button_images[key].get_rect(center=positions[key])

# === Музыка ===
pygame.mixer.music.load("assets/audio/menu_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# === Рисовать кнопку с эффектом наведения и нажатия ===
def draw_button(key):
    img = button_images[key]
    rect = button_rects[key]
    scale_factor = 1.05 if hover_states[key] else 1.0
    if scale_factor != 1.0:
        img = pygame.transform.scale(img, (int(200 * scale_factor), int(50 * scale_factor)))
        rect = img.get_rect(center=positions[key])
    screen.blit(img, rect)
    button_rects[key] = rect

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
            draw_button(key)

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
