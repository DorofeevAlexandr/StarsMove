from random import randint, uniform
from math import pi
from time import sleep
import sys
import pygame

MAX_SPEED = 0.5
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


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
        self.vx = uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = uniform(-MAX_SPEED, MAX_SPEED)

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
        impulse_x = self.vx * self.massa + other.vx * other.massa
        impulse_y = self.vy * self.massa + other.vy * other.massa
        self.massa += other.massa
        self.radius = int((self.massa / pi) ** 0.5)
        self.vx = impulse_x / self.massa
        self.vy = impulse_y / self.massa
        return self

    def star_collisions(self, others):
        for other in others:
            if self != other:
                if abs(self.x - other.x) < self.radius and abs(self.y - other.y) < self.radius:
                    others.append(self + other)
                    others.remove(self)
                    others.remove(other)
                    print(len(others))


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


def run_game():
    stars = [Star(n, SCREEN_WIDTH, SCREEN_HEIGHT) for n in range(10)]
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Движение звезд")
    # Назначение цвета фона.
    bg_color = (0, 0, 0)

    # Запуск основного цикла.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                sys.exit()

        # При каждом проходе цикла перерисовывается экран.
        screen.fill(bg_color)
        for star in stars:
            # star.update()
            star.star_move(stars)
            star.star_collisions(stars)
            star.star_paint(screen)

        if len(stars) <= 1:
            stars.clear()
            stars = [Star(n, SCREEN_WIDTH, SCREEN_HEIGHT) for n in range(10)]

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
        # Pause.
        sleep(0.02)


run_game()
