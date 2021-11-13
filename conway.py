import pygame
import random
import numpy

# 設定視窗及初始化
pygame.init()
screen = pygame.display.set_mode([1024, 1024])
screen.fill([0, 0, 0])
life = numpy.zeros([64, 64])
clock = pygame.time.Clock()
born = []
dead = []
flag = True
pause = True

# 記下8個方向
direction = [(1, 0), (0, 1), (1, 1), (-1, 0),
             (0, -1), (-1, -1), (-1, 1), (1, -1)]

# 處理將要復活的細胞


def process_born():
    for i in born:
        life[i[0]][i[1]] = True
        screen.fill([70, 130, 180], ([i[0]*16, i[1]*16], (16, 16)))
    born.clear()

# 處理將要死亡的細胞


def process_dead():
    for i in dead:
        life[i[0]][i[1]] = False
        screen.fill([0, 0, 0], ([i[0]*16, i[1]*16], (16, 16)))
    dead.clear()

# 默示錄，清除所有細胞


def clear():
    global life
    born.clear()
    dead.clear()
    screen.fill([0, 0, 0])
    life = numpy.zeros([64, 64])


# 開始的時候隨機產生細胞
a = [i for i in range(64)]
for i in range(64):
    b = random.sample(a, random.randint(10, 40))
    for j in b:
        born.append([i, j])
process_born()

while flag:
    # 1秒更新三次
    clock.tick(3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pause = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            clear()
        # 處理滑鼠點擊事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]//16
            y = event.pos[1]//16
            if life[x][y]:
                dead.append((x, y))
            else:
                born.append((x, y))

    # 暫停的時候會被鎖在這個迴圈
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
        # 處理復活及死亡
        process_born()
        process_dead()
        pygame.display.update()

    # 找到所有符合死亡及復活條件的細胞，分別丟入dead,born兩個串列
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
    # 處理復活及死亡
    process_born()
    process_dead()
    pygame.display.update()
pygame.quit()
