# Day81  python使用pynput库操作、监控你的鼠标和键盘



pynput，是专门针对鼠标和键盘的，至于pygame、pyglet等游戏框架虽然也提供了鼠标、键盘的监控事件，但它们毕竟是用来开发游戏的，还提供了创建窗口、图形绘制、物体的碰撞检测等等很多复杂的功能。如果只是单纯的操作鼠标和键盘，使用这种游戏框架有点小题大做了，下面我们就来看看这个名叫pynput的模块吧，看看它的使用方法。

## 鼠标

### 操作鼠标

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
```



```python
from pynput.mouse import Controller

mouse = Controller()

# 垂直方向、沿着y轴滑动
# 第一个参数是针对水平方向的，暂时不用管，为0则表示不变。
# 第二个参数是针对垂直方向的，大于0表示向下，小于0表示向上
mouse.scroll(0, 2)



from pynput.mouse import Controller

mouse = Controller()
# 大于0向右，小于0向左
mouse.scroll(3, 0)
```

### 监控鼠标

我们可以使用pynput操作鼠标，同时pynput也支持我们在手动操作鼠标的时候记录我们做了哪些操作，同理后面介绍的键盘也是一样的，都分为操作、监控两部分。

```python
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
```

上面实例化一个Listener时，相当于开启了一个线程，因为Listener这个类继承自threading.Thread。所以我们调用listener.join()相当于就阻塞在这里了，会一直监控鼠标事件。所以我们需要一个机制来让它停下来：

```python
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
```

另外执行的时候，你会发现，程序会一直阻塞在listener.join()处，如果下面还有代码要怎么执行呢？

```python
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
```

## 键盘

操作键盘也比较简单，无非也是按下某个键、松开某个键，或者在按下某个键(或者多个)不松开的前提下、按下另一个键，下面来操作一下。方法和操作鼠标比较类似：

```python
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
```

下面来看看如何在按住某个键不放的前提下，按下另外的键

```python
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
```

### 监控

监控键盘使用的方法和监控鼠标非常类似，依旧是实例化一个类Listener

```python
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
```

所以定义函数的方式和操作鼠标也是类似的，该Listener同样会开启一个线程。另外这里的key打印的是"Key.xxx"，我们转成字符串其实已经可以判断按下了哪个键了。不过key里面还是提供了方法，让我们获取操作的键

```python
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

此时返回的就是普通的键的名称，没有Key.这个前缀了。
以上就是这个模块的内容了，具体怎么使用可以由你自己决定。另外这个模块在Linux上也是可以运行的，但前提是必须有显示器，而公司用的服务器肯定是不带显示器的，所以不推荐Linux上使用

以上就是python使用pynput库操作、监控你的鼠标和键盘的详细内容，更多关于python pynput库操作监控鼠标键盘的资料请关注Wordpress教程网其它相关文章！