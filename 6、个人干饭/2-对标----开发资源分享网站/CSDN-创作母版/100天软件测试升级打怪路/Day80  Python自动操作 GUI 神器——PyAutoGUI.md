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





























