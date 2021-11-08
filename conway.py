import pygame
import random
import asyncio
import numpy
from pygame.constants import KEYDOWN

pygame.init()
screen = pygame.display.set_mode([512, 512])
screen.fill([0, 0, 0])
life = numpy.zeros([64, 64])

direction = [(1, 0), (0, 1), (1, 1), (-1, 0),
             (0, -1), (-1, -1), (-1, 1), (1, -1)]
born = []
dead = []
flag = True
pause = True


def process_born():
    for i in born:
        life[i[0]][i[1]] = True
        screen.fill([70, 130, 180], ([i[0]*8, i[1]*8], (8, 8)))
    born.clear()


def process_dead():
    for i in dead:
        life[i[0]][i[1]] = False
        screen.fill([0, 0, 0], ([i[0]*8, i[1]*8], (8, 8)))
    dead.clear()


clock = pygame.time.Clock()

a = [i for i in range(64)]

for i in range(64):
    b = random.sample(a, random.randint(10, 40))
    for j in b:
        born.append([i, j])
process_born()

while flag:
    clock.tick(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pause = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            born.append((event.pos[0]//8, event.pos[1]//8))

    while pause == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                born.append((event.pos[0]//8, event.pos[1]//8))
                process_born()
        pygame.display.update()

    for i in range(64):
        for j in range(64):
            cnt = 0
            for d in direction:
                if life[(i+d[0]+64) % 64][(j+d[1]+64) % 64]:
                    cnt += 1
            if life[i][j]:
                if cnt < 2 or cnt > 3:
                    dead.append((i, j))
            else:
                if cnt == 3:
                    born.append((i, j))
    process_born()
    process_dead()
    pygame.display.update()
pygame.quit()
