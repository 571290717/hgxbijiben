# 导入类库
import time
import threading
import pynput.mouse  # 导入pynput库中的mouse模块，用于控制鼠标
from pynput.keyboard import Key, Listener  # 导入pynput库中的keyboard模块，用于监听键盘事件
from tkinter import *  # 导入tkinter库，用于创建GUI界面
import ctypes
import pyautogui

LEFT = 0  # 定义常量，表示左键的编号为0
RIGHT = 1  # 定义常量，表示右键的编号为1
list1 = []

# 鼠标连点控制类
class MouseClick:
    def __init__(self):
        self.mouse = pynput.mouse.Controller() 
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        

        
    def on_press(self,key):

        if key == Key.esc:
            state.insert(INSERT, "你按下了esc，监听结束\n")
            #   print(f"你按下了esc，监听结束")
            return False
        elif key == Key.f8:
            state.delete('0.0', END)
            state.insert(INSERT, "成功录入：")
            # print("成功录入：")
            state.insert(INSERT, f'当前鼠标位置是：{pyautogui.position()}\n')
            # print(f'当前鼠标位置是：{pyautogui.position()}')
            list1.append(pyautogui.position())
            state.insert(INSERT, f"已成功录入的位置有：\n")
            j=0
            for i in list1:
                j+=1
                state.insert(INSERT, f'{j}:x={i[0]},y={i[1]}\n')

        
        elif key == Key.f9:
            j=0
            for i in list1:
                j+=1
                state2.insert(INSERT, f'执行点击第{j}个位置x={i[0]},y={i[1]}\n')
                # print(f'执行点击第{j}个位置x={i[0]},y={i[1]}')
                pyautogui.click(i[0],i[1],button='left')
                time.sleep(0.5)

    def on_release(self,key):
        return
        # state.insert(INSERT, "成功录入1个鼠标位置")
        # print("成功录入1个鼠标位置")
        # print(f"你松开了{key}键")
        
def new_thread_start():
    MouseClick()

# 开始按键处理函数
def start():
    try:
        state.delete('0.0', END)
        state.insert(INSERT, " 移动鼠标到想录制的位置，按下 F8 录制\n")
        # 开启新线程，避免GUI卡死
        t = threading.Thread(target=new_thread_start)
        # 开启守护线程，这样在GUI意外关闭时线程能正常退出
        t.start()
        # 不能使用 t.join()，# 否则也会卡死
    except:
        state.delete('0.0', END)
        state.insert(INSERT, "出错了\n")
        from tkinter import Tk

# -------------------------------- 以下是GUI界面 --------------------------------
root = Tk()  # 创建Tkinter窗口

root.title('鼠标录入点击器')
root.geometry('500x300')
lab2 = Label(root, text='点击F8开始录入需要点击的鼠标位置', font=("微软雅黑", 11), fg="lightsteelblue")
lab2.place(relx=0.1, y=10, relwidth=0.8, height=30)

# 创建一个文本框，用于显示当前状态和说明
state = Text(root, relief="flat", font=("微软雅黑", 10))
state.place(relx=0.05, y=50, relwidth=0.9, height=80)
state.insert(INSERT, "当前状态：空闲摸鱼中ฅ^•ﻌ•^ฅ\n")
state.insert(INSERT, "请点击“开始”按钮。\n")


# 创建一个文本框，用于显示当前鼠标运行状态
state2 = Text(root, relief="flat", font=("微软雅黑", 10))
state2.place(relx=0.05, y=140, relwidth=0.9, height=60)
state2.insert(INSERT, "这里是鼠标运行状态框\n")

# 创建一个按钮，用于开始连点
btn_start = Button(root,
                   text='开始',
                   font=("微软雅黑", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=start)
btn_start.place(relx=0.3, y=210, relwidth=0.4, height=30)

root.mainloop()  # 进入GUI主循环
# -------------------------------- 以上是GUI界面 --------------------------------