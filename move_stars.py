from random import randint
from math import pi
from time import sleep
import sys
import pygame


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


a = Star(0)
b = Star(0)
c = a + b
print(a, b, c, sep='')

stars = [Star(n) for n in range(1000)]

print(*stars, sep='')
print(sum(s.massa for s in stars))


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((1200, 400))
    pygame.display.set_caption("Движение звезд")
    # Назначение цвета фона.
    bg_color = (230, 230, 230)
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(bg_color)
    # pygame.draw.circle(screen, (0, 255, 0), (350, 350), 30)
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # При каждом проходе цикла перерисовывается экран.
        screen.fill(bg_color)
        for star in stars:
            star.update()
            star.star_paint(screen)

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
        # Pause.
        sleep(0.5)


run_game()
