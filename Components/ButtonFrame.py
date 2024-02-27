from tkinter import *
import functools

class ButtonFrame(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.root = master #定义内部变量root 
        self.creatButtons() 

    def creatButtons(self,  size=29):  # 创建按钮的方法
        length = 600 / size - 1
        self.buttons = []
        def setColor(i, j):  # 颜色转换的功能
            # print(i)
            if self.buttons[i][j]['bg'] == 'black':
                self.buttons[i][j]['bg'] = 'white'
            else:
                self.buttons[i][j]['bg'] = 'black'
        for i in range(size):
            self.buttons.append([])  # 使用数组管理
            for j in range(size):
                self.buttons[i].append(Button(master=self.root, bitmap='gray12', width=length, height=length, bg='white',
                                            command=functools.partial(setColor, i=i, j=j)))
                # 此处内容填入了一个系统自带的位图，便于调节按钮的大小
                # 因为command参数为函数名，无法带参数，故此处借助偏函数，
                self.buttons[i][j].grid(row=i, column=j, )
                # 借助网格布局，布置出细胞网络