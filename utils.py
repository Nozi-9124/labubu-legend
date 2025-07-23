# utils.py
import pygame
import os

def load_image(path, colorkey=None):
    """Загрузка изображения из assets/images."""
    full_path = os.path.join("assets", "images", path)
    image = pygame.image.load(full_path).convert_alpha()
    if colorkey is not None:
        image.set_colorkey(colorkey)
    return image

def load_music(filename):
    """Воспроизведение фона — из папки assets/audio."""
    path = os.path.join("assets", "audio", filename)
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)  # бесконечный цикл

def load_sound(filename):
    """Однократный звуковой эффект."""
    path = os.path.join("assets", "audio", filename)
    return pygame.mixer.Sound(path)

def draw_text(screen, text, size, pos, color=(255, 255, 255)):
    """Вывод текста на экран."""
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect(center=pos)
    screen.blit(text_surface, rect)

def animate_sprite(sprite_sheet, frame_width, frame_height, frame_count):
    """Разрезание спрайт-листа на кадры."""
    frames = []
    for i in range(frame_count):
        frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frames.append(frame)
    return frames
