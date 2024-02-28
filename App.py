#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from Views import Main

class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("细胞自动机")
        self.geometry("754x754")

if __name__ == "__main__":
    app = MyApp()
    Main(app) 
    app.mainloop()