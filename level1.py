import pygame
import sys

# === Цвета ===
WHITE = (255, 255, 255)
GROUND_Y = 500

# === Игрок ===
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spritesheet = pygame.image.load("assets/images/labubu_run.png").convert_alpha()
        self.frames = self.load_frames()
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom=(100, GROUND_Y))
        self.vel_y = 0
        self.on_ground = True
        self.anim_timer = 0

    def load_frames(self):
        frame_width = 64
        return [self.spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, 64)) for i in range(6)]

    def update(self):
        self.anim_timer += 0.15
        if self.anim_timer >= 1:
            self.anim_timer = 0
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -15
            self.on_ground = False

        self.vel_y += 1  # гравитация
        self.rect.y += self.vel_y

        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.on_ground = True

# === Главная функция уровня ===
def run_level_1():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("ЛАБУБУ: Уровень 1")
    clock = pygame.time.Clock()

    # Музыка
    pygame.mixer.music.load("assets/audio/level1_music.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    player = Player()
    player_group = pygame.sprite.GroupSingle(player)

    running = True
    while running:
        screen.fill((150, 200, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player_group.update()
        player_group.draw(screen)

        pygame.draw.rect(screen, (70, 40, 0), (0, GROUND_Y, 800, 100))  # земля

        pygame.display.flip()
        clock.tick(60)

# === Запуск при прямом запуске файла ===
if __name__ == "__main__":
    run_level_1()

