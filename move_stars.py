from random import randint
from math import pi
from time import sleep
import sys
import pygame

MAX_SPEED = 2
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


class Star:
    def __init__(self, numer=0, screen_width=1200, screen_height=400):
        self.color = (randint(0, 255),
                      randint(0, 255),
                      randint(0, 255))
        self.massa = randint(1, 1000)
        self.radius = int((self.massa / pi) ** 0.5)
        self.num = numer
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = randint(1, screen_width)
        self.y = randint(1, screen_height)
        self.vx = randint(-MAX_SPEED, MAX_SPEED)
        self.vy = randint(-MAX_SPEED, MAX_SPEED)

    def star_acceleration(self, others):
        acceleration_x = 0
        acceleration_y = 0
        k = 10
        for other in others:
            if self != other:
                square_distance = (self.x - other.x)**2 + (self.y - other.y)**2;
                # Max(0.0000001, RKvadrat);
                acceleration = k * other.massa / square_distance;
                acceleration_x += acceleration * (other.x - self.x) / square_distance**0.5;
                acceleration_y += acceleration * (other.y - self.y) / square_distance ** 0.5;
        self.vx += acceleration_x
        self.vy += acceleration_y

    def star_move(self, others):
        self.star_acceleration(others)
        self.x += self.vx
        self.y += self.vy
        if self.x < 0:
            self.vx = abs(self.vx)
        if self.y < 0:
            self.vy = abs(self.vy)
        if self.x > self.screen_width:
            self.vx = -abs(self.vx)
        if self.y > self.screen_height:
            self.vy = -abs(self.vy)

    def __add__(self, other):
        self.massa += other.massa
        self.radius += other.radius
        return self

    def update(self):
        self.color = (randint(0, 255),
                      randint(0, 255),
                      randint(0, 255))
        self.massa = randint(1, 1000)
        self.radius = int((self.massa / pi) ** 0.5)
        self.x = randint(1, self.screen_width)
        self.y = randint(1, self.screen_height)

    def star_paint(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def __str__(self):
        s = '==   ' + str(self.num) + '\r\n'
        s += 'Massa = ' + str(self.massa) + '\r\n' + 'Radius = ' + str(self.radius) + '\r\n'
        return s


stars = [Star(n, SCREEN_WIDTH, SCREEN_HEIGHT) for n in range(30)]


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Движение звезд")
    # Назначение цвета фона.
    bg_color = (0, 0, 0)
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(bg_color)
    # Запуск основного цикла.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # При каждом проходе цикла перерисовывается экран.
        screen.fill(bg_color)
        for star in stars:
            # star.update()
            star.star_move(stars)
            star.star_paint(screen)

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
        # Pause.
        sleep(0.05)


run_game()
