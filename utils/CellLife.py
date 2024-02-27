import random
import threading
import time
import functools
from tkinter import *

# 线程
lock = threading.RLock()  # 借助线程锁机制实现暂停开始功能，防止用户失误多次申请，使用RLock
lock.acquire()

class CellLife():  #演化
    speed = 1
    stop = False
    def __init__(self, buttons):
        self.buttons=buttons
        self.length = len(self.buttons)
        self.data = [[0 for i in range(self.length)] for j in range(self.length)]

    def cellLife(self):
        while True:
            if self.stop:
                return
            lock.acquire()
            self.dieOrLife()
            lock.release()
            time.sleep(self.speed)
    
    def dieOrLife(self):  # 判断每一步细胞生死的功能函数
        life = []
        die = []
        # print('running')
        for i in range(self.length):
            for j in range(self.length):
                if self.buttons[i][j]['bg'] == 'black':
                    self.data[i][j] = 1
                else:
                    self.data[i][j] = 0
        for i in range(self.length):
            for j in range(self.length):
                sum = 0
                for l in range(-1, 2):
                    for m in range(-1, 2):
                        if l + i >= 0 and m + j >= 0 and l + i < self.length and m + j < self.length:
                            sum += self.data[i + l][j + m]
                sum -= self.data[i][j]
                # print(sum)
                if sum == 2 or sum == 3:
                    if sum == 3:  # 繁殖
                        life.append([i, j])
                else:
                    die.append([i, j])#死亡
        if len(life) == 0 and len(die) == 0:
            return
        if len(life) != 0:
            for l in life:
                self.buttons[l[0]][l[1]]['bg'] = 'black'
        if len(die) != 0:
            for d in die:
                self.buttons[d[0]][d[1]]['bg'] = 'white'