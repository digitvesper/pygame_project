import pygame
import time
import random

# Инициализация Pygame
pygame.init()

# Размер экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Размер блока
BLOCK_SIZE = 20

# Скорость змейки
SNAKE_SPEED = 5

# Шрифт
FONT = pygame.font.SysFont(None, 30)

# Функция для отрисовки змейки
def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, GREEN, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])

# Функция вывода сообщения на экран
def message_to_screen(msg, color):
    screen_text = FONT.render(msg, True, color)
    game_display.blit(screen_text, [SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2])

# Основная функция игры
def game_loop():
    game_exit = False
    game_over = False

    # Начальные координаты змейки
    lead_x = SCREEN_WIDTH / 2
    lead_y = SCREEN_HEIGHT / 2

    # Изменение координат
    lead_x_change = 0
    lead_y_change = 0

    # Координаты фрукта
    rand_apple_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    rand_apple_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    snake_list = []
    snake_length = 1

    while not game_exit:
        while game_over:
            game_display.fill(WHITE)
            message_to_screen("Game Over! Press C to play again or Q to quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0

        # Проверка на выход за границы экрана
        if lead_x >= SCREEN_WIDTH or lead_x < 0 or lead_y >= SCREEN_HEIGHT or lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(BLACK)

        pygame.draw.rect(game_display, RED, [rand_apple_x, rand_apple_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        draw_snake(snake_list)

        pygame.display.update()

        if lead_x == rand_apple_x and lead_y == rand_apple_y:
            rand_apple_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            rand_apple_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Инициализация окна
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Инициализация часов
clock = pygame.time.Clock()

# Запуск игры
game_loop()
