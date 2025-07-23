import pygame

def load_image(path, size=None):
    """Загрузить изображение с опциональным изменением размера."""
    img = pygame.image.load(path)
    if size:
        img = pygame.transform.scale(img, size)
    return img

def load_sound(path, volume=1.0):
    """Загрузить звуковой эффект с заданной громкостью."""
    sound = pygame.mixer.Sound(path)
    sound.set_volume(volume)
    return sound

def load_music(path, volume=1.0):
    """Загрузить и воспроизвести фоновую музыку."""
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)

def draw_scaled_button(surface, image, center_pos, hover=False):
    """Нарисовать кнопку с эффектом наведения."""
    scale = 1.05 if hover else 1.0
    size = (int(image.get_width() * scale), int(image.get_height() * scale))
    img_scaled = pygame.transform.scale(image, size)
    rect = img_scaled.get_rect(center=center_pos)
    surface.blit(img_scaled, rect)
    return rect
