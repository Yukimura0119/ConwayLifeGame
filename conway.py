import pygame
import random
import numpy

# Set up screen
factor = 1
pixel = 16//factor
scale = 64*factor
fps = 3
# set up color
BgColor = [0, 0, 0]
CellColor = [70, 130, 180]

# init
ScreenSize = [pixel*scale, pixel*scale]
LifeSize = [scale, scale]
pygame.init()
screen = pygame.display.set_mode(ScreenSize)
screen.fill(BgColor)
life = numpy.zeros([scale, scale])
clock = pygame.time.Clock()
born = []
dead = []
flag = True
pause = True

# 8 direction to cell
direction = [(1, 0), (0, 1), (1, 1), (-1, 0),
             (0, -1), (-1, -1), (-1, 1), (1, -1)]


# process the will-born list
def process_born():
    print(len(born), 'cells born')
    for i in born:
        life[i[0], i[1]] = True
        screen.fill(CellColor, ([i[0]*pixel, i[1]*pixel], [pixel, pixel]))
    born.clear()


# process the will-dead list
def process_dead():
    print(len(dead), 'cells dead\n')
    for i in dead:
        life[i[0], i[1]] = False
        screen.fill(BgColor, ([i[0]*pixel, i[1]*pixel], [pixel, pixel]))
    dead.clear()


# clear all the cells
def clear():
    global life
    born.clear()
    dead.clear()
    screen.fill([0, 0, 0])
    life = numpy.zeros(LifeSize)


# generate a lot of cells when game starts
a = [i for i in range(scale)]
for i in range(scale):
    b = random.sample(a, random.randint(scale//3, scale*2//3))
    for j in b:
        born.append([i, j])
process_born()

while flag:
    # update 3 times in a second
    clock.tick(fps)

    # detect key event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pause = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            clear()

    # when paused, the program would stuck in the while loop
    while pause == True:
        # detect key event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                clear()

        # detect mouse press
        if pygame.mouse.get_pressed()[0]:
            x = pygame.mouse.get_pos()[0]//pixel
            y = pygame.mouse.get_pos()[1]//pixel
            if x >= 0 and x < LifeSize[1] and life[x, y] == 0:
                born.append([x, y])
        if pygame.mouse.get_pressed()[2]:
            x = pygame.mouse.get_pos()[0]//pixel
            y = pygame.mouse.get_pos()[1]//pixel
            if x > 0 and x < LifeSize[1] and life[x, y] == 1:
                dead.append([x, y])

        # procees born and dead
        process_born()
        process_dead()
        pygame.display.update()

    # Find all the cell that would dead or born, and add them to the born and dead list
    for i in range(scale):
        for j in range(scale):
            cnt = 0
            for d in direction:
                if life[(i+d[0]+LifeSize[0]) % LifeSize[0], (j+d[1]+LifeSize[1]) % LifeSize[1]]:
                    cnt += 1
            if life[i, j]:
                if cnt < 2 or cnt > 3:
                    dead.append([i, j])
            else:
                if cnt == 3:
                    born.append([i, j])

    # process born and dead
    process_born()
    process_dead()
    pygame.display.update()

pygame.quit()
