import pygame
import sys
import os
from utils.utils import load_image, play_sound

pygame.init()

# === Основные параметры ===
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ЛАБУБУ: Уровень 1")
clock = pygame.time.Clock()

# === Загрузка ресурсов ===
background = load_image("assets/images/level1_background.png", (WIDTH, HEIGHT))
labubu_img = load_image("assets/images/labubu_idle.png", (50, 50))
coin_img = load_image("assets/images/coin.png", (30, 30))
enemy_img = load_image("assets/images/enemy.png", (50, 50))
door_img = load_image("assets/images/door.png", (60, 80))
font = pygame.font.SysFont("Arial", 28)

# === Музыка ===
pygame.mixer.music.load("assets/audio/level1_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
coin_sound = pygame.mixer.Sound("assets/audio/coin.wav")

# === Игровые объекты ===
player = pygame.Rect(100, 450, 50, 50)
player_vel_y = 0
gravity = 0.8
jump_power = -15
on_ground = False
coins = [pygame.Rect(300, 500, 30, 30), pygame.Rect(500, 400, 30, 30)]
enemies = [pygame.Rect(400, 500, 50, 50)]
door = pygame.Rect(700, 450, 60, 80)
score = 0
lives = 3
level_time = 60  # секунд
start_ticks = pygame.time.get_ticks()

# === Платформы ===
platforms = [
    pygame.Rect(0, 550, 800, 50),
    pygame.Rect(250, 480, 150, 20),
    pygame.Rect(470, 380, 150, 20)
]

# === Пауза ===
paused = False

def draw_game():
    screen.blit(background, (0, 0))
    screen.blit(labubu_img, player)

    for plat in platforms:
        pygame.draw.rect(screen, (160, 82, 45), plat)

    for coin in coins:
        screen.blit(coin_img, coin)

    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    screen.blit(door_img, door)

    timer = max(0, level_time - (pygame.time.get_ticks() - start_ticks) // 1000)
    time_text = font.render(f"Время: {timer}", True, (255, 255, 255))
    score_text = font.render(f"Монеты: {score}", True, (255, 255, 0))
    lives_text = font.render(f"Жизни: {lives}", True, (255, 0, 0))

    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))
    screen.blit(time_text, (10, 70))

def run_level_1():
    global player_vel_y, on_ground, score, lives, paused

    running = True
    while running:
        clock.tick(60)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                if event.key == pygame.K_SPACE and on_ground and not paused:
                    player_vel_y = jump_power

        if paused:
            pause_text = font.render("Пауза", True, (255, 255, 255))
            screen.blit(pause_text, (WIDTH // 2 - 50, HEIGHT // 2))
            pygame.display.flip()
            continue

        # Движение
        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
        player.x += dx

        # Гравитация
        player_vel_y += gravity
        player.y += player_vel_y

        # Проверка на платформы
        on_ground = False
        for plat in platforms:
            if player.colliderect(plat) and player_vel_y >= 0:
                player.bottom = plat.top
                player_vel_y = 0
                on_ground = True

        # Монеты
        for coin in coins[:]:
            if player.colliderect(coin):
                coins.remove(coin)
                score += 1
                play_sound(coin_sound)

        # Враги
        for enemy in enemies:
            if player.colliderect(enemy):
                lives -= 1
                player.x, player.y = 100, 450
                if lives <= 0:
                    pygame.mixer.music.stop()
                    print("Поражение!")
                    return

        # Дверь выхода
        if player.colliderect(door):
            pygame.mixer.music.stop()
            print("Уровень пройден!")
            os.system("python levels/level2.py")
            return

        # Таймер
        time_left = level_time - (pygame.time.get_ticks() - start_ticks) // 1000
        if time_left <= 0:
            pygame.mixer.music.stop()
            print("Время вышло!")
            return

        draw_game()
        pygame.display.flip()

if __name__ == "__main__":
    run_level_1()
