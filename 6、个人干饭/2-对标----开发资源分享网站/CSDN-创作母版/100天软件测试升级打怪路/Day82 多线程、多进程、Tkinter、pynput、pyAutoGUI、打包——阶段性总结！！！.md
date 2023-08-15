# Day82 多线程、多进程、Tkinter、pynput、pyAutoGUI、打包——阶段性总结！！！



# 多进程

多任务是指在**同一时间内**执行**多个任务**

进程，**它是操作系统进行资源分配的基本单位**

````
#导入进程包
import multiprocessing


**Process([group [, target [, name [, args [, kwargs]]]]])**

- group：指定进程组，目前只能使用None
- target：执行的目标任务名
- name：进程名字
- args：以元组方式给执行任务传参
- kwargs：以字典方式给执行任务传参

**Process创建的实例对象的常用方法:**

- start()：启动子进程实例（创建子进程）
- join()：等待子进程执行结束
- terminate()：不管任务是否完成，立即终止子进程

**Process创建的实例对象的常用属性:**

name：当前进程的别名，默认为Process-N，N为从1开始递增的整数


### 3. 多进程完成多任务的代码

```py
import multiprocessing
import time


# 跳舞任务
def dance():
    for i in range(5):
        print("跳舞中...")
        time.sleep(0.2)


# 唱歌任务
def sing():
    for i in range(5):
        print("唱歌中...")
        time.sleep(0.2)

if __name__ == '__main__':
    # 创建跳舞的子进程
    # group: 表示进程组，目前只能使用None
    # target: 表示执行的目标任务名(函数名、方法名)
    # name: 进程名称, 默认是Process-1, .....
    dance_process = multiprocessing.Process(target=dance, name="myprocess1")
    sing_process = multiprocessing.Process(target=sing)

    # 启动子进程执行对应的任务
    dance_process.start()
    sing_process.start()
```

**执行结果:**

```py
唱歌中...
跳舞中...
唱歌中...
跳舞中...
唱歌中...
跳舞中...
唱歌中...
跳舞中...
唱歌中...
跳舞中...
```

### 


牢记简单使用：

1. 导入进程包
   - import multiprocessing
2. 创建子进程并指定执行的任务
   - sub_process = multiprocessing.Process (target=任务名)
3. 启动进程执行任务
   - sub_process.start()




````

> 牢记简单使用：
>
> 1. 导入进程包
>    - import multiprocessing
> 2. 创建子进程并指定执行的任务
>    - sub_process = multiprocessing.Process (target=任务名)
> 3. 启动进程执行任务
>    - sub_process.start()





**获取进程编号的目的是验证主进程和子进程的关系，可以得知子进程是由那个主进程创建出来的。**

```
import os
**os.getpid()** 表示获取当前进程编号
**os.getppid()** 表示获取当前父进程编号


import multiprocessing
    # 获取当前进程
print("main:", multiprocessing.current_process())
```



1个进程可以拥有多个线程，进程间不共享全局变量

so：我们写的时候，需要共享全局变量会用多线程

进程=火车，线程=车厢



# 多线程



````
### 1. 导入线程模块

```py
#导入线程模块
import threading
```

### 2. 线程类Thread参数说明

Thread([group [, target [, name [, args [, kwargs]]]]])

- group: 线程组，目前只能使用None
- target: 执行的目标任务名
- args: 以元组的方式给执行任务传参
- kwargs: 以字典方式给执行任务传参
- name: 线程名，一般不用设置

### 3. 启动线程

启动线程使用start方法

### 4. 多线程完成多任务的代码

```py
import threading
import time

# 唱歌任务
def sing():
    # 扩展： 获取当前线程
    # print("sing当前执行的线程为：", threading.current_thread())
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)

# 跳舞任务
def dance():
    # 扩展： 获取当前线程
    # print("dance当前执行的线程为：", threading.current_thread())
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)


if __name__ == '__main__':
    # 扩展： 获取当前线程
    # print("当前执行的线程为：", threading.current_thread())
    # 创建唱歌的线程
    # target： 线程执行的函数名
    sing_thread = threading.Thread(target=sing)

    # 创建跳舞的线程
    dance_thread = threading.Thread(target=dance)

    # 开启线程
    sing_thread.start()
    dance_thread.start()
```

**执行结果:**

```py
正在唱歌...0
正在跳舞...0
正在唱歌...1
正在跳舞...1
正在唱歌...2
正在跳舞...2
```

### 

### 5. 小结

1. 导入线程模块
   - import threading
2. 创建子线程并指定执行的任务
   - sub_thread = threading.Thread(target=任务名)
3. 启动线程执行任务
   - sub_thread.start()
````

> 1. 导入线程模块
>    - import threading
> 2. 创建子线程并指定执行的任务
>    - sub_thread = threading.Thread(target=任务名)
> 3. 启动线程执行任务
>    - sub_thread.start()



# Tkinter

　Tkinter 是使用 python 进行窗口视窗设计的模块

```python
Tkinter支持16个核心的窗口部件

**Button：**一个简单的按钮，用来执行一个命令或别的操作。

**Canvas：**组织图形。这个部件可以用来绘制图表和图，创建图形编辑器，实现定制窗口部件。

**Checkbutton：**代表一个变量，它有两个不同的值。点击这个按钮将会在这两个值间切换。

**Entry：**文本输入域。

**Frame：**一个容器窗口部件。帧可以有边框和背景，当创建一个应用程序或dialog(对话）版面时，帧被用来组织其它的窗口部件。

**Label：**显示一个文本或图象。

**Listbox：**显示供选方案的一个列表。listbox能够被配置来得到radiobutton或checklist的行为。

**Menu：**菜单条。用来实现下拉和弹出式菜单。

**Menubutton：**菜单按钮。用来实现下拉式菜单。

**Message：**显示一文本。类似label窗口部件，但是能够自动地调整文本到给定的宽度或比率。

**Radiobutton：**代表一个变量，它可以有多个值中的一个。点击它将为这个变量设置值，并且清除与这同一变量相关的其它radiobutton。

**Scale：**允许你通过滑块来设置一数字值。

**Scrollbar：**为配合使用canvas, entry, listbox, and text窗口部件的标准滚动条。

**Text：**格式化文本显示。允许你用不同的样式和属性来显示和编辑文本。同时支持内嵌图象和窗口。

**Toplevel：**一个容器窗口部件，作为一个单独的、最上面的窗口显示。

**messageBox**：消息框，用于显示你应用程序的消息框。(Python2中为tkMessagebox)




import tkinter as tk  # 使用Tkinter前需要先导入
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
 
 
 
 # 创建一个标签，用于显示“鼠标按钮”文本
lab1 = Label(window, text='鼠标按钮', font=("微软雅黑", 11), fg="green")
lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
 
 
# 第4步，在图形界面上设定标签
l = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
 
# 第5步，放置标签
l.pack()    # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();
 
 
 
 
 # 第4步，在图形界面上设定标签
var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.pack()
 
# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')
 
# 第5步，在窗口界面设置放置Button按键
b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()

#3. Entry窗口部件

# 第4步，在图形界面上设定输入框控件entry并放置控件
e1 = tk.Entry(window, show='*', font=('Arial', 14))   # 显示成密文形式
e2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
e1.pack()
e2.pack()

 
# Text窗口部件
 
 # 第4步，在图形界面上设定输入框控件entry框并放置
e = tk.Entry(window, show = None)#显示成明文形式
e.pack()
 
# 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def insert_point(): # 在鼠标焦点处插入输入内容
    var = e.get()
    t.insert('insert', var)
def insert_end():   # 在文本框内容最后接着插入输入内容
    var = e.get()
    t.insert('end', var)
 
# 第6步，创建并放置两个按钮分别触发两种情况
b1 = tk.Button(window, text='insert point', width=10,
               height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=10,
               height=2, command=insert_end)
b2.pack()
 
# 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
t = tk.Text(window, height=3)
t.pack()
 
 
 
 state = Text(root, relief="flat", font=("微软雅黑", 10))
state.place(relx=0.05, y=110, relwidth=0.9, height=120)
 state.insert(INSERT, "当前状态：鱼猫空闲摸鱼中ฅ^•ﻌ•^ฅ\n")
 state.delete('0.0', END)
 
# Listbox窗口部件
 
 
 
 # 第4步，在图形界面上创建一个标签label用以显示并放置
var1 = tk.StringVar()  # 创建变量，用var1用来接收鼠标点击具体选项的内容
l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var1)
l.pack()
 
# 第6步，创建一个方法用于按钮的点击事件
def print_selection():
    value = lb.get(lb.curselection())   # 获取当前选中的文本
    var1.set(value)  # 为label设置值
 
# 第5步，创建一个按钮并放置，点击按钮调用print_selection函数
b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()
 
# 第7步，创建Listbox并为其添加内容
var2 = tk.StringVar()
var2.set((1,2,3,4)) # 为变量var2设置值
# 创建Listbox
lb = tk.Listbox(window, listvariable=var2)  #将var2的值赋给Listbox
# 创建一个list并将值循环添加到Listbox控件中
list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end', item)  # 从最后一个位置开始加入值
lb.insert(1, 'first')       # 在第一个位置加入'first'字符
lb.insert(2, 'second')      # 在第二个位置加入'second'字符
lb.delete(2)                # 删除第二个位置的字符
lb.pack()
 
 
 
# **Radiobutton：**代表一个变量，它可以有多个值中的一个。点击它将为这个变量设置值，并且清除与这同一变量相关的其它radiobutton。
 # 第4步，在图形界面上创建一个标签label用以显示并放置
var = tk.StringVar()    # 定义一个var用来将radiobutton的值和Label的值联系在一起.
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()
 
# 第6步，定义选项触发函数功能
def print_selection():
    l.config(text='you have selected ' + var.get())
 
# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
r3.pack()
 
 
 
 
 
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

#Checkbutton  勾选框

#　　**Checkbutton：**代表一个变量，它有两个不同的值。点击这个按钮将会在这两个值间切换，选择和取消选择。


# 第4步，在图形界面上创建一个标签label用以显示并放置
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()
 
# 第6步，定义触发函数功能
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):     # 如果选中第一个选项，未选中第二个选项
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):   # 如果选中第二个选项，未选中第一个选项
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):   # 如果两个选项都未选中
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')             # 如果两个选项都选中
 
# 第5步，定义两个Checkbutton选项并放置
var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)    # 传值原理类似于radiobutton部件
c1.pack()
c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()


 #Scale窗口滑动条
 　#**Scale： 尺度（拉动条），**允许你通过滑块来设置一数字值。
 
 # 第4步，在图形界面上创建一个标签label用以显示并放置
l = tk.Label(window, bg='green', fg='white', width=20, text='empty')
l.pack()
 
# 第6步，定义一个触发函数功能
def print_selection(v):
    l.config(text='you have selected ' + v)<br>
# 第5步，创建一个尺度滑条，长度200字符，从0开始10结束，以2为刻度，精度为0.01，触发调用print_selection函数
s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
s.pack()
 
       #  Canvas窗口部件
  #**Canvas：画布，**提供绘图功能(直线、椭圆、多边形、矩形) 可以包含图形或位图，用来绘制图表和图，创建图形编辑器，实现定制窗口部件。                                            
                                              
                                              
         # 第4步，在图形界面上创建 500 * 200 大小的画布并放置各种元素
canvas = tk.Canvas(window, bg='green', height=200, width=500)
# 说明图片位置，并导入图片到画布上
image_file = tk.PhotoImage(file='pic.gif')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
image = canvas.create_image(250, 0, anchor='n',image=image_file)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
# 定义多边形参数，然后在画布上画出指定图形
x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)                   # 画直线
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')  # 画圆 用黄色填充
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)      # 画扇形 从0度打开收到180度结束
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)                  # 画矩形正方形
canvas.pack()
 
# 第6步，触发函数，用来一定指定图形
def moveit():
    canvas.move(rect, 2, 2) # 移动正方形rect（也可以改成其他图形名字用以移动一起图形、元素），按每次（x=2, y=2）步长进行移动
 
# 第5步，定义一个按钮用来移动指定图形的在画布上的位置
b = tk.Button(window, text='move item',command=moveit).pack()                                     
                                              
                                              
 #       Menu窗口部件                                      
  　#**Menu：**菜单条，用来实现下拉和弹出式菜单，点下菜单后弹出的一个选项列表,用户可以从中选择                                            
   # 第4步，在图形界面上创建一个标签用以显示内容并放置
l = tk.Label(window, text='      ', bg='green')
l.pack()
 
# 第10步，定义一个函数功能，用来代表菜单选项的功能，这里为了操作简单，定义的功能比较简单
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter += 1
 
# 第5步，创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tk.Menu(window)
 
# 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
filemenu = tk.Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='File', menu=filemenu)
 
# 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()    # 添加一条分隔线
filemenu.add_command(label='Exit', command=window.quit) # 用tkinter里面自带的quit()函数
 
# 第7步，创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
editmenu = tk.Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='Edit', menu=editmenu)
 
# 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)
 
# 第8步，创建第二级菜单，即菜单项里面的菜单
submenu = tk.Menu(filemenu) # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
filemenu.add_cascade(label='Import', menu=submenu, underline=0) # 给放入的菜单submenu命名为Import
 
# 第9步，创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
submenu.add_command(label='Submenu_1', command=do_job)   # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1　                     
                                              
# Frame 窗口部件
# Frame：框架，用来承载放置其他GUI元素，就是一个容器        
                                              
                                              
  # 第4步，在图形界面上创建一个标签用以显示内容并放置
tk.Label(window, text='on the window', bg='red', font=('Arial', 16)).pack()   # 和前面部件分开创建和放置不同，其实可以创建和放置一步完成
 
# 第5步，创建一个主frame，长在主window窗口上
frame = tk.Frame(window)
frame.pack()
 
# 第6步，创建第二层框架frame，长在主框架frame上面
frame_l = tk.Frame(frame)# 第二层frame，左frame，长在主frame上
frame_r = tk.Frame(frame)# 第二层frame，右frame，长在主frame上
frame_l.pack(side='left')
frame_r.pack(side='right')
 
# 第7步，创建三组标签，为第二层frame上面的内容，分为左区域和右区域，用不同颜色标识
tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r2', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()
                                            
                                              
  #  messageBox                                          
  # 　messageBox：消息框，用于显示你应用程序的消息框。                                    tkinter.messagebox.showinfo(title='Hi', message='你好！')            # 提示信息对话窗
tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'       
 # 第5步，定义触发函数功能
def hit_me():
    tkinter.messagebox.showinfo(title='Hi', message='你好！')              # 提示信息对话窗
    # tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
    # tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
    # print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
    # print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
    # print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'
 
# 第4步，在图形界面上创建一个标签用以显示内容并放置
tk.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()                                             
                                              
                                              
#  窗口部件三种放置方式pack/grid/place

                                             
                                              
                                              
                                              
        # 第4步，pack 放置方法
tk.Label(window, text='P', fg='red').pack(side='top')    # 上
tk.Label(window, text='P', fg='red').pack(side='bottom') # 下
tk.Label(window, text='P', fg='red').pack(side='left')   # 左
tk.Label(window, text='P', fg='red').pack(side='right')  # 右                     # 第4步，place 放置方法（精准的放置到指定坐标点的位置上）
tk.Label(window, text='Pl', font=('Arial', 20), ).place(x=50, y=100, anchor='nw')                 
                                              
# 第6步，主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。








```





eg：

```
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('Wellcome to Hongwei Website')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('400x300')  # 这里的乘是小x
 
# 第4步，加载 wellcome image
canvas = tk.Canvas(window, width=400, height=135, bg='green')
image_file = tk.PhotoImage(file='pic.gif')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(window, text='Wellcome',font=('Arial', 16)).pack()
 
# 第5步，用户信息
tk.Label(window, text='User name:', font=('Arial', 14)).place(x=10, y=170)
tk.Label(window, text='Password:', font=('Arial', 14)).place(x=10, y=210)
 
# 第6步，用户登录输入框entry
# 用户名
var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120,y=175)
# 用户密码
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120,y=215)
 
# 第8步，定义用户登录功能
def usr_login():
    # 这两行代码就是获取用户输入的usr_name和usr_pwd
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
 
    # 这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。
    # 中间的两行就是我们的匹配，即程序将输入的信息和文件中的信息匹配。
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        # 这里就是我们在没有读取到`usr_file`的时候，程序会创建一个`usr_file`这个文件，并将管理员
        # 的用户和密码写入，即用户名为`admin`密码为`admin`。
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
            usr_file.close()    # 必须先关闭，否则pickle.load()会出现EOFError: Ran out of input
 
    # 如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗how are you? 加上你的用户名。
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tkinter.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        # 如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
        else:
            tkinter.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:  # 如果发现用户名不存在
        is_sign_up = tkinter.messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
        # 提示需不需要注册新用户
        if is_sign_up:
            usr_sign_up()
 
# 第9步，定义用户注册功能
def usr_sign_up():
    def sign_to_Hongwei_Website():
        # 以下三行就是获取我们注册时所输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
 
        # 这里是打开我们记录数据的文件，将注册信息读出
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        # 这里就是判断，如果两次密码输入不一致，则提示Error, Password and confirm password must be the same!
        if np != npf:
            tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')
 
        # 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!
        elif nn in exist_usr_info:
            tkinter.messagebox.showerror('Error', 'The user has already signed up!')
 
        # 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            # 然后销毁窗口。
            window_sign_up.destroy()
 
    # 定义长在窗口上的窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('Sign up window')
 
    new_name = tk.StringVar()  # 将输入的注册名赋值给变量
    new_name.set('example@python.com')  # 将最初显示定为'example@python.com'
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.
 
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=130, y=50)
 
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=130, y=90)
 
    # 下面的 sign_to_Hongwei_Website
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Hongwei_Website)
    btn_comfirm_sign_up.place(x=180, y=120)
 
# 第7步，login and sign up 按钮
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=120, y=240)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=200, y=240)
 
# 第10步，主窗口循环显示
window.mainloop()
```





# PyAutoGUI

```python
#pip3 install pyautogui


import pyautigui

# 移动鼠标
pyautogui.moveTo(200,400,duration=2)
pyautogui.moveRel(200,500,duration=2)

print(pyautogui.position())  

# 鼠标点击，默认左键
pyautogui.click(100,100)   
# 单击左键
pyautogui.click(100,100,button='left')  
# 单击右键
pyautogui.click(100,300,button='right') 
# 单击中间 
pyautogui.click(100,300,button='middle') 
# 双击左键
pyautogui.doubleClick(10,10)  
# 双击右键
pyautogui.rightClick(10,10)   
# 双击中键
pyautogui.middleClick(10,10) 
# 鼠标按下
pyautogui.mouseDown()   
# 鼠标释放
pyautogui.mouseUp()  


pyautogui.dragTo(100,300,duration=1)   

duration
n.	持续时间; 期间

pyautogui.dragRel(100,300,duration=4) 
pyautogui.scroll(30000) 

im = pyautogui.screenshot()
im.save('screenshot.png')
rgb = im.getpixel((100, 500))
print(rgb)
match = pyautogui.pixelMatchesColor(500,500,(12,120,400))
print(match)
#第一个是获取屏幕截图函数，它可以返回一个 Pillow 的 image 对象; 第二个是获取屏幕截图中指定坐标点的颜色，返回 rgb 颜色值；第三个是将指定坐标点的颜色和目标的颜色进行比对，返回布尔值。
# 图像识别（一个）
oneLocation = pyautogui.locateOnScreen('1.png')
print(oneLocation)  

# 图像识别（多个）
allLocation = pyautogui.locateAllOnScreen('1.png')
print(list(allLocation))
### 键盘输入

### 键盘函数

- keyDown()：模拟按键按下
- keyUP()：模拟按键松开
- press()：模拟一次按键过程，即 keyDown 和 keyUP 的组合
- typewrite()：模拟键盘输出内容
pyautogui.keyDown('shift')    
pyautogui.press('1')    
pyautogui.keyUp('shift')   

pyautogui.typewrite('python', 1)
#第一个参数是输出的内容，第二个参数是间隔时间，单位是秒。
#运行上面代码，你的编辑器里面就会每隔1秒钟按顺序输出 python 的6个字母。
特殊符号
pyautogui.typewrite(['p','y','t','h','o','n','enter'])   

快捷键
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')
pyautogui.hotkey('ctrl','c')


信息框
way = pyautogui.confirm('领导，该走哪条路？', buttons=['农村路', '水路', '陆路'])
print(way)
# 警告框
alert = pyautogui.alert(text='警告！敌军来袭！', title='警告框')
print(alert)
# 密码框
password = pyautogui.password('请输入密码')
print(password)
# 普通输入框
input = pyautogui.prompt('请输入指令：')
print(input)
































```



# pynput

pynput，是专门针对鼠标和键盘的，至于pygame、pyglet等游戏框架虽然也提供了鼠标、键盘的监控事件，但它们毕竟是用来开发游戏的，还提供了创建窗口、图形绘制、物体的碰撞检测等等很多复杂的功能。如果只是单纯的操作鼠标和键盘，使用这种游戏框架有点小题大做了，下面我们就来看看这个名叫pynput的模块吧，看看它的使用方法。



```python
from pynput.mouse import Button, Controller

# 实例化Controller得到一个可以操作鼠标的对象
mouse = Controller()
# mouse.position: 获取当前鼠标位置。
# 屏幕左上角坐标为(0, 0) 右下角为(屏幕宽度, 屏幕高度)
print(f"当前鼠标位置: {mouse.position}") # 当前鼠标位置: (881, 467)

# 给mouse.position赋值等于移动鼠标，这里相当于移动到(100, 100)的位置
# 如果坐标小于0，那么等于0。如果超出屏幕范围，那么等于最大范围
mouse.position = (100, 100) # 此方法等价于mouse.move(100, 100)
print(f"当前鼠标位置: {mouse.position}") # 当前鼠标位置: (100, 100)


# 按下左键,同理Button.right是右键
mouse.press(Button.left)
# 松开左键
mouse.release(Button.left)
# 上面两行连在一起等于一次单击。如果上面两行紧接着再重复一次，那么整体会实现双击的效果
# 因为两次单击是连续执行的，没有等待时间。如果中间来一个time.sleep几秒，那么就变成两次单击了


# 当然鼠标点击我们有更合适的办法，使用click函数
# 该函数接收两个参数：点击鼠标的哪个键、以及点击次数
# 这里连续点击两次，等于双击
mouse.click(Button.right, 2)



# 垂直方向、沿着y轴滑动
# 第一个参数是针对水平方向的，暂时不用管，为0则表示不变。
# 第二个参数是针对垂直方向的，大于0表示向下，小于0表示向上
mouse.scroll(0, 2)
# 大于0向右，小于0向左
mouse.scroll(3, 0)

from pynput.mouse import Listener


def on_move(x, y):
 print(f"鼠标移动到: ({x}, {y})")


def on_click(x, y, button, is_press):
 print(f"鼠标{button}键在({x}, {y})处{"按下" if is_press else "松开"}")


def on_scroll(x, y, dx, dy):
 if dx:
  print(f"滑轮在({x}, {y})处向{"右" if dx > 0 else "左"}滑")
 else:
  print(f"滑轮在({x}, {y})处向{"下" if dy > 0 else "上"}滑")


with Listener(
 # 上面函数名不能变，记得对应
 on_move=on_move,
 on_click=on_click,
 on_scroll=on_scroll
) as listener:
 listener.join()
"""
鼠标移动到: (1090, 369)
鼠标移动到: (1090, 368)
鼠标移动到: (1090, 368)
鼠标移动到: (1090, 367)
鼠标Button.left键在(1090, 367)处按下
鼠标Button.left键在(1090, 367)处松开
滑轮在(1090, 367)处向上滑
"""
上面实例化一个Listener时，相当于开启了一个线程，因为Listener这个类继承自threading.Thread。所以我们调用listener.join()相当于就阻塞在这里了，会一直监控鼠标事件。所以我们需要一个机制来让它停下来：


from pynput.mouse import Listener, Button


def on_move(x, y):
 print(f"鼠标移动到: ({x}, {y})")


def on_click(x, y, button, is_press):
 if button == Button.right:
  # 一旦当某个事件返回了False，那么就会停止了
  # 这里我们选择右键吧
  print("点击右键，停止监控")
  return False
 print(f"鼠标{button}键在({x}, {y})处{"按下" if is_press else "松开"}")


def on_scroll(x, y, dx, dy):
 if dx:
  print(f"滑轮在({x}, {y})处向{"右" if dx > 0 else "左"}滑")
 else:
  print(f"滑轮在({x}, {y})处向{"下" if dy > 0 else "上"}滑")


with Listener(
 on_move=on_move,
 on_click=on_click,
 on_scroll=on_scroll
) as listener:
 listener.join()
"""
鼠标Button.left键在(881, 606)处按下
鼠标Button.left键在(881, 606)处松开
点击右键，停止监控
"""

from pynput.mouse import Listener


def on_move(x, y):
 print(f"鼠标移动到: ({x}, {y})")


def on_click(x, y, button, is_press):
 print(f"鼠标{button}键在({x}, {y})处{"按下" if is_press else "松开"}")


def on_scroll(x, y, dx, dy):
 if dx:
  print(f"滑轮在({x}, {y})处向{"右" if dx > 0 else "左"}滑")
 else:
  print(f"滑轮在({x}, {y})处向{"下" if dy > 0 else "上"}滑")


listener = Listener(
 on_move=on_move,
 on_click=on_click,
 on_scroll=on_scroll)

# 启动线程，主线程会继续向下执行
listener.start()
print("执行下面代码")
print(123)

# 此外我们也可以不通过让事件返回False，结束监听
# 而是就让它一直监听，等我们的逻辑执行完毕之后，手动结束监听
# 结束监听是通listener.stop()
import time
time.sleep(3) # 这里睡3s，相当于执行一段长逻辑了，否则子线程还未启动，就直接被主线程强制stop掉了
# 结束监听
listener.stop()
print("程序结束")
"""
执行下面代码
123
鼠标移动到: (850, 525)
鼠标Button.left键在(850, 525)处按下
鼠标Button.left键在(850, 525)处松开
鼠标Button.right键在(850, 525)处按下
鼠标Button.right键在(850, 525)处松开
程序结束
"""










from pynput.keyboard import Key, Controller

# 实例化一个可以操作键盘的对象
keyboard = Controller()

# 按下a键,小写
keyboard.press("a")
# 松开a键
keyboard.release("a")

# 按下A键，大写
keyboard.press("A")
# 松开A键
keyboard.release("A")
"""
像英文字符、数字等等直接输入相应的字符即可
但如果是shift、ctrl等键，那么需要调用Key里面属性
"""
# 按下大写键
keyboard.press(Key.caps_lock)
# 松开大写键
keyboard.release(Key.caps_lock)
from pynput.keyboard import Key, Controller

# 实例化一个可以操作键盘的对象
keyboard = Controller()

# 注意调用的方法，是pressed，不是press
# shift有两个键，一个是左边的、一个是右边的
with keyboard.pressed(Key.shift_l):
 keyboard.press("1")
 keyboard.release("1")
"""
上面的结果会输出一个感叹号，另外我们键盘的上方有数字键、右侧也有数字键。
我们平时输出感叹号用的都是shift加上键盘上方的数字键，用右侧的数字键会没有效果

但是对于pynput则没有区别，都会输出感叹号，因为你用键盘上方和有方的数字键打出来的都是数字
"""
# 如果要同时按下多个键呢？那就输入多个键即可，细心的老铁可能发现了，这正是pycharm启动程序的快捷键
with keyboard.pressed(Key.shift_l, Key.ctrl_l):
 keyboard.press(Key.f10)


from pynput.keyboard import Key, Listener


# 此时的Listener是从keyboard里面导入的

def on_press(key):
 # 当按下esc，结束监听
 if key == Key.esc:
  print(f"你按下了esc，监听结束")
  return False
 print(f"你按下了{key}键")


def on_release(key):
 print(f"你松开了{key}键")


with Listener(on_press=on_press, on_release=on_release) as listener:
     
"""
你按下了"a"键
你松开了"a"键
你按下了Key.shift键
你松开了Key.shift键
你按下了Key.right键
你松开了Key.right键
你按下了Key.down键
你松开了Key.down键
你按下了esc，监听结束
"""
from pynput.keyboard import Key, Listener

def on_press(key):
 """
 我们之前说按下某个键的时候，如果是英文字符、数字这些，直接输入相应的字符即可
 但如果是ctrl、shift这些键，需要从keyboard.Key里面获取

 那么同理，在这里我们如果想要获取具体按下、松开哪个键的话，那么可以调用key.char或者key.name
 如果是英文字符、数字这些，调用key.char；如果是ctrl、shift、f1、f12这些键，则需要调用key.name
 """
 if key == Key.esc:
  print(f"你按下了esc，监听结束")
  return False
 print(f"你按下了{key.char if hasattr(key, "char") else key.name}键")


def on_release(key):
 print(f"你松开了{key.char if hasattr(key, "char") else key.name}键")


with Listener(on_press=on_press, on_release=on_release) as listener:
 listener.join()
"""
你按下了shift键
你松开了shift键
你按下了a键
你松开了a键
你按下了esc，监听结束
"""









```





  实践

```Python
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
            try:
                time1 = float(input.get())
                j=0
                print(list1)
                for i in list1:
                        time.sleep(time1)
                        j+=1
                        state2.insert(INSERT, f'执行点击第{j}个位置x={i[0]},y={i[1]}\n')
                        # print(f'执行点击第{j}个位置x={i[0]},y={i[1]}')
                        pyautogui.click(i[0],i[1],button='left')
            except:
                state.delete('0.0', END)
                state.insert(INSERT, "铲屎官的时间输入格式错误瞄！\n")
                state.insert(INSERT, "铲屎官应该输入整数或小数瞄~")

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



# 创建一个标签，用于显示“时间间隔”文本
lab2 = Label(root, text='请输入时间间隔', font=("微软雅黑", 11), fg="lightsteelblue")
lab2.place(relx=0.1, y=40, relwidth=0.4, height=30)

# 创建一个文本框，用于输入时间间隔
input = Entry(root, relief="flat", font=("微软雅黑", 10))
input.place(relx=0.55, y=40, relwidth=0.4, height=30)

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
```



# 打包



pip install pyinstaller



```
 pyinstaller -F -w -i python.ico Demo.py 就表示 -F，打包只生成一个 exe 文件，-w，在运行程序的时候不打打开命令行的窗口，-i 就是打包带有自己设置的 ico 图标。
 
 参数以及用法

1. -F生成结果是一个exe文件，所有的第三方依赖、资源和代码均被打包进该exe内
2. -D生成结果是一个目录，各种第三方依赖、资源和exe 同时存储在该目录
3. （默认）-a不包含unicode支持-d执行生成的exe时，会输出一些log，有助于查错
4. -w不显示命令行窗口
5. -c显示命令行窗口
6. （默认）-p指定额外的import路径，类似于使用python path
7. -i指定图标
8. -v显示版本号
9. -n生成的.exe 的文件名
```













































































