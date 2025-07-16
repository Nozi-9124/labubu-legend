import pygame
import sys
import os
from pause_menu import pause_menu

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ЛАБУБУ: Уровень 2")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GROUND_Y = 500
FPS = 60

# Музыка уровня
pygame.mixer.music.load("assets/audio/level2_music.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

# Игровые ресурсы
heart_img = pygame.image.load("assets/images/heart.png")
heart_img = pygame.transform.scale(heart_img, (32, 32))
coin_img = pygame.Surface((24, 24))
coin_img.fill((255, 223, 0))  # Жёлтая монета

max_lives = 3
lives = max_lives
score = 0
time_left = 120

# Монеты
coin_rects = [pygame.Rect(x, GROUND_Y - 50, 24, 24) for x in (200, 400, 600)]

# Враги
enemy_rects = [pygame.Rect(500, GROUND_Y - 40, 40, 40)]

# Дверь (появляется при сборе всех монет)
door_rect = pygame.Rect(750, GROUND_Y - 60, 30, 60)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spritesheet = pygame.image.load("assets/images/labubu_run.png").convert_alpha()
        self.frames = [self.spritesheet.subsurface(pygame.Rect(i * 64, 0, 64, 64)) for i in range(6)]
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom=(100, GROUND_Y))
        self.vel_y = 0
        self.on_ground = True
        self.anim_timer = 0

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

        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.on_ground = True

def run_level_2():
    global lives, score, time_left
    player = Player()
    player_group = pygame.sprite.GroupSingle(player)

    pygame.time.set_timer(pygame.USEREVENT, 1000)  # каждая секунда

    running = True
    while running:
        screen.fill((120, 180, 255))  # фон

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause_menu(screen, clock)

            elif event.type == pygame.USEREVENT:
                time_left -= 1
                if time_left <= 0:
                    pygame.mixer.music.stop()
                    import lose_screen
                    lose_screen.lose_screen()
                    return

        player_group.update()

        # Столкновение с врагами
        for enemy in enemy_rects:
            if player.rect.colliderect(enemy):
                lives -= 1
                player.rect.topleft = (100, 300)
                if lives <= 0:
                    pygame.mixer.music.stop()
                    import lose_screen
                    lose_screen.lose_screen()
                    return

        # Сбор монет
        for coin in coin_rects[:]:
            if player.rect.colliderect(coin):
                coin_rects.remove(coin)
                score += 1

        # Победа: если все монеты собраны и дошёл до двери
        if not coin_rects and player.rect.colliderect(door_rect):
            pygame.mixer.music.stop()
            import win_screen
            win_screen.win_screen()
            return

        # Отрисовка мира
        pygame.draw.rect(screen, (100, 60, 20), (0, GROUND_Y, 800, 100))  # земля
        for enemy in enemy_rects:
            pygame.draw.rect(screen, (180, 50, 50), enemy)
        for coin in coin_rects:
            screen.blit(coin_img, coin)
        if not coin_rects:
            pygame.draw.rect(screen, (50, 200, 50), door_rect)

        # Отрисовка игрока
        player_group.draw(screen)

        # Жизни
        for i in range(lives):
            screen.blit(heart_img, (10 + i * 36, 10))

        # Таймер
        font = pygame.font.SysFont(None, 36)
        timer_text = font.render(f"⏳ {time_left} сек", True, (0, 0, 0))
        screen.blit(timer_text, (650, 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    run_level_2()
