import pygame
import random
import asyncio
import numpy

pygame.init()
screen = pygame.display.set_mode([512, 512])
screen.fill([0, 0, 0])
life = numpy.zeros([64, 64])

direction = [(1, 0), (0, 1), (1, 1), (-1, 0),
             (0, -1), (-1, -1), (-1, 1), (1, -1)]
born = []
dead = []
flag = True
clock = pygame.time.Clock()
for i in range(150):
    born.append([random.randint(0, 63), random.randint(0, 63)])

while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            life[event.pos[0]//8][event.pos[1]//8] = True
            born.append((event.pos[0]//8, event.pos[1]//8))

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

    for i in born:
        life[i[0]][i[1]] = True
        screen.fill([255, 255, 255], ([i[0]*8, i[1]*8], (8, 8)))
    for i in dead:
        life[i[0]][i[1]] = False
        screen.fill([0, 0, 0], ([i[0]*8, i[1]*8], (8, 8)))
    born = []
    dead = []
    pygame.display.update()
    clock.tick(3)
pygame.quit()
