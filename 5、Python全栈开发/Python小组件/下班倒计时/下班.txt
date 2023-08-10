import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter import *  
import time
import datetime


def out_time():
    input_str = input1.get()
    print(input_str)
    time1 = datetime.datetime.now()
    now_day = datetime.date.today()
    time2 = datetime.datetime.strptime(f"{now_day} {input_str}","%Y-%m-%d %H:%M:%S")
    time3 = time2 - time1
    td_without_microseconds = datetime.timedelta(seconds=int(time3.total_seconds()))
    if time2 > time1:
        dstr.set(td_without_microseconds)
    else:
        dstr.set("可以溜溜了~")


# 获取时间的函数
def gettime():
    # 获取当前时间
    # dstr.set(time.strftime("%H:%M:%S"))
    str001.set(f'你好，现在是：{time.strftime("%H:%M:%S")}')
    # 每隔 1s 调用一次 gettime()函数来获取时间
    window.after(1000, gettime)

window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('下班倒计时！！！')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

str001 = tk.StringVar()
# 第4步，在图形界面上设定标签
l001 = tk.Label(window, textvariable=str001, bg='lightsteelblue',fg="#4592FE", font=('Microsoft YaHei UI', 16), width=30, height=2)

l001.pack() 
lab2 = Label(window, text='时间间隔 :', font=("微软雅黑", 11), fg="lightsteelblue")
lab2.place(relx=0.10, y=80, relwidth=0.2, height=30)

# 创建动字符串
Dy_String = tk.StringVar()
input1 = Entry(window,textvariable =Dy_String,fg="#C1DAFE", relief="flat", font=("微软雅黑", 10),validate ="focusin")
input1.insert(0,'17:30:00')
input1.place(relx=0.30, y=80, relwidth=0.4, height=30)

# 创建一个按钮，用于开始连点
btn_start = Button(window,
                   text='告诉我还有多久可以溜溜~',
                   font=("微软雅黑", 12),
                   fg="white",
                   bg="lightsteelblue",
                   relief="flat",
                   command=out_time)
btn_start.place(relx=0.1, y=120, relwidth=0.4, height=30)

# 生成动态字符串
dstr = tk.StringVar()
# 利用 textvariable 来实现文本变化
lb = tk.Label(window,textvariable=dstr,fg='lightsteelblue',font=("微软雅黑",55))
lb.place(relx=0.1, y=160, relwidth=0.8, height=60)
# 调用生成时间的函数
gettime()

# 第6步，主窗口循环显示
window.mainloop()