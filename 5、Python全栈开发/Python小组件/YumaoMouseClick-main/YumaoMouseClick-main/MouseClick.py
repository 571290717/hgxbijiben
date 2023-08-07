# ----------------------------------------------------------
# 免责声明：
# 本代码仅供学习和参考使用，不得用于任何商业用途。
# 作者不对代码的正确性、稳定性或适用性做出任何保证。
# 作者不承担任何因使用本代码而导致的任何直接或间接损失。
# 使用者应该在理解代码的基础上谨慎使用，并自行承担风险。
# 软件名称：鱼猫鼠标连点器
# 软件版本：0.3.0
# 最后编辑时间：2023/5/21
# ----------------------------------------------------------

 # 导入类库
import time
import threading
import pynput.mouse  # 导入pynput库中的mouse模块，用于控制鼠标
from pynput.keyboard import Key, Listener  # 导入pynput库中的keyboard模块，用于监听键盘事件
from tkinter import *  # 导入tkinter库，用于创建GUI界面
import ctypes

LEFT = 0  # 定义常量，表示左键的编号为0
RIGHT = 1  # 定义常量，表示右键的编号为1


# 鼠标连点控制类
class MouseClick:
    def __init__(self, button, time):
        self.mouse = pynput.mouse.Controller()  # 创建鼠标控制器对象
        self.running = False  # 确认是否在运行
        self.time = time  # 连点时间间隔
        self.button = button  # 连点的鼠标按钮
        # 开启主监听线程，监听键盘按键事件
        self.listener = Listener(on_press=self.key_press)
        self.listener.start()

    def key_press(self, key):
        # 键盘按键事件处理函数
        if key == Key.f8:
            if self.running:
                self.running = False
                state.delete('0.0', END)
                state.insert(INSERT, "当前状态：鱼猫工作中，但是并没有开始连续点击ฅ(°ω°ฅ)\n")
                state.insert(INSERT, "按下 Esc 让鱼猫进入摸鱼状态。\n")
                state.insert(INSERT, "按下 F8 开始连续点击。\n")
                # 停止连点也需要调用这个函数
                self.mouse_click()
            else:
                self.running = True
                state.delete('0.0', END)
                state.insert(INSERT, "当前状态：连续点击中◥(ฅº￦ºฅ)◤\n")
                state.insert(INSERT, "不需要按Esc，只需再次按下F8就可以停止连续点击，铲屎官要记住瞄~\n")
                self.mouse_click()
        elif key == Key.esc:
            btn_start['state'] = NORMAL
            state.delete('0.0', END)
            state.insert(INSERT, "当前状态：鱼猫空闲摸鱼中ฅ^•ﻌ•^ฅ\n")
            state.insert(
                INSERT, "选择要连续点击的鼠标按钮并设置时间间隔，之后点击“开始”按钮。")
            # 退出主监听线程
            self.listener.stop()

    def mouse_click(self):
        # 这里还需要额外线程进行监听，为了能够更新self.running，防止陷入死循环
        key_listener = Listener(on_press=self.key_press)
        key_listener.start()
        while self.running:
            self.mouse.click(self.button)  # 模拟鼠标点击
            time.sleep(self.time)  # 间隔一定时间
        key_listener.stop()


# 新线程处理函数
def new_thread_start(button, time):
    MouseClick(button, time)


# 开始按键处理函数
def start():
    try:
        # 将文本框读到的字符串转化为浮点数
        time = float(input.get())
        if mouse.get() == LEFT:
            button = pynput.mouse.Button.left
        elif mouse.get() == RIGHT:
            button = pynput.mouse.Button.right
        btn_start['state'] = DISABLED
        state.delete('0.0', END)
        state.insert(INSERT, "当前状态：鱼猫工作中，但是并没有开始连续点击ฅ(°ω°ฅ)\n")
        state.insert(INSERT, "按下 Esc 让鱼猫进入摸鱼状态。\n")
        state.insert(INSERT, "按下 F8 开始连续点击。\n")
        # 开启新线程，避免GUI卡死
        t = threading.Thread(target=new_thread_start, args=(button, time))
        # 开启守护线程，这样在GUI意外关闭时线程能正常退出
        t.start()
        # 不能使用 t.join()，# 否则也会卡死
    except:
        state.delete('0.0', END)
        state.insert(INSERT, "铲屎官的时间输入格式错误瞄！\n")
        state.insert(INSERT, "铲屎官应该输入整数或小数瞄~")
        from tkinter import Tk


# -------------------------------- 以下是GUI界面 --------------------------------
root = Tk()  # 创建Tkinter窗口对象

# 高dpi设置
ctypes.windll.shcore.SetProcessDpiAwareness(1)  # 设置高dpi
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)  # 获取缩放因子
root.tk.call('tk', 'scaling', ScaleFactor / 75)  # 设置缩放因子

root.title('鱼猫鼠标连点器 V0.3.0')  # 设置窗口标题
root.geometry('500x300')  # 设置窗口大小
root.iconbitmap(r'F:\yumao.ico')  # 设置窗口图标路径
root.resizable(False, False)  # 禁止用户调整窗口大小

mouse = IntVar()  # 创建一个整数变量，用于存储鼠标按钮选择

# 创建一个标签，用于显示“鼠标按钮”文本
lab1 = Label(root, text='鼠标按钮', font=("微软雅黑", 11), fg="green")
lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)

# 创建两个单选按钮，分别用于选择左键和右键
r1 = Radiobutton(root,
                 text='左键',
                 font=("微软雅黑", 10),
                 value=0,
                 variable=mouse)
r1.place(relx=0.05, y=40, relwidth=0.15, height=30)

r2 = Radiobutton(root,
                 text='右键',
                 font=("微软雅黑", 10),
                 value=1,
                 variable=mouse)
r2.place(relx=0.2, y=40, relwidth=0.3, height=30)

# 创建一个标签，用于显示“时间间隔”文本
lab2 = Label(root, text='时间间隔', font=("微软雅黑", 11), fg="red")
lab2.place(relx=0.55, y=10, relwidth=0.4, height=30)

# 创建一个文本框，用于输入时间间隔
input = Entry(root, relief="flat", font=("微软雅黑", 10))
input.place(relx=0.55, y=40, relwidth=0.4, height=30)

# 创建一个标签，用于显示“当前状态和说明”文本
label3 = Label(root,
               text='---------- 当前状态和说明 ----------',
               font=("微软雅黑", 8),
               fg="blue")
label3.place(relx=0.05, y=90, relwidth=0.9, height=20)

# 创建一个文本框，用于显示当前状态和说明
state = Text(root, relief="flat", font=("微软雅黑", 10))
state.place(relx=0.05, y=110, relwidth=0.9, height=120)
state.insert(INSERT, "当前状态：鱼猫空闲摸鱼中ฅ^•ﻌ•^ฅ\n")
state.insert(INSERT, "选择要连点的鼠标按钮并设置时间间隔，之后点击“开始”按钮。\n")

# 创建一个按钮，用于开始连点
btn_start = Button(root,
                   text='开始',
                   font=("微软雅黑", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=start)
btn_start.place(relx=0.3, y=240, relwidth=0.4, height=30)

root.mainloop()  # 进入GUI主循环
# -------------------------------- 以上是GUI界面 --------------------------------
