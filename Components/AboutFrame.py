from tkinter import *
from tkinter.messagebox import *
class AboutFrame(Frame): # 继承Frame类 
    def __init__(self, master=None): 
        Frame.__init__(self, master) 
        self.root = master #定义内部变量root 
        self.createPage() 
        
    def createPage(self): 
        Label(self, text='细胞自动机').grid() 
        Label(self, text='作者：Yang Quan').grid() 

if __name__ == "__main__":
    app = Tk()
    app.geometry("754x754")
    AboutFrame(app).grid()
    app.mainloop()