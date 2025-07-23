import pygame
import sys
import os
from utils.utils import load_image, play_sound

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ЛАБУБУ: Уровень 4")
clock = pygame.time.Clock()

# Ресурсы
background = load_image("assets/images/level4_background.png", (WIDTH, HEIGHT))
labubu_img = load_image("assets/images/labubu_idle.png", (50, 50))
coin_img = load_image("assets/images/coin.png", (30, 30))
enemy_img = load_image("assets/images/enemy.png", (50, 50))
door_img = load_image("assets/images/door.png", (60, 80))
font = pygame.font.SysFont("Arial", 28)

# Музыка
pygame.mixer.music.load("assets/audio/level4_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
coin_sound = pygame.mixer.Sound("assets/audio/coin.wav")

player = pygame.Rect(100, 450, 50, 50)
player_vel_y = 0
gravity = 0.8
jump_power = -15
on_ground = False

coins = [
    pygame.Rect(250, 520, 30, 30),
    pygame.Rect(480, 440, 30, 30),
    pygame.Rect(700, 320, 30, 30)
]

enemies = [
    pygame.Rect(350, 520, 50, 50),
    pygame.Rect(580, 520, 50, 50),
    pygame.Rect(650, 260, 50, 50)
]

door = pygame.Rect(730, 240, 60, 80)
score = 0
lives = 3
level_time = 40
start_ticks = pygame.time.get_ticks()

# Платформы
static_platforms = [
    pygame.Rect(0, 550, 800, 50),
    pygame.Rect(300, 480, 150, 20),
    pygame.Rect(500, 380, 150, 20)
]

falling_platforms = [
    {"rect": pygame.Rect(650, 280, 120, 20), "falling": False, "fall_speed": 5}
]

paused = False

def draw_game():
    screen.blit(background, (0, 0))
    screen.blit(labubu_img, player)

    for plat in static_platforms:
        pygame.draw.rect(screen, (139, 69, 19), plat)

    for p in falling_platforms:
        pygame.draw.rect(screen, (165, 42, 42), p["rect"])

    for coin in coins:
        screen.blit(coin_img, coin)

    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    screen.blit(door_img, door)

    timer = max(0, level_time - (pygame.time.get_ticks() - start_ticks) // 1000)
    screen.blit(font.render(f"Время: {timer}", True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(f"Монеты: {score}", True, (255, 255, 0)), (10, 40))
    screen.blit(font.render(f"Жизни: {lives}", True, (255, 0, 0)), (10, 70))

def run_level_4():
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
            screen.blit(font.render("Пауза", True, (255, 255, 255)), (WIDTH//2 - 50, HEIGHT//2))
            pygame.display.flip()
            continue

        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
        player.x += dx

        player_vel_y += gravity
        player.y += player_vel_y

        on_ground = False
        for plat in static_platforms + [p["rect"] for p in falling_platforms]:
            if player.colliderect(plat) and player_vel_y >= 0:
                player.bottom = plat.top
                player_vel_y = 0
                on_ground = True
                # Если это падающая платформа — запускаем падение
                for fp in falling_platforms:
                    if plat == fp["rect"]:
                        fp["falling"] = True

        # Падение платформ
        for fp in falling_platforms:
            if fp["falling"]:
                fp["rect"].y += fp["fall_speed"]

        for coin in coins[:]:
            if player.colliderect(coin):
                coins.remove(coin)
                score += 1
                play_sound(coin_sound)

        for enemy in enemies:
            if player.colliderect(enemy):
                lives -= 1
                player.x, player.y = 100, 450
                if lives <= 0:
                    pygame.mixer.music.stop()
                    print("Проигрыш!")
                    return

        if player.colliderect(door):
            pygame.mixer.music.stop()
            print("Уровень 4 пройден!")
            os.system("python levels/level5.py")
            return

        if level_time - (pygame.time.get_ticks() - start_ticks) // 1000 <= 0:
            pygame.mixer.music.stop()
            print("Время вышло!")
            return

        draw_game()
        pygame.display.flip()

if __name__ == "__main__":
    run_level_4()
