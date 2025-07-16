import pygame
import sys
import os

# === Инициализация ===
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ЛАБУБУ: Уровень 1")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GROUND_Y = 500

# === Шрифт и музыка ===
font = pygame.font.SysFont(None, 36)
pygame.mixer.music.load("assets/audio/level1_music.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

# === Платформы ===
platforms = [
    pygame.Rect(200, 400, 120, 20),
    pygame.Rect(400, 350, 120, 20),
    pygame.Rect(600, 300, 120, 20),
]

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

        self.vel_y += 1
        self.rect.y += self.vel_y
        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform) and self.vel_y > 0 and self.rect.bottom <= platform.bottom:
                self.rect.bottom = platform.top
                self.vel_y = 0
                self.on_ground = True

        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.on_ground = True

# === Враг ===
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, left_bound, right_bound):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((200, 50, 50))
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = 2
        self.left_bound = left_bound
        self.right_bound = right_bound

    def update(self):
        self.rect.x += self.speed
        if self.rect.left <= self.left_bound or self.rect.right >= self.right_bound:
            self.speed *= -1

# === Монета ===
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect(center=(x, y))

def run_level_1():
    player = Player()
    player_group = pygame.sprite.GroupSingle(player)

    # Враги
    enemy1 = Enemy(220, 400, 200, 320)
    enemy2 = Enemy(620, 300, 600, 720)
    enemies = pygame.sprite.Group(enemy1, enemy2)

    # Монеты
    coins = pygame.sprite.Group(
        Coin(250, 370),
        Coin(420, 320),
        Coin(620, 270),
        Coin(750, GROUND_Y - 70),
        Coin(100, GROUND_Y - 70),
    )
    total_coins = len(coins)
    collected = 0

    # Жизни
    lives = 3
    heart_img = pygame.image.load("assets/images/heart.png")
    heart_img = pygame.transform.scale(heart_img, (32, 32))

    # Дверь
    door_rect = pygame.Rect(750, GROUND_Y - 50, 40, 50)

    # Таймер
    level_time = 90
    start_ticks = pygame.time.get_ticks()

    running = True
    while running:
        screen.fill((150, 200, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Таймер
        seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
        time_left = max(0, level_time - seconds_passed)
        if time_left <= 0:
            print("⏰ Время вышло!")
            pygame.mixer.music.stop()
            os.system("python lose_screen.py")
            return

        # Обновление
        player_group.update()
        enemies.update()

        # Сбор монет
        hits = pygame.sprite.spritecollide(player, coins, dokill=True)
        collected += len(hits)

        # Столкновение с врагами
        if pygame.sprite.spritecollide(player, enemies, False):
            lives -= 1
            print(f"💥 Удар! Осталось жизней: {lives}")
            pygame.time.delay(800)
            player.rect.midbottom = (100, GROUND_Y)
            player.vel_y = 0
            if lives <= 0:
                print("💀 Все жизни потеряны.")
                pygame.mixer.music.stop()
                os.system("python lose_screen.py")
                return

        # Победа
        if player.rect.colliderect(door_rect):
            print("🚪 Уровень пройден!")
            pygame.time.delay(1000)
            pygame.mixer.music.stop()
            os.system("python win_screen.py")
            return

        # Отрисовка
        player_group.draw(screen)
        enemies.draw(screen)
        coins.draw(screen)

        pygame.draw.rect(screen, (70, 40, 0), (0, GROUND_Y, 800, 100))  # земля
        for plat in platforms:
            pygame.draw.rect(screen, (100, 80, 50), plat)
        pygame.draw.rect(screen, (0, 200, 0), door_rect)  # дверь

        # UI
        coin_text = font.render(f"Монеты: {collected} / {total_coins}", True, (0, 0, 0))
        screen.blit(coin_text, (20, 20))

        time_text = font.render(f"Время: {time_left}", True, (0, 0, 0))
        screen.blit(time_text, (20, 60))

        for i in range(lives):
            screen.blit(heart_img, (700 + i * 35, 20))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_level_1()
