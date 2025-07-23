import pygame
import sys
import os
from utils.utils import load_image, play_sound

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ЛАБУБУ: Уровень 5")
clock = pygame.time.Clock()

background = load_image("assets/images/level5_background.png", (WIDTH, HEIGHT))
labubu_img = load_image("assets/images/labubu_idle.png", (50, 50))
coin_img = load_image("assets/images/coin.png", (30, 30))
enemy_img = load_image("assets/images/enemy.png", (50, 50))
laser_img = load_image("assets/images/laser_beam.png", (200, 10))
door_img = load_image("assets/images/door.png", (60, 80))
font = pygame.font.SysFont("Arial", 28)

pygame.mixer.music.load("assets/audio/level5_music.mp3")
pygame.mixer.music.play(-1)
coin_sound = pygame.mixer.Sound("assets/audio/coin.wav")

player = pygame.Rect(100, 450, 50, 50)
player_vel_y = 0
gravity = 0.8
jump_power = -15
on_ground = False

coins = [
    pygame.Rect(200, 520, 30, 30),
    pygame.Rect(400, 300, 30, 30),
    pygame.Rect(600, 200, 30, 30)
]

enemies = [pygame.Rect(500, 520, 50, 50)]
door = pygame.Rect(700, 120, 60, 80)

platforms = [
    pygame.Rect(0, 550, 800, 50),
    pygame.Rect(300, 480, 150, 20),
    pygame.Rect(500, 380, 150, 20),
    pygame.Rect(650, 280, 150, 20),
]

# Лазеры появляются каждые 2 секунды на платформе
laser_rect = pygame.Rect(300, 475, 200, 10)
laser_timer = 0
laser_active = False

score = 0
lives = 3
level_time = 45
start_ticks = pygame.time.get_ticks()
paused = False

def draw_game():
    screen.blit(background, (0, 0))
    screen.blit(labubu_img, player)

    for plat in platforms:
        pygame.draw.rect(screen, (139, 69, 19), plat)

    for coin in coins:
        screen.blit(coin_img, coin)

    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    if laser_active:
        screen.blit(laser_img, laser_rect)

    screen.blit(door_img, door)
    timer = max(0, level_time - (pygame.time.get_ticks() - start_ticks) // 1000)
    screen.blit(font.render(f"Время: {timer}", True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(f"Монеты: {score}", True, (255, 255, 0)), (10, 40))
    screen.blit(font.render(f"Жизни: {lives}", True, (255, 0, 0)), (10, 70))

def run_level_5():
    global player_vel_y, on_ground, score, lives, paused, laser_active, laser_timer

    running = True
    while running:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()

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
            screen.blit(font.render("Пауза", True, (255, 255, 255)), (WIDTH // 2 - 50, HEIGHT // 2))
            pygame.display.flip()
            continue

        # Лазеры включаются/выключаются каждые 2 секунды
        if now - laser_timer > 2000:
            laser_active = not laser_active
            laser_timer = now

        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
        player.x += dx

        player_vel_y += gravity
        player.y += player_vel_y

        on_ground = False
        for plat in platforms:
            if player.colliderect(plat) and player_vel_y >= 0:
                player.bottom = plat.top
                player_vel_y = 0
                on_ground = True

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

        if laser_active and player.colliderect(laser_rect):
            lives -= 1
            player.x, player.y = 100, 450
            if lives <= 0:
                pygame.mixer.music.stop()
                print("Проигрыш!")
                return

        if player.colliderect(door):
            pygame.mixer.music.stop()
            print("Уровень 5 пройден!")
            os.system("python levels/level6.py")
            return

        time_left = level_time - (pygame.time.get_ticks() - start_ticks) // 1000
        if time_left <= 0:
            pygame.mixer.music.stop()
            print("Время вышло!")
            return

        draw_game()
        pygame.display.flip()

if __name__ == "__main__":
    run_level_5()
