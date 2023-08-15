import tkinter as tk 
from tkinter import *  
import time
import datetime
import random
import numpy as np
from PIL import Image,ImageTk
import tkinter.simpledialog as dialog
import tkinter.messagebox as message


b = np.load("foodname.npy")
list1=list(b)
np.save("foodname.npy", list1)
#  添加菜品
def add_food():
    #弹窗
    string = dialog.askstring("添加的菜品名称~", "请输出需要添加的菜品名称：")
    list1.append(string)
    np.save("foodname.npy", list1)
    print(string)
    Refresh()

def del_food():
    try:
        #弹窗
        string = dialog.askstring("删除的菜品名称~", "请输出需要删除的菜品名称：")
        list1.remove(string)
        np.save("foodname.npy", list1)
        print(string)
        Refresh()
    except:
        message.showinfo(title='提示框', message='菜单里没有此菜哦~')              # 提示信息对话窗

def modify_food():
    try:
        #弹窗
        string1 = dialog.askstring("修改菜品名称~", "请输出需要修改的菜品名称：")
        #弹窗
        string2 = dialog.askstring("修改的菜品名称~", "修改为：")
        k = list1.index(string1)
        list1[k] = string2
        Refresh()
    except:
        message.showinfo(title='提示框', message='查无此菜哦~')

def eat():
    state.delete('0.0', END)
    k = random.randint(0,int(len(list1)-1))
    state.insert(INSERT, f"今天推荐吃：{list1[k]}\n\n")
    state.insert(INSERT, "(如不满意可再点击“开始”)")

window = tk.Tk()

window.title('随机吃啥？')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x



im_root = ImageTk.PhotoImage(Image.open('1.png'))   #打开图片
im_root1 = ImageTk.PhotoImage(Image.open('1.png'))
canvas_root = Canvas(window, width=640, height=360)
canvas_root.create_image(640, 360, image=im_root)   #放置图片
canvas_root.pack()

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='菜品操作', menu=filemenu)
filemenu.add_command(label='添加菜品', command=add_food)
filemenu.add_command(label='删除菜品', command=del_food)
filemenu.add_command(label='修改菜品', command=modify_food)
filemenu.add_separator()    # 添加一条分隔线
filemenu.add_command(label='Exit', command=window.quit) # 用tkinter里面自带的quit()函数
window.config(menu=menubar)


def Refresh():
    var2 = tk.StringVar()
    lb = tk.Listbox(window, listvariable=var2) 
    for item in list1:
        lb.insert('end', item) 
    lb.place(relx=0.05, y=10, relwidth=0.4)


Refresh()

state = Text(window, relief="flat", font=("微软雅黑", 10))
state.place(relx=0.55, y=40, relwidth=0.40, height=60)
state.insert(INSERT, "这里将会告诉您吃啥子")
# state.insert(INSERT, "请点击“开始”按钮。\n")

btn_start = Button(window,
                   text='开始',
                   font=("微软雅黑", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=eat
                   )
btn_start.place(relx=0.55, y=120, relwidth=0.40, height=30)

 
# 创建一个按钮，用于开始连点
btn_start = Button(window,
                   text='刷新',
                   font=("微软雅黑", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=Refresh
                   )
btn_start.place(relx=0.55, y=180, relwidth=0.40, height=30)
 
window.mainloop()