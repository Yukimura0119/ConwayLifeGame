import pygame
import random
import numpy

# �]�w�����Ϊ�l��
pygame.init()
screen = pygame.display.set_mode([1024, 1024])
screen.fill([0, 0, 0])
life = numpy.zeros([64, 64])
clock = pygame.time.Clock()
born = []
dead = []
flag = True
pause = True

# �O�U8�Ӥ�V
direction = [(1, 0), (0, 1), (1, 1), (-1, 0),
             (0, -1), (-1, -1), (-1, 1), (1, -1)]

# �B�z�N�n�_�����ӭM


def process_born():
    for i in born:
        life[i[0]][i[1]] = True
        screen.fill([70, 130, 180], ([i[0]*16, i[1]*16], (16, 16)))
    born.clear()

# �B�z�N�n���`���ӭM


def process_dead():
    for i in dead:
        life[i[0]][i[1]] = False
        screen.fill([0, 0, 0], ([i[0]*16, i[1]*16], (16, 16)))
    dead.clear()

# �q�ܿ��A�M���Ҧ��ӭM


def clear():
    global life
    born.clear()
    dead.clear()
    screen.fill([0, 0, 0])
    life = numpy.zeros([64, 64])


# �}�l���ɭ��H�����ͲӭM
a = [i for i in range(64)]
for i in range(64):
    b = random.sample(a, random.randint(10, 40))
    for j in b:
        born.append([i, j])
process_born()

while flag:
    # 1���s�T��
    clock.tick(3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pause = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            clear()
        # �B�z�ƹ��I���ƥ�
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]//16
            y = event.pos[1]//16
            if life[x][y]:
                dead.append((x, y))
            else:
                born.append((x, y))

    # �Ȱ����ɭԷ|�Q��b�o�Ӱj��
    while pause == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                clear()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]//16
                y = event.pos[1]//16
                if life[x][y]:
                    dead.append((x, y))
                else:
                    born.append((x, y))
        # �B�z�_���Φ��`
        process_born()
        process_dead()
        pygame.display.update()

    # ���Ҧ��ŦX���`�δ_�����󪺲ӭM�A���O��Jdead,born��Ӧ�C
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
    # �B�z�_���Φ��`
    process_born()
    process_dead()
    pygame.display.update()
pygame.quit()
