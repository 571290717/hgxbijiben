# Day80  Python自动操作 GUI 神器——PyAutoGUI



安装

```
pip3 install pyautogui
```



### 鼠标移动

桌面操作最基本的就是鼠标操作了，我们可以控制鼠标的移动：

```
# 移动鼠标
pyautogui.moveTo(200,400,duration=2)
pyautogui.moveRel(200,500,duration=2)
```

整个桌面是以左上角为坐标轴的原点，所有的操作都以这个原点，来确定操作位置。

第一行是将鼠标移动到指定的像素(200,400)位置，第二行代码是将鼠标按照当前点向右移动200px，向下移动400px这个方向移动。

两行代码中都有一个共同的参数 `duration`，这个参数表示移动时间，即在指定时间内完成移动操作，单位是秒。



获取鼠标位置：

```
print(pyautogui.position())  
```

这个很好理解，就是获取鼠标在当前屏幕中的坐标位置，运行这行代码，我们会得到诸如下面的信息：

> Point(x=400, y=900)

`pyautogui`针对这三个按键操作都有相应的处理：

```
# 鼠标点击，默认左键
pyautogui.click(100,100)   
# 单击左键
pyautogui.click(100,100,button='left')  
# 单击右键
pyautogui.click(100,300,button='right') 
# 单击中间 
pyautogui.click(100,300,button='middle')  
```

有双击操作：

```
# 双击左键
pyautogui.doubleClick(10,10)  
# 双击右键
pyautogui.rightClick(10,10)   
# 双击中键
pyautogui.middleClick(10,10) 
```

```
# 鼠标按下
pyautogui.mouseDown()   
# 鼠标释放
pyautogui.mouseUp()    
```

### 鼠标拖动

可以控制鼠标拖动到指定坐标位置，并且设置操作时间：

```
pyautogui.dragTo(100,300,duration=1)   

duration
n.	持续时间; 期间
```

这个运行效果和前面移动类似。

根据前面移动的经验，我们也有按照方向拖动鼠标：

```
pyautogui.dragRel(100,300,duration=4) 
```

### 鼠标滚动

在桌面操作中，我们有时候需要滚动鼠标到达向上或者向下的位置，这时候我们可以使用 `scroll` 这个函数来控制：

```
pyautogui.scroll(30000) 
```

参数是整数，表示向上或向下滚动多少个单位，这个单位根据不同的操作系统可能不一样。如果向上滚动，传入正整数，向下滚动传入负整数。



### 屏幕处理





### 获取屏幕截图

我们先来假设一个场景：我现在要在屏幕上找到一个红色的点，你会怎么做？通常的做法是拿到这个红色点的颜色值，然后再对屏幕上的点逐个进行比较，直到找到为止。

`pyautogui` 为我们这个操作场景提供了支持，分别有三个函数可以完成这三件事情。

```
im = pyautogui.screenshot()
im.save('screenshot.png')
rgb = im.getpixel((100, 500))
print(rgb)
match = pyautogui.pixelMatchesColor(500,500,(12,120,400))
print(match)
```

第一个是获取屏幕截图函数，它可以返回一个 Pillow 的 image 对象; 第二个是获取屏幕截图中指定坐标点的颜色，返回 rgb 颜色值；第三个是将指定坐标点的颜色和目标的颜色进行比对，返回布尔值。

我们再来升级一下需求：

我现在要在屏幕上找到 edge 浏览器的图标，你会怎么做？

通常的做法是先知道 edge 浏览器的图标长啥样，是绿色还是蓝色，是胖的还是瘦的，对吧？然后再在屏幕上去进行图标的匹配，直到找到一个图标跟我们目标图标一样，就得到了结果。

于是，我们的代码如下：

```
# 图像识别（一个）
oneLocation = pyautogui.locateOnScreen('1.png')
print(oneLocation)  

# 图像识别（多个）
allLocation = pyautogui.locateAllOnScreen('1.png')
print(list(allLocation))
```

你可以在桌面上将某个应用的图标截取下来，保存为图片，然后使用上面几行代码来识别，识别成功，你会返回类似下面的结果：

```
Box(left=20, top=89, width=33, height=34)
[Box(left=20, top=89, width=33, height=34)]
```

这就是图片在桌面的位置，如果找不到图片，就会返回 None。

### 键盘输入

### 键盘函数

键盘输入有下面几个常用的函数：

- keyDown()：模拟按键按下
- keyUP()：模拟按键松开
- press()：模拟一次按键过程，即 keyDown 和 keyUP 的组合
- typewrite()：模拟键盘输出内容

举个例子，大家平时输入感叹号（！）是怎么操作键盘的？

按住 shift 按键，然后再按住 1 按键，就可以了。用 `pyautogui` 控制就是：

```
pyautogui.keyDown('shift')    
pyautogui.press('1')    
pyautogui.keyUp('shift')   
```

运行上面的代码，如果你的鼠标是放在编辑框中，你会得到一个感叹号！

我们还可以直接输出内容：

```
pyautogui.typewrite('python', 1)
```

第一个参数是输出的内容，第二个参数是间隔时间，单位是秒。

运行上面代码，你的编辑器里面就会每隔1秒钟按顺序输出 python 的6个字母。

### 特殊符号

有时我们需要输入键盘的一些特殊的符号按键，比如 换行、方向键等，这些有相对应的键盘字符串表示：

```
pyautogui.typewrite(['p','y','t','h','o','n','enter'])   
```

运行上面代码，编辑器里面就会输出 python 之后换行。

其他特殊按键对应的字符串请参考官方说明。

### 快捷键

如果我要复制一个内容，大部分情况下会使用快键键 ctrl + c，按照上面讲的，我们应该这么实现：

```
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')
```

这样写起来很麻烦，而且需要掌控按键的按下和释放的顺序。

`pyautogui` 为我们提供了一个快捷的函数：

```
pyautogui.hotkey('ctrl','c')
```

实现的效果和上面的4行代码相同。

### 信息框

当你在模拟一个桌面操作的时候，如果有分支操作需要根据实际情况来判断，你是不是需要有一个地方可以让你选择走哪个分支？

`pyautogui` 贴心地考虑到了这种情况，你可以通过弹出一个选择框来中断当前的操作，选择操作分支。

```
way = pyautogui.confirm('领导，该走哪条路？', buttons=['农村路', '水路', '陆路'])
print(way)
```

这里就是我们 HTML 页面的 confirm 选择框，选择了选项之后，我们可以获取到选择的选项，然后基于这个选项做判断，进入相应的操作分支。

除了选择确认框之外，还有其他一些提示信息框：

```
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







