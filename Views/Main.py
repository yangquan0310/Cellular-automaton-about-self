#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'细胞自动机'

__author__ = 'Little Huang'

import random
import threading
import functools
from tkinter import *
from Components import ButtonFrame,AboutFrame
from utils import CellLife, lock, loc1,loc2,loc3


class Main:
    def __init__(self,master=None):
        self.root = master #定义内部变量root 
        self.about_frame = AboutFrame(self.root)
        self.button_frame=ButtonFrame(self.root)
        self.buttons=self.button_frame.buttons
        self.creatMenu()  # 创建菜单
        self.cellLife = CellLife(self.buttons)
        dataThread = threading.Thread(target=self.cellLife.cellLife)
        # 由于UI界面，必须需要一个线程循环，因此使用多线程，另开一线程进行计算细胞状态
        dataThread.start()  # 先开启运算线程，由于信号量已经被申请，故不会直接运行而会等待用户按下开始 

    def creatMenu(self):  # 创建菜单栏
        menubar = Menu(self.root)
        # 选项菜单栏
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='选项', menu=filemenu)
        filemenu.add_command(label='开始', command=self.start)
        filemenu.add_command(label='暂停', command=self.pause)
        filemenu.add_command(label='重置', command=self.reseat)
        filemenu.add_command(label='保存', command=self.save)
        filemenu.add_command(label='退出', command=self.quit)
        # 设置菜单栏
        setmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='设置', menu=setmenu)
        # 变化速度菜单
        speedmenu = Menu()
        setmenu.add_cascade(label='变化速度', menu=speedmenu)
        speedmenu.add_command(label='慢', command=functools.partial(self.setSpeed, newspeed=2))
        speedmenu.add_command(label='较慢', command=functools.partial(self.setSpeed, newspeed=1.5))
        speedmenu.add_command(label='中等', command=functools.partial(self.setSpeed, newspeed=1))
        speedmenu.add_command(label='快', command=functools.partial(self.setSpeed, newspeed=0.5))
        speedmenu.add_command(label='极快', command=functools.partial(self.setSpeed, newspeed=0.1))
        # 预设菜单
        imgmenu = Menu()
        setmenu.add_cascade(label='预设图案', menu=imgmenu)
        # 将预设图案添加到二级菜单中
        imgmenu.add_command(label='太空舰队', command=functools.partial(self.setImg, locs=loc1))
        imgmenu.add_command(label='广场舞', command=functools.partial(self.setImg, locs=loc2))
        imgmenu.add_command(label='百变脸谱', command=functools.partial(self.setImg, locs=loc3))
        imgmenu.add_command(label='随机图案', command=self.randImg)
        # 说明菜单栏
        # menubar.add_command(label='说明', command=self.aboutDisp)
        self.root.config(menu=menubar)
    def start(self):  # 开始功能
        try:
            lock.release()
        except:
            pass
    def pause(self):  # 暂停功能
        lock.acquire()
    def reseat(self):  # 重置功能
        lock.acquire()
        for i in self.buttons:
            for j in i:
                j['bg'] = 'white'
    def quit(self):  # 退出功能
        self.cellLife.stop = True
        self.root.quit()
    def save(self):  # 保存功能
        with open('image.txt', 'w') as f:
            for x in range(len(self.buttons)):
                for y in range(len(self.buttons[x])):
                    if self.buttons[x][y]['bg'] == 'black':
                        f.write('[' + str(x) + ',' + str(y) + '],')
    def setSpeed(self,newspeed):  # 调节速度
        self.cellLife.speed = newspeed
    def setImg(self,locs):  # 修改初始图案
        for x in self.buttons:
            for y in x:
                y['bg'] = 'white'
        for l in locs:
            self.buttons[l[0]][l[1]]['bg'] = 'black'
    def randImg(self):  # 随机初始图案
        for x in self.buttons:
            for y in x:
                if random.choice((True, False)):
                    y['bg'] = 'black'
                else:
                    y['bg'] = 'white'
    def aboutDisp(self):
        self.button_frame.grid_forget()
        self.about_frame.grid()

if __name__ == '__main__':
    window = Tk()  # 创建窗口
    Main(window)  # 创建窗口并制定方格数目
    window.mainloop()  # 主窗口函数
    # winThread.run()
