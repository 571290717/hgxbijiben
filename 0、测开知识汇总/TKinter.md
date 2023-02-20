# TKinter



Python3  GUI 编程
	tkinter
		http://c.biancheng.net/tkinter/widget-and-attribute.html
		 python -m tkinter
		第一个Tkinter程序
			一个最简单的 Tkinter 程序至少应包含以下四个部分：
				导入 tkinter 模块
				创建主窗口，也称 root 窗口（即根窗口）
				添加人机交互控件，同时编写相应的事件函数
				通过主循环（mainloop）来显示主窗口
			上述四个步骤中，只有第三步属于 Tkinter 编程的重点，其余三个步骤属于固定的代码格式，如下所示：

# -*- coding:utf-8 -*-
import tkinter as tk
# 调用Tk()创建主窗口
root_window =tk.Tk()
# 给主窗口起一个名字，也就是窗口的名字
root_window.title('C语言中文网：c.biancheng.net')
#开启主循环，让窗口处于显示状态
root_window.mainloop()
			# -*- coding:utf-8 -*-
import tkinter as tk
root_window =tk.Tk()
# 设置窗口title
root_window.title('C语言中文网：c.biancheng.net')
# 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
root_window.geometry('450x300')
# 更改左上角窗口的的icon图标,加载C语言中文网logo标
root_window.iconbitmap('C:/Users/Administrator/Desktop/favicon.ico')
# 设置主窗口的背景颜色,颜色值可以是英文单词，或者颜色值的16进制数,除此之外还可以使用Tk内置的颜色常量
root_window["background"] = "#C9C9C9"
# 添加文本内,设置字体的前景色和背景色，和字体类型、大小
text=tk.Label(root_window,text="C语言中文网，欢迎您",bg="yellow",fg="red",font=('Times', 20, 'bold italic'))
# 将文本内容放置在主窗口内
text.pack()
# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
button=tk.Button(root_window,text="关闭",command=root_window.quit)
# 将按钮放置在主窗口内
button.pack(side="bottom")
#进入主循环，显示主窗口
root_window.mainloop()
				
		Tkinter常用控件和属性
			控件类型
			下表列出了 Tkinter 中常用的 15 个控件：

控件类型	控件名称	控件作用
Button	按钮	点击按钮时触发/执行一些事件（函数）
Canvas	画布	提供绘制图，比如直线、矩形、多边形等
Checkbutton	复选框	多项选择按钮，用于在程序中提供多项选择框
Entry	文本框输入框	用于接收单行文本输入
Frame	框架（容器）控件	定义一个窗体（根窗口也是一个窗体），用于承载其他控件，即作为其他控件的容器
Lable	标签控件	用于显示单行文本或者图片
LableFrame	容器控件	一个简单的容器控件，常用于复杂的窗口布局。
Listbox	列表框控件	以列表的形式显示文本
Menu	菜单控件	菜单组件（下拉菜单和弹出菜单）
Menubutton	菜单按钮控件	用于显示菜单项
Message	信息控件	用于显示多行不可编辑的文本，与 Label控件类似，增加了自动分行的功能
messageBox	消息框控件	定义与用户交互的消息对话框
OptionMenu	选项菜单	下拉菜单
PanedWindow	窗口布局管理组件	为组件提供一个框架，允许用户自己划分窗口空间
Radiobutton	单选框	单项选择按钮，只允许从多个选项中选择一项
Scale	进度条控件	定义一个线性“滑块”用来控制范围，可以设定起始值和结束值，并显示当前位置的精确值
Spinbox	高级输入框	Entry 控件的升级版，可以通过该组件的上、下箭头选择不同的值
Scrollbar	滚动条	默认垂直方向，鼠标拖动改变数值，可以和 Text、Listbox、Canvas等控件配合使用
Text	多行文本框	接收或输出多行文本内容
Toplevel	子窗口	在创建一个独立于主窗口之外的子窗口，位于主窗口的上一层，可作为其他控件的容器
			控件基本属性
				属性名称	说明
				anchor	定义控件或者文字信息在窗口内的位置
				bg	bg 是 background 的缩写，用来定义控件的背景颜色，参数值可以颜色的十六进制数，或者颜色英文单词
				bitmap	定义显示在控件内的位图文件
				borderwidth	定于控件的边框宽度，单位是像素
				command	该参数用于执行事件函数，比如单击按钮时执行特定的动作，可将执行用户自定义的函数
				cursor	当鼠标指针移动到控件上时，定义鼠标指针的类型，字符换格式，参数值有 crosshair（十字光标）watch（待加载圆圈）plus（加号）arrow（箭头）等
				font	若控件支持设置标题文字，就可以使用此属性来定义，它是一个数组格式的参数 (字体,大小，字体样式)
				fg	fg 是 foreground 的缩写，用来定义控件的前景色，也就是字体的颜色
				height	该参数值用来设置控件的高度，文本控件以字符的数目为高度（px），其他控件则以像素为单位
				image	定义显示在控件内的图片文件
				justify	定义多行文字的排列方式，此属性可以是 LEFT/CENTER/RIGHT
				padx/pady	定义控件内的文字或者图片与控件边框之间的水平/垂直距离
				relief	定义控件的边框样式，参数值为FLAT（平的）/RAISED（凸起的）/SUNKEN（凹陷的）/GROOVE（沟槽桩边缘）/RIDGE（脊状边缘）
				text	定义控件的标题文字
				state	控制控件是否处于可用状态，参数值默认为 NORMAL/DISABLED，默认为 NORMAL（正常的）
				width	用于设置控件的宽度，使用方法与 height 相同
		Tkinter主窗口
			创建一个空白窗口
				# 导入tk
from tkinter import *
# 创建一个主窗口对象
window = Tk()
# 调用mainloop()显示主窗口
window.mainloop()
			1) 窗口常用方法
				函数	说明
window.title("my title")	接受一个字符串参数，为窗口起一个标题
window.resizable()	是否允许用户拉伸主窗口大小，默认为可更改，当设置为 resizable(0,0)或者resizable(False,False)时不可更改
window.geometry()	设定主窗口的大小以及位置，当参数值为 None 时表示获取窗口的大小和位置信息。
window.quit()	关闭当前窗口
window.update()	刷新当前窗口
window.mainloop()	设置窗口主循环，使窗口循环显示（一直显示，指导窗口被关闭）
window.iconbitmap()	设置窗口左上角的图标（图标是.ico文件类型）
window.config(background ="red")	设置窗口的背景色为红色，也可以接受 16 进制的颜色值
window.minsize(50,50)	设置窗口被允许调整的最小范围，即宽和高各50
window.maxsize(400,400)	设置窗口被允许调整的最大范围，即宽和高各400
window.attributes("-alpha",0.5)	用来设置窗口的一些属性，比如透明度（-alpha）、是否置顶（-topmost）即将主屏置于其他图标之上、是否全屏（-fullscreen）全屏显示等
window.state("normal")	用来设置窗口的显示状态，参数值 normal（正常显示），icon（最小化），zoomed（最大化），
window.withdraw()	用来隐藏主窗口，但不会销毁窗口。
window.iconify()	设置窗口最小化
window.deiconify()	将窗口从隐藏状态还原
window.winfo_screenwidth()
window.winfo_screenheight()	获取电脑屏幕的分辨率（尺寸）
window.winfo_width()
window.winfo_height() 	获取窗口的大小，同样也适用于其他控件，但是使用前需要使用 window.update() 刷新屏幕，否则返回值为1
window.protocol("协议名",回调函数)	启用协议处理机制，常用协议有 WN_DELETE_WINDOW，当用户点击关闭窗口时，窗口不会关闭，而是触发回调函数。
			import tkinter as tk
window =tk.Tk()
#设置窗口title
window.title('C语言中文网')
#设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
window.geometry('450x300')
# 获取电脑屏幕的大小
print("电脑的分辨率是%dx%d"%(window.winfo_screenwidth(),window.winfo_screenheight()))
# 要求窗口的大小，必须先刷新一下屏幕
window.update()
print("窗口的分辨率是%dx%d"%(window.winfo_width(),window.winfo_height()))
# 如使用该函数则窗口不能被拉伸
# window.resizable(0,0)
# 改变背景颜色
window.config(background="#6fb765")
# 设置窗口处于顶层
window.attributes('-topmost',True)
# 设置窗口的透明度
window.attributes('-alpha',1)
# 设置窗口被允许最大调整的范围，与resizble()冲突
window.maxsize(600,600)
# 设置窗口被允许最小调整的范围，与resizble()冲突
window.minsize(50,50)
#更改左上角窗口的的icon图标,加载C语言中文网logo标
window.iconbitmap('C:/Users/Administrator/Desktop/favicon.ico')
#添加文本内容,并对字体添加相应的格式 font(字体,字号,"字体类型")
text=tk.Label(window,text="C语言中文网，网址：c.biancheng.net",bg="yellow",fg="red",font=('Times', 15, 'bold italic underline'))
#将文本内容放置在主窗口内
text.pack()
# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
button=tk.Button(window,text="关闭",command=window.quit)
# 将按钮放置在主窗口内
button.pack(side="bottom")
#进入主循环，显示主窗口
window.mainloop()
			2) protocol协议处理机制
				Tinter 除了提供事件绑定机制之外，还提供了协议处理机制，它指的是应用程序和窗口管理器之间的交互，最常用的协议为 WM_DELETE_WINDOW。

当 Tkinter 使用 WM_DELETE_WINDOW 协议与主窗口进行交互时，Tkinter 主窗口右上角x号的关闭功能失效，也就是无法通过点击x来关闭窗口，而是转变成调用用户自定义的函数。
			from tkinter import Tk
# 导入 对话框控件
from tkinter import messagebox
# 创建主窗口
root = Tk()
# 定义回调函数，当用户点击窗口x退出时，执行用户自定义的函数
def QueryWindow():
    # 显示一个警告信息，点击确后，销毁窗口
    if messagebox.showwarning("警告","出现了一个错误"):
        # 这里必须使用 destory()关闭窗口
        root.destroy()
# 使用协议机制与窗口交互，并回调用户自定义的函数
root.protocol('WM_DELETE_WINDOW', QueryWindow)
root.mainloop()
				import tkinter as tk
# 定义窗口
window = tk.Tk()
window.title('c语言中文网')
window.geometry('300x300')
window.iconbitmap('C:/Users/Administrator/Desktop/favicon.ico')
# 定义回调函数
def callback():
    print("执行回调函数","C语言中文网欢迎您")
# 点击执行按钮
button = tk.Button(window, text="执行", command=callback)
button.pack()
window.mainloop()
			geometry('450x400+300+200')
上述代码表示，设置主窗口的宽度为 450，高度为 400，同时窗口距离左边屏幕的距离为 300（以像素为单位），距离屏幕顶部的距离为 200，这里我们将带“+”的参数值称为“位置参数”，当然，您也可以将它们设置为负数，如下所示：
geometry('+-1500+-2000')
			import tkinter as tk
window = tk.Tk()
window.title('c语言中文网')
window.iconbitmap('C:/Users/Administrator/Desktop/favicon.ico')
# 设置窗口大小变量
width = 300
height = 300
# 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
window.geometry(size_geo)
window.mainloop()
				程序运行后窗口将出现在屏幕的中间位置
		Tkinter Label标签控件
			Label（标签）控件，是 Tkinter 中最常使用的一种控件，主要用来显示窗口中的文本或者图像，并且不同的 Lable（标签）允许设置各自不同的背景图片。
			下面对 Label（标签）的常用属性做简单介绍：
				属性名称	说明
				anchor	控制文本（或图像）在 Label 中显示的位置（方位），通过方位的英文字符串缩写（n、ne、e、se、s、sw、w、nw、center）实现定位，默认为居中（center）
				bg	用来设置背景色
				bd	即 borderwidth 用来指定 Label 控件的边框宽度，单位为像素，默认为 2 个像素
				bitmap	指定显示在 Label 控件上的位图，若指定了 image 参数，则该参数会被忽略
				compound	控制 Lable 中文本和图像的混合模式，若选项设置为 CENTER，则文本显示在图像上，如果将选项设置为 BOTTOM、LEFT、RIGHT、TOP，则图像显示在文本旁边。
				cursor	指定当鼠标在 Label 上掠过的时候，鼠标的的显示样式，参数值为 arrow、circle、cross、plus
				disableforeground	指定当 Label 设置为不可用状态的时候前景色的颜色
				font	指定 Lable 中文本的 (字体,大小,样式）元组参数格式，一个 Lable 只能设置一种字体
				fg	设置 Label 的前景色
				height/width	设置 Lable 的高度/宽度，如果 Lable 显示的是文本，那么单位是文本单元，如果 Label 显示的是图像，那么单位就是像素，如果不设置，Label 会自动根据内容来计算出标签的高度
				highlightbackground	当 Label 没有获得焦点的时候高亮边框的颜色，系统的默认是标准背景色
				highlightcolor	指定当 Lable 获得焦点的话时候高亮边框的颜色，系统默认为0，不带高亮边框
				image	指定 Label 显示的图片，一般是 PhotoImage、BitmapImage 的对象
				justify	表示多行文本的对齐方式，参数值为 left、right、center，注意文本的位置取决于 anchor 选项
				padx/pady	padx 指定 Label 水平方向上的间距（即内容和边框间），pady 指定 Lable 水平方向上的间距（内容和边框间的距离）
				relief	指定边框样式，默认值是 "flat"，其他参数值有 "groove"、"raised"、"ridge"、"solid"或者"sunken"
				state	该参数用来指定 Lable 的状态，默认值为"normal"（正常状态），其他可选参数值有"active"和"disabled"
				takefocus	默认值为False，如果是 True，表示该标签接受输入焦点
				text	用来指定 Lable 显示的文本，注意文本内可以包含换行符
				underline	给指定的字符添加下划线，默认值为 -1 表示不添加，当设置为 1 时，表示给第二个文本字符添加下划线。
				wraplength	将 Label 显示的文本分行，该参数指定了分行后每一行的长度，默认值为 0
			1) Label控件构成
				一个控件主要由背景和前景两部分组成。其中背景由三部分构成分别是内容区域、填充区、边框，这三个区域的大小通过以下属性进行控制，如下所示：

width/height
padx/pady
borderwidth
				import tkinter as tk
win = tk.Tk()
win.title("C语言中文网")
win.geometry('400x200')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 若内容是文字则以字符为单位，图像则以像素为单位
label = tk.Label(win, text="网址：c.biancheng.net",font=('宋体',20, 'bold italic'),bg="#7CCD7C",
                 # 设置标签内容区大小
                 width=30,height=5,
                 # 设置填充区距离、边框宽度和其样式（凹陷式）
                 padx=10, pady=15, borderwidth=10, relief="sunken")
label.pack()
win.mainloop()
			2) 标签添加背景图
				Label（标签）除了可以显示文本之外，还可以用来显示图片，通过一组示例做简单的说明，代码如下所示：
				import tkinter as  tk
win = tk.Tk()
win.title("C语言中文网")
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
#显示图片(注意这里默认支持的图片格式为GIF)
photo = tk.PhotoImage(file = 'C:/Users/Administrator/Desktop/c.biancheng.gif')
print(type(photo))
# 将图片放在主窗口的右边
lab =tk.Label(win,image=photo).pack(side="right")
# 显示文字，设置文本格式
text = "C语言中文网欢迎您,\n"\
       "这里有精彩的教程,\n "\
       "这里有数不尽的知识宝藏"
lab_text =tk.Label(win,text=text,fg ='#7CCD7C',font=('微软雅黑',15,'italic'),justify='left',padx=10).pack(side='left')
win.mainloop()
			3) Message控件
				Message 控件与 Label 控件的功能类似，它主要用来显示多行不可编辑的文本信息，与 Label 的不同之处在于该控件增加了自动分行的功能。下面对它做简单的介绍，示例如下：
				from tkinter import *
#创建主窗口
win = Tk()
win.config(bg='#8DB6CD')
win.title("C语言中文网")
win.geometry('400x300')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
txt = "C语言中文网，网址是：c.biancheng.net"
msg = Message (win, text=txt,width =60,font=('微软雅黑',10,'bold'))
msg .pack (side=LEFT)
#开始程序循环
win .mainloop ()
		Tkinter Button按钮控件
			Button 控件是 Tkinter 中常用的窗口部件之一，同时也是实现程序与用户交互的主要控件。通过用户点击按钮的行为来执行回调函数，是 Button 控件的主要功用。首先自定义一个函数或者方法，然后将函数与按钮关联起来，最后，当用户按下这个按钮时，Tkinter 就会自动调用相关函数。
			import tkinter as tk
# 创建窗口
window =tk.Tk()
# 设置回调函数
def callback():
    print ("click me!")
# 使用按钮控件调用函数
b = tk.Button(window, text="点击执行回调函数", command=callback).pack()
# 显示窗口
tk.mainloop()
			Button 控件的常营属性如下所示：
				属性	说明
				anchor	控制文本所在的位置，默认为中心位置（CENTER）
				activebackground	当鼠标放在按钮上时候，按妞的背景颜色
				activeforeground	当鼠标放在按钮上时候，按钮的前景色
				bd	按钮边框的大小，默认为 2 个像素
				bg	按钮的背景色
				command	用来执行按钮关联的回调函数。当按钮被点击时，执行该函数
				fg	按钮的前景色
				font	按钮文本的字体样样式
				height	按钮的高度
				highlightcolor	按钮控件高亮处要显示的颜色
				image	按钮上要显示的图片
				justify	按钮显示多行文本时，用来指定文本的对齐方式，参数值有 LEFT/RIGHT/CENTER
				padx/pady	padx 指定 x 轴（水平方向）的间距大小，pady 则表示 y轴（垂直方向）的间距大小
				ipadx/ipady	ipadx 指标签文字与标签容器之间的横向距离；ipady 则表示标签文字与标签容器之间的纵向距离
				state	设置按钮的可用状态，可选参数有NORMAL/ACTIVE/DISABLED，默认为 NORMAL
				text	按钮控件要显示的文本
			除了 Button 按钮之外，和其类似的按钮还有复选框按钮（Checkbutton）和单选框按钮（Radiobutton），它们分别有着不同语法和使用场景，后续会做详细介绍。

下面通过一组示例对 Button 控件的用法做简单的说明：
				import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
# 设置窗口的标题
window.title('C语言中文网')
# 设置并调整窗口的大小、位置
window.geometry('400x300+300+200')
# 当按钮被点击的时候执行click_button()函数
def click_button():
    # 使用消息对话框控件，showinfo()表示温馨提示
    messagebox.showinfo(title='温馨提示', message='欢迎使用C语言中文网')
# 点击按钮时执行的函数
button = tk.Button(window,text='点击前往',bg='#7CCD7C',width=20, height=5,command=click_button).pack()
# 显示窗口
window.mainloop()
			下面为 Button 控件添加一张背景图片
				import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
# 设置窗口的标题
window.title('C语言中文网')
# 设置窗口的大小
window.geometry('400x300+300+200')
# 当按钮被点击的时候执行click_button()函数
def click_button():
    # 使用消息对话框控件，showinfo()表示温馨提示
    messagebox.showinfo(title='温馨提示', message='欢迎使用C语言中文网')
# 创建图片对象
im = tk.PhotoImage(file='C:/Users/Administrator/Desktop/按钮.gif')
# 通过image参数传递图片对象
button = tk.Button(window,image=im,command=click_button).pack()
# 启动窗口
window.mainloop()
			扩展：按钮的布局
				按钮在主窗口中的布局，通常使用 grid() 函数来完成，该函数以网格状的形式（即行和列）来管理窗口的布局。

grid() 布局管理器提供了一个sticky参数，通过该参数可以设置按钮的方位，该参数默认将控件设置居中，其他参数值有 N/S/W/E（上/下/左/右），而且可以组合在一起使用，比如 NW/WE/SE/SW/NE 等，这与anchor参数控制文本的显示位置，有着异曲同工之妙。
				import tkinter as tk
from tkinter import messagebox
win = tk.Tk()
win.title("C语言中文网")
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
win.geometry('400x200+100+100')
win.resizable(0,0)
# 将俩个标签分别布置在第一行、第二行
tk.Label(win, text="账号：").grid(row=0)
tk.Label(win, text="密码：").grid(row=1)
# 创建输入框控件
e1 = tk.Entry(win)
# 以 * 的形式显示密码
e2 = tk.Entry(win,show='*')
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)
# 编写一个简单的回调函数
def login():
    messagebox.showinfo('欢迎您到来')
# 使用 grid()的函数来布局，并控制按钮的显示位置
tk.Button(win, text="登录", width=10, command=login).grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Button(win, text="退出", width=10, command=win.quit).grid(row=3, column=1, sticky="e", padx=10, pady=5)
win.mainloop()
		Tkinter Entry输入控件
			Entry 控件是 Tkinter GUI 编程中的基础控件之一，它的作用就是允许用户输入内容，从而实现 GUI 程序与用户的交互，比如当用户登录软件时，输入用户名和密码，此时就需要使用 Entry 控件。

Entry 控件使用起来非常简单，下面对该控件做简单的介绍。基本语法格式如下：
tk_entry = Entry( master, option, ... )
			基本属性
				Entry 控件除了具备一些共有属性之外，还有一些自身的特殊属性，如下表所示：
				属性名称	说明
				exportselection	默认情况下，如果在输入框中选中文本会复制到粘贴板，如果要忽略这个功能，可以设置为 exportselection=0
				selectbackground	选中文字时的背景颜色
				selectforeground	选中文字时的前景色
				show	指定文本框内容以何种样式的字符显示，比如密码可以将值设为 show="*"
				textvariable	输入框内值，也称动态字符串，使用 StringVar() 对象来设置，而 text 为静态字符串对象
				xscrollcommand	设置输入框内容滚动条，当输入的内容大于输入框的宽度时使用户
			1) 动态数据类型
				下面通过一个时钟示例对“动态字符串”做进一步了解，代码如下：
纯文本复制
import tkinter as tk
import time
root = tk.Tk()
root.title("C语言中文网")
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
root.geometry('450x150+100+100')
root.resizable(0,0)
root.title('我们的时钟')
# 获取时间的函数
def gettime():
    # 获取当前时间
    dstr.set(time.strftime("%H:%M:%S"))
    # 每隔 1s 调用一次 gettime()函数来获取时间
    root.after(1000, gettime)
# 生成动态字符串
dstr = tk.StringVar()
# 利用 textvariable 来实现文本变化
lb = tk.Label(root,textvariable=dstr,fg='green',font=("微软雅黑",85))
lb.pack()
# 调用生成时间的函数
gettime()
# 显示窗口
root.mainloop()
			常用方法
				除了一些基本的属性之外，Entry 控件还提供了一些常用的方法，如下所示：

方法	说明
delete()	根据索引值删除输入框内的值
get()	获取输入框内的是
set()	设置输入框内的值
insert()	在指定的位置插入字符串
index()	返回指定的索引值
select_clear()	取消选中状态
select_adujst()	确保输入框中选中的范围包含 index 参数所指定的字符，选中指定索引和光标所在位置之前的字符
select_from (index)	设置一个新的选中范围，通过索引值 index 来设置
select_present()	返回输入框是否有处于选中状态的文本，如果有则返回 true，否则返回 false。
select_to()	选中指定索引与光标之间的所有值
select_range()	选中指定索引与光标之间的所有值，参数值为 start,end，要求 start 必须小于 end。
注意：在 Entry 控件中，我们可以通过以下方式来指定字符的所在位置：
数字索引：表示从 0 开始的索引数字；
"ANCHOE"：在存在字符的情况下，它对应第一个被选中的字符；
"END"：对应已存在文本中的最后一个位置；
"insert(index,'字符')：将字符插入到 index 指定的索引位置。

				import tkinter as tk
win = tk.Tk()
# 设置主窗口
win.geometry('250x100')
win.title("C语言中文网")
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
win.resizable(0,0)
# 创建输入框控件
entry1 = tk.Entry(win)
# 放置输入框，并设置位置
entry1.pack(padx=20, pady=20)
entry1.delete(0, "end")
# 插入默认文本
entry1.insert(0,'C语言中文网，网址：c.biancheng.net')
# 得到输入框字符串
print(entry1.get())
# 删除所有字符
# entry1.delete(0, tk.END)
win.mainloop()
				import tkinter as tk
win =tk.Tk()
# 设置主窗口
win.geometry('250x100')
win.title("C语言中文网")
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
win.resizable(0,0)
# 新建文本标签
labe1 = tk.Label(win,text="账号：")
labe2 = tk.Label(win,text="密码：")
# grid()控件布局管理器，以行、列的形式对控件进行布局，后续会做详细介绍
labe1.grid(row=0)
labe2.grid(row=1)
# 为上面的文本标签，创建两个输入框控件
entry1 = tk.Entry(win)
entry2 = tk.Entry(win)
# 对控件进行布局管理，放在文本标签的后面
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
# 显示主窗口
win.mainloop()
		Entry控件验证功能
			Entry 控件也提供了对输入内容的验证功能，比如要求输入英文字母，你却输入了数字，这就属于非法输入，Entry 控件通过以下参数实现对内容的校验：
				参数	说明
validate	指定验证方式，字符串参数，参数值有 focus、focusin、focusout、key、all、none。 
validatecommand	指定用户自定义的验证函数，该函数只能返回 True 或者 Fasle
invalidcommand	当 validatecommand 指定的验证函数返回 False 时，可以使用该参数值再指定一个验证函数。
下面对 validate 的参数值做简单的介绍：

参数值	说明
focus	当 Entry 组件获得或失去焦点的时候验证
focusin	当 Entry 组件获得焦点的时候验证
focuson	当 Entry 组件失去焦点的时候验证
key	当输入框被编辑的时候验证
all	当出现上边任何一种情况的时候验证
none	 默认不启用验证功能，需要注意的是这里是字符串的 'none'
				import tkinter as tk
from tkinter import messagebox
win = tk.Tk()
# 设置主窗口
win.geometry('250x200+250+200')
win.title("C语言中文网")
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
win.resizable(0,0)
# 创建验证函数
def check():
    if entry1.get() == "C语言中文网":
        messagebox.showinfo("输入正确")
        return True
    else:
        messagebox.showwarning("输入不正确")
        entry1.delete(0,tk.END)
        return False
# 新建文本标签
labe1 = tk.Label(win,text="账号：")
labe2 = tk.Label(win,text="密码：")
labe1.grid(row=0)
labe2.grid(row=1)
# 创建动字符串
Dy_String = tk.StringVar()
# 使用验证参数 validata,参数值为 focusout 当失去焦点的时候，验证输入框内容是否正确
entry1 = tk.Entry(win,textvariable =Dy_String,validate ="focusout",validatecommand=check)
entry2 = tk.Entry(win)
# 对控件进行布局管理，放在文本标签的后面
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
win.mainloop()
				
不仅如此，Tkinter 还为验证函数提供可一些额外的选项，不过想要使用这些额外选项，需要提前使用 register() 方法对验证函数进行注册，。常用的选项如下所示：

选项	说明
%d	有 3 个参数值，其中 0 表示删除操作；1 表示插入操作；2 表示获得、失去焦点或 textvariable 变量的值被修改导
%i	当用户进行插入或者删除操作的时，该选项不爱哦是插入或者删除的索引位置，若是其他的情况则选项值为 -1
%P	该选项值指定了输入框内的文本内容，只有当输入框的值允许改变的时候，该选项值才会生效。
%s	改值为调用验证函数钱输入框内的文本内容
%S	该选项值，只有插入或者删除操作触发验证函数的时候才会生效，它表示了被删除或者插入的内容
%v	表示当前 Entry 控件的 validate 参数的值
%V	表示触发验证函数的原因，值为 focus、focusin 、focusout、all、key.. 中的一个。
%W	该选项表示控件类型，即控件的名字（Entry）
				import tkinter as tk
from tkinter import messagebox
win = tk.Tk()
# 设置主窗口
win.geometry('250x200+250+200')
win.title("C语言中文网")
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
win.resizable(0,0)
# 新建文本标签
labe1 = tk.Label(win,text="账号：")
labe2 = tk.Label(win,text="密码：")
labe1.grid(row=0)
labe2.grid(row=1)
# 创建动字符串
Dy_String = tk.StringVar()
# 创建验证函数
def check(strings,reason, id):
    if entry1.get() == "C语言中文网":
        messagebox.showinfo("输入正确")
        print(strings,reason,id)
        return True
    else:
        messagebox.showwarning("输入不正确")
        print(strings,reason,id)
        return False
# 对验证函数进行注册
CheckTest = win.register(check)
# 使用验证参数 validata,参数值为 focusout 当失去焦点的时验证输入框内容是否正确
entry1 = tk.Entry(win,textvariable =Dy_String,validate ="focusout",validatecommand=(CheckTest,'%P','%V','%W'))
entry2 = tk.Entry(win)
# 对控件进行布局管理，放在文本标签的后面
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
win.mainloop()
			实例演示
				from tkinter import *
# 创建窗体
win = Tk()
win.title("C语言中文网")
win.geometry('300x300')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 创建一个容器来包括其他控件
frame = Frame (win)
# 创建一个计算器
def calc() :
# 用户输入的表达式，计算结果后转换为字符串
    result = "= "+ str (eval(expression.get()))
    #将计算的结果显示在Label控件上
    label.config(text =result)
#创建一个Label控件
label = Label (frame)
#创建一个Entry控件
entry = Entry (frame)
#读取用户输入的表达式
expression = StringVar ()
#将用户输入的表达式显示在Entry控件上
entry ["textvariable"] = expression
#创建-一个 Button控件.当用户输入完毕后，单击此按钮即计算表达式的结果
button1 = Button (frame, text="等 于",command=calc)
#设置Entry控件为焦点所在
entry.focus ()
frame.pack ()
#Entry控件位于窗体的上方
entry .pack()
#Label控件位于窗体的左方
label .pack (side="left")
#Button控件位于窗体的右方
button1.pack (side="right")
#开始程序循环
frame .mainloop()
			Spinbox 高级输入框
				Spinbox 是 Entry 控件的升级版，它是 Tkinter 8.4 版本后新增的控件，该控件不仅允许用户直接输入内容，还支持用户使用微调选择器（即上下按钮调节器）来输入内容。在一般情况下，Spinbox 控件用于在固定的范围内选取一个值的时候使用。下面看一组简单的应用示例：
				import tkinter as tk
root = tk.Tk()
root.title("C语言中文网")
root.geometry('300x200+300+300')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 如果是数字使用 from_和to参数，范围 0-20,并且与2步长递增或递减
w = tk.Spinbox(root,from_=0,to=20, increment=2,width = 15,bg='#9BCD9B')
w.pack()
# 显示窗口
root.mainloop()
				import tkinter as tk
root = tk.Tk()
root.title("C语言中文网")
root.geometry('300x200+300+300')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 使用 values 参数以元组的形式进行传参
strings = tk.Spinbox(root,values=('Python','java','C语言','PHP'))
strings.pack()
# 开启事件循环
root.mainloop()
		Tkinter Text文本框控件
			基本属性
				属性	说明
				autoseparators	默认为 True，表示执行撤销操作时是否自动插入一个“分隔符”（其作用是用于分隔操作记录）
				exportselection	默认值为 True，表示被选中的文本是否可以被复制到剪切板，若是 False 则表示不允许。
				insertbackground	设置插入光标的颜色，默认为 BLACK
				insertborderwidth	设置插入光标的边框宽度，默认值为 0
				insertofftime	该选项控制光标的闪烁频频率（灭的状态）
				insertontime	该选项控制光标的闪烁频频率（亮的状态）
				selectbackground	指定被选中文本的背景颜色，默认由系统决定
				selectborderwidth	指定被选中文本的背景颜色，默认值是0
				selectforeground	指定被选中文本的字体颜色，默认值由系统指定
				setgrid	默认值是 False，指定一个布尔类型的值，确定是否启用网格控制
				spacing1	指定 Text 控件文本块中每一行与上方的空白间隔，注意忽略自动换行，且默认值为 0。
				spacing2	指定 Text 控件文本块中自动换行的各行间的空白间隔，忽略换行符，默认值为0
				spacing3	指定 Text 组件文本中每一行与下方的空白间隔，忽略自动换行，默认值是 0
				tabs	定制 Tag 所描述的文本块中 Tab 按键的功能，默认被定义为 8 个字符宽度，比如 tabs=('1c', '2c', '8c') 表示前 3 个 Tab 宽度分别为 1厘米，2厘米，8厘米。
				undo	该参数默认为 False，表示关闭 Text 控件的“撤销”功能，若为 True 则表示开启
				wrap	该参数用来设置当一行文本的长度超过 width 选项设置的宽度时，是否自动换行，参数值 none（不自动换行）、char（按字符自动换行）、word（按单词自动换行）
				xscrollcommand	该参数与 Scrollbar 相关联，表示沿水平方向上下滑动
				yscrollcommand	该参数与 Scrollbar 相关联，表示沿垂直方向左右滑动
			基本方法
				方法	说明
				bbox(index)	返回指定索引的字符的边界框，返回值是一个 4 元组，格式为(x,y,width,height)
				edit_modified()	该方法用于查询和设置 modified 标志（该标标志用于追踪 Text 组件的内容是否发生变化）
				edit_redo()	“恢复”上一次的“撤销”操作，如果设置 undo 选项为 False，则该方法无效。
				edit_separator()	插入一个“分隔符”到存放操作记录的栈中，用于表示已经完成一次完整的操作，如果设置 undo 选项为 False，则该方法无效。
				get(index1, index2)	返回特定位置的字符，或者一个范围内的文字。
				image_cget(index, option)	返回 index 参数指定的嵌入 image 对象的 option 选项的值，如果给定的位置没有嵌入 image 对象，则抛出 TclError 异常
				image_create()	在 index 参数指定的位置嵌入一个 image 对象，该 image 对象必须是 Tkinter 的 PhotoImage 或 BitmapImage 实例。
				insert(index, text)	在 index 参数指定的位置插入字符串，第一个参数也可以设置为 INSERT，表示在光标处插入，END 表示在末尾处插入。
				delete(startindex [, endindex])	删除特定位置的字符，或者一个范围内的文字。
				see(index)	如果指定索引位置的文字是可见的，则返回 True，否则返回 False。
			from tkinter import *
win = Tk()
win.title("C语言中文网")
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
win.geometry('400x420')
# 创建一个文本控件
# width 一行可见的字符数；height 显示的行数
text = Text(win, width=50, height=30, undo=True, autoseparators=False)
# 适用 pack(fill=X) 可以设置文本域的填充模式。比如 X表示沿水平方向填充，Y表示沿垂直方向填充，BOTH表示沿水平、垂直方向填充
text.pack()
# INSERT 光标处插入；END 末尾处插入
text.insert(INSERT, 'C语言中文网，一个有温度的网站')
win.mainloop()
			from tkinter import *
win = Tk()
win.title("C语言中文网")
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
win.geometry('400x300')
# 创建一个文本控件
# width 一行可见的字符数；height 显示的行数
text = Text(win, width=50, height=20, undo=True, autoseparators=False)
text.grid()
# INSERT 光标处插入；END 末尾处插入
text.insert(INSERT, 'C语言中文网，一个有温度的网站')
# 定义撤销和恢复方法，调用edit_undo()和 edit_redo()方法
def backout():
    text.edit_undo()
def regain():
    text.edit_redo()
# 定义撤销和恢复按钮
Button(win,text = '撤销',command = backout).grid(row=3, column=0, sticky="w", padx=10, pady=5)
Button(win,text = '恢复',command = regain).grid(row=3, column=0, sticky="e", padx=10, pady=5)
win.mainloop()
			Index文本索引
				索引类型	说明
				INSERT	对应插入光标的位置
				CURRENT	对应与鼠标坐标最接近的位置
				END	对应 Text 控件的文本域中最后一个字符的下一个位置
				"line.column"	表示某一行某一列的一个位置，比如 1.2 表示第一行第二列的一个位置
				"line.end"	表示某一行到末尾的最后一个位置
				SEL	一种针对于 Tag 的特殊索引用法，(SEL_FIRST,SEL_LAST) 表示当前被选中的范围
			from tkinter import *
root = Tk()
root.title("C语言中文网")
root.geometry('400x200')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
text =Text(root, width=35, heigh=15)
text.pack()
# 在文本域中插入文字
text.insert(INSERT, 'C语言中文网')
# 继续向后插入文字
text.insert("insert", "，I love Python")
# 获取字符，使用get() 方法
print(text.get("1.3", "1.end"))
# 显示窗口
root.mainloop()
			Tag文本标签
				方法	说明
				tag_add(tagName,index1,index2)	为指定索引范围内的内容添加一个标签名字，如果 index2 不存在，则单独为 Index1 指定的内容添加 Tag
				tag_bind(tagName, sequence, func, add=None)	为 Tag 绑定事件，解除绑定使用 tag_unbind() 方法
				tag_cget（tagName,option）	返回 tagName 指定的 option 选项的值
				tag_configure(tagName, cnf=None, **kw)	设置 tagName 的选项
				tag_delete(tagNames)	删除单个或者多个 tagNames 指定的标签
				tag_lower(tagName, belowThis=None)	降低 Tag 的优先级，如果 belowThis 参数不为空，则表示 tagName 需要比 belowThis 指定的 Tag 优先级更低
				tag_names(index=None)	如果不带参数，表示返回 Text 组件中所有 Tags 的名字，若存在 index 参数则返回该位置上所有 Tags 的名字
				tag_nextrange(tagName, index1, index2=None)	 在 index1 到 index2 的范围内第一个 tagName 的位置，若不存在则返回空字符串。
				tag_raise(tagName, aboveThis=None)	提高 Tag 的优先级，如果 aboveThis 参数不为空，则表示 tagName 需要比 aboveThis 指定的 Tag 优先级更高
				tag_ranges(tagName)	返回所有 tagName 指定的文本，并将它们的范围以列表的形式返回
				tag_remove(tagName, index1, index2=None)	删除 index1 到 index2 之间所有的 tagName，如果忽略 index2 参数，那么只删除 index1 指定字符的 tagName
			from tkinter import *
# 创建多行文本框控件
from tkinter import *
# 创建主窗口
win = Tk()
win.title(string = "C语言中文网")
# 创建一个Text控件
text = Text (win)
# 在Text控件内插入- -段文字 ，INSERT表示在光标处插入，END表示在末尾处插入
text.insert (INSERT,  "C语言中文网（网址：c.biancheng.net），一个有温度的网站，一生只做一件事\n\n")
# 跳下一行
text.insert (INSERT, "\n\n")
# 在Text控件内插入- -个按钮
button = Button(text, text="关闭",command=win.quit)
text. window_create (END, window=button)
# 填充水平和垂直方向,这里设置 expand为 True 否则不能垂直方向延展
text .pack (fill=BOTH,expand=True)
# 在第一行文字的第0个字符到第6个字符处插入标签，标签名称为"name"
text.tag_add("name", "1.0", "1.6")
# 将插入的按钮设置其标签名为"button"
text.tag_add ("button", button)
#使用 tag_config() 来改变标签"name"的前景与背景颜色,并加下画线，通过标签控制字符的样式
text.tag_config("name", font=('微软雅黑',18,'bold'),background="yellow", foreground= "blue",underline=1)
#设置标签"button"的居中排列
text. tag_config("button", justify="center")
#开始程序循环
win .mainloop()
			Mark文本标记
				方法	说明
				mark_gravity(markName, direction=None)	设置 Mark 的移动方向，默认是 "right"，也可以设置为 "left" ，表示即如果在 Mark 处插入文本的话，Mark 的标记移动方向，也就是文本的插入方向。
				mark_names()	返回 Text 组件中所有 Marks 的名字
				mark_next(index)	返回在 index 指定的位置后边的一个 Mark 的名字
				mark_previous(index)	返回在 index 指定的位置前边的一个 Mark 的名字
				mark_set(markName, index)	移动 Mark 到 index 参数指定的位置，如果 markName 参数指定的 Mark 不存在，则创建一个新的 Mark
				mark_unset(MarkName)	删除指定的 Mark
			import tkinter as tk
root = tk.Tk()
root.title("C语言中文网")
root.geometry('400x200')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
text = tk.Text(root, width=35, heigh=15)
text.pack()
text.insert("insert", "C语言中文网")
# 设置标记，这里的 1.end 表示 第一行最后一个字符，当然也可以使用数字来表示比如 1.5 表示第一行第五个字符
text.mark_set("name", "1.end")
# 在标记之后插入相应的文字
text.insert("name", ",网址：c.biancheng.net")
# 跟着自动移动，往后插入，而不是停留在原位置
text.insert("name", ",欢迎光临")
# 若使用 mark_unset() 可以删除指定的标记
# text.mark_unset("name")
# 但使用delete来清楚所有的内容， mark 标记依旧会存在
# text.delete("1.0","end")
# 依然可以使用 name标记来插入
# text.insert("name", "Python答疑")
# 显示窗口
root.mainloop()
		10Tkinter列表框和组合框
			列表框（Listbox）和复选框（Combobox）是 Tkinter 中两个控件，由于其非常相似，本节将它们放在一起进行介绍。
			Listbox控件
				首先介绍一下列表框，即 Listbox。在使用 Tkinter 进行 GUI 编程的过程中，如果需要用户自己进行选择时就可以使用列表框控件。列表框中的选项可以是多个条目，也可以是单个唯一条目，但常用于多个条目。
				下面对列表框控件（Listbox）的常用方法做简单的介绍
				方法	说明
				activate(index)	将给定索引号对应的选项激活，即文本下方画一条下划线
				bbox(index)	返回给定索引号对应的选项的边框，返回值是一个以像素为单位的 4 元祖表示边框：(xoffset, yoffset, width, height)， xoffset 和 yoffset 表示距离左上角的偏移位置
				curselection()	返回一个元组，包含被选中的选项序号（从 0 开始）
				delete(first, last=None)	 删除参数 first 到 last 范围内（包含 first 和 last）的所有选项
				get(first, last=None)	返回一个元组，包含参数 first 到 last 范围内（包含 first 和 last）的所有选项的文本
				index(index)	返回与 index 参数相应选项的序号
				itemcget(index, option)	获得 index 参数指定的项目对应的选项（由 option 参数指定）
				itemconfig(index, **options)	设置 index 参数指定的项目对应的选项（由可变参数 **option 指定）
				nearest(y)	返回与给定参数 y 在垂直坐标上最接近的项目的序号
				selection_set(first, last=None)	设置参数 first 到 last 范围内（包含 first 和 last）选项为选中状态，使用 selection_includes(序号) 可以判断选项是否被选中。 
				size()	返回 Listbox 组件中选项的数量
				xview(*args)	该方法用于在水平方向上滚动 Listbox 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现。 如果第一个参数是 "moveto"，则第二个参数表示滚动到指定的位置：0.0 表示最左端，1.0 表示最右端；如果第一个参数是 "scroll"，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 "units" 或 "pages"），例如：xview("scroll", 2, "pages")表示向右滚动二行。
				yview(*args)	该方法用于在垂直方向上滚动 Listbox 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现
			除了共有属性之外，列表框控件也有一些其他属性，如下表所示：
				属性	说明
				listvariable	1. 指向一个 StringVar 类型的变量，该变量存放 Listbox 中所有的项目
				2. 在 StringVar 类型的变量中，用空格分隔每个项目，例如 var.set("c c++ java python")
				selectbackground	1. 指定当某个项目被选中的时候背景颜色，默认值由系统指定
				selectborderwidth	1. 指定当某个项目被选中的时候边框的宽度
				2. 默认是由 selectbackground 指定的颜色填充，没有边框
				3. 如果设置了此选项，Listbox 的每一项会相应变大，被选中项为 "raised" 样式
				selectforeground	1. 指定当某个项目被选中的时候文本颜色，默认值由系统指定
				selectmode	1. 决定选择的模式，tk 提供了四种不同的选择模式，分别是："single"（单选）、"browse"（也是单选，但拖动鼠标或通过方向键可以直接改变选项）、"multiple"（多选）和 "extended"（也是多选，但需要同时按住 Shift 键或 Ctrl 键或拖拽鼠标实现），默认是 "browse"
				setgrid	指定一个布尔类型的值，决定是否启用网格控制，默认值是 False
				takefocus	指定该组件是否接受输入焦点（用户可以通过 tab 键将焦点转移上来），默认值是 True
				xscrollcommand	为 Listbox 组件添加一条水平滚动条，将此选项与 Scrollbar 组件相关联即可
				yscrollcommand	为 Listbox 组件添加一条垂直滚动条，将此选项与 Scrollbar 组件相关联即可
			1) 创建列表框控件
				# 创建一个列表控件，并增加相应的选项
from tkinter import *
# 创建主窗口
win = Tk()
win.title("C语言中文网")
win.geometry('400x200')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 创建列表选项
listbox1 =Listbox(win)
listbox1.pack()
# i表示索引值，item 表示值，根据索引值的位置依次插入
for i,item in enumerate(["C","C++","C#","Python","Java"]):
    listbox1.insert(i,item)
# 显示窗口
win.mainloop()
				组件摆放-------->pack()
			2) 增加滚动条和删除功能
				下面为上述示例增加一个滚动条和选项的删除功能，如下所示：
				from tkinter import *
# 创建主窗口
win = Tk()
win.title("C语言中文网")
win.geometry('400x180')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 创建滚动条
s = Scrollbar(win)
# 设置垂直滚动条显示的位置，使得滚动条，靠右侧；通过 fill 沿着 Y 轴填充
s.pack(side = RIGHT,fill = Y)
# 将 selectmode 设置为多选模式，并为Listbox控件添加滚动条
listbox1 =Listbox(win,selectmode = MULTIPLE,height =5, yscrollcommand = s.set)
# i 表示索引值，item 表示值，根据索引值的位置依次插入
for i,item in enumerate(range(1,50)):
    listbox1.insert(i,item)
listbox1.pack()
# 设置滚动条，使用 yview使其在垂直方向上滚动 Listbox 组件的内容，通过绑定 Scollbar 组件的 command 参数实现
s.config(command = listbox1.yview)
# 使用匿名函数,创建删除函数，点击删除按钮，会删除选项
bt = Button(win,text='删除',command = lambda x = listbox1:x.delete(ACTIVE))
# 将按钮放置在底部
bt.pack(side = BOTTOM)
# 显示窗口
win.mainloop()
			3) StringVar() 添加列表选项
				下面演示如何通过  StringVar() 方法动态地获取列表框中的选项，示例代码如下：
				import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("C语言中文网")
window.geometry('400x180')
window.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 创建变量，用var1用来接收鼠标点击的具体选项内容
var1 = tk.StringVar()
l = tk.Label(window, bg='#B0B0B0', font=('微软雅黑', 15), width=20, textvariable=var1)
l.pack()
# 创建一个按钮的点击事件
def click_button():
    # 使用 curselection来选中文本
    try:
        val = lb.get(lb.curselection())
    # 设置label值
        var1.set(val)
    except Exception as e:
        e = '发现一个错误'
        messagebox.showwarning(e,'没有选择任何条目')
# 创建一个按钮并放置，点击按钮调用print_selection函数
b1 = tk.Button(window, text='获取当前选项', command=click_button)
b1.pack()
# 创建Listbox并为其添加内容
var2 = tk.StringVar()
var2.set(("C语言辅导班", "Python答疑辅导", "Java答疑辅导", "C++辅导"))
# 创建Listbox，通过 listvariable来传递变量
lb = tk.Listbox(window, listvariable=var2)
# 新建一个序列，然后将值循环添加到Listbox控件中
items = ["C", "Java", "Python", "C#", "Golang", "Runby"]
for i in items:
    lb.insert('end', i)  # 从最后一个位置开始加入值
lb.insert(0, '编程学习')  # 在第一个位置插入一段字符串
lb.delete(4)  # 删除第2个位置处的索引
lb.pack()
#主窗显示
window.mainloop()
			Combobox控件
				通过前面内容的介绍我们知道 Listbox 是一个供用户从列表项中选择相应条目的控件。但在有些情况下，比如列表的项目过多时，若使用列表控件，列出所有选项就会显得界面格外臃肿，这时就需要用到 Combobox 控件，也就是下拉菜单控件（或称复合框），该控件是列表控件的改进版，具有更加灵活的界面，因此其应用场景相比于前者要更加广泛。

不过需要注意的是 Combobox 并不包含在 tkinter 模块中，而是包含在tkinter.ttk子模块中，因此若想使用 Combobox 控件，需要使用下面的导包方式：
from tkinter import ttk
下面对 Combobox 控件做简单的介绍，其语法格式如下所示：
cbox=Combobox(窗口对象,[参数列表])
Combobox 控件在形式虽然与列表控件存在不同，但它们的本质是相同，因此属性和方法是通用的。

对于 Combobox 控件而言，它常用的方法有两个，分别是 get() 和 current()，前者表示获取当前选中选项的内容，后者表示获取选中选项的索引值。下面通过一组简单的示例进一步了解 Combobox 控件，示例代码如下：
				import tkinter
from tkinter import ttk # 导入ttk模块，下拉菜单控件位于ttk子模块中
# 创建窗口
win = tkinter.Tk()
win.title("C语言中文网")
# win.geometry('400x200')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
win.geometry('400x250')
win.resizable(0,0)
# 创建下拉菜单
cbox = ttk.Combobox(win)
# 使用 grid() 来控制控件的位置
cbox.grid(row = 1, sticky="NW")
# 设置下拉菜单中的值
cbox['value'] = ('C','C#','Go','Python','Java')
#通过 current() 设置下拉菜单选项的默认值
cbox.current(3)
# 编写回调函数，绑定执行事件,向文本插入选中文本
def func(event):
    text.insert('insert',cbox.get()+"\n")
# 绑定下拉菜单事件
cbox.bind("<<ComboboxSelected>>",func)
# 新建文本框
text = tkinter.Text(win)
# 布局
text.grid(pady = 5)
win.mainloop()
		11Tkinter单选框和多选框按钮
			单选框按钮控件（Radiobutton），同样允许用户选择具体的选项值，不过与 Listbox 相比，单选按钮控件仅允许用户选择单一的选项值，各个选项值之间是互斥的关系，因此只有一个选项可以被用户选择。

Radiobutton 控件通常都是成组出现的，所有控件都使用相同的变量。Radiobutton 可以包含文本或图像，每一个按钮都可以与一个 Python 函数相关联。当按钮被按下时，对应的函数会被执行。这里需要注意的是，单选按钮控件仅能显示单一字体的文本，但文本可以跨越多行，除此之外，您还可以为个别的字符添加下划线。

Radiobutton 除常用的共有属性之外，还具有一些其他属性，如下表所示：

属性	说明
activebackground	设置当 Radiobutton 处于活动状态（通过 state 选项设置状态）的背景色，默认值由系统指定
activeforeground	设置当 Radiobutton 处于活动状态（通过 state 选项设置状态）的前景色，默认值由系统指定
compound	1. 默认值为 None，控制 Radiobutton 中文本和图像的混合模式，默认情况下，如果有指定位图或图片，则不显示文本
2. 如果该选项设置为 "center"，文本显示在图像上（文本重叠图像）
3. 设置为 "bottom"，"left"，"right" 或 "top"，那么图像显示在文本的旁边，比如如"bottom"，则显示图像在文本的下方。
disabledforeground	指定当 Radiobutton 不可用的时的前景色颜色，默认由系统指定
indicatoron	1. 该参数表示选项前面的小圆圈是否被绘制，默认为 True，即绘制；
2. 如果设置为 False，则会改变单选按钮的样式，当点击时按钮会变成 "sunken"（凹陷），再次点击变为 "raised"（凸起）
selectcolor	设置当 Radiobutton 为选中状态的时候显示的图片；如果没有指定 image 选项，该选项被忽略
takefocus	如果是 True，该组件接受输入焦点，默认为 False
variable	表示与 Radiobutton 控件关联的变量，注意同一组中的所有按钮的 variable 选项应该都指向同一个变量，通过将该变量与 value 选项值对比，可以判断用户选中了哪个按钮。
Radiobutton 控件的常用方法如下所示：

方法	说明
deselect()	取消该按钮的选中状态
flash()	刷新 Radiobutton 控件，该方法将重绘 Radiobutton控件若干次（即在"active" 和 "normal" 状态间切换）
invoke()	1. 调用 Radiobutton 中 command 参数指定的函数，并返回函数的返回值
2. 如果 Radiobutton 控件的 state(状态) 是 "disabled" （不可用）或没有指定 command 选项，则该方法无效
select()	将 Radiobutton 控件设置为选中状态
Radiobutton 控件用来解决多选一的问题，它通常是成组出现的，下面看一组简答的示例：
import tkinter as tk
window = tk.Tk()
window.title("C语言中文网")
window.geometry('400x180')
window.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# IntVar() 用于处理整数类型的变量
v = tk.IntVar()
# 根据单选按钮的 value 值来选择相应的选项
v.set(0)
# 使用 variable 参数来关联 IntVar() 的变量 v
tk.Radiobutton(window, text="C语言中文网", fg='blue',font=('微软雅黑','12','bold'),variable=v, value=0).pack(anchor = 'w')
tk.Radiobutton(window, text="CSDN平台", variable=v, value=2).pack(anchor = 'w')
tk.Radiobutton(window, text="知乎平台", variable=v, value=3).pack(anchor = 'w')
tk.Radiobutton(window, text="牛客网平台", variable=v, value=4).pack(anchor = 'w')
# 显示窗口
window.mainloop()
程序运行结果如下：


图1：tkinter Radiobutton控件

上述代码是比较直接的写法，虽然编码过程简单，但是从代码重构的角度来讲，它是比较冗余的，因此我们推荐下面这种写法，如下所示：
import tkinter as tk
window = tk.Tk()
window.title("C语言中文网")
window.geometry('400x180')
window.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
site = [('美团外卖',1),
        ('饿了么外卖',2),
        ('美团闪购',3),
        ('艾奇外卖',4)]
# IntVar() 用于处理整数类型的变量
v = tk.IntVar()
# 重构后的写法，也非常简单易懂
for name, num in site:
    radio_button = tk.Radiobutton(window,text = name, variable = v,value =num)
    radio_button.pack(anchor ='w')
# 显示窗口
window.mainloop()
程序运行结果如下：
tkinter radiobutton
图2：tkinter Radioburron控件

对上述代码稍作修改，当点击某一按钮时，获取选项的内容，代码如下：
import tkinter as tk
def select():
    dict = {1:'C语言中文网',2:'菜鸟教程',3:'W3SCHOOL',4:'微学苑'}
    strings = '您选择了' + dict.get(v.get()) + '，祝您学习愉快'
    lable.config(text = strings)
window = tk.Tk()
window.title("C语言中文网")
window.geometry('400x180')
window.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
lable = tk.Label(window,font=('微软雅黑', '15','bold'),fg='#43CD80')
lable.pack(side ='bottom')
site = [('C语言中文网',1),
        ('菜鸟教程',2),
        ('W3SCHOOL',3),
        ('微学苑',4)]
# IntVar() 用于处理整数类型的变量
v = tk.IntVar()
for name, num in site:
    radio_button = tk.Radiobutton(window,text = name, variable = v,value =num,command = select,indicatoron = False)
    radio_button.pack(anchor ='w')
# 显示窗口
window.mainloop()
程序运行结果如下：

tkinter单选按钮控件
图3：单选按钮控件
Checkbutton复选框控件
Checkbutton 控件是一种供用户选择相应条目的按钮控件，但与 Radiobutton 不同的是，Checkbutton 控件不仅允许用户选择一项，还允许用户同时选择多项，各个选项之间属于并列的关系。

复选框控件同样有许多适用场景，比如选择兴趣爱好、选择选修课，以及购买多个物品等，在这种情况下都可以使用复选框控件，其语法格式如下：
Checkbutton(master=None, **options)
复选框控件，除了具有常用的共有属性之外，还具有一些其他重要属性和常用方法，下面对它们做简单地介绍：

属性	说明
text	显示的文本，使用 "\n" 来对文本进行换行。
variable	1. 和复选框按钮关联的变量，该变量值会随着用户选择行为来改变（选或不选），即在 onvalue 和 offvalue 设置值之间切换，这些操作由系统自动完成
2. 在默认情况下，variable 选项设置为 1 表示选中状态，反之则为 0，表示不选中。
onvalue	通过设置 onvalue 的值来自定义选中状态的值。
offvalue	通过设置 offvalue 的值来自定义未选中状态的值。
indicatoron	默认为 True，表示是否绘制用来选择的选项的小方块，当设置为 False 时，会改变原有按钮的样式，与单选按钮相同
selectcolor	选择框的颜色（即小方块的颜色），默认由系统指定
selectimage	设置当 Checkbutton 为选中状态的时候显示的图片，若如果没有指定 image 选项，该选项被忽略
textvariable	Checkbutton 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容，如果变量被修改，Checkbutton 的文本会自动更新
wraplength	表示复选框文本应该被分成多少行，该选项指定每行的长度，单位是屏幕单元，默认值为 0
下面看一组简单的示例，创建一组复选框控件，代码如下：
from tkinter import *
win = Tk()
win.title("C语言中文网")
win.geometry('500x200')
win.resizable(0,0)
lb = Label(text='C语言中文网答疑辅导班',font=('微软雅黑', 18,'bold'),fg='#CD7054')
lb.pack()
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 新建整型变量
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
# 设置三个复选框控件，使用variable参数来接收变量
check1 = Checkbutton(win, text="Python",font=('微软雅黑', 15,'bold'),variable = CheckVar1,onvalue=1,offvalue=0)
check2 = Checkbutton(win, text="C语言",font=('微软雅黑', 15,'bold'),variable = CheckVar2,onvalue=1,offvalue=0)
check3 = Checkbutton(win, text="Java",font=('微软雅黑', 15,'bold'),variable = CheckVar3,onvalue=1,offvalue=0)
# 选择第一个为默认选项
# check1.select ()
check1.pack (side = LEFT)
check2.pack (side = LEFT)
check3.pack (side = LEFT)
# 定义执行函数
def study():
    # 没有选择任何项目的情况下
​    if (CheckVar1.get() == 0 and CheckVar2.get() == 0 and CheckVar3.get() == 0):
​        s = '您还没选择任语言'
​    else:
​        s1 = "Python" if CheckVar1.get() == 1 else ""
​        s2 = "C语言" if CheckVar2.get() == 1 else ""
​        s3 = "Java" if CheckVar3.get() == 1 else ""
​        s = "您选择了%s %s %s" % (s1, s2, s3)
​     #设置标签lb2的字体
​    lb2.config(text=s)
btn = Button(win,text="选好了",bg='#BEBEBE',command=study)
btn.pack(side = LEFT)

# 该标签，用来显示选择的文本
lb2 = Label(win,text='',bg ='#9BCD9B',font=('微软雅黑', 11,'bold'),width = 5,height=2)
lb2.pack(side = BOTTOM, fill = X)
# 显示窗口
win.mainloop()
程序运行结果如下：
tkinter 复选框控件
图4：复选框控件

复选框控件提供以下常用方法，如下表所示：

方法	属性
desellect()	取消 Checkbutton 组件的选中状态，也就是设置 variable 为 offvalue
flash()	刷新 Checkbutton 组件，对其进行重绘操作，即将前景色与背景色互换从而产生闪烁的效果。
invoke()	1. 调用 Checkbutton 中 command 选项指定的函数或方法，并返回函数的返回值
2. 如果 Checkbutton 的state(状态)"disabled"是 （不可用）或没有指定 command 选项，则该方法无效
select()	将 Checkbutton 组件设置为选中状态，也就是设置 variable 为 onvalue
toggle()	改变复选框的状态，如果复选框现在状态是 on，就改成 off，反之亦然
下面看一组简答的示例，如下所示：
from tkinter import *
win = Tk()
win.title("C语言中文网")
win.geometry('500x200')
win.resizable(0,0)
lb = Label(text='C语言中文网答疑辅导班',font=('微软雅黑', 18,'bold'),fg='#CD7054')
lb.pack()
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 设置三个复选框控件，
check1 = Checkbutton(win, text="Python",font=('微软雅黑', 15,'bold'),onvalue=1,offvalue=0)
check2 = Checkbutton(win, text="C语言",font=('微软雅黑', 15,'bold'),onvalue=1,offvalue=0)
check3 = Checkbutton(win, text="Java",font=('微软雅黑', 15,'bold'),onvalue=1,offvalue=0)
# 将第一个 复选框按钮的 variable值，设置为 onvalue =1 ，表示选中状态
check1.select ()
# 取消了第一个复选框的选中状态
check1.toggle()
check1.pack (side = LEFT)
check2.pack (side = LEFT)
check3.pack (side = LEFT)
# 显示窗口
win.mainloop()
程序运行结果如下：
6tkinter checkbutton
图5：tkinter复选框控件
		12Tkinter Scale控件详解
			Scale 控件，即滑块控件或标尺控件，该控件可以创建一个类似于标尺式的滑动条对象，用户通过操作它可以直接设置相应的数值（刻度值)。

Scale 控件同样有许多应用场景，并且在我们日常工作中也会经常用到，比如电脑上调节音量的滑动条（数值范围 0-100），如下图所示：

Scale控件应用场景
图1：音量控件面板

Scale 控件常用的基本属性如下所示：

参数	说明
activebackground	指定当鼠标在上方飘过的时候滑块的背景颜色
bigincrement	1. 设置“大”增长量
2. 该选项设置增长量的大小
3. 默认值是 0，增长量为范围的 1/10
borderwidth	1. 指定边框宽度
2. 默认值是 2
command	1. 指定一个函数，每当滑块发生改变的时候都会自动调用该函数
2. 该函数有一个唯一的参数，就是最新的滑块位置
3. 如果滑块快速地移动，函数可能无法获得每一个位置，但一定会获得滑块停下时的最终位置
digits	1. 设置最多显示多少位数字
2. 补充注释：例如设置 from 选项为 0，to 选项为 20，digits 选项设置为 5，那么滑块的范围就是在 0.000 ~ 20.000 直接滑动
3. 默认值是 0（不开启）
font	1. 指定滑块左侧的 Label 和刻度的文字字体
2. 默认值由系统指定
from_	1. 设置滑块最顶（左）端的位置
2. 默认值是 0
highlightcolor	1. 指定当 Scale 获得焦点的时候高亮边框的颜色
2. 默认值由系统指定
label	1. 你可以在垂直的 Scale 组件的顶端右侧（水平的话是左端上方）显示一个文本标签
2. 默认值是不显示标签
length	1. Scale 组件的长度，默认值是 100 像素
orient	1. 设置 Scale 控件是水平放置（HORIZONTAL）还是垂直放置（VERTICAL）
2. 默认值是 VERTICAL（垂直放置）
repeatdelay	1. 该选项指定鼠标左键点击滚动条凹槽的响应时间
2. 默认值是 300（毫秒）
repeatinterval	1. 该选项指定鼠标左键紧按滚动条凹槽时的响应间隔
2. 默认值是 100（毫秒）
resolution	1. 指定 Scale 组件的分辨率（每点击一下移动的步长）
示例： 比如 resolution 选项设置为 0.1 的话，那么每点击一下鼠标就是在 0.0 ~ 20.0 之间以 0.1 的步长移动
2. 该参数的默认值是 1
showvalue	1. 设置是否显示滑块旁边的数字
2. 默认值为 True
sliderlength	1. 设置滑块的长度
2. 默认值是 30 像素
state	1. 默认情况下 Scale 组件支持鼠标事件和键盘事件，可以通过设置该选项为 DISABLED 来禁用此功能
2. 默认值是 NORMAL
takefocus	1. 指定使用 Tab 键是否可以将焦点移动到该 Scale 组件上
2. 默认是开启的，可以通过将该选项设置为 False 避免焦点落在此组件上
tickinterval	1. 设置显示的刻度，如果设置一个值，那么就会按照该值的倍数显示刻度
2. 默认值是不显示刻度
to	1. 设置滑块最底（右）端的位置
2. 默认值是 100
troughcolor	1. 设置凹槽的颜色
2. 默认值由系统指定
variable	1. 指定一个与 Scale 组件相关联的 Tkinter 变量，该变量存放滑块最新的位置
2. 当滑块移动的时候，该变量的值也会发生相应的变化
width	1. 指定 Scale 组件的宽度
2. 默认值是 15 像素
Scale 常用方法有如下四个，见下表所示：

方法	说明
coords(value=None)	1. 获得当前滑块位置相对于 Scale 控件左上角位置的相对坐标，
2. 如果设置了 value 值，则返回当滑块位于该位置时与左上角的相对坐标
get()	获得当前滑块的位置（即当前数值），返回值可以为整型或者浮点型
identify(x, y)	返回一个字符串表示指定位置下的 Scale 控件
set(value)	设置 Scale 控件的值，即滑块的位置，默认为初始位置
下面看一组简单的实例应用：创建一个 Scale 控件
from tkinter import *
# 创建主窗口
win =Tk()
win.title("控制管理界面")
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
win.geometry('400x250')
# 添加一个 Scale 控件，默认垂直方向，步长设置为 5，长度为200，滑动块的大小为 50，最后使用label参数文本
s=Scale(win, from_ =100, to =0,resolution =5,length =200,sliderlength= 20,label ='音量控制' )
s.pack()
# 设置滑块的位置
s.set(value=15)
# 显示窗口
mainloop()
程序运行结果如下：
tkinter scale控件
图1：音量控制界面

下面看一个稍微复杂点的应用示例，代码如下：
import tkinter as tk
window = tk.Tk()
window.title("购物车界面")
window.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
window.geometry('450x200+450+250')
window.resizable(0,0)
# 创建一个文本标签
label = tk.Label(window, bg='#9FB6CD',width=18, text='')
label.grid(row =2)
# 创建执行函数
def select_price(value):
    label.config(text='您购买的数量是 ' + value)
# 创建 Scale控件
scale = tk.Scale(window,
             label='选择您要购买的数量',
             from_=1,
             to= 100,
             orient=tk.HORIZONTAL,   # 设置Scale控件平方向显示
             length=400,
             tickinterval=9,       # 设置刻度滑动条的间隔
             command=select_price)  # 调用执行函数，是数值显示在 Label控件中
scale.grid(row =1)
# 显示窗口
window.mainloop()
程序运行结果如下：
tkinter scale控件
图2：tkinter Scale控件示例
		13Tkinter Canvas画布控件
			Canvas 控件具有两个功能，首先它可以用来绘制各种图形，比如弧形、线条、椭圆形、多边形和矩形等，其次 Canvas 控件还可以用来展示图片（包括位图），我们将这些绘制在画布控件上的图形，称之为“画布对象”。
每一个画布对象都有一个“唯一身份ID”，这是 Tkinter 自动为其创建的，从而方便控制和操作这些画布对象。

通过 Canvas 控件创建一个简单的图形编辑器，让用户可以达到自定义图形的目的，就像使用画笔在画布上绘画一样，可以绘制各式各样的形状，从而有更好的人机交互体验。
Canvas控件基本属性
下面对 Canvas 控件的常用属性做简单的介绍，如下表所示：

属性	方法
background(bg)	指定 Canvas 控件的背景颜色
borderwidth(bd)	指定 Canvas 控件的边框宽度
closeenough	1. 指定一个距离，当鼠标与画布对象的距离小于该值时，认为鼠标位于画布对象上
2. 该选项是一个浮点类型的值
confine	1. 指定 Canvas 控件是否允许滚动超出 scrollregion 选项设置的滚动范围，默认值为 True
selectbackground	指定当画布对象（即在 Canvas 画布上绘制的图形）被选中时的背景色，
selectborderwidth	指定当画布对象被选中时的边框宽度（选中边框）
selectforeground	指定当画布对象被选中时的前景色
state	设置 Canvas 的状态："normal" 或 "disabled"，默认值是 "normal"，注意，该值不会影响画布对象的状态
takefocus	指定使用 Tab 键可以将焦点移动到输入框中，默认为开启，将该选项设置为 False 避免焦点在此输入框中
width	指定 Canvas 的宽度，单位为像素
xscrollcommand	与 scrollbar（滚动条）控件相关联（沿着 x 轴水平方向）
xscrollincrement	1. 该选项指定 Canvas 水平滚动的“步长”
2. 例如 '3c' 表示 3 厘米，还可以选择的单位有 'i'（英寸），'m'（毫米）和 'p'（DPI，大约是 '1i' 等于 '72p'）
3. 默认为 0，表示可以水平滚动到任意位置
yscrollcommand	与 scrollbar 控件（滚动条）相关联（沿着 y 轴垂直方向）
yscrollincrement	1. 该选项指定 Canvas 垂直滚动的“步长”
2. 例如 '3c' 表示 3 厘米，还可以选择的单位有 'i'（英寸），'m'（毫米）和 'p'（DPI，大约是 '1i' 等于 '72p'）
3. 默认值是 0，表示可以垂直方向滚动到任意位置
上述属性是用来设置 Canvas 控件的，下面示例定义了出一张画布（Canvas），如下所示：
import tkinter as tk
window = tk.Tk()
window.title("C语言中文网")
window.geometry('400x200')
# 创库不允许改变
window.resizable(0,0)
window.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 创建画布
canvas = tk.Canvas(window,
                   bg='#CDC9A5',
                   height=200,
                   width=300)
canvas.pack()
window.mainloop()
程序运行结果如下：


tkinter canvas画布
图1：tkinter Canvas控件

Canvas控件绘图常用方法
Cansvas 控件提供了一系列绘制几何图形的常用方法，下面对这些方法做简单介绍:


方法	说明
create_line(x0, y0, x1, y1, ... , xn, yn, options)	1. 根据给定的坐标创建一条或者多条线段；
2. 参数 x0,y0,x1,y1,...,xn,yn 定义线条的坐标；
3. 参数 options 表示其他可选参数
create_oval(x0, y0, x1, y1, options)	1. 绘制一个圆形或椭圆形；
2. 参数 x0 与 y0 定义绘图区域的左上角坐标；参数 x1 与 y1 定义绘图区域的右下角坐标；
3. 参数 options 表示其他可选参数
create_polygon(x0, y0, x1, y1, ... , xn, yn, options)	1. 绘制一个至少三个点的多边形；
2. 参数 x0、y0、x1、y1、...、xn、yn 定义多边形的坐标；
3. 参数 options 表示其他可选参数
create_rectangle(x0, y0, x1, y1, options)	1. 绘制一个矩形；
2. 参数 x0 与 y0 定义矩形的左上角坐标；参数 x 与 y1 定义矩形的右下角坐标；
3. 参数 options 表示其他可选参数
create_text(x0, y0, text, options)	1. 绘制一个文字字符串。其中
2. 参数 x0 与 y0 定义文字字符串的左上角坐标，参数 text 定义文字字符串的文字；
3. 参数 options 表示其他可选参数
create_image(x, y, image)	1. 创建一个图片;
2. 参数 x 与 y 定义图片的左上角坐标；
3. 参数 image 定义图片的来源，必须是 tkinter 模块的 BitmapImage 类或 PhotoImage 类的实例变量。
create_bitmap(x, y, bitmap)	1. 创建一个位图；
2. 参数 x 与 y 定义位图的左上角坐标；
3. 参数 bitmap 定义位图的来源，参数值可以是 gray12、gray25、gray50、gray75、hourglass、error、questhead、info、warning 或 question，或者也可以直接使用 XBM（X Bitmap）类型的文件，此时需要在 XBM 文件名称前添加一个 @ 符号，例如 bitmap=@hello.xbm
create_arc(coord, start, extent, fill)	1. 绘制一个弧形；
2. 参数 coord 定义画弧形区块的左上角与右下角坐标；
3. 参数 start 定义画弧形区块的起始角度（逆时针方向）；
4. 参数 extent 定义画弧形区块的结束角度（逆时针方向）；
5. 参数 fill 定义填充弧形区块的颜色。
注意：上述方法都会返回一个画布对象的唯一 ID。关于 options 参数，下面会通过一个示例对经常使用的参数做相关介绍。（但由于可选参数较多，并且每个方法中的参数作用大同小异，因此对它们不再逐一列举）

从上述表格不难看出，Canvas 控件采用了坐标系的方式来确定画布中的每一点。一般情况下，默认主窗口的左上角为坐标原点，这种坐标系被称作为“窗口坐标系”，但也会存在另外一种情况，即画布的大小可能大于主窗口，当发生这种情况的时，可以采用带滚动条的 Canvas 控件，此时会以画布的左上角为坐标原点，我们将这种坐标系称为“画布坐标系”。
1) 绘制直线
下面示例展示了如何在画布（Canvas控件）上绘制一条虚线和实线，代码如下：
from tkinter import *
root = Tk()
# 设置窗口的背景颜色以区别画布
root.config(bg='#87CEEB')
root.title("C语言中文网")
root.geometry('450x350')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 设置画布的背景颜色为白色
cv=Canvas(root,bg="white",width =300, height = 250)
# 将控件放置在主窗口中
cv.pack()
# 设置坐标点,此处可以元组的形式来设置坐标点
point=[(10,20),(20,30),(30,40),(40,100),(80,120),(150,90)]
# 创建画布，添加线条
# fill 参数指定填充的颜色，如果为空字符串，则表示透明
# dash 参数表示用来绘制虚线轮廓，元组参数，分别代表虚线中线段的长度和线段之间的间隔
# arrow 设线段的箭头样式，默认不带箭头，参数值 first 表示添加箭头带线段开始位置，last表示到末尾占位置，both表示两端均添加
# smooth 布尔值参数，表示是否以曲线的样式划线，默认为 False
# width 控制线宽
line1=cv.create_line(point,fill="purple",dash=(1,1),arrow=LAST,width=5)
print('线段line1的画布id号:',line1)
line2=cv.create_line(point,fill="red",arrow=BOTH,smooth=TRUE,width=5)
print('线段line2的画布id号:',line2)
# 移动其中一条线段，只需要更改其坐标就可以,使用 coords()方法移动曲线
cv.coords(line2,50,30,25,35,35,40,50,120,60,170,10,180)
# 显示窗口
root.mainloop()
程序运行的最终结果，见下图：
tkinter canvas控件
图1：tkinter Canvas控件


上述示例中涉及了一部分参数，比如 fill、dash、arrow 等，下表对 create_line() 函数的相关参数做了简单介绍：

属性	说明
activedash	当画布对象状态为 "active" 的时候，绘制虚线
activefill	当画布对象状态为 "active" 的时候，填充颜色
activestipple	当画布对象状态为 "active" 的时候，指定填充的位图
activewidth	当画布对象状态为 "active" 的时候，指定边框的宽度
arrow	1. 默认线段是不带箭头的，通过设置该选项添加箭头到线段中
2. "first" 表示添加箭头到线段开始的位置
3. "last" 表示添加箭头到线段结束的位置
4. "both" 表示两端均添加箭头
arrowshape	1. 用一个三元组来指定箭头的形状，默认值是 (8, 10, 3)，元组中的数值分别代表箭头中三条边的长度
capstyle	1. 指定线段两端的样式，默认值是 "butt"
2. 该选项的值可以是：
"butt"（线段的两段平切于起点和终点）
"projecting"（线段的两段在起点和终点的位置将 width 选项设置的长度分别延长一半）
"round"（线段的两段在起点和终点的位置将 width设置的长度分别延长一半，并以圆角进行绘制）
dash	绘制虚线，该选项值是一个整数元组，元组中的元素分别代表短线的长度和间隔，比如 (3, 5) 代表 3 个像素的短线和 5 个像素的间隔
dashoffset	指定虚线开始的偏移位置，比如 dash=(5, 1, 2, 1)，dashoffset=3，则从 2 开始画虚线
disableddash	当画布对象状态为 "disabled" 的时候，绘制虚线
disabledfill	当画布对象状态为 "disabled" 的时候，填充颜色
disabledstipple	当画布对象状态为 "disabled" 的时候，指定填充的位图
disabledwidth	当画布对象状态为 "disabled" 的时候，指定边框的宽度
fill	1. 指定填充的颜色，空字符串表示透明
joinstyle	1. 指定当绘制两个相邻线段之间时接口的样式，默认为 "round"
2. 该选项的值可以是：
"round"（以连接点为圆心，1/2 width 选项设置的长度为半径来绘制圆角）
"bevel"（在连接点处将两线段的夹角做平切操作）
"miter"（沿着两线段的夹角延伸至一个点）
offset	指定当点画模式时填充位图的偏移
smooth	默认值为 False，若设置为 True，表示将以曲线的样式代替所绘线段
splinesteps	当绘制曲线的时，该选项指定由多少条折线来构成曲线，默认值是 12，这里需要注意，只有当 smooth 选项为 True 时该选项才会生效。
state	指定该画布对象的状态，默认值为 "normal"，参数值有 "normal"，"disabled"（不可用）和 "hidden"（隐藏）三种状态。
stipple	指定一个位图进行填充，默认值为空字符串，表示实心
tags	为创建的画布对象添加标签
width	指定边框的宽度
对于扇形、矩形、三角形、圆形等，这些封闭式图形，它们由轮廓线和填充颜色两部分组成。在绘制这些图形时相关函数的可选参数与上述表格也存在略微差异，下面以绘制扇形的 create_arc() 函数为例做简单的介绍：

属性	方法
activedash	当画布对象状态为 "active" 的时候，绘制虚线
activefill	当画布对象状态为 "active" 的时候，填充颜色
activeoutline	当画布对象状态为 "active" 的时候，绘制轮廓线
activeoutlinestipple	当画布对象状态为 "active" 的时候，指定填充轮廓的位图
activestipple	当画布对象状态为 "active" 的时候，指定填充的位图
activewidth	当画布对象状态为 "active" 的时候，指定边框的宽度
dash	指定绘制虚线轮廓，与绘制线段的含义相同
dashoffset	指定虚线轮廓开始的偏移位置
disableddash	当画布对象状态为 "disabled" 的时候，绘制虚线
disabledfill	当画布对象状态为 "disabled" 的时候，填充颜色
disabledoutline	当画布对象状态为 "disabled" 的时候，绘制轮廓线
disabledoutlinestipple	当画布对象状态为 "disabled" 的时候，指定填充轮廓的位图
disabledstipple	当画布对象状态为 "disabled" 的时候，指定填充的位图
disabledwidth	当画布对象状态为 "disabled" 的时候，指定边框的宽度
extent	指定跨度（从 start 选项指定的位置开始到结束位置的角度）默认值是 90.0
fill	与上述表格的含义相同，表示指定的填充颜色，若为空字符串则为透明色
offset	指定当点画模式时填充位置的偏移，参数值为 "x,y"坐标偏移和位置偏移两种方式，比如 "ne"/"e" 等
outline	指定轮廓的颜色
outlineoffset	指定当点画模式绘制轮廓时位图的偏移
outlinestipple	当 outline 选项被设置时，该选项用于指定一个位图来填充边框，默认值是空字符串，表示黑色
start	指定起始位置的偏移角度
style	 默认创建的是扇形，指定该方法创建的是扇形（"pieslice"）、弓形（"chord"）还是弧形（"arc"）
tags	为创建的画布对象添加标签
width	指定边框的宽度
在实际的使用的过程中经常用到的参数有 dash、fill、outline、extend 和 start，但是这么多的参数我们也不可能都记住，这时查手册是一种很好的方法，官网文档地址：点击前往。

下面让我们来一组绘制几何图形的简单示例：
from tkinter import *
root = Tk()
# 设置主窗口区的背景颜色以区别画布区的颜色
root.config(bg='#8DB6CD')
root.title("C语言中文网")
root.geometry('500x400')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 将画布设置为白色
canvas = Canvas(root,width = 400,height = 400,bg='white')
# 设置基准坐标
x0,y0,x1,y1 = 10,10,80,80
# 绘制扇形,起始角度为 0 度，结束角度为 270, 扇形区域填充色为淡蓝色，轮廓线为蓝色，线宽为 2px
arc = canvas.create_arc(x0, y0, x1, y1,start = 0, extent = 270, fill = '#B0E0E6',outline ='blue',width = 2)
# 绘制圆形
oval = canvas.create_oval(x0+150, y0, x1+150, y1,fill ='#CD950C',outline = 'blue',width=2)
# 绘制矩形,并将轮廓线设置为透明色，即不显示最外围的轮廓线，默认为黑色
rect = canvas.create_rectangle(x0,y0+100,x1,y1+100,fill='red',outline = '')
# 绘制一个三角形，填充色为绿色
trigon = canvas.create_polygon(80,80,150,80,200,200, outline="", fill="green",)
# 当然也可以绘制一个任意多边形，只要你的坐标正确就可以
# 绘制一个多边形，首先定义一系列的多边形上的坐标点
poly_points=[(0,280),(140,200),(140,240),(270,240),(270,320),(140,320),(140,360)]
polygon = canvas.create_polygon(poly_points,fill="#BF3EFF")
# 放置画布在主窗口
canvas.pack()
# 显示窗口
root.mainloop()
程序运行结果如下所示：


tkinter canvas画布控件
图2：tkinter绘制几何图形

注意：create_rectangle() 方法的前两个参数决定了矩形的左上角坐标，后两个参数决定了矩形的右下角坐标；另外 create_oval() 方法并不是只能绘制圆形，还能绘制椭圆形，这取决于传入的参数。

除了能够绘制几何图形之外，Tkinter 还可以展示图片、创建位图以及文本信息等，示例如下所示：
from tkinter import *
root=Tk()
# # 设置主窗口区的背景颜色以区别画布区的颜色
root.config(bg='#8DB6CD')
root.title("C语言中文网")
root.geometry('500x300')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# # 将画布设置为白色
cv = Canvas(root,bg='white')
# tkinter 提供的内置位图名称
bitmaps = ["error", "gray75", "gray50", "gray25", "gray12",
"hourglass", "info", "questhead", "question", "warning"]
# 列出所有的位图样式
for i in range(len(bitmaps)):
    # 前两个参数指定一个位图的位置，后续依次排列
    cv.create_bitmap((i+1)*30,30,bitmap=bitmaps[i])
#并在画布上添加文本
# 参数说明，前两个参数（x0，y0）参照点，指定文字字符串的左上角坐标
# anchor 指定了文本的对于参照点的相对位置，以方位来指定,比如 W/E/N/S等
cv.create_text(30,80,text = "tkinter内置位图预览",fill ='#7CCD7C',anchor = W,font =('微软雅黑',15,'bold'))
# 展示图片，使用 PhotoImage()来加载图片
img = PhotoImage (file="C:/Users/Administrator/Desktop/c.biancheng.gif")
cv.create_image(30,150,image = img,anchor =W)
cv.create_text(30,220,text = "图片预览",fill ='#7CCD7C',anchor = W,font =('微软雅黑',15,'bold'))
cv.pack()
mainloop()
程序运行结果如下：
tkinter canvas画布控件
图3：tkinter Canvas控件

注意，添加到 Canvas 上的对象会一直保留直着。如果你希望修改它们，您可以使用 coords() 和 move() 方法来移动画布上的对象，当然您可以使用 delete() 来删除它们，示例如下：
from tkinter import *
root=Tk()
# # 设置主窗口区的背景颜色以区别画布区的颜色
root.config(bg='#8DB6CD')
root.title("C语言中文网")
root.geometry('500x300')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 定义移动函数
def move_img():
    # 定义移动坐标
    cv.move(image1,50,30)
# # 将画布设置为白色
cv = Canvas(root,bg='white')
# 使用 PhotoImage()来加载图片
img = PhotoImage (file="C:/Users/Administrator/Desktop/c.biancheng.gif")
image1=cv.create_image(30,150,image = img,anchor =W)
# 将按钮放置在画布中
btn=Button(cv,text="点击移动画布",bg="#8A8A8A",activebackground="#7CCD7C",command=move_img)
# 在指定位置创建一个窗口控件，tags来添加标签
cv.create_window(365,250,height=30,width=30,window=btn)
# 调用delete() 删除画布对象,若传入ALL，则删除所有的画布对象
#cv.delete(image1)
cv.pack()
# 显示窗口
root.mainloop()
程序运行结果如下：
tkinter canvas控件
图4：移动画布对象
		14Tkinter Menu菜单控件
			Menu 控件（菜单控件）可以说是 GUI 中“精髓所在”，它以可视化的方式将一系列的“功能选项卡”进行分组，并在每个分组下又“隐藏”了许多其他的“选项卡”。当打开菜单时，这些选项卡就会“显式”的呈现出来，方便用户进行选择，比如 Windows 系统中记事本文件（.txt文件类型）的界面：

menu菜单控件
图1：Menu菜单界面

通过使用菜单控件（Menu）可以充分地节省有限的窗口区域，让我们的界面更加简洁优雅，避免臃肿、混乱。 

Tkinter Menu 控件提供了三种类型的菜单，分别是：topleve（主目录菜单）、pull-down（下拉式菜单）、pop-up（弹出式菜单，或称快捷式菜单）。

下表列出创建菜单时用到的相关方法，如下所示：

方法	说明
add_cascade(**options)	添加一个父菜单，将一个指定的子菜单，通过 menu 参数与父菜单连接，从而创建一个下拉菜单。
add_checkbutton(**options)	添加一个多选按钮的菜单项
add_command(**options)	 添加一个普通的命令菜单项
add_radiobutton(**options)	添加一个单选按钮的菜单项
add_separator(**options)	 添加一条分割线
add(add(itemType, options))	添加菜单项，此处 itemType 参数可以是以下几种："command"、"cascade"，
"checkbutton"、"radiobutton"、"separator" 五种，并使用 options 选项来设置
菜单其他属性。
除了上述方法之外，Menu 控件也提供了一些其他方法来操作菜单项，比如删除菜单项、获取菜单项、设置指定的菜单项等，如下表所示：

方法	说明
delete(index1, index2=None)	1. 删除 index1 ~ index2（包含）的所有菜单项
2. 如果忽略 index2 参数，则删除 index1 指向的菜单项
entrycget(index, option)	获得指定菜单项的某选项的值
entryconfig(index, **options)	设置指定菜单项的选项
index(index)	返回与 index 参数相应的选项的序号
insert(index, itemType, **options)	插入指定类型的菜单项到 index 参数指定的位置，类型可以是
是："command"，"cascade"，"checkbutton"，"radiobutton"
或 "separator" 中的一个，或者也可以使用 insert_类型() 形式来，
比如 insert_cascade(index, **options)..等
invoke(index)	调用 index 指定的菜单项相关联的方法
post(x, y)	在指定的位置显示弹出菜单
type(index)	获得 index 参数指定菜单项的类型
unpost()	移除弹出菜单
yposition(index)	返回 index 参数指定的菜单项的垂直偏移位置
下面对 Menu 控件的 options 参数做简单地介绍，如下所示：

属性	说明
accelerator	1. 设置菜单项的快捷键，快捷键会显示在菜单项目的右边，比如 accelerator = "Ctrl+O" 表示打开；
2. 注意，此选项并不会自动将快捷键与菜单项连接在一起，必须通过按键绑定来实现
command	选择菜单项时执行的 callback 函数
label	定义菜单项内的文字
menu	此属性与 add_cascade() 方法一起使用，用来新增菜单项的子菜单项
selectcolor	指定当菜单项显示为单选按钮或多选按钮时选择中标志的颜色
state	定义菜单项的状态，可以是 normal、active 或 disabled
onvalue/offvalue	1. 默认情况下，variable 选项设置为 1 表示选中状态，反之设置为 0，设置 offvalue/onvalue 的值可以自定义未选中状态的值
2. 
tearoff	1. 如果此选项为 True，在菜单项的上面就会显示一个可选择的分隔线；
2. 注意：分隔线会将此菜单项分离出来成为一个新的窗口
underline	设置菜单项中哪一个字符要有下画线
value	1. 设置按钮菜单项的值
2. 在同一组中的所有按钮应该拥有各不相同的值
3. 通过将该值与 variable 选项的值对比，即可判断用户选中了哪个按钮
variable	当菜单项是单选按钮或多选按钮时，与之关联的变量
1）创建主目录菜单
主目录菜单也称之为“顶级菜单”，下拉菜单等其他子菜单的都需要建立在“顶级菜单”的基础之上，下面示例创建了一个类似于“记事本”界面的程序，代码如下：
from tkinter import *
import tkinter . messagebox
#创建主窗口
win = Tk()
win.config(bg='#87CEEB')
win.title("C语言中文网")
win.geometry('450x350+300+200')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 绑定一个执行函数，当点击菜单项的时候会显示一个消息对话框
def menuCommand() :
    tkinter.messagebox.showinfo("主菜单栏","你正在使用主菜单栏")
# 创建一个主目录菜单，也被称为顶级菜单
main_menu = Menu (win)
#新增命令菜单项，使用 add_command() 实现
main_menu.add_command (label="文件",command=menuCommand)
main_menu.add_command (label="编辑",command=menuCommand)
main_menu.add_command (label="格式",command=menuCommand)
main_menu.add_command (label="查看",command=menuCommand)
main_menu.add_command (label="帮助",command=menuCommand)
#显示菜单
win.config (menu=main_menu)
win.mainloop()
程序 运行结果如下：
tkinter menu控件
图2：Menu 控件创建主菜单

如上图所示，当点击主目录中的任意一个菜单选项时都会跳出一个消息对话框。
2) 创建下拉菜单
下拉菜单时主菜单的重要组成部分，也是用户选择相关命令的重要交互界面，下拉菜单的创建方式也非常简单，不过需要我们注意，下拉菜单是建立的主菜单（即顶级菜单）的基础之上的，并非主窗口之上，这一点千万不要搞混，否则创建下拉菜单会失败。

下面继续仿照“记事本”的相关功能来创建下拉菜单，示例如下：
#创建一个下拉式菜单
from tkinter import *
import tkinter .messagebox
#创建主窗口
win = Tk()
win.config(bg='#87CEEB')
win.title("C语言中文网")
win.geometry('450x350+300+200')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
#创建一个执行函数，点击下拉菜单中命令时执行
def menuCommand() :
    tkinter .messagebox .showinfo("下拉菜单", "您正在使用下拉菜单功能")
#创建主目录菜单（顶级菜单）
mainmenu = Menu (win)
#在顶级菜单上新增"文件"菜单的子菜单，同时不添加分割线
filemenu = Menu (mainmenu, tearoff=False)
#新增"文件"菜单的菜单项，并使用 accelerator 设置菜单项的快捷键
filemenu.add_command (label="新建",command=menuCommand,accelerator="Ctrl+N")
filemenu.add_command (label="打开",command=menuCommand, accelerator="Ctrl+O")
filemenu.add_command (label="保存",command=menuCommand, accelerator="Ctrl+S")
# 添加一条分割线
filemenu.add_separator ()
filemenu.add_command (label="退出",command=win. quit)
#在主目录菜单上新增"文件"选项，并通过menu参数与下拉菜单绑定
mainmenu.add_cascade (label="文件",menu=filemenu)
# 将主菜单设置在窗口上
win.config (menu=mainmenu)
# 绑定键盘事件，按下键盘上的相应的键时都会触发执行函数
win.bind ("<Control-n>",menuCommand)
win. bind ("<Control-N>", menuCommand)
win.bind ("<Control-o>",menuCommand)
win. bind ("<Control-O>", menuCommand)
win. bind ("<Control-s>", menuCommand)
win.bind ("<Control-S>",menuCommand)
# 显示主窗口
win.mainloop()
程序运行解结果如下：
tkinter menu控件
图3：Menu 控件下拉菜单

3) 创建弹出菜单栏
弹出式菜单栏，也称为快捷式菜单栏，比如通过点击鼠标右键弹出一个菜单栏，其中包含一些常用的选项卡，如复制、粘贴等，如下所示：在记事本的空白处点击鼠标右键会弹出一个菜单栏。

弹出式菜单栏
图4：弹出式菜单栏

Tkinter Menu 控件同样可以是实现上述功能，而且并不复杂，示例如下：
import tkinter as tk
root = tk.Tk()
root.config(bg='#8DB6CD')
root.title("C语言中文网")
root.geometry('400x300')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
def func():
    print('您通过弹出菜单执行了命令')
# 创建一个弹出菜单
menu = tk.Menu(root, tearoff=False)
menu.add_command(label="新建", command=func)
menu.add_command(label="复制", command=func)
menu.add_command(label="粘贴", command=func)
menu.add_command(label="剪切", command=func)
# 定义事件函数
def command(event):
    # 使用 post()在指定的位置显示弹出菜单
    menu.post(event.x_root, event.y_root)

# 绑定鼠标右键，这是鼠标绑定事件
# <Button-3>表示点击鼠标的右键，1 表示左键，2表示点击中间的滑轮
root.bind("<Button-3>", command)
root.mainloop()
程序运行结果如下：
tkinter menu弹出菜单
图5：Menu控件弹出菜单
4) 菜单按钮控件
Menubutton（菜单按钮控件）是一个与 Menu 控件相关联的按钮，当我们按下按钮的时候下拉菜单就会自动弹出。通过 Menubutton 创建的菜单按钮可以自由地放置在窗口中的任意位置，从而提高了 GUI 界面的灵活性。

下面看一组简单使用示例：
from tkinter import *
win=Tk()
win.config(bg='#87CEEB')
win.title("C语言中文网")
win.geometry('450x350+300+200')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
#创建一个菜单按钮
menubtn=Menubutton(win, text='点击进行操作', relief='sunk')
# 设置位置（布局）
menubtn.grid(padx=195, pady=105)
#添加菜单,使用 tearoff 参数不显示分割线
filemenu=Menu(menubtn,tearoff = False)
filemenu.add_command(label='新建')
filemenu.add_command(label='删除')
filemenu.add_command(label='复制')
filemenu.add_command(label='保存')
# 显示菜单，将菜单命令绑定在菜单按钮对象上
menubtn.config(menu=filemenu)
win.mainloop()
程序运行结果如下：
tkinter Menubutton
图6：Menubutton菜单按钮
		15Tkinter Scrollbar滚动条控件
			Scrollbar 控件常用于创建一个水平或者垂直的滚动条，通常情况下，Scrollbar 控件可以与 Listbox、Text、Canvas 以及 Entry 等控件一起使。

滚动条控件是 GUI  程序中经常使用的一种控件类型，它主要用来控制控件区域的可见范围，比如当 Text 控件的文本内容非常多时，为了方便用户阅读，可以给 Text 控件增加滚动条，用户只需拖动滚动条就能完成内容的阅读。

Scrollbar 控件的常用属性，如下表所示：

属性	说明
activebackground	指定当鼠标在上方飘过的时候滑块和箭头的背景颜色，默认由系统决定
activerelief	指定当鼠标在滑块上方飘过时滑块的样式，默认值是 "raised"，其他可选值有 "flat"，"sunken"，"groove"，"ridge"
background(bg)	指定背景颜色，默认值由系统指定
borderwidth(bd)	指定边框宽度，默认值是 0
command	当滚动条更新时回调的函数，通常指定对应组件的 xview() 或 yview() 方法
cursor	指定当鼠标在上方飘过的时的鼠标样式，默认值由系统指定
elementborderwidth	1. 指定滚动条和箭头的边框宽度
2. 默认值是 -1（表示使用 borderwidth 选项的值）
jump	1. 指定当用户拖拽滚动条时的行为
2. 默认值为 False，滚动条的任何一丝变动都会即刻调用 command 指定的回调函数
3. 设置为 True 则当用户松开鼠标才调用
orient	指定绘制 "horizontal"（垂直滚动条）还是 "vertical"（水平滚动条），默认值是 VERTICAL
repeatdelay	该选项指定鼠标左键点击滚动条凹槽的响应时间，默认值是 300（毫秒）
repeatinterval	该选项指定鼠标左键紧按滚动条凹槽时的响应间隔，默认值是 100（毫秒）
takefocus	指定使用 Tab 键可以将焦点移到该 Scrollbar 组件上，默认为开启，可以将该选项设置为 False 避免焦点在此组件上
troughcolor	指定凹槽的颜色，默认由系统指定
width	指定滚动条的宽度,默认值是 16px
下面是介绍了 Scrollbar 控件常用的函数：

属性	说明
activate(element) 	1. 显示 element 参数指定的元素的背景颜色和样式;
2. element 参数可以设置为："arrow1"（箭头1），"arrow2"（箭头2）或 "slider"（滑块）
delta(deltax, deltay)	1. 给定一个鼠标移动的范围 deltax 和 deltay，然后该方法返回一个浮点类型的值（范围 -1.0 ~ 1.0）
2. 注意：deltax 表示水平移动量，deltay 表示垂直移动量
fraction(x, y)	给定一个像素坐标 (x, y)，该方法返回最接近给定坐标的滚动条位置。
get()	 返回当前滑块的位置 (a, b)，其中 a 值表示当前滑块的顶端或左端的位置，b 值表示当前滑块的底端或右端的位置。
identify(x, y)	1. 返回一个字符串表示指定位置下（如果有的话）的滚动条部件，
2. 返回值可以是："arrow1"（箭头1），"arrow2"（箭头2）、"slider"（滑块）或 ""（空）
set(*args)	1. 设置当前滚动条的位置
2. 该方法有两个参数即 (first, last)，其中 first 表示当前滑块的顶端或左端的位置，last 表示当前滑块的底端或右端的位置（范围 0.0 ~ 1.0）
下面看一组简单的示例：
import tkinter as tk
root = tk.Tk()
root.title("C语言中文网")
root.geometry('450x180+300+200')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 创建一个滚动条控件，默认为垂直方向
sbar1= tk.Scrollbar(root)
# 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
sbar1.pack(side=RIGHT, fill=Y)
# 创建水平滚动条，默认为水平方向,当拖动窗口时会沿着X轴方向填充
sbar2 = Scrollbar (root, orient=HORIZONTAL)
sbar2.pack(side=BOTTOM, fill=X)
# 创建列表框控件,并添加两个滚动条（分别在垂直和水平方向），使用 set() 进行设置
mylist = tk.Listbox(root,xscrollcommand = sbar2.set,yscrollcommand = sbar1.set)
for i in range(30):
    mylist.insert(END,'第'+ str(i+1)+'次:'+'C语言中文网，网址为：c.biancheng.net'+ '\n' )
# 当窗口改变大小时会在X与Y方向填满窗口
mylist.pack(side=LEFT,fill = BOTH)
# 使用 command 关联控件的 yview、xview方法
sbar1.config(command =mylist.yview)
sbar2.config(command = mylist.xview)
#  显示主窗口
root.mainloop()
程序运行结果：
tkinter scrollbar控件
图1：Scrollbar控件
通过滑动滚动条可以浏览列表框中的内容，垂直方向的滚动条沿着上下浏览，水平方向的滚动条则沿着左右方向浏览。
		16Tkinter Event事件处理
			事件处理，是 GUI 程序中不可或缺的重要组成部分，相比来说，控件只是组成一台机器的零部件， 而事件处理则是驱动这台机器“正常”运转的关键所在，它能够将零部件之间“优雅”的贯穿起来，因此“事件处理”可谓是 GUI 程序的“灵魂”，同时它也是实现人机交互的关键。
对于“事件”这一名词，在讲解控件时也偶尔提及过，在本节我们将对 Tkinter 中的事件处理机制做更为详细的介绍。

在一款 GUI 程序中，我们将用户对软件的操作统称为“事件”，比如鼠标点击按钮、键盘输入文本以及窗口管理器触发的重绘事件等，这些事件有一个共同的特点，即都是由用户直接或者间接触发的。
事件绑定方法
Tkinter 提供的事件处理机制允许我们为“控件”绑定相应的事件和事件处理函数（即 callback函数），从而实现控件与用户的交互，其语法格式如下：
widget.bind("<event>",func)
上述语法中，widget 代表控件的实例对象，之后，采用 bind() 方法进行事件绑定，该函数有两个参数：
<event>：一个字符串参数，表示事件的类型，并使用“尖括号”的形式进行包裹；
func：表示事件的处理函数（callback，即回调函数），当触发事件时，Tk 会携带事件对象（Event）去调用 func 方法。

注意：bind() 方法可以完成事件与处理函数绑定，而使用 unbind() 方法可以将事件与处理函数解绑。
常用事件类型
事件类型（也称事件码）是 Tkinter 模块规定的，主要包括鼠标、键盘、光标等相关事件，Tkinter 为其规定了相应的语法格式：
<modifier-type-detail>
上述语法由三部分组成，说明如下：
<>：事件类型必须包含在“尖括号”内；
modifier：可选项，事件类型的修饰符，通常用于描述组合键、双击<Double-Button-1>、大写锁定键<Lock>以及<Alt-Shift>等；
type：是必不可少的一项，表示事件的具体类型；
detail：可选项，通常用于描述具体的哪个按键，比如 <Button-1> 表示鼠标左键；

这里有必要对经常使用的 modifier 修饰符做简单的介绍，修饰符可以修改事件的激活条件，比如双击鼠标或者需要同时按下某个键才触发事件，常用的修饰符如下：

修饰符	说明
Control	事件发生时需按下 Control 键
Alt	事件发生时需按下 Alt 键
Shift	事件发生时需按下 Shift 键
Lock	事件发生时需处于大写锁定状态
Double	事件连续发生两次，比如双击鼠标
Triple	事件连续发生三次
Quadruple	事件连续发生四次
下述表格中介绍了 Tkinter 中经常使用的事件类型，如下所示：

事件码	说明
<ButtonPress-1>	单击鼠标左键，简写为<Button-1>，后面的数字可以是1/2/3，分别代表左键、中间滑轮、右键
<ButtonRelease-1>	释放鼠标左键，后面数字可以是1/2/3，分别代表释放左键、滑轮、右键
<B1-Motion>	按住鼠标左键移动，<B2-Motion>和<B3-Motion>分别表示按住鼠标滑轮移动、右键移动
<MouseWheel>	转动鼠标滑轮
<Double-Button-1>	双击鼠标左键
<Enter>	鼠标光标进入控件实例
<Leave>	鼠标光标离开控件实例
<Key>	按下键盘上的任意键
<KeyPress-字母>/<KeyPress-数字>	按下键盘上的某一个字母或者数字键
<KeyRelease>	释放键盘上的按键
<Return>	回车键，其他同类型键有<Shift>/<Tab>/<Control>/<Alt>
<Space>	空格键
<UP>/<Down>/<Left>/<Right>	方向键
<F1>...<F12>	常用的功能键
<Control-Alt>	组合键，再比如<Control-Shift-KeyPress-T>，表示用户同时点击 Ctrl + Shift + T
<FocusIn>	当控件获取焦点时候触发，比如鼠标点击输入控件输入内容，可以调用 focus_set() 方法使控件获得焦点
<FocusOut>	当控件失去焦点时激活，比如当鼠标离开输入框的时候
<Configure >	控件的发生改变的时候触发事件，比如调整了控件的大小等
<Deactivate>	当控件的状态从“激活”变为“未激活”时触发事件
<Destroy>	当控件被销毁的时候触发执行事件的函数
<Expose>	当窗口或组件的某部分不再被覆盖的时候触发事件
<Visibility>	当应用程序至少有一部分在屏幕中是可见状态时触发事件
Event事件对象
当事件触发后，Tkinter 会自动将事件对象交给回调函数进行下步的处理，Event 对象包含了以下常用属性：

属性	说明
widget	发生事件的是哪一个控件
x,y	相对于窗口的左上角而言，当前鼠标的坐标位置
x_root,y_root	相对于屏幕的左上角而言，当前鼠标的坐标位置
char	用来显示所按键相对应的字符
keysym	按键名，比如 Control_L 表示左边的 Ctrl 按键
keycode	按键码，一个按键的数字编号，比如 Delete 按键码是107
num	1/2/3中的一个，表示点击了鼠标的哪个按键，按键分为左、中、右
width,height	控件的修改后的尺寸，对应着 <Configure>事件
type	事件类型
下面看一组关于“键盘事件”的使用示例：
from tkinter import *
# 定义事件函数，必须用event参数
def show_key(event):
    # 查看触发事件的按钮
    s=event.keysym
    # 将其显示在按钮控件上
    lb.config(text=s)
root=Tk()
root.config(bg='#87CEEB')
root.title("C语言中文网")
root.geometry('450x350+300+200')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 添加一个按钮控件
lb=Label(root,text='请按键',fg='blue',font=('微软雅黑',15))
# 给按钮控件绑定事件，按下任意键，然后调用事件处理函数。注意，此处需要在英文状态下进行输入
lb.bind('<Key>',show_key)
# 设置按钮获取焦点
lb.focus_set()
lb.pack()
# 显示窗口
root.mainloop()
程序运行结果如下：

tkinter事件处理
图1：Tkinter事件处理
注意：在上述示例中，只有当 Label 控件获取焦点后才能接收键盘事件，因此在给控件绑定事件和回调函数后，需要使用 focus_set() 方法来获取焦点。

下面再看一组关于“鼠标事件”的相关示例：
# 定义事件函数
from tkinter import *
def handleMotion(event):
    lb1['text'] = '你移动了光标的所在位置'
    lb2['text'] = '目前光标位置：x ='+ str(event.x)+';y='+str(event.y)
    print('光标当前位置',event.x,event.y)
# 创建主窗口
win = Tk()
win.config(bg='#87CEEB')
win.title("C语言中文网")
win.geometry('450x350+300+200')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 创建一个窗体容器frame
frame = Frame (win, relief=RAISED, borderwidth=2, width=300,height=200)
frame.bind('<Motion>',handleMotion)
lb1 = Label(frame,text='没有任何事件触发', bg='purple', )
# 使用place进行位置布局，下一节会介绍
lb1.place (x=20,y=20)
lb2 = Label(frame,text='')
lb2.place (x=16,y=60)
frame.pack(side=TOP)
# 显示窗口
win.mainloop()
程序运行结果如下:
tkinter事件机制
图2：Tkinter鼠标移动事件
		17Tkinter布局管理方法
			当我们在开发一个 GUI 程序的时候，布局管理发挥着非常重要的作用，它指的是通过管理控件在窗口中的位置（排版），从而实现对窗口和控件布局的目的。

一个优秀的图形用户界面，更像是艺术家的作品，它会给用户非常良好的感官体验，因此布局管理不单单是枯燥的程序代码，更需要以“美”的角度去审视每一个细节，这才是学习布局管理的“不二法门”。Tkinter 提供了一系列布局管理的方法和容器控件，通过对这些内容的学习，您将掌握如何使用不同的方法完成界面布局。

Tkinter 提供了三种常用的布局管理器，分别是 pack()、grid() 以及 place()，如下表所示：

方法	说明
pack()	按照控件的添加顺序其进行排列，遗憾的是此方法灵活性较差
grid()	以行和列（网格）形式对控件进行排列，此种方法使用起来较为灵活
place()	可以指定组件大小以及摆放位置，三个方法中最为灵活的布局方法
上述三种方法适用于 Tkinter 中的所有控件，在讲解前面内容时，对其中一些方法已经做了相关的介绍，比如 pack() 和 grid()。在本节会对上述三个方法的应用场景做更为详细的介绍。
pack()
pack() 是一种较为简单的布局方法，在不使用任何参数的情况下，它会将控件以添加时的先后顺序，自上而下，一行一行的进行排列，并且默认居中显示。pack() 方法的常用参数如下所示：

属性	说明
anchor	组件在窗口中的对齐方式，有 9 个方位参数值，比如"n"/"w"/"s"/"e"/"ne"，以及 "center" 等（这里的 e w s n分别代表，东西南北）
expand	是否可扩展窗口，参数值为 True（扩展）或者 False（不扩展），默认为 False，若设置为 True，则控件的位置始终位于窗口的中央位置
fill	参数值为 X/Y/BOTH/NONE，表示允许控件在水平/垂直/同时在两个方向上进行拉伸，比如当 fill = X 时，控件会占满水平方向上的所有剩余的空间。
ipadx,ipady	需要与 fill 参数值共同使用，表示组件与内容和组件边框的距离（内边距），比如文本内容和组件边框的距离，单位为像素(p)，或者厘米(c)、英寸(i)
padx,pady	用于控制组件之间的上下、左右的距离（外边距），单位为像素(p)，或者厘米(c)、英寸(i)
side	组件放置在窗口的哪个位置上，参数值 'top','bottom','left','right'。注意，单词小写时需要使用字符串格式，若为大写单词则不必使用字符串格式
下面看一组简单的使用示例：
from tkinter import  *
win = Tk()
win.title("C语言中文网")
win.geometry('450x300+300+300')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
lb_red = Label(win,text="红色",bg="Red",fg='#ffffff',relief=GROOVE)
# 默认以top方式放置
lb_red.pack()
lb_blue = Label(win,text="蓝色",bg="blue",fg='#ffffff',relief=GROOVE)
# 沿着水平方向填充，使用 pady 控制蓝色标签与其他标签的上下距离为 5 个像素
lb_blue.pack(fill=X,pady='5px')
lb_green = Label(win,text="绿色",bg="green",fg='#ffffff',relief=RAISED)
# 将 黄色标签所在区域都填充为黄色，当使用 fill 参数时，必须设置 expand = 1，否则不能生效
lb_green.pack(side=LEFT,expand=1,fill = BOTH)
win.mainloop()
程序运行结果：
tkinter pack布局管理
图1：pack()布局管理
grid()
grid() 函数是一种基于网格式的布局管理方法，相当于把窗口看成了一张由行和列组成的表格。当使用该 grid 函数进行布局的时，表格内的每个单元格都可以放置一个控件。，从而实现对界面的布局管理。
注意：这里的所说的“表格”是虚拟出来，目的是便于大家理解，其实窗体并不会因为使用了 gird() 函数，而增加一个表格。

grid() 函数的常用参数如下所示：

属性	说明
column	控件位于表格中的第几列，窗体最左边的为起始列，默认为第 0 列
columnsapn	控件实例所跨的列数，默认为 1 列，通过该参数可以合并一行中多个领近单元格。
ipadx,ipady	用于控制内边距，在单元格内部，左右、上下方向上填充指定大小的空间。
padx,pady	用于控制外边距，在单元格外部，左右、上下方向上填充指定大小的空间。
row	控件位于表格中的第几行，窗体最上面为起始行，默认为第 0 行
rowspan	控件实例所跨的行数，默认为 1 行，通过该参数可以合并一列中多个领近单元格。
sticky	该属性用来设置控件位于单元格那个方位上，参数值和 anchor 相同，若不设置该参数则控件在单元格内居中
grid() 方法相比 pack() 方法来说要更加灵活，以网格的方式对组件进行布局管理，让整个布局显得非常简洁、优雅。如果说非要从三个布局管理器中选择一个使用的话，那么我推荐大家使用 grid() 方法。
这里有一点需要大家要特别注意，在一个程序中不能同时使用 pack() 和 grid() 方法，这两个方法只能二选一，否则程序会运行错误。


下面看一组有关 grid() 函数的简单的示例：
from tkinter import *
#主窗口
win = Tk()
win.config(bg='#87CEEB')
win.title("C语言中文网")
win.geometry('500x350+300+300')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
#在窗口内创建按钮，以表格的形式依次排列
for i in range (10):
    for j in range (10):
        Button (win, text=" (" + str(i) + ","+ str(j)+ ")",bg='#D1EEEE') .grid(row=i,column=j)
# 在第5行第11列添加一个Label标签
Label(win,text="C语言中文网",fg='blue',font=('楷体',12,'bold')).grid(row =4,column=11)
#开始窗口的事件循环
win. mainloop()
程序的运行结果：
tkinter grid()布局管理
图2：grid()布局管理

当使用 grid 函数布局的时，其实就是为各个控件指定行号、列号的过程，我们不需要为每个单元格指定大小，因为 grid 会为每个单元格自动设置一个适合的尺寸。

下面通过 grid() 布局管理器制作一个简易的登录界面，代码如下所示：
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("C语言中文网")
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
root.resizable(0,0)
tk.Label(root, text="用户名").grid(row=0, sticky="w")
tk.Label(root, text="密码").grid(row=1, sticky="w")
tk.Entry(root).grid(row=0, column=1)
tk.Entry(root, show="*").grid(row=1, column=1)
# 加载图片LOGO,注意这里是gif格式的图片
photo = tk.PhotoImage(file="C:/Users/Administrator/Desktop/1.gif")
tk.Label(root, image=photo).grid(row=0, column=2, rowspan=2, padx='4px', pady='5px')
# 编写一个简单的回调函数
def login():
    messagebox.showinfo('欢迎来到C语言中文网')
# 使用grid()函数来布局，并控制按钮的显示位置
tk.Button(root, text="登录", width=10, command=login).grid(row=3, column=0, columnspan=2,sticky="w", padx=10, pady=5)
tk.Button(root, text="退出", width=10, command=root.quit).grid(row=3, column=1, columnspan=2,sticky="e", padx=10, pady=5)
# 开启事件主循环
root.mainloop()
程序运行结果：
tkinter grid()布局管理
图3：grid()布局管理
place()
与前两种布局方法相比，采用 place() 方法进行布局管理要更加精细化，通过 place() 布局管理器可以直接指定控件在窗体内的绝对位置，或者相对于其他控件定位的相对位置。

下面对 place 布局管理器的常用属性做相关介绍：

属性	说明
anchor	定义控件在窗体内的方位，参数值N/NE/E/SE/S/SW/W/NW 或 CENTER，默认值是 NW
bordermode	定义控件的坐标是否要考虑边界的宽度，参数值为 OUTSIDE（排除边界） 或 INSIDE（包含边界），默认值 INSIDE。
x、y	定义控件在根窗体中水平和垂直方向上的起始绝对位置
relx、rely	1. 定义控件相对于根窗口（或其他控件）在水平和垂直方向上的相对位置（即位移比例），取值范围再 0.0~1.0 之间
2. 可设置 in_ 参数项，相对于某个其他控件的位置
height、width	控件自身的高度和宽度（单位为像素）
relheight、relwidth	控件高度和宽度相对于根窗体高度和宽度的比例，取值也在 0.0~1.0 之间
通过上述描述我们知道，relx和rely参数指定的是控件相对于父组件的位置，而relwidth和relheight参数则是指定控件相对于父组件的尺寸大小。
注意：这里父组件指的是当前可操作控件的上层组件，比如在没有使用容器控件（frame）的窗体中，控件的父组件就是主窗口本身，在《Tkinter布局管理容器控件》一节会做针对性介绍。

上述表格中关于距离位置的参数容易产生“疑惑”，下面通过一组简单的示例来进一步说明：
from tkinter import *
#主窗口
win = Tk()
win.title("C语言中文网")
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
#创建一个frame窗体对象，用来包裹标签
frame = Frame (win, relief=SUNKEN, borderwidth=2, width=450, height=250)
# 在水平、垂直方向上填充窗体
frame. pack (side=TOP, fill=BOTH, expand=1)
# 创建 "位置1"
Label1 = Label ( frame, text="位置1",bg='blue',fg='white')
# 使用 place,设置第一个标签位于距离窗体左上角的位置（40,40）和其大小（width，height）
# 注意这里（x,y）位置坐标指的是标签左上角的位置（以NW左上角进行绝对定位，默认为NW）
Label1.place (x=40,y=40, width=60, height=30)
# 设置标签2
Label2 = Label (frame, text="位置2",bg='purple',fg='white')
# 以右上角进行绝对值定位，anchor=NE，第二个标签的位置在距离窗体左上角的(180，80)
Label2.place(x=180,y=80, anchor=NE, width=60, height=30)
# 设置标签3
Label3 = Label (frame, text="位置3",bg='green',fg='white')
# 设置水平起始位置相对于窗体水平距离的0.6倍，垂直的绝对距离为80，大小为60，30
Label3.place(relx=0.6,y=80, width=60, height=30)
# 设置标签4
Label4 = Label (frame, text="位置4",bg='gray',fg='white')
# 设置水平起始位置相对于窗体水平距离的0.01倍，垂直的绝对距离为80，并设置高度为窗体高度比例的0.5倍，宽度为80
Label4.place(relx=0.01,y=80,relheight=0.4,width=80)
#开始事件循环
win. mainloop()
程序运行结果：
tkinter place布局管理
图4：place()布局管理器
注意：在一个父组件中 place()方法可以与 grid() 方法混合使用，要与 pack() 进行区别。
		18Tkinter布局管理控件
			除了上一节《Tkinter布局管理方法》中提到的三个常用方法外，Tkinter  还提供了几个常用的布局管理控件，比如 Frame 、LabelFrame 等，这些控件的主要作用是为其他控件提供载体，并将主窗口界面划分成多个区域，从而方便开发者对不同区域进行设计与管理。

在前文讲解其他的 Tkinter 控件时，我们列举的大多数示例都是将控件直接放置在主窗口（即根窗口）内，这样做的目的是为了便于大家理解。但在实际的开发过程中，控件一般放置在容器中，比如 Frame 容器控件，如同 HTML 中的<div>标签一样，把容器看做成一个框架，其他控件则是这个框架中的“元素”。

本节介绍了四种常用的容器控件以及它们的使用方法，分别是 Frame、LabelFrame、PanedWindow 以及 Toplevel。
Frame控件
Frame 本质上也是一个矩形窗体，同其他控件一样也需要位于主窗口内。我们可以在主窗口内放置多个 Frame 控件，并且每个 Frame 中还可以嵌套一个或者多个Frame，从而将主窗口界面划分成多个区域。

Frame 控件的常用属性如下表所示：

属性	说明
bg	设置 Frame 的背景颜色
bd	指定 Frame 的边框宽度
colormap	指定  Frame 组件及其子组件的颜色映射
container	布尔值参数，若参数值为 True，则窗体将被用作容器使用，一些其他程序也可以被嵌入。
cursor	指定鼠标在 Frame 上飘过的鼠标样式，默认由系统指定
height/width	设置 Frame 的高度和宽度
highlightbackground	指定当 Frame 没有获得焦点的时候高亮边框的颜色，通常由系统指定为标准颜色
highlightcolor	指定当 Frame 获得焦点的时候高亮边框的颜色
highlightthickness	指定高亮边框的宽度，默认值是 0
padx/pady	距离主窗口在水平/垂直方向上的外边距
relief	指定边框的样式，参数值 "sunken"，"raised"，"groove" 或 "ridge"，"flat"，默认为 "falt'
takefocus	布尔值参数，默认为 False，指定该组件是否接受输入焦点（即用户通过 Tab 键将焦点转移上来）
下面看一组简单的示例，通过 Frame 将主窗口分成左右两个部分，如下所示：
import tkinter as tk
win = tk.Tk()
win.title("C语言中文网")
win.geometry('400x350+200+200')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 在主窗口上添加一个frame控件
frame1 = tk.Frame(win)
frame1.pack()
# 在frame_1上添加另外两个frame， 一个在靠左，一个靠右
#左侧的frame
frame_left = tk.Frame(frame1)
tk.Label(frame_left,text='左侧标签1',bg='green',width=10,height=5).grid(row =0,column=0)
tk.Label(frame_left,text='左侧标签2',bg='blue',width=10,height=5).grid(row = 1 ,column =1)
frame_left.pack(side=tk.LEFT)
frame_right = tk.Frame(frame1)
tk.Label(frame_right,text='右侧标签1',bg='gray',width=10,height=5).grid(row = 0 ,column =1)
tk.Label(frame_right,text='右侧标签2',bg='pink',width=10,height=5).grid(row = 1 ,column =0)
tk.Label(frame_right,text='右侧标签3',bg='purple',width=10,height=5).grid(row= 1,column=1)
frame_right.pack(side=tk.RIGHT)
win.mainloop()
程序运行结果：

tkinter frame容器控件
图1：Frame控件布局管理

上述示例利用 Frame 控件将主窗口分成了左右两个子区域，同时在各自区域中添加了 Label 标签，而且区域之间互不干扰。采用这种分区、分块的布局方式，可以使得 GUI 程序更加规范、简洁化。
LabelFrame控件
LabelFrame 控件也是一种容器类型的控件，它属于是 Frame 控件的变体，因此它们的属性选项大体相同。

在默认情况下，LabelFrame 会在其包裹的子组件周围绘制一个边框和一个标题。当我们想要将一些相关的组件分为一组时，就可以使用 LabelFrame 组件，比如把一系列 Radiobutton（单选按钮）放在一起来供用户选择。

同 Frame 控件一样，LabelFrame 的主要作用也是对控件进行分组处理，下面看一个具体的实例：
import tkinter as tk
win = tk.Tk()
win.title("C语言中文网")
win.geometry('800x350+200+200')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 定义第一个容器，使用 labelanchor ='w' 来设置标题的方位
frame_left = tk.LabelFrame(win, text="教程", labelanchor="w",bg='#5CACEE')
# 使用 place 控制 LabelFrame 的位置
frame_left.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.5)
label_1 = tk.Label(frame_left, text="C语言")
label_1.place(relx=0.2, rely=0.2)
label_2 = tk.Label(frame_left, text="Python")
label_2.place(relx=0.6, rely=0.2)
label_3 = tk.Label(frame_left, text="Java")
label_3.place(relx=0.2, rely=0.6)
label_4 = tk.Label(frame_left, text="C++")
label_4.place(relx=0.6, rely=0.6)
# 定义第二个容器，使用 labelanchor ='w' 来设置标题的方位
frame_right = tk.LabelFrame(win, text="辅导班", labelanchor="w",bg='#66CDAA')
# 使用 place 控制 LabelFrame 的位置
frame_right.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.6)
label_1 = tk.Label(frame_right, text="C语言辅导班")
label_1.place(relx=0.2, rely=0.2)
label_2 = tk.Label(frame_right, text="数据结构")
label_2.place(relx=0.6, rely=0.2)
label_3 = tk.Label(frame_right, text="C++辅导班")
label_3.place(relx=0.2, rely=0.6)
label_4 = tk.Label(frame_right, text="Python答疑")
label_4.place(relx=0.6, rely=0.6)
win.mainloop()
程序运行结果：

tkinter LableFrame容器控件
图2：LabelFrame容器控件
PanedWindow控件
PanedWindow（窗格界面）也可以理解成一个特殊的 Frame 控件，它是 Tkinter 8.4 版本后新增的空间管理组件，其主要目的是为其他组件提供一个容器或者框架，从而实现以分块的形式对图形界面进行布局。

与 Frame 控件不同， PanedWindow 允许用户自主地调整界面划分以及每块区域的大小。因此，当您需要让用户自己调节每块区域的大小时，就可以采用 PanedWindow 作为组件载体来进行界面的布局。

不仅如此 PanedWindow 组件还提供了“手柄” 功能（设置参数 showhandle=True 来启用），通过拖动“手柄”图标也可以改变每块区域的大小。PanedWindow 组件语法格式如下所示：
PanedWindow(master=None, **options) 
其中 master 表示父组件，即包裹该组件的上层组件。其常用属性如下表所示：

属性	说明
handlepad	1. 调节“手柄”的位置
2. 比如当 orient ='vertical' 设置垂直时，handlepad 表示“分割线”上的手柄与左端的距离，默认为 8 像素
handlesize	设置“手柄”的尺寸（由于“手柄”必须是一个正方形，所以是设置正方形的边长）默认为 8 像素
opaqueresize	1. 该选项定义了用户调整窗格尺寸的操作，如果该选项的值为 True（默认），窗格的尺寸随用户鼠标的拖拽而改变
2.  如果该选项的值为 False，那么窗格的尺寸，在用户释放鼠标时才会更新到新的位置上
orient	指定窗格的分布方式，默认为水平方向分布（"horizontal"），或者还可以设置为垂直纵向分布（"vertical"）
relif	指定边框的样式，默认为 "flat"，还可以设置为  "sunken"，"raised"，"groove" 或 "ridge"
sashpad	设置每一条分割线到窗格间的间距
sashrelief	设置分割线的样式，默认值是："flat"，还可以设置 "sunken"，"raised"，"groove" 或 "ridge"
sashwidth	设置分割线的宽度
showhandle	设置是否显示调节窗格的手柄，默认为 False
height/width	设置 PanedWindow 的高度、宽度，若不设置，则其大小由其子组件的尺寸决定
PanedWindow 的常用方法如下表所示：

方法	说明
add(child)	添加一个新的子组件到窗格中语法格式 add(child,**option)，参数值 after、before、sticky
forget(child)	删除一个子组件
panecget(child, option)	获得子组件指定选项的值
paneconfig(child, **options)	设置子组件的各种选项
panes()	将父组件中包含的子组件以列表的形式返回
sash_coord(index)	返回一个二元组表示指定分割线的起点坐标
sash_place(index, x, y)	将指定的分割线移动到一个新的位置
下面示例设计一个简单的界面布局，然后将图形界面分割成四部分：创建一个水平方向的 PanedWindow，并向其中添加两个 Label 组件，之后创建一个垂直的方向的 PanedWindow，并向其中中添加两个 Label 标签。示例代码如下：
import tkinter as tk
win = tk.Tk()
win.title("C语言中文网")
win.geometry('400x400+200+200')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 创建一个水平方向的 panedwindow，并添加到主窗口中，默认为水平方向
p_window1 = tk.PanedWindow(win)
p_window1.pack(fill=tk.BOTH, expand=1)
# 在窗口区的左侧添加两个水平方向的 Label
left1 =tk. Label(p_window1, text='C语言中文网', bg='#7CCD7C', width=10,font=('微软雅黑',15))
p_window1.add(left1)
left2 =tk.Label(p_window1, text='网址：c.biancheng.net', bg='#9AC0CD', width=10,font=('微软雅黑',15))
p_window1.add(left2)
# 创建一个垂直方向的panedwindow,并添加一个手柄，设置分割线样式
p_window2 = tk.PanedWindow(orient=tk.VERTICAL,showhandle=True,sashrelief='sunken')
# 添加到 p_window1中
p_window1.add(p_window2)
# 在 p_window2 中添加两个垂直方向的标签
top_label =tk. Label(p_window2, text='教程', bg='#7171C6', height=8,font=('宋体',15))
p_window2.add(top_label)
bottom_label =tk. Label(p_window2, text='辅导班', bg='#8968CD',font=('宋体',15))
p_window2.add(bottom_label)
win.mainloop()
程序运行结果：

tkinter panedwindow容器组件
图3：PanedWindow空间布局

注意：从上述示例中可以看出 PanedWindw 会为每一个 Label 控件创建一个独立的窗格， 当我们将鼠标悬停在两个控件接壤处的白色边框上时，就会出现可以上下或者左右拉伸的指示光标，用户按照可以按照自己的意愿来调整每块区域的大小。
Toplevel控件
Topleve 是一个顶级窗口控件（也被称为“子窗体”控件），同样类似于 Frame 控件， 不过该控件会脱离根窗口另行创建一个独立窗口，因此它的存在形式不同于上述其他容器。

Toplevel 控件同样隶属于主窗口的子组件，只是存在形式特殊而已。Toplevel 是主窗口之外的弹出框窗口（通过事件来触发执行），在这个窗口内也可以包含其他组件。但需要注意，顶级窗口并不是必须位于窗口的顶部位置，之所以称其为顶级窗口，是因为相对于主窗口而言，Topleve 位于主窗口的上一层。

Toplevel 控件拥有根窗口控件的所有方法和属性，同时它还拥有一些独有的方法，如下表所示：

方法	说明
deiconify()	在使用 iconify() 或 withdraw() 方法后，即窗口最小化和移除窗口后（只是看不见，并没销毁），使用该方法来显示该窗口
frame()	返回一个系统特定的窗口识别码
group(window)	将顶级窗口加入 window 窗口群组中，如果忽略该参数，将返回当前窗口群的主窗口
 iconify()	将窗口图标化（最小化），需要重新显示窗口，使用 deiconify() 方法
 protocol(name, function)	将回调函数 function 与相应的规则 name 绑定；
1) name 参数可以是 "WM_DELETE_WINDOW"：窗口被关闭的时候；
2) name 参数可以是 "WM_SAVE_YOURSELF"：窗口被保存的时候；
3) name 参数可以是 "WM_TAKE_FOCUS"：窗口获得焦点的时候。
 state()	设置和获得当前窗口的状态，参数值 "normal"（正常状态），"withdrawn（移除窗口）"，"icon"（最小化）和 "zoomed"（放大）
 transient(master)	指定为 master 的临时窗口
 withdraw()	将窗口从屏幕上移除，只是移动到了窗口之外，并没销毁，需要重新显示窗口，使用 deiconify() 方法

下面看一组关于创建 Toplevel 的示例，如下所示：
import tkinter as tk
root = tk.Tk()
root.config(bg='#87CEEB')
root.title("C语言中文网")
root.geometry('400x350+300+300')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
def create_toplevel():
    top = tk.Toplevel()
    top.title("C语言中文网")
    top.geometry('300x200+100+100')
    top.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
    # 多行文本显示Message控件
    msg = tk.Label(top, text="网址：c.biancheng.net",bg='#9BCD9B',font=('宋体',15))
    msg.pack()
tk.Button(root, text="点击创建Toplevel组件", width=20,height=3,command=create_toplevel).pack()
root.mainloop()
程序的运行结果如下：

toplevel组件顶级窗口
图4：Toplevel组件创建顶级窗口
		19Tkinter对话框控件
			在前面的章节中，我们花费了大量的时间讲解了 Tkinter 中常用基本控件，通过对这些控件的学习，我们对  GUI 开发有了基本的认识与掌握，一个完整的 GUI 程序就是由这些组件以合理、美观的布局方式构成的。

除了基本的控件之外，Tkinter 还提供了三种对话框控件：
文件选择对话框：filedailog
颜色选择对话框：colorchooser
消息对话框：messagebox

这些对话框的使用能够在一定程度上增强用户的交互体验，下面对这些对话框控件进行详细地介绍。
文件选择对话框
文件对话框在 GUI 程序中经常的使用到，比如上传文档需要从本地选择一个文件，包括文件的打开和保存功能都需要一个文件对话框来实现。Tkinter 提供文件对话框被封装在tkinter.filedailog模块中，该模块提供了有关文件对话框的常用函数，经常使用的有以下几个：

方法	说明
Open()	打开个某个文件
SaveAs()	打开一个保存文件的对话框
askopenfilename()	打开某个文件，并以包函文件名的路径作为返回值
askopenfilenames()	同时打开多个文件，并以元组形式返回多个文件名
askopenfile()	打开文件，并返回文件流对象
askopenfiles()	打开多个文件，并以列表形式返回多个文件流对象
asksaveasfilename()	选择以什么文件名保存文件，并返回文件名
asksaveasfile()	选择以什么类型保存文件，并返回文件流对象
askdirectory	选择目录，并返回目录名
上述方法的常用参数值如下所示：

参数	说明
defaultextension	指定文件的后缀名，当保存文件时自动添加文件名，如果自动添加了文件的后缀名，则该选项值不会生效
filetypes	指定筛选文件类型的下拉菜单选项，该选项值是由 2 元祖构成的列表，其中每个二元祖由两部分组成 (类型名,后缀)，比如 filetypes = [("PNG","*.png"), ("JPG", "*.jpg"), ("GIF","*.gif"),("文本文件","*.txt")...] 
initialdir	指定打开/保存文件的默认路径，默认路径是当前文件夹
parent	 如果不指定该选项，那么对话框默认显示在根窗口上，通过设置该参数可以使得对话框显示在子窗口上
title	指定文件对话框的标题
下面看一组具体的实例应用：
from tkinter import *
import tkinter.filedialog  # 注意次数要将文件对话框导入
# 定义一个处理文件的相关函数
def askfile():
    # 从本地选择一个文件，并返回文件的目录
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text= filename)
    else:
         lb.config(text='您没有选择任何文件')
root = Tk()
root.config(bg='#87CEEB')
root.title("C语言中文网")
root.geometry('400x200+300+300')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
btn=Button(root,text='选择文件',relief=RAISED,command=askfile)
btn.grid(row=0,column=0)
lb = Label(root,text='',bg='#87CEEB')
lb.grid(row=0,column=1,padx=5)
# 显示窗口
root.mainloop()
程序运行结果：

图1：文件选择界面

下面再看一组“保存文件”的示例代码如下：
import tkinter as tk
from tkinter import filedialog
from PIL import Image
def open_img():
    try:
        global img
        filepath = filedialog.askopenfilename() # 打开文件，返回该文件的完整路径
        filename.set(filepath)
        img = Image.open(filename.get())
    except Exception as e:
        print("您没有选择任何文件",e)
def save_png():
    try:
        filetypes = [("PNG","*.png"), ("JPG", "*.jpg"), ("GIF","*.gif"),("txt files","*.txt"),('All files','*')]
        # 返回一个 pathname 文件路径字符串，如果取消或者关闭则返回空字符，返回文件如何操作是后续代码的事情，
        # 该函数知识返回选择文件的文件名字，不具备保存文件的能力
        filenewpath= filedialog.asksaveasfilename(title='保存文件',
                                                filetypes=filetypes,
                                                defaultextension='.png',
                                                initialdir='C:/Users/Administrator/Desktop' )
        path_var.set(filenewpath)
        # 保存文件
        img.save(str(path_var.get()))
    except Exception as e:
        print(e)
window = tk.Tk()
window.title("C语言中文网")
window.geometry('400x200+300+300')
window.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
filename = tk.StringVar()
path_var = tk.StringVar()
# 定义读取文件的组件
entry = tk.Entry(window, textvariable=filename)
entry.grid(row=1, column=0, padx=5, pady=5)
tk.Button(window, text='选择文件', command=open_img).grid(row=1, column=1, padx=5, pady=5)
# 定义保存文件的组件
entry1 = tk.Entry(window, textvariable=path_var)
entry1.grid(row=2, column=0, padx=5, pady=5)
tk.Button(window, text='保存文件', command=save_png).grid(row=2, column=1, padx=5, pady=5)
window.mainloop()
程序运行结果：

tkinter文件选择对话框
图2：程序运行结果
颜色选择对话框
颜色选择对话框（colorchooser），提供了一个非常友善的颜色面板，它允许用户选择自己所需要的颜色。 当用户在面板上选择一个颜色并按下“确定”按钮后，它会返回一个二元祖，其第 1 个元素是选择的 RGB 颜色值，第 2 个元素是对应的 16 进制颜色值。

颜色选择对话款主要应用在画笔、涂鸦等功能上，通过它可以绘制出五彩缤纷的颜色，该对话框的使用非常简单，主要有以下两个常用方法：

方法	说明
askcolor()	打开一个颜色对话框，并将用户选择的颜色值以元组的形式返回（没选择返回None），格式为((R, G, B), "#rrggbb")
Chooser()	打开一个颜色对话框，并用户选择颜色确定后，返回一个二元组，格式为（(R, G, B), "#rrggbb"）
常用的颜色对话框的参数值如下表所示：

属性	说明
default	要显示的初始的颜色，默认颜色是浅灰色（light gray）
title	指定颜色选择器标题栏的文本，默认标题为“颜色”
parent	1. 如果不指定该选项，那么对话框默认显示在根窗口上
2. 如果想要将对话框显示在子窗口上，那么可以设置 parent = 子窗口对象
下面看一组简单的使用示例：
import tkinter as tk
from tkinter import colorchooser
root = tk.Tk()
root.title("颜色选择")
root.geometry('400x200+300+300')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
def callback():
    # 打开颜色对话款
    colorvalue = tk.colorchooser.askcolor()
    # 在颜色面板点击确定后，会在窗口显示二元组颜色值
    lb.config(text='颜色值:'+ str(colorvalue))
lb=tk.Label(root,text='',font=('宋体',10))
# 将label标签放置在主窗口
lb.pack()
tk.Button(root, text="点击选择颜色", command=callback, width=10, bg='#9AC0CD').pack()
# 显示界面
root.mainloop()
颜色对话框如下所示：

tkinter颜色对话框
图3：tkinter颜色对话框

上述程序的运行结果如下：

colorchooser颜色对话框控件
图4：程序运行结果
消息对话框
关于消息对话款（messagebox），在前面介绍其他控件时已经使用过，在本节仅对它做简单介绍。

消息对话框主要起到信息提示、警告、说明、询问等作用，通常配合“事件函数”一起使用，比如执行某个操作出现了错误，然后弹出错误消息提示框。通过使用消息对话框可以提升用户的交互体验，也使得 GUI 程序更加人性化。消息对话框主要包含了以下常用方法：

方法	说明
askokcancel(title=None, message=None)	打开一个“确定／取消”的对话框
askquestion(title=None, message=None)	打开一个“是／否”的对话框。
askretrycancel(title=None, message=None)	打开一个“重试／取消”的对话框
askyesno(title=None, message=None)	打开一个“是／否”的对话框
showerror(title=None, message=None)	打开一个错误提示对话框
showinfo(title=None, message=None)	打开一个信息提示对话框
showwarning(title=None, message=None)	打开一个警告提示对话框
上述方法拥有相同的选项参数，如下表所示：

属性	说明
default	1. 设置默认的按钮（也就是按下回车响应的那个按钮）
2. 默认是第一个按钮（像“确定”，“是”或“重试”）
3. 可以设置的值根据对话框函数的不同，可以选择 CANCEL，IGNORE，OK，NO，RETRY 或 YES
icon	1. 指定对话框显示的图标
2. 可以指定的值有：ERROR，INFO，QUESTION 或 WARNING
3. 注意：不能指定自己的图标
parent	1. 如果不指定该选项，那么对话框默认显示在根窗口上
2. 如果想要将对话框显示在子窗口上，那么可以设置 parent= 子窗口对象
上述方法的返回值一般会是一个布尔值，或者是“YES”，“NO”，“OK”等，这些方法使用较为简单，此处不进行逐一列举，看个简单的示例即可：
import tkinter.messagebox
result=tkinter.messagebox.askokcancel ("提示"," 你确定要关闭窗口吗? ")
# 返回布尔值参数
print(result)
程序运行结果：
tkinter消息对话框
图5：消息对话框
		20案例：构建数字时钟
			截止到本节为止，和 Tkinter 相关的知识就讲解完毕了，本套教程从 GUI 是什么开始入门讲解，然后带领大家深入学习了 Python GUI 标准库 Tkinter，在教程中，我们主要介绍了 GUI 的相关概念、常用组件和布局方式等知识，下面使用 Tkinter 的相关知识实现一个数字时钟的简单案例。

Tkinter 实现上述功能并不复杂，只要使用 Tkinter 的相关组件和一些简单的逻辑处理即可，在编写这个案例的过程中大家要做到温故而知新。

程序代码如下所示：
from tkinter import *
from time import strftime
root = Tk()
root.geometry('500x350+300+300')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
root.title("C语言中文网出品")
# 设置文本标签
lb = Label(root, font=("微软雅黑", 50, "bold"), bg='#87CEEB', fg="#B452CD")
lb.pack(anchor="center", fill="both", expand=1)
# 定义一个mode标志
mode = 'time'
# 定义显示时间的函数
def showtime():
    if mode == 'time':
        #时间格式化处理   
        string = strftime("%H:%M:%S %p")
    else:
        string = strftime("%Y-%m-%d")
    lb.config(text=string)
    # 每隔 1秒钟执行time函数
    lb.after(1000, showtime)
# 定义鼠标处理事件，点击时间切换为日期样式显示
def mouseClick(event):
    global mode
    if mode == 'time':
        # 点击切换mode样式为日期样式
        mode = 'date'
    else:
        mode = 'time'
lb.bind("<Button>", mouseClick)
# 调用showtime()函数
showtime()
# 显示窗口
mainloop()
程序运行结果如下：

tkinter项目案例
图1：简单的数字时钟

通过上述代码就实现了一个简单的数字时钟，是不是非常的简单。

	打包
		将python3项目打包成exe可执行程序
			第一步：进入命令行安装pyinstaller，安装命令：pip install pyinstaller。直到提示Successfully installed pyinstaller-xxx表示安装完成。
			第二步：进到打包程序目录。(就是要进入到需要打包文件的文件夹下)
			第三步：在地址栏中输入cmd并回车来打开命令行窗口。
			第四步:在命令行窗口中输入命令行：pyinstaller -F xxx.py并回车（xxx.py是要打包的文件，我们这里是test.py）。直到提示completed successfully表示打包完成。
				
			第五步:进到打包文件目录查看打包的程序并执行
	实例















## [Python GUI之tkinter窗口视窗教程大集合（看这篇就够了）](https://www.cnblogs.com/shwee/p/9427975.html)

**个人博客转移至：[https://sunhwee.com](https://sunhwee.com/)，第一时间会先发在前者，有时间再更新至博客园。**

## 一、前言

　　由于本篇文章较长，所以下面给出内容目录方便跳转阅读，当然也可以用博客页面最右侧的文章目录导航栏进行跳转查阅。

　　[一、前言](https://www.cnblogs.com/shwee/p/9427975.html#A)

　　[二、Tkinter 是什么](https://www.cnblogs.com/shwee/p/9427975.html#B)

　　[三、Tkinter 控件详细介绍](https://www.cnblogs.com/shwee/p/9427975.html#C)

　　　　[1. Tkinter 模块元素简要说明](https://www.cnblogs.com/shwee/p/9427975.html#C1)

　　　　[2. 常用窗口部件及简要说明：](https://www.cnblogs.com/shwee/p/9427975.html#C2)

　　[四、动手实践学习](https://www.cnblogs.com/shwee/p/9427975.html#D)

　　　　[1. 创建主窗口及Label部件（标签）创建使用](https://www.cnblogs.com/shwee/p/9427975.html#D1)

　　　　[2. Button窗口部件](https://www.cnblogs.com/shwee/p/9427975.html#D2)

　　　　[3. Entry窗口部件](https://www.cnblogs.com/shwee/p/9427975.html#D3)

　　　　[4. Text窗口部件](https://www.cnblogs.com/shwee/p/9427975.html#D4)

　　　　[5. Listbox窗口部件](https://www.cnblogs.com/shwee/p/9427975.html#D5)

　　　　[6. Radiobutton窗口部件](https://www.cnblogs.com/shwee/p/9427975.html#D6)

　　　　[7. Checkbutton窗口部件 ](https://www.cnblogs.com/shwee/p/9427975.html#D7)

　　　　[8. Scale窗口部件](https://www.cnblogs.com/shwee/p/9427975.html#D8)

　　　　[9. Canvas窗口部件](https://www.cnblogs.com/shwee/p/9427975.html#D9)

　　　　[10. Menu窗口部件](https://www.cnblogs.com/shwee/p/9427975.html#D10)

　　　　[11. Frame 窗口部件](https://www.cnblogs.com/shwee/p/9427975.html#D11)

　　　　[12. messageBox窗口部件](https://www.cnblogs.com/shwee/p/9427975.html#D12)

　　　　[13. 窗口部件三种放置方式pack/grid/place](https://www.cnblogs.com/shwee/p/9427975.html#D13)

　　　　[14. 综合练习，用户登录窗口例子](https://www.cnblogs.com/shwee/p/9427975.html#D14)

　　　　[15. 其他部件后续再补充...](https://www.cnblogs.com/shwee/p/9427975.html#D15)

## 二、Tkinter是什么

　　Tkinter 是使用 python 进行窗口视窗设计的模块。Tkinter模块("Tk 接口")是[Python](https://baike.baidu.com/item/Python/407313)的标准Tk GUI工具包的接口。作为 python 特定的GUI界面，是一个图像的窗口，tkinter是python 自带的，可以编辑的GUI界面，我们可以用GUI 实现很多直观的功能，比如想开发一个计算器，如果只是一个程序输入，输出窗口的话，是没用用户体验的。所有开发一个图像化的小窗口，就是必要的。

　　对于稍有GUI编程经验的人来说，[Python](http://lib.csdn.net/base/python)的Tkinter界面库是非常简单的。[python](http://lib.csdn.net/base/python)的GUI库非常多，选择Tkinter，一是最为简单，二是自带库，不需下载安装，随时使用，三则是从需求出发，Python作为一种脚本语言，一种胶水语言，一般不会用它来开发复杂的桌面应用，它并不具备这方面的优势，使用Python，可以把它作为一个灵活的工具，而不是作为主要开发语言，那么在工作中，需要制作一个小工具，肯定是需要有界面的，不仅自己用，也能分享别人使用，在这种需求下，Tkinter是足够胜任的！

　　这篇文章主要做一个简单概述和实践编程，对于从没有接触过GUI的新手，在脑中树立一个基本的界面编程概念，同时自己也能学会如何简单的实现一些小的图形窗口功能。

　　**对于Tkinter编程，可以用两个比喻来理解：**

- 第一个，作画。我们都见过美术生写生的情景，先支一个画架，放上画板，蒙上画布，构思内容，用铅笔画草图，组织结构和比例，调色板调色，最后画笔勾勒。相应的，对应到tkinter编程，那么我们的显示屏就是支起来的画架，根窗体就是画板，在tkinter中则是Toplevel，画布就是tkinter中的容器（Frame），画板上可以放很多张画布（Convas），tkinter中的容器中也可以放很多个容器，绘画中的构图布局则是tkinter中的布局管理器（几何管理器），绘画的内容就是tkinter中的一个个小组件，一幅画由许多元素构成，而我们的GUI界面，就是有一个个组件拼装起来的，它们就是widget。
- 第二个，我们小时候都玩过积木，只要发挥创意，相同的积木可以堆出各种造型。tkinter的组件也可以看做一个个积木，形状或许不同，其本质都是一样的，就是一个积木，不管它长什么样子，它始终就是积木！所以这些小组件都有许多共性，另外，个人认为，学习界面编程，最重要的不是一开始学习每个积木的样子，不是学习每个组件怎么用，而是这些组件该怎么放。初始学习中，怎么放远远比怎么用重要的多。网上有大量的文章资料，基本全是介绍组件怎么用的，对于怎么放，也就是tkinter中的布局管理器，都是一笔带过，这对初学者有点本末倒置，或许绝大部分是转载的原因吧，极少是自己真正写的。组件怎么用不是最迫切的，用到的时候再去了解也不迟，边用边学反而更好。因此我将专门写一章，详细介绍布局管理器的使用。

## 三、Tkinter 控件详细介绍

### 1. Tkinter 模块元素简要说明

| ![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180805235412647-270287964.png) | [The Button Widget](http://effbot.org/tkinterbook/button.htm) [The Canvas Widget](http://effbot.org/tkinterbook/canvas.htm) [The Checkbutton Widget](http://effbot.org/tkinterbook/checkbutton.htm) [The Entry Widget](http://effbot.org/tkinterbook/entry.htm) [The Frame Widget](http://effbot.org/tkinterbook/frame.htm) [The Label Widget](http://effbot.org/tkinterbook/label.htm) [The LabelFrame Widget](http://effbot.org/tkinterbook/labelframe.htm) [The Listbox Widget](http://effbot.org/tkinterbook/listbox.htm) [The Menu Widget](http://effbot.org/tkinterbook/menu.htm) [The Menubutton Widget](http://effbot.org/tkinterbook/menubutton.htm) [The Message Widget](http://effbot.org/tkinterbook/message.htm) [The OptionMenu Widget](http://effbot.org/tkinterbook/optionmenu.htm) [The PanedWindow Widget](http://effbot.org/tkinterbook/panedwindow.htm) [The Radiobutton Widget](http://effbot.org/tkinterbook/radiobutton.htm) [The Scale Widget](http://effbot.org/tkinterbook/scale.htm) [The Scrollbar Widget](http://effbot.org/tkinterbook/scrollbar.htm) [The Spinbox Widget](http://effbot.org/tkinterbook/spinbox.htm) [The Text Widget](http://effbot.org/tkinterbook/text.htm) [The Toplevel Widget](http://effbot.org/tkinterbook/toplevel.htm) [Basic Widget Methods](http://effbot.org/tkinterbook/widget.htm) [Toplevel Window Methods](http://effbot.org/tkinterbook/wm.htm) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

### 2. 常用窗口部件及简要说明：

　　Tkinter支持16个核心的窗口部件，这个16个核心窗口部件类简要描述如下：

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

注意在Tkinter中窗口部件类没有分级；所有的窗口部件类在树中都是兄弟关系。

所有这些窗口部件提供了Misc和几何管理方法、配置管理方法和部件自己定义的另外的方法。此外，Toplevel类也提供窗口管理接口。这意味一个典型的窗口部件类提供了大约150种方法。

## 四、动手实践学习

### 1. 创建主窗口及Label部件（标签）创建使用

　　我们要学习使用上面提到的这些控件首先要创建一个主窗口，就像作画一样，先要架好架子和画板，然后才能在上面放画纸和各种绘画元素，创建好主窗口才能在上面放置各种控件元素。而创建过程是很简单的，如下：

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，在图形界面上设定标签``l ``=` `tk.Label(window, text``=``'你好！this is Tkinter'``, bg``=``'green'``, font``=``(``'Arial'``, ``12``), width``=``30``, height``=``2``)``# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高` `# 第5步，放置标签``l.pack()  ``# Label内容content区域放置位置，自动调节尺寸``# 放置lable的方法有：1）l.pack(); 2)l.place();` `# 第6步，主窗口循环显示``window.mainloop()``# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环``# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
```

　　**测试效果：**

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807110943755-658426730.png)

### 2. Button窗口部件

　　**简单说明：**

　　Button（按钮）部件是一个标准的Tkinter窗口部件，用来实现各种按钮。按钮能够包含文本或图象，并且你能够将按钮与一个Python函数或方法相关联。当这个按钮被按下时，Tkinter自动调用相关联的函数或方法。

按钮仅能显示一种字体，但是这个文本可以跨行。另外，这个文本中的一个字母可以有下划线，例如标明一个快捷键。默认情况，Tab键用于将焦点移动到一个按钮部件。

　　**什么时候用按钮部件**

　　简言之，按钮部件用来让用户说“马上给我执行这个任务”，通常我们用显示在按钮上的文本或图象来提示。按钮通常用在工具条中或应用程序窗口中，并且用来接收或忽略输入在对话框中的数据。关于按钮和输入的数据的配合，可以参看Checkbutton和Radiobutton部件。

　　**如何创建：**

普通的按钮很容易被创建，仅仅指定按钮的内容（文本、位图、图象）和一个当按钮被按下时的回调函数即可：

b = tk.Button(window, text="hit me", command=hit_me)

没有回调函数的按钮是没有用的，当你按下这个按钮时它什么也不做。你可能在开发一个应用程序的时候想实现这种按钮，比如为了不干扰你的beta版的测试者：

b = tk.Button(window, text="Help", command=DISABLED)

 　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，在图形界面上设定标签``var ``=` `tk.StringVar()  ``# 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上``l ``=` `tk.Label(window, textvariable``=``var, bg``=``'green'``, fg``=``'white'``, font``=``(``'Arial'``, ``12``), width``=``30``, height``=``2``)``# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高``l.pack()` `# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名``on_hit ``=` `False``def` `hit_me():``  ``global` `on_hit``  ``if` `on_hit ``=``=` `False``:``    ``on_hit ``=` `True``    ``var.``set``(``'you hit me'``)``  ``else``:``    ``on_hit ``=` `False``    ``var.``set``('')` `# 第5步，在窗口界面设置放置Button按键``b ``=` `tk.Button(window, text``=``'hit me'``, font``=``(``'Arial'``, ``12``), width``=``10``, height``=``1``, command``=``hit_me)``b.pack()` `# 第6步，主窗口循环显示``window.mainloop()
```

　　测试**效果：**

 ![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807114422575-1561247351.png)![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807114448762-732697318.png)

### 3. Entry窗口部件

　　**简单说明：**　　

　　Entry是tkinter类中提供的的一个单行文本输入域，用来输入显示一行文本，收集键盘输入(类似 HTML 中的 text)。

　　**什么时候用：**

　　需要用户输入用户信息时，比如我们平时使用软件、登录网页时，用户交互界面让我们登录账户信息等时候可以用到。

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，在图形界面上设定输入框控件entry并放置控件``e1 ``=` `tk.Entry(window, show``=``'*'``, font``=``(``'Arial'``, ``14``))  ``# 显示成密文形式``e2 ``=` `tk.Entry(window, show``=``None``, font``=``(``'Arial'``, ``14``)) ``# 显示成明文形式``e1.pack()``e2.pack()` `# 第5步，主窗口循环显示``window.mainloop()
```

　　**测试效果：**

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807142042155-1964518061.png)

### 4. Text窗口部件

　　**简单说明：**　　

　　Text是tkinter类中提供的的一个多行文本区域，显示多行文本，可用来收集(或显示)用户输入的文字(类似 HTML 中的 textarea)，格式化文本显示，允许你用不同的样式和属性来显示和编辑文本，同时支持内嵌图象和窗口。

　　**什么时候用：**

　　在需要显示编辑用户、产品多行信息时，比如显示用户详细描述文字，产品简介等等，支持随时编辑。

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，在图形界面上设定输入框控件entry框并放置``e ``=` `tk.Entry(window, show ``=` `None``)``#显示成明文形式``e.pack()` `# 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）``def` `insert_point(): ``# 在鼠标焦点处插入输入内容``  ``var ``=` `e.get()``  ``t.insert(``'insert'``, var)``def` `insert_end():  ``# 在文本框内容最后接着插入输入内容``  ``var ``=` `e.get()``  ``t.insert(``'end'``, var)` `# 第6步，创建并放置两个按钮分别触发两种情况``b1 ``=` `tk.Button(window, text``=``'insert point'``, width``=``10``,``        ``height``=``2``, command``=``insert_point)``b1.pack()``b2 ``=` `tk.Button(window, text``=``'insert end'``, width``=``10``,``        ``height``=``2``, command``=``insert_end)``b2.pack()` `# 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度``t ``=` `tk.Text(window, height``=``3``)``t.pack()` `# 第8步，主窗口循环显示``window.mainloop()
```

　　测试效果：

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807144407310-92869541.png)

### 5. Listbox窗口部件

　　**简单说明：**　　

　　Text是tkinter类中提供的的列表框部件，显示供选方案的一个列表。listbox能够被配置来得到radiobutton或checklist的行为。

　　**什么时候用：**

　　在有一个很多内容选项组成的列表提供用户选择时会用到。

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，在图形界面上创建一个标签label用以显示并放置``var1 ``=` `tk.StringVar() ``# 创建变量，用var1用来接收鼠标点击具体选项的内容``l ``=` `tk.Label(window, bg``=``'green'``, fg``=``'yellow'``,font``=``(``'Arial'``, ``12``), width``=``10``, textvariable``=``var1)``l.pack()` `# 第6步，创建一个方法用于按钮的点击事件``def` `print_selection():``  ``value ``=` `lb.get(lb.curselection())  ``# 获取当前选中的文本``  ``var1.``set``(value) ``# 为label设置值` `# 第5步，创建一个按钮并放置，点击按钮调用print_selection函数``b1 ``=` `tk.Button(window, text``=``'print selection'``, width``=``15``, height``=``2``, command``=``print_selection)``b1.pack()` `# 第7步，创建Listbox并为其添加内容``var2 ``=` `tk.StringVar()``var2.``set``((``1``,``2``,``3``,``4``)) ``# 为变量var2设置值``# 创建Listbox``lb ``=` `tk.Listbox(window, listvariable``=``var2) ``#将var2的值赋给Listbox``# 创建一个list并将值循环添加到Listbox控件中``list_items ``=` `[``11``,``22``,``33``,``44``]``for` `item ``in` `list_items:``  ``lb.insert(``'end'``, item) ``# 从最后一个位置开始加入值``lb.insert(``1``, ``'first'``)    ``# 在第一个位置加入'first'字符``lb.insert(``2``, ``'second'``)   ``# 在第二个位置加入'second'字符``lb.delete(``2``)        ``# 删除第二个位置的字符``lb.pack()` `# 第8步，主窗口循环显示``window.mainloop()
```

　　**测试效果：**

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807152825021-1491949329.png)

### 6. Radiobutton窗口部件

　　**简单说明：**　　

　　**Radiobutton：**代表一个变量，它可以有多个值中的一个。点击它将为这个变量设置值，并且清除与这同一变量相关的其它radiobutton。

　　**什么时候用：**

　　在有一个很多内容选项组成的选项列表提供用户选择时会用到，用户一次只能选择其中一个，不能多选。

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，在图形界面上创建一个标签label用以显示并放置``var ``=` `tk.StringVar()  ``# 定义一个var用来将radiobutton的值和Label的值联系在一起.``l ``=` `tk.Label(window, bg``=``'yellow'``, width``=``20``, text``=``'empty'``)``l.pack()` `# 第6步，定义选项触发函数功能``def` `print_selection():``  ``l.config(text``=``'you have selected '` `+` `var.get())` `# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable``r1 ``=` `tk.Radiobutton(window, text``=``'Option A'``, variable``=``var, value``=``'A'``, command``=``print_selection)``r1.pack()``r2 ``=` `tk.Radiobutton(window, text``=``'Option B'``, variable``=``var, value``=``'B'``, command``=``print_selection)``r2.pack()``r3 ``=` `tk.Radiobutton(window, text``=``'Option C'``, variable``=``var, value``=``'C'``, command``=``print_selection)``r3.pack()` `# 第7步，主窗口循环显示``window.mainloop()
```

　　**测试效果：**

**![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807154149998-1781234846.png)![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807154247492-700211406.png)**

### 7. Checkbutton窗口部件

　　**简单说明：**　　

　　**Checkbutton：**代表一个变量，它有两个不同的值。点击这个按钮将会在这两个值间切换，选择和取消选择。

　　**什么时候用：**

　　在有一个很多内容选项组成的选项列表提供用户选择时会用到，用户一次可以选择多个。

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，在图形界面上创建一个标签label用以显示并放置``l ``=` `tk.Label(window, bg``=``'yellow'``, width``=``20``, text``=``'empty'``)``l.pack()` `# 第6步，定义触发函数功能``def` `print_selection():``  ``if` `(var1.get() ``=``=` `1``) & (var2.get() ``=``=` `0``):   ``# 如果选中第一个选项，未选中第二个选项``    ``l.config(text``=``'I love only Python '``)``  ``elif` `(var1.get() ``=``=` `0``) & (var2.get() ``=``=` `1``):  ``# 如果选中第二个选项，未选中第一个选项``    ``l.config(text``=``'I love only C++'``)``  ``elif` `(var1.get() ``=``=` `0``) & (var2.get() ``=``=` `0``):  ``# 如果两个选项都未选中``    ``l.config(text``=``'I do not love either'``)``  ``else``:``    ``l.config(text``=``'I love both'``)       ``# 如果两个选项都选中` `# 第5步，定义两个Checkbutton选项并放置``var1 ``=` `tk.IntVar() ``# 定义var1和var2整型变量用来存放选择行为返回值``var2 ``=` `tk.IntVar()``c1 ``=` `tk.Checkbutton(window, text``=``'Python'``,variable``=``var1, onvalue``=``1``, offvalue``=``0``, command``=``print_selection)  ``# 传值原理类似于radiobutton部件``c1.pack()``c2 ``=` `tk.Checkbutton(window, text``=``'C++'``,variable``=``var2, onvalue``=``1``, offvalue``=``0``, command``=``print_selection)``c2.pack()` `# 第7步，主窗口循环显示``window.mainloop()
```

　　**测试效果：**

 ![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807155946145-339576184.png)![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807160018594-1404446854.png)![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807160042074-949383027.png) 

### 8. Scale窗口部件

　　**简单说明：**　　

　　**Scale： 尺度（拉动条），**允许你通过滑块来设置一数字值。

　　**什么时候用：**

　　在需要用户给出评价等级，或者给出一个评价分数，或者拉动滑动条提供一个具体的数值等等。

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，在图形界面上创建一个标签label用以显示并放置``l ``=` `tk.Label(window, bg``=``'green'``, fg``=``'white'``, width``=``20``, text``=``'empty'``)``l.pack()` `# 第6步，定义一个触发函数功能``def` `print_selection(v):``  ``l.config(text``=``'you have selected '` `+` `v)<br>``# 第5步，创建一个尺度滑条，长度200字符，从0开始10结束，以2为刻度，精度为0.01，触发调用print_selection函数``s ``=` `tk.Scale(window, label``=``'try me'``, from_``=``0``, to``=``10``, orient``=``tk.HORIZONTAL, length``=``200``, showvalue``=``0``,tickinterval``=``2``, resolution``=``0.01``, command``=``print_selection)``s.pack()` `# 第7步，主窗口循环显示``window.mainloop()
```

　　**测试效果：**

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807161524147-2124951218.png)![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180807161542624-274942134.png)

### 9. Canvas窗口部件

　　**简单说明：**　　

　　**Canvas：画布，**提供绘图功能(直线、椭圆、多边形、矩形) 可以包含图形或位图，用来绘制图表和图，创建图形编辑器，实现定制窗口部件。

　　**什么时候用：**

　　在比如像用户交互界面等，需要提供设计的图标、图形、logo等信息是可以用到画布。

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，在图形界面上创建 500 * 200 大小的画布并放置各种元素``canvas ``=` `tk.Canvas(window, bg``=``'green'``, height``=``200``, width``=``500``)``# 说明图片位置，并导入图片到画布上``image_file ``=` `tk.PhotoImage(``file``=``'pic.gif'``) ``# 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）``image ``=` `canvas.create_image(``250``, ``0``, anchor``=``'n'``,image``=``image_file)    ``# 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处``# 定义多边形参数，然后在画布上画出指定图形``x0, y0, x1, y1 ``=` `100``, ``100``, ``150``, ``150``line ``=` `canvas.create_line(x0``-``50``, y0``-``50``, x1``-``50``, y1``-``50``)          ``# 画直线``oval ``=` `canvas.create_oval(x0``+``120``, y0``+``50``, x1``+``120``, y1``+``50``, fill``=``'yellow'``) ``# 画圆 用黄色填充``arc ``=` `canvas.create_arc(x0, y0``+``50``, x1, y1``+``50``, start``=``0``, extent``=``180``)   ``# 画扇形 从0度打开收到180度结束``rect ``=` `canvas.create_rectangle(``330``, ``30``, ``330``+``20``, ``30``+``20``)         ``# 画矩形正方形``canvas.pack()` `# 第6步，触发函数，用来一定指定图形``def` `moveit():``  ``canvas.move(rect, ``2``, ``2``) ``# 移动正方形rect（也可以改成其他图形名字用以移动一起图形、元素），按每次（x=2, y=2）步长进行移动` `# 第5步，定义一个按钮用来移动指定图形的在画布上的位置``b ``=` `tk.Button(window, text``=``'move item'``,command``=``moveit).pack()` `# 第7步，主窗口循环显示``window.mainloop()
```

　　**所用图片：**

　　当然你可以随意用你的一张图片导入画布试一试效果，图片可以用画图工具改一下像素大小，以免图片太大，导入画布显示不全，当然你也可以用我提供的素材，下面是链接：https://files.cnblogs.com/files/shwee/pic.gif

 ![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808213752551-737495553.gif)

　　**图片锚定点位置参数图：**

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808214423234-2053303150.png)

　　**测试效果：**

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808214010611-964561892.png)![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808214052169-1659760377.png)

### 10. Menu窗口部件

　　**简单说明：**　　

　　**Menu：**菜单条，用来实现下拉和弹出式菜单，点下菜单后弹出的一个选项列表,用户可以从中选择

　　**什么时候用：**

　　在比如像软件或网页交互界面等，需要提供菜单选项功能提供用户选择菜单选项功能时用到。

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，在图形界面上创建一个标签用以显示内容并放置``l ``=` `tk.Label(window, text``=``'   '``, bg``=``'green'``)``l.pack()` `# 第10步，定义一个函数功能，用来代表菜单选项的功能，这里为了操作简单，定义的功能比较简单``counter ``=` `0``def` `do_job():``  ``global` `counter``  ``l.config(text``=``'do '``+` `str``(counter))``  ``counter ``+``=` `1` `# 第5步，创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方``menubar ``=` `tk.Menu(window)` `# 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）``filemenu ``=` `tk.Menu(menubar, tearoff``=``0``)``# 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中``menubar.add_cascade(label``=``'File'``, menu``=``filemenu)` `# 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。``filemenu.add_command(label``=``'New'``, command``=``do_job)``filemenu.add_command(label``=``'Open'``, command``=``do_job)``filemenu.add_command(label``=``'Save'``, command``=``do_job)``filemenu.add_separator()  ``# 添加一条分隔线``filemenu.add_command(label``=``'Exit'``, command``=``window.quit) ``# 用tkinter里面自带的quit()函数` `# 第7步，创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）``editmenu ``=` `tk.Menu(menubar, tearoff``=``0``)``# 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中``menubar.add_cascade(label``=``'Edit'``, menu``=``editmenu)` `# 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能``editmenu.add_command(label``=``'Cut'``, command``=``do_job)``editmenu.add_command(label``=``'Copy'``, command``=``do_job)``editmenu.add_command(label``=``'Paste'``, command``=``do_job)` `# 第8步，创建第二级菜单，即菜单项里面的菜单``submenu ``=` `tk.Menu(filemenu) ``# 和上面定义菜单一样，不过此处实在File上创建一个空的菜单``filemenu.add_cascade(label``=``'Import'``, menu``=``submenu, underline``=``0``) ``# 给放入的菜单submenu命名为Import` `# 第9步，创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）``submenu.add_command(label``=``'Submenu_1'``, command``=``do_job)  ``# 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1` `# 第11步，创建菜单栏完成后，配置让菜单栏menubar显示出来``window.config(menu``=``menubar)` `# 第12步，主窗口循环显示``window.mainloop()
```

　　**测试效果：**

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808224139791-265028894.gif)

### 11. Frame 窗口部件

　　**简单说明：**　　

　　Frame：框架，用来承载放置其他GUI元素，就是一个容器，是一个在 Windows 上分离小区域的部件, 它能将 Windows 分成不同的区,然后存放不同的其他部件. 同时一个 Frame 上也能再分成两个 Frame, Frame 可以认为是一种容器.

　　**什么时候用：**

　　在比如像软件或网页交互界面等，有不同的界面逻辑层级和功能区域划分时可以用到，让交互界面逻辑更加清晰。

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，在图形界面上创建一个标签用以显示内容并放置``tk.Label(window, text``=``'on the window'``, bg``=``'red'``, font``=``(``'Arial'``, ``16``)).pack()  ``# 和前面部件分开创建和放置不同，其实可以创建和放置一步完成` `# 第5步，创建一个主frame，长在主window窗口上``frame ``=` `tk.Frame(window)``frame.pack()` `# 第6步，创建第二层框架frame，长在主框架frame上面``frame_l ``=` `tk.Frame(frame)``# 第二层frame，左frame，长在主frame上``frame_r ``=` `tk.Frame(frame)``# 第二层frame，右frame，长在主frame上``frame_l.pack(side``=``'left'``)``frame_r.pack(side``=``'right'``)` `# 第7步，创建三组标签，为第二层frame上面的内容，分为左区域和右区域，用不同颜色标识``tk.Label(frame_l, text``=``'on the frame_l1'``, bg``=``'green'``).pack()``tk.Label(frame_l, text``=``'on the frame_l2'``, bg``=``'green'``).pack()``tk.Label(frame_l, text``=``'on the frame_l3'``, bg``=``'green'``).pack()``tk.Label(frame_r, text``=``'on the frame_r1'``, bg``=``'yellow'``).pack()``tk.Label(frame_r, text``=``'on the frame_r2'``, bg``=``'yellow'``).pack()``tk.Label(frame_r, text``=``'on the frame_r3'``, bg``=``'yellow'``).pack()` `# 第8步，主窗口循环显示``window.mainloop()
```

　　**测试效果：**

 ![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808230952254-1515620535.png)

### 12. messageBox窗口部件

　　**简单说明：**　　

　　messageBox：消息框，用于显示你应用程序的消息框。(Python2中为tkMessagebox)，其实这里的messageBox就是我们平时看到的弹窗。 我们首先需要定义一个触发功能，来触发这个弹窗，这里我们就放上以前学过的button按钮，通过触发功能，调用messagebox吧，点击button按钮就会弹出提示对话框。下面给出messagebox提示信息的几种形式：

```
tkinter.messagebox.showinfo(title``=``'Hi'``, message``=``'你好！'``)      ``# 提示信息对话窗``tkinter.messagebox.showwarning(title``=``'Hi'``, message``=``'有警告！'``)    ``# 提出警告对话窗``tkinter.messagebox.showerror(title``=``'Hi'``, message``=``'出错了！'``)     ``# 提出错误对话窗``print``(tkinter.messagebox.askquestion(title``=``'Hi'``, message``=``'你好！'``)) ``# 询问选择对话窗return 'yes', 'no'``print``(tkinter.messagebox.askyesno(title``=``'Hi'``, message``=``'你好！'``))   ``# return 'True', 'False'``print``(tkinter.messagebox.askokcancel(title``=``'Hi'``, message``=``'你好！'``)) ``# return 'True', 'False'
```

　　**什么时候用：**

　　在比如像软件或网页交互界面等，有不同的界面逻辑层级和功能区域划分时可以用到，让交互界面逻辑更加清晰。

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入``import` `tkinter.messagebox ``# 要使用messagebox先要导入模块` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第5步，定义触发函数功能``def` `hit_me():``  ``tkinter.messagebox.showinfo(title``=``'Hi'``, message``=``'你好！'``)       ``# 提示信息对话窗``  ``# tkinter.messagebox.showwarning(title='Hi', message='有警告！')    # 提出警告对话窗``  ``# tkinter.messagebox.showerror(title='Hi', message='出错了！')     # 提出错误对话窗``  ``# print(tkinter.messagebox.askquestion(title='Hi', message='你好！')) # 询问选择对话窗return 'yes', 'no'``  ``# print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))   # return 'True', 'False'``  ``# print(tkinter.messagebox.askokcancel(title='Hi', message='你好！')) # return 'True', 'False'` `# 第4步，在图形界面上创建一个标签用以显示内容并放置``tk.Button(window, text``=``'hit me'``, bg``=``'green'``, font``=``(``'Arial'``, ``14``), command``=``hit_me).pack()` `# 第6步，主窗口循环显示``window.mainloop()
```

　　**测试效果：**

 ![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808233448829-65209831.png)![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808233531668-1546902314.png)

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808233622649-1216743879.png)![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808233706164-1056501102.png)

### 13. 窗口部件三种放置方式pack/grid/place

　　**参考来源：**

[The Grid Geometry Manager](http://effbot.org/tkinterbook/grid.htm)
[The Pack Geometry Manager](http://effbot.org/tkinterbook/pack.htm)
[The Place Geometry Manager](http://effbot.org/tkinterbook/place.htm)

　　**1. Grid：[The Grid Geometry Manager](http://effbot.org/tkinterbook/grid.htm)**　　

　　grid 是方格, 所以所有的内容会被放在这些规律的方格中。例如：

```
for` `i ``in` `range``(``3``):``  ``for` `j ``in` `range``(``3``):``    ``tk.Label(window, text``=``1``).grid(row``=``i, column``=``j, padx``=``10``, pady``=``10``, ipadx``=``10``, ipady``=``10``)
```

　　以上的代码就是创建一个三行三列的表格，其实 grid 就是用表格的形式定位的。这里的参数 row 为行，colum 为列，padx 就是单元格左右间距，pady 就是单元格上下间距，ipadx是单元格内部元素与单元格的左右间距，ipady是单元格内部元素与单元格的上下间距。

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，grid 放置方法``for` `i ``in` `range``(``3``):``  ``for` `j ``in` `range``(``3``):``    ``tk.Label(window, text``=``1``).grid(row``=``i, column``=``j, padx``=``10``, pady``=``10``, ipadx``=``10``, ipady``=``10``)` `# 第5步，主窗口循环显示``window.mainloop()
```

　　**测试效果：**

 ![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808235921409-1694739142.png)

　　**2. Pack：[The Pack Geometry Manager](http://effbot.org/tkinterbook/pack.htm)**

 　我们常用的pack(), 他会按照上下左右的方式排列.例如：

```
tk.Label(window, text``=``'P'``, fg``=``'red'``).pack(side``=``'top'``)  ``# 上``tk.Label(window, text``=``'P'``, fg``=``'red'``).pack(side``=``'bottom'``) ``# 下``tk.Label(window, text``=``'P'``, fg``=``'red'``).pack(side``=``'left'``)  ``# 左``tk.Label(window, text``=``'P'``, fg``=``'red'``).pack(side``=``'right'``) ``# 右
```

　　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，pack 放置方法``tk.Label(window, text``=``'P'``, fg``=``'red'``).pack(side``=``'top'``)  ``# 上``tk.Label(window, text``=``'P'``, fg``=``'red'``).pack(side``=``'bottom'``) ``# 下``tk.Label(window, text``=``'P'``, fg``=``'red'``).pack(side``=``'left'``)  ``# 左``tk.Label(window, text``=``'P'``, fg``=``'red'``).pack(side``=``'right'``) ``# 右` `# 第5步，主窗口循环显示``window.mainloop()
```

　　**测试效果：**

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180809000808064-1701266400.png)

　　**3. Place：[The Place Geometry Manager](http://effbot.org/tkinterbook/place.htm)**

 　再接下来我们来看place(), 这个比较容易理解，就是给精确的坐标来定位，如此处给的(50, 100)，就是将这个部件放在坐标为(x=50, y=100)的这个位置, 后面的参数 anchor='nw'，就是前面所讲的锚定点是西北角。例如：

```
tk.Label(window, text``=``'Pl'``, font``=``(``'Arial'``, ``20``), ).place(x``=``50``, y``=``100``, anchor``=``'nw'``)
```

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'My Window'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'500x300'``) ``# 这里的乘是小x` `# 第4步，place 放置方法（精准的放置到指定坐标点的位置上）``tk.Label(window, text``=``'Pl'``, font``=``(``'Arial'``, ``20``), ).place(x``=``50``, y``=``100``, anchor``=``'nw'``)` `# 第5步，主窗口循环显示``window.mainloop()
```

　　**测试效果：**

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180809001609402-1946078906.png)

### 14. 综合练习，用户登录窗口例子

　　编写一个用户登录界面，用户可以登录账户信息，如果账户已经存在，可以直接登录，登录名或者登录密码输入错误会提示，如果账户不存在，提示用户注册，点击注册进去注册页面，输入注册信息，确定后便可以返回登录界面进行登录。

　　**示例代码：**

```
#!/usr/bin/env python``# -*- coding: utf-8 -*-``# author:洪卫` `import` `tkinter as tk ``# 使用Tkinter前需要先导入``import` `tkinter.messagebox``import` `pickle` `# 第1步，实例化object，建立窗口window``window ``=` `tk.Tk()` `# 第2步，给窗口的可视化起名字``window.title(``'Wellcome to Hongwei Website'``)` `# 第3步，设定窗口的大小(长 * 宽)``window.geometry(``'400x300'``) ``# 这里的乘是小x` `# 第4步，加载 wellcome image``canvas ``=` `tk.Canvas(window, width``=``400``, height``=``135``, bg``=``'green'``)``image_file ``=` `tk.PhotoImage(``file``=``'pic.gif'``)``image ``=` `canvas.create_image(``200``, ``0``, anchor``=``'n'``, image``=``image_file)``canvas.pack(side``=``'top'``)``tk.Label(window, text``=``'Wellcome'``,font``=``(``'Arial'``, ``16``)).pack()` `# 第5步，用户信息``tk.Label(window, text``=``'User name:'``, font``=``(``'Arial'``, ``14``)).place(x``=``10``, y``=``170``)``tk.Label(window, text``=``'Password:'``, font``=``(``'Arial'``, ``14``)).place(x``=``10``, y``=``210``)` `# 第6步，用户登录输入框entry``# 用户名``var_usr_name ``=` `tk.StringVar()``var_usr_name.``set``(``'example@python.com'``)``entry_usr_name ``=` `tk.Entry(window, textvariable``=``var_usr_name, font``=``(``'Arial'``, ``14``))``entry_usr_name.place(x``=``120``,y``=``175``)``# 用户密码``var_usr_pwd ``=` `tk.StringVar()``entry_usr_pwd ``=` `tk.Entry(window, textvariable``=``var_usr_pwd, font``=``(``'Arial'``, ``14``), show``=``'*'``)``entry_usr_pwd.place(x``=``120``,y``=``215``)` `# 第8步，定义用户登录功能``def` `usr_login():``  ``# 这两行代码就是获取用户输入的usr_name和usr_pwd``  ``usr_name ``=` `var_usr_name.get()``  ``usr_pwd ``=` `var_usr_pwd.get()` `  ``# 这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。``  ``# 中间的两行就是我们的匹配，即程序将输入的信息和文件中的信息匹配。``  ``try``:``    ``with ``open``(``'usrs_info.pickle'``, ``'rb'``) as usr_file:``      ``usrs_info ``=` `pickle.load(usr_file)``  ``except` `FileNotFoundError:``    ``# 这里就是我们在没有读取到`usr_file`的时候，程序会创建一个`usr_file`这个文件，并将管理员``    ``# 的用户和密码写入，即用户名为`admin`密码为`admin`。``    ``with ``open``(``'usrs_info.pickle'``, ``'wb'``) as usr_file:``      ``usrs_info ``=` `{``'admin'``: ``'admin'``}``      ``pickle.dump(usrs_info, usr_file)``      ``usr_file.close()  ``# 必须先关闭，否则pickle.load()会出现EOFError: Ran out of input` `  ``# 如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗how are you? 加上你的用户名。``  ``if` `usr_name ``in` `usrs_info:``    ``if` `usr_pwd ``=``=` `usrs_info[usr_name]:``      ``tkinter.messagebox.showinfo(title``=``'Welcome'``, message``=``'How are you? '` `+` `usr_name)``    ``# 如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'``    ``else``:``      ``tkinter.messagebox.showerror(message``=``'Error, your password is wrong, try again.'``)``  ``else``: ``# 如果发现用户名不存在``    ``is_sign_up ``=` `tkinter.messagebox.askyesno(``'Welcome！ '``, ``'You have not sign up yet. Sign up now?'``)``    ``# 提示需不需要注册新用户``    ``if` `is_sign_up:``      ``usr_sign_up()` `# 第9步，定义用户注册功能``def` `usr_sign_up():``  ``def` `sign_to_Hongwei_Website():``    ``# 以下三行就是获取我们注册时所输入的信息``    ``np ``=` `new_pwd.get()``    ``npf ``=` `new_pwd_confirm.get()``    ``nn ``=` `new_name.get()` `    ``# 这里是打开我们记录数据的文件，将注册信息读出``    ``with ``open``(``'usrs_info.pickle'``, ``'rb'``) as usr_file:``      ``exist_usr_info ``=` `pickle.load(usr_file)``    ``# 这里就是判断，如果两次密码输入不一致，则提示Error, Password and confirm password must be the same!``    ``if` `np !``=` `npf:``      ``tkinter.messagebox.showerror(``'Error'``, ``'Password and confirm password must be the same!'``)` `    ``# 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!``    ``elif` `nn ``in` `exist_usr_info:``      ``tkinter.messagebox.showerror(``'Error'``, ``'The user has already signed up!'``)` `    ``# 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。``    ``else``:``      ``exist_usr_info[nn] ``=` `np``      ``with ``open``(``'usrs_info.pickle'``, ``'wb'``) as usr_file:``        ``pickle.dump(exist_usr_info, usr_file)``      ``tkinter.messagebox.showinfo(``'Welcome'``, ``'You have successfully signed up!'``)``      ``# 然后销毁窗口。``      ``window_sign_up.destroy()` `  ``# 定义长在窗口上的窗口``  ``window_sign_up ``=` `tk.Toplevel(window)``  ``window_sign_up.geometry(``'300x200'``)``  ``window_sign_up.title(``'Sign up window'``)` `  ``new_name ``=` `tk.StringVar() ``# 将输入的注册名赋值给变量``  ``new_name.``set``(``'example@python.com'``) ``# 将最初显示定为'example@python.com'``  ``tk.Label(window_sign_up, text``=``'User name: '``).place(x``=``10``, y``=``10``) ``# 将`User name:`放置在坐标（10,10）。``  ``entry_new_name ``=` `tk.Entry(window_sign_up, textvariable``=``new_name) ``# 创建一个注册名的`entry`，变量为`new_name```  ``entry_new_name.place(x``=``130``, y``=``10``) ``# `entry`放置在坐标（150,10）.` `  ``new_pwd ``=` `tk.StringVar()``  ``tk.Label(window_sign_up, text``=``'Password: '``).place(x``=``10``, y``=``50``)``  ``entry_usr_pwd ``=` `tk.Entry(window_sign_up, textvariable``=``new_pwd, show``=``'*'``)``  ``entry_usr_pwd.place(x``=``130``, y``=``50``)` `  ``new_pwd_confirm ``=` `tk.StringVar()``  ``tk.Label(window_sign_up, text``=``'Confirm password: '``).place(x``=``10``, y``=``90``)``  ``entry_usr_pwd_confirm ``=` `tk.Entry(window_sign_up, textvariable``=``new_pwd_confirm, show``=``'*'``)``  ``entry_usr_pwd_confirm.place(x``=``130``, y``=``90``)` `  ``# 下面的 sign_to_Hongwei_Website``  ``btn_comfirm_sign_up ``=` `tk.Button(window_sign_up, text``=``'Sign up'``, command``=``sign_to_Hongwei_Website)``  ``btn_comfirm_sign_up.place(x``=``180``, y``=``120``)` `# 第7步，login and sign up 按钮``btn_login ``=` `tk.Button(window, text``=``'Login'``, command``=``usr_login)``btn_login.place(x``=``120``, y``=``240``)``btn_sign_up ``=` `tk.Button(window, text``=``'Sign up'``, command``=``usr_sign_up)``btn_sign_up.place(x``=``200``, y``=``240``)` `# 第10步，主窗口循环显示``window.mainloop()
```

　　测试效果：

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180809012148716-1242674498.png)![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180809012218625-275586165.png)