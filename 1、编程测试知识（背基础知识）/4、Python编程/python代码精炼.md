```python
print()
1
type()



int \ flobat \ bool \ str \ list \tuple \ set \ dict \

print(f'XXX{xx}')

print(F'XXX{xxx}')

print('%s'%(xx))

print('%s'.format(xx))

%s  %d  %f

\n \t 

print(XX ,seq="",end="")

input("XX")

int(xx) \ float( )  \ complex (real ,imag )

str(xx) \   repr ( ) 表达式变成字符串

eval（ ） 字符串变成表达式 

 tuple（xx） list(xx) chr(xxx)整数变字符

ord(xx)字符变整数

hex(x) 16  oct( x) 8 bin(x) 2



+-*/    //  % **  ()   =  += -= *= /= //= %= **=

== != > <   >=  <=

and or not  

if ... else ...

if ... elif ... else ...

if if if ..

import random

random.randint(frist ,end )

date1 if bool else date2

while..

break continue

for i in strxxx:

​	XXXXXXxx

#字符串
#下标
#切片  
#!!!!!!!!!!!!!------序列【开始位置下标：结束位置下标：步长】--------!!!!!!!!!!
str.find(str(zi),begin，end)
str.index(str(zi),begin,end)
rfind()
rindex()
count()
str.replace(oldstr(zi),newstr(zi),changes_number)
str.split(str(zi),[num])
str(zi).join(str [or other])


str.capitalize() 首字母大写

capitalize - 必应词典
美[ˈkæpɪt(ə)lˌaɪz]英[ˈkæpɪtəlaɪz]
v.用大写字母书写（或印刷）；把…首字母大写；变卖资产；变现
网络资本化；首字大写；利用


title()

lower()

upper()
lstrip()
rstrip()
strip()
'''它的函数原型：string.strip(s[, chars])，它返回的是字符串的副本，并删除前导和后缀字符。
（意思就是你想去掉字符串里面的哪些字符，那么你就把这些字符当参数传入。此函数只会删除头和尾的字符，中间的不会删除。）
如果strip()的参数为空，那么会默认删除字符串头和尾的空白字符(包括\n，\r，\t这些)。
lstrip()：去除左边
rstrip()：去除右边

示例一：
>>> str = ' ab cd '
>>> str
' ab cd '
>>> str.strip() #删除头尾空格
'ab cd'
>>> str.lstrip() #删除开头空格
'ab cd '
>>> str.rstrip() #删除结尾空格
' ab cd'

示例二：
>>> str2 = '1a2b12c21'
>>> str2.strip('12') #删除头尾的1和2
'a2b12c'
>>> str2.lstrip('12') #删除开头的1和2
'a2b12c21'
>>> str2.rstrip('12') #删除结尾的1和2
'1a2b12c'


示例三：
a="aabcacb1111acbba"
print(a.strip("abc"))
print(a.strip("acb"))
print(a.strip("bac"))
print(a.strip("bca"))
print(a.strip("cab"))
print(a.strip("cba"))

输出：
1111
1111
1111
1111
1111
1111'''


#ljust()返回一个原字符串对齐，使用指定字符填充对应长度的新字符串
str.ljust(length,tianstr)
rljust()
center()


startswith()：检查字符串是否是以指定子串开头，是则返回 True，否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。

str.startwith(str(zi),begin,end)
str.endwith(str(zi),begin,end)
str.isalpha() 至少有一个str全是字母
str.isdigit() 只是数字
str.isalnum() isalphe并isdigit
str.isspace() 只是空白


#列表
list[x]  查找
list.index(list(zi),begin,end)
count()
len()
'xx' in list   ->bool
'xx' not in list -> bool
list.append(xx) 尾加1
list.extend(x,x) 尾加n
list.insert(num,str)
del XXX
list.pop([num])
list.remove(str)
list.clear()
list[x]='xx'
list.reverse()
list.sort([ket=按第几个数来排默认第一个,reverse=false])
list.copy()
while i < len(list):
    print(list[i])
    
for i in list:
    print(i)
list[i][j]

#元组
typle=(xx,XX)
index()
count()
len()

# zidian
dict = {"xx":"XX"} 
dict[xx]=XX #zen
del dict[xx]
dict.clear()
dict['xx'] #cha
dict.get('xx')
dict.keys()
dict.values()
dict.items()
for key in dict.keys(): 
    print(key)
for value in dict.values():
    print(value)
for item in dict.items():
    print(item)
for key , value in dict1.items():
    print(f'{key} = {values}')

#集合
{}、set()
add()、update()
remove()、discard()
pop() 、 
in 
not in


# 

| 运算符 |      描述      |      支持的容器类型      |
| :----: | :------------: | :----------------------: |
|   +    |      合并      |    字符串、列表、元组    |
|   *    |      复制      |    字符串、列表、元组    |
|   in   |  元素是否存在  | 字符串、列表、元组、字典 |
| not in | 元素是否不存在 | 字符串、列表、元组、字典 |


len()
del()
max()
min()    
range(n,m,x)
enumerate(可遍历对象，start=0)
tuple()
list()
set()
while
for 
[i for i in range(10)]
[(i,j) for i in range(1,3) for j in range(3)]
dict1 = {i : i*2 for i in range(1,5)}
dict2 = {list1[i] : list2[j] for i in range(len(list1))}
dict3 = {key : value for key,value in counts.items() if value>=200}

def xxx():
    """xxxxxxXXXXX"""
    XXX
    return xxxxxxX
help(xxx)
   
  
global a 


#拆包和交换变量值

def return_num():
    return 100,200
num1 , num2 = return_num() #100 , 200

dict1={xx1:xx1,xx2:xx2}
a,b=dict1 #xx1,xx2

a,b=b,a

id(XX)

递归

lambda 参数 ： 表达式
fn1 = lambda a,b : a + b

fn1 =lambda a ,b : a if a>b else b

students = [
    {'name ':'Tom' , 'age' : 20 },
    {'name ':'Rose' , 'age' : 19 },
    {'name ':'Jack' , 'age' : 22 }
    
]

#按name值升序排列
students.sort(key=lambda x : x['name'])
#
student.sort(key=lambda x : x['name'] , reverse = True)
#
student.sort(key=lambda x : x['age'])

#!高阶函数
abs(-10)
round(1.2)
eg:
    def sum_num(a,b,f):
        return f(a) + f(b)
    
    result = sum_num(-1,-2,abs)
    print(result)
    
map(func,list1)
reduce(func,list1) #reduce vi ，vt 减少 降低 ，归纳为
filter(func list1)

?# 文件操作
open(name ,mode)
name: '路径'
mode: 打开模式
    
| 模式 | 描述                                                         |
| :--: | ------------------------------------------------------------ |
|  r   | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
|  rb  | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。 |
|  r+  | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 |
|  w   | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
|  wb  | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
|  w+  | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
|  a   | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
|  ab  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
|  a+  | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

eg：
 f=open('test.txt','w')
    
    f此时为文件对象
   文件对象.write('内容')
f.write('hello world1')
f.close()

f.read(num)
f.readlines()

f.seek(偏移量，起始位置)

    起始位置：

- 0：文件开头
- 1：当前位置
- 2：文件结尾


#文件备份
old_name = input('请输入您要备份的文件名：')
index = old_name.rfind('.')

#print(index)后缀中的.的下标
#print(old_name[:index])源文件名（无后缀）
new_name = old_name[:index] + '[备份]' + old_name[index:]d

print(new_name)

old_f = open(old_name , ' rb')
new_f = open(new_name, 'wb')

while True:
    con = old_f.read(1024)
    if len(con) ==0:
        break
     
    new_f.write(con)
    
    
old_f.close()
new_f.close()


import os
 
 os.函数名（）
os.rename(目标文件名，新文件名)
os.remove(目标文件名)
os.mkdir(文件夹名字)
os.rmdir(文件夹名字)
os.getcwd()#获得当前目录
os.chdir(目录)#改变默认目录
os.listdir(目录)




#面对对象

class Washer():
    def wash(self):
        print('xxxx')

# 创建对象
对象名 = 类名()

# 创建对象
haier1 = Washer()
# haier对象调用实例方法
haier1.wash()

?# self指的是调用该函数的对象

leiwai:
duixiang.shuxin = xxx
duixiang.shuxin

leili:
    self.shuxin

__xx__()#魔术方法

__init__()
__str__()
__del__()

class A(object):
    XXXx
    
 class B(A):
    XXXX
    
 

 # 如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用自己子类的初始化
        self.__init__()

  # 调用父类方法，但是为保证调用到的也是父类的属性，必须在调用方法前调用父类的初始化
    def B(self):
        A.__init__(self)


 #调用父类
super().XXX


 		 # 方法2.1
        # super(School, self).__init__()
        # super(School, self).make_cake()

        # 方法2.2
        super().__init__()
        super().make_cake()
 


 # 一次性调用父类的同名属性和方法
    def make_old_cake(self):
        # 方法一：代码冗余；父类类名如果变化，这里代码需要频繁修改
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)

        # 方法二: super()
        # 方法2.1 super(当前类名, self).函数()
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()

        # 方法2.2 super().函数()
        super().__init__()
        super().make_cake()


        
        
       设置私有权限的方法：在属性名和方法名 前面 加上两个下划线 __ 
        
        即设置某个实例属性或实例方法不继承给子类。
        
        一般定义函数名`get_xx`用来获取私有属性，定义`set_xx`用来修改私有属性值。
        
class 类名():
  # 私有属性
  __属性名 = 值

  # 私有方法
  def __函数名(self):
    代码
        
  多态指的是一类事物有多种形态，（一个抽象类有多个子类，因而多态的概念依赖于继承）。

- 定义：多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果      
        
        
        
 ### 类方法      
需要用装饰器`@classmethod`来标识其为类方法，对于类方法，**第一个参数必须是类对象**，一般以`cls`作为第一个参数。

- 当方法中 **需要使用类对象** (如访问私有类属性等)时，定义类方法
- 类方法一般和类属性配合使用


class Dog(object):
    __tooth = 10
    
    @classmethod
    def get_tooth(cls):
        return cls.__tooth
    
    wangcai = Dog()
    result = wangcai.get_tooth()
    print(result)
    
###  静态方法特点

- 需要通过装饰器`@staticmethod`来进行修饰，**静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）**。
- 静态方法 也能够通过 **实例对象** 和 **类对象** 去访问。

## 4.2.2 静态方法使用场景

- 当方法中 **既不需要使用实例对象**(如实例对象，实例属性)，**也不需要使用类对象** (如类属性、类方法、创建实例等)时，定义静态方法
- **取消不需要的参数传递**，有利于 **减少不必要的内存占用和性能消耗**
class Dog(object):
 	@staticmmethod
    def info_print():
        print('xXAXASXASXAs')
        
wangcao = Dog()
# 静态方法既可以使用对象访问又可以使用类访问
wangcai.info_print()
Dog.info_print()
 
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码


try:
    可能发生错误的代码
except 异常类型:
    如果捕获到该异常类型执行的代码


try :
    print(1)
except Exception as result:
    print(result)
else:
    print('我是else，是没有异常执行的代码')
finally:
    print('我是else，是没有异常的时候执行的代码')
    
    
raise xxx


class ShortInputError(Exceptin):
    def __init__(self,length,min_len):
        self.length = length
        self.min_len = min_len
     def __str__(slef):
        return f'你输入的长度是{self.length}，不能少于{self.min_len}个字符'
    
def main():
    try:
        con = input('请输入密码:')
        if lem(con) <3 :
			raise ShortInputError(len(con),3)
   except Exception as result :
    	print(reslt)
   else:
    	print('chenggong')
 

main(c)
    

    from xxx import xxx as ccc
    
 如果一个模块文件中有`__all__`变量，当使用`from xxx import *`导入时，只能导入这个列表中的元素

    __all__ = ['testA']


def testA():
    print('testA')


def testB():
    print('testB')
    
    
 import baoname.modulename

baoname.modulename.mubiao
    
  ### 多任务

- 使用多任务就能充分利用CPU资源，提高程序的执行效率，让你的程序具备处理多个任务的能力。
- 多任务执行方式有两种方式：**并发**和**并行**，这里并行才是多个任务真正意义一起执行。  
    
    
    import multiprocessing
    
    Processs([group[,terget[,name[,args[,kwargs]]]])
     		 group:指定进程组   
     		 terget：执行的目标任务名字
              name：进程名字
              args：以元组方式给执行任务传参
              kwargs：以字典形参传参
    Process创建的实例对象的常用方法：
              start（）：启动子进程实例（创建子进程）
    		join（）：等待子进程执行结束
              terminate（）：不管任务是否完成，立即终止子进程
              
terminate	英[ˈtɜːmɪneɪt]
美[ˈtɜːrmɪneɪt]
v.	终止; (使)停止; 结束; 到达终点站;
adj.	终止的; 有限的(小数等);

    name：当前进程的别名，默认为Process-N，N为从1开始递增的整数
    
    
   import multiprocessing
   import time
              
    def dance():
              for i in range(5);
              		print('dancing。。。')
               		time.sleep(0.2)
    # 唱歌任务
    def sing():
        for i in range(5):
            print("唱歌中...")
            time.sleep(0.2)	
    
     if __name__ == '__main__':
     		#创建跳舞子进程
     		#group表示进程组，目前只能用None
     		#target：表示执行的目标任务名（函数名、方法名）
     		#name：进程名称，默认Process-1，......
     		dance_process = multiprocessing.Process(target = dance           ,name="myprocess1")
     		sing_process = multiprocessing.Process(target=sing)
    		
    		#启动子进程执行对应的任务
    		dance_process.start()
    		sing_process.start()
    		
   
   #总结
   import multiprocessing
   sub_process=multiprocessing.Process(target=任务名)
   sub_process.start()
   
    ###获取进程编号的目的是验证主进程和子进程的关系，可以得知子进程是由那个主进程创建出来的
    
    os.getpid()#获取当前进程编号
    os.kill(os.getpid(),9)#根据进程编号杀死进程
    os.getppid()#获取当前父进程编号
    
    ###带参数,元组形式tuple
    sub_process = mutiprocessing.Process(target=XXX ,arg=(x,xx))
    #kwargs:表示以字典方式传入参数
    sub_process = multiprocessing.Process(target=task,kwargs={'xxx'=xxx})
    
- **元组方式传参(args)**: 元组方式传参一定要和参数的顺序保持一致。
- **字典方式传参(kwargs)**: 字典方式传参字典中的key一定要和参数名保持一致    
    
    
1. 进程之间不共享全局变量
2. 主进程会等待所有的子进程执行结束再结束

**守护主进程:**

- 守护主进程就是主进程退出子进程销毁不再执行

sub_process.daemon = True

- 为了保证子进程能够正常的运行，主进程会等所有的子进程执行完成以后再销毁，设置守护主进程的目的是**主进程退出子进程销毁，不让主进程再等待子进程去执行**。
- 设置守护主进程方式： **子进程对象.daemon = True**
- 销毁子进程方式： **子进程对象.terminate()



####线程
多线程可以完成多任务

import threading

Thread([group[,target[,name[,args[,kwargs]]]]])
- group: 线程组，目前只能使用None
- target: 执行的目标任务名
- args: 以元组的方式给执行任务传参
- kwargs: 以字典方式给执行任务传参
- name: 线程名，一般不用设置

start()

##eg:
import threading

sub_thread = threading.Thread(target=任务名,arg=(xx,xx),kwarg={'xxx'=xx})

sub_thread.start()

1. 线程之间执行是无序的
2. 主线程会等待所有的子线程执行结束再结束
3. 线程之间共享全局变量
4. 线程之间共享全局变量数据出现错误问题



**守护主线程:**

- 守护主线程就是主线程退出子线程销毁不再执行

**设置守护主线程有两种方式：**

1. threading.Thread(target=show_info, daemon=True)
2. 线程对象.setDaemon(True)


if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)

    # 启动线程
    first_thread.start()
    # 主线程等待第一个线程执行完成以后代码再继续执行，让其执行第二个线程
    # 线程同步： 一个任务执行完成以后另外一个任务才能执行，同一个时刻只有一个任务在执行
    first_thread.join()
    # 启动线程
    second_thread.start()


线程之间共享全局变量可能会导致数据出现错误问题，可以使用线程同步方式来解决这个问题。

- 线程等待(join)

互斥锁: 对共享数据进行锁定，保证同一时刻只能有一个线程去操作。

mutex = threading.Lock()
mutex.acquire()
xxxxx
xxxxXXX
...
mutex.release()
# 提示：加上互斥锁，那个线程抢到这个锁我们决定不了，那线程抢到锁那个线程先执行，没有抢到的线程需要等待
    # 加上互斥锁多任务瞬间变成单任务，性能会下降，也就是说同一时刻只能有一个线程去执行

###用互斥锁完成2个线程对同一个全局变量各加100万次的操作
import threading

g_num = 0

lock = threading.Locck()

def sum_num1():
	lock.acquire()
	for i in range(1000000):
		global g_num
		g_num +=1
	print("sum1:", g_num)
	lockrelease()
	
def sum_num2():
	lock.acquire()
	for i in range(1000000):
		global g_num
		g_num +=1
	print("sum1:", g_num)
	lockrelease()	

if __name__ == '__main__':
	first_thread = threading.Thread(target=sum_num1)
	second_thread = threading.Thread(target=sum_num2)
	
	first_thread.start()
	second_thread.start()
	
- 使用互斥锁的时候需要注意死锁的问题，要在合适的地方注意释放锁。
- 死锁一旦产生就会造成应用程序的停止响应，应用程序无法再继续往下执行了。



####IP地址
ifconfig  or  ipconfig 
ping 
IP 地址的作用是标识网络中唯一的一台设备的
IP 地址的表现形式分为: IPv4 和 IPv6
查看网卡信息：ifconfig
检查网络： ping
端口是传输数据的通道，是数据传输必经之路。
端口的作用就是给运行的应用程序提供传输数据的通道。
端口号的作用是用来区分和管理不同端口的，通过端口号能找到唯一个的一个端口。
端口号可以分为两类： 知名端口号 和 动态端口号
知名端口号的范围是0到1023
动态端口号的范围是1024到65535
TCP 是一个稳定、可靠的传输协议，常用于对数据进行准确无误的传输，比如: 文件下载，浏览器上网。
进程之间网络数据的传输可以通过 socket 来完成， socket 就是进程间网络数据通信的工具。

###TCP 客户端程序开发流程的介绍
步骤说明:
创建客户端套接字对象
和服务端套接字建立连接
发送数据
接收数据
关闭客户端套接字

导入socket模块
创建TCP套接字‘socket’
参数1: ‘AF_INET’, 表示IPv4地址类型
参数2: ‘SOCK_STREAM’, 表示TCP传输协议类型
发送数据‘send’
参数1: 要发送的二进制数据， 注意: 字符串需要使用encode()方法进行编码
接收数据‘recv’
参数1: 表示每次接收数据的大小，单位是字节
关闭套接字‘socket’表示通信完成

#介绍 socket
import socket
socket.socket(AddressFamily,Type)

connect((host,port))
send(data)
recv(buffersize)

import socket

if __name__ == '__main__':
	tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	tcp_client_socket = connect(('localhost',8080))
	send_data = "XXXXXXX".encode('gbk')
	tcp_client_socket.send(send_data)
	recv_data = tcp_client_socket.recv(1024)
	print(recv_data)
	recv_content = recv_data.decode('gbk')
	print('recv_content:',recv_content)
	tcp_click_socket.close()
	
##开发 TCP 服务端程序开发步骤回顾
创建服务端端套接字对象
绑定端口号
设置监听
等待接受客户端的连接请求
接收数据
发送数据
关闭套接字

import socket
socket.socket(AddressFamily,Type)
bind((host,port))
listen(backlog)
accept()
send(data)
recv(buffersize)  buffersize 是每次接收数据的长度


buffer	英[ˈbʌfə(r)]
美[ˈbʌfər]
n.	缓冲器; 缓冲物; 起缓冲作用的人; (火车头尾或轨道末端的)减震器; 缓存区; 缓冲存储器; 愚蠢老头;
vt.	缓存; 减少(伤害); 保护; 使不受…的侵害; 缓冲; 存储;
buffersize 缓冲区大小



##eg:
import socket

if __name__ =='__main__':
	tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
	tcp_server_socket.bind(("",8989))
	tcp_server_socket.listen(128)
	service_client_socket,ip_port = tcp_server_socket.accept()
	print("客户端的ip地址和端口号",ip_port)
	recv_data = service_client_socket.recv(1024)
	send_data = "ok,xxxxx".encode('gbk')
	service_client_socket.send(send_data)
	service_client_socket.close()
	tcp_server_socket.close()
	
# 参数1: 表示当前套接字
# 参数2: 设置端口号复用选项
# 参数3: 设置端口号复用选项对应的值
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

###多任务版TCP服务端程序的示例代码:

import socket
import threading

def handle_client_request(service_client_socket,ip_port):
	while True:
		recv_data = service_client_socket.recv(1024)
		if recv_data:
			print(recv_data.decode("gbk"),ip_port)
			service_client_socket.send("ok，问题真正处理中。。。".encode("gbk"))
		else:
			print("XXXX",ip_port)
			break
	service_client_socket.close()
	


if __name__ =='__main__':
	tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
	tcp_server_socket.bind(("",9090))
	tcp_server_socket.listen(128)
	while True;
		service_client_socket,ip_port = tcp_server_socket.accpet()
		print("客户端连接成功:", ip_port)
		sub_thread = threading.Thread(target= handle_client_request,args=(service_client_socket,ip_port))
		sub_thread.setDaemon(True)
		sub_thread.start()


- HTTP协议是一个超文本传输协议
- HTTP协议是一个基于TCP传输协议传输数据的
- HTTP协议规定了浏览器和 Web 服务器通信数据的格式

**URL的组成部分:**

1. **协议部分**: https://、http://、ftp://
2. **域名部分**: news.163.com
3. **资源路径部分**: /18/1122/10/E178J2O4000189FH.html
4.   查询参数部分 [可选]

GET POST

200 请求成功
307 重定向
400 请求错误，请求地址或者参数错误
404 请求资源在服务器不存在
500 服务器内部源代码出现错误

#请求行 请求头 空行 
#请求行 请求头 空行 请求体

#响应行 响应头 空行 响应体

搭建Python自带的静态Web服务器：

python -m http.server xxxx (default:8000)

###静态Web服务器-返回固定页面数据的示例代码
import socket

if __name__ == "__main__":
	tcp_server_socket = socket.socket (socket.AF_INET , socket.SOCK_STREAM)
	tcp_server_socket.setsocket(socket.SOL_SOCKET.SO_REUSEADDR,True)
	tcp_server_socket.bind(("",9000))
	tcp_server_socket.listen(128)
	while True:
		new_socket,ip_port = tcp_server_socket.accept()
		recv_client_data = new_socket.recv(4096)
		recv_client_content = recv_client_data.decode("utf-8")
		print(recv_client_content)
		
		with open("static/index.html","rb") as file:
			file_data = file.read()
			
		response_line = "HTTP/1.1 200 OK\r\n"
		response_header = "Server : PWS1.0\r\n"
		
		response_body = file_data
		
		response_data = (response_line + response_header + "\r\n").encode("utf-8") +response_body
		new_socket.send(response_data)
		
		new_socket.close()



##eg:返回指定页面、多任务版、面对对象开发、命令行启动动态绑定端口号，的 web服务器
import socket
import threading
import sys


class HttpWebServer(object):
	def __init__(self,port):
		tcp_server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		tcp_server_socket = setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
		tcp_server_socket.bind(("",port))
		tcp_server_socket.listen(128)
		self.tcp_server_socket = tcp_server_socket
	
	@staticmethod
	def handle_client_request(new_socket):
		recv_client_data = new_socket.recv(4096)
		if len(recv_client_data) == 0:
			print("DOWN!!!")
			new_socket.close()
			return
		
		recv_client_content=recv_client_data.decode("utf-8")
		print(recv_client_content)
		request_list = recv_client_content.Split(" ",maxsplit=2)
		
		request_path=request_list[1]
		print(request_path)
		
		if request_path == "/":
              request_path="/index.html"
        try:
              with open("static" + request_path ,"rb") as file:
              file_data = file.read()
         except Exception as e:
              response_line = "HTTP/1.1 404 Not Found\r\n"
              response_header = "Server :PWS1.0\r\n"
			  with open("static/error.html","rb") as file:
              	file_data = file.read()
              response_body =file_data
              response_data= (response_line + response_header + "\r\n").encode("utf-8") + response_body
              new_socket.send(response_data)
       finally:
       		new_socket .close()
       		
              
     
	
	
	def start(self):
		while True:
			new_socket,ip_port = self.tcp_server_socket.accept()
			sub_thread = threading.Thread(target=self.handle_client_request,args=(new_socket,))
			sub_thread.setDaemon(True)
			sub_thread.start()
			
def main():
	prit(sys.argv)
	if len(sys.argv)!=2:
		print("执行命令如下: python3 xxx.py 8000")
		return
		
	if not sys.argv[1].isdigit():
		print("执行命令如下: python3 xxx.py 8000")
		return
	port = int(sys.argv[1])
	web_sever = HttpWebServer(port)
	web_server.start()
	
if __name__ == '__main__':
	main()
	


####闭包#####
用外部函数变量的内部函数称为闭

def  func_out(num1):
	def func_inner(num2):
		result = num1 + num2
		print("结果是："，result)
	return func_inner

f = fun_out(1)
f(2)
闭包可以对外部函数的变量进行保存
闭包还可以提高代码的可重用性，不需要再手动定义额外的功能函数。

修改闭包内使用的外部函数变量使用 nonlocal 关键字来完成。

nonlocal xxx1
xxx1 = xxxx

####  装饰器的定义

就是**给已有函数增加额外功能的函数，它本质上就是一个闭包函数**。

**装饰器的功能特点:**

1. 不修改已有函数的源代码
2. 不修改已有函数的调用方式
3. 给已有函数增加额外的功能

def decorator(fn):
	def inner():
		'''执行函数之前'''
		fn()
		'''执行函数之后'''
	return inner
	
@XXX ==>  func = XXX(func)


import time 

def get_time(func):
	def inner():
		begin = time.time()
		func()
		end = time.time()
		print("函数执行花费%f" % (end-begin))
	return inner

@get_time
def func1():
	xxxxxx

finc1()

#通用装饰器
def logging(fn):
	def inner(*args,**kwargs):
		print("--正在计算————")
		result = fn(*args,**kwargs)
		return result
	
	return inner
	
多个装饰器的装饰过程是: 离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰，由内到外的装饰过程  -$$#由内到外
# 装饰过程: 1 content = make_p(content) 2 content = make_div(content)
# content = make_div(make_p(content))
@make_div
@make_p
def content():

		
###  类装饰器的介绍

装饰器还有一种特殊的用法就是类装饰器，就是通过定义一个类来装饰函数

#eg:
class Check(object):
	def __init__(self,fn):
		self.__fn = fn
		
	def __call__(self,*args,**kwargs):
		print("xxxx")
		self.__fn()
		
@Check
def comment():
	print("xxxx")
	
comment()

@Check 等价于 comment = Check(comment),

web服务器主要是接收用户的http请求,根据用户的请求返回不同的资源数据
web框架专门负责处理用户的动态资源请求，这个web框架其实就是一个为web服务器提供服务的应用程序**，简称web框架。

WSGI协议规定web服务器把动态资源的请求信息传给web框架处理，web框架把处理好的结果返回给web服务器。

###mini-Web框架 （自己写一个简单系统）

个人编写一个：web框架+web服务器 +mysql+ajax渲染+logging日志的网页系统


系统内部流程分析：
web浏览器——》web服务器-->web框架———》模板--》mysql———》web框架汇总--》
web服务器———》发web浏览器

要是静态网页直接 浏览器———》服务器--》拿资源--》服务器发给浏览器

框架就是用来处理资源
第一步
搭建好服务器（socket+多线程）

设计：

	导包xxx
	面对对象写一class
	写socket监听
	处理发送（这里是web框架）
	写启动（多线程启动）
	定义主函数（可使用终端命令行的方式启动）
	运行

              python中装饰器是随着程序的加载运行而自动加载的，跟调不调用方法没有关系.所以只要是装饰器内部函数以外的部分都会自动加载执行，不用调用。注释的分类
              
代码编写：
 服务器代码：
 
import socket
import os
import threading
import sys
import framework

class HttpWebServer(object):
	def __init__(self,port):
		tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
		tcp_server_socket.bind(("",port))
		tcp_server_socket.listen(128)
		self.tcp_server_socket = tcp_server_socket
		
	@staticmethod
	def handle_client_request(new_socket):
		recv_data = new_socket.recv(4096)
		if len(recv_data) == 0:
			new_socket.close()
			return
		recv_content = recv_data.decode("utf-8")
		
		request_list = recv_content.split(" ", maxsplit=2)
        
        request_path = request_list[1]
        
        if request_path == "/":
        	request_path = "/index.html"
        
        if request_path.endswith(".html"):
        	'''web框架'''
        	env = {
        		"request_path":request_path,
        		
        	}
            
            status ,header,response_body = framework.handle_request(env)
            print(staus.headers,response_body)
            response_line = "HTTP/1.1 %s\r\n"%status
            response_header = ""
            for header in headers:
            	response_header +="%s: %s\r\n" % header
            
            	response_data = (reaponse_line +
            		response_header +
            		"\r\n" +
            		response_body).encode("utf-8")
            	
            	new_socket.send(response_data）
            	
            	new_socket.close()
         else:
         	try:
         		with open("static","rb") as file:
         			file_data = file.read()
         	except Exception as e:
         		response_line = "HTTP/1.1 404 Not Found\r\n"
         		response_header = "Server : PWS/1.0\r\n"
         		with open("statc","rb") as file:
         			file_data = file.read()
         		response_body = file_data
         		response_data = (reaponse_line +
            		response_header +
            		"\r\n" ).encode("utf-8") + response_body
            	
            	new_socket.send(response)
            else:
            	response_line = "HTTP/1.1 404 Not Found\r\n"
         		response_header = "Server : PWS/1.0\r\n"
            	response_body = file_data
         		response_data = (reaponse_line +
            		response_header +
            		"\r\n" ).encode("utf-8") + response_body
            	
            	new_socket.send(response)
            finally:
            	new_socket.close()
    
    def start(self):
    	while True:
    		new_socket,ip_port = self.tcp_server_socket.accept()
    		sub_thread = threading.Thread(target=self.handle_client_request,args=(new_socket,))
    		sub_thread.setDaemon(True)
    		sub_thread.start(),
    
    def main():
    	web_server = HttpWebServer(8000)
    	web_server.start()
    	
    
    if __name__ == '__main':
    	main()
    	
    	
####Web框架
import time
import pymysql
import json

route_list = [       ]

def route(path):
	def decorator(func):
		route_list.append((path,func))
		
		def inner():
			
			result = func()
			return result
		
		return inner
    return decorator
    
@route("/index.html")
def index():
	status = "200 ok"
	response_header = [("server","PWS/1.1")]
	with open("static","rb") as file:
		file_data = file.read()
	
	conn = pymysql.connect(host="localhost",
							port=3306,
							user="root",
							password = "XXXXXX",
							database="XXXXX",
							charset="utf8"
							)
	
	cursor = conn.cusor()
    sql = "select * form info ;"
    cursor.excute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    
    data = ""
    for row in result:
    	data +='''
    	
    	        xxx
    	        xxx
    	        xxx
    	'''%row
    response_body = file_data.replace("{% xxxx%}") , data)
    
    return status ,response_header , response_body
    
@route("/center_data.html")
def center_data():
	
	
	conn = pymysql.connect(host="localhost",
							port=3306,
							user="root",
							password = "XXXXXX",
							database="XXXXX",
							charset="utf8"
							)
    cursor = conn.cursor()
    sql = '''select i.code , i.short,i.cha,i.turnover,i.price,i.highs, f.note_info
    form info as i  inner join focus as f
     on i.id = f.info_id'''
    cursor.execute(sql)
  	result = cursor.fetchall()
    center_data_list = [{
        "code" : row[0],
        "short": row[1],
        "chg":row[2],
        "turnover":row[3],
        "price":str(row[4]),
        "highs":str(row[5]),
        "note_info": row[6]
    } for row in result ]
     
	json_str = json.dupms(center_data_list,ensure_ascii = False)             
    '''
    json.dumps()函数是将字典转化为字符串
    json.loads()函数是将字符串转化为字典
    json.dump()用于将dict类型的数据转成str，并写入到json文件中。
    json.dump(name_emb,open(emb_filename,"w"))
    res=json.load(file) file为文件路径
    '''          
    cursor.close()         
	conn.close()  
    status = "200 OK"          
  	response_header= [
        ("Server","PWS/1.1"),
        ("Content-Type","text/html;charset=utf-8")
        
    ]
    return status ,response_header,json_str
              
  @route("/center.html")
  def center():
      status = "200 OK"
      response_header =  [("Server","PWS/1.1")]
      with open("static","r",encoding='utf-8') as file:
              file_data = file.read()
      response_body = file_data.replace("{%content%}","")
      return status , response_header ,response_body
       
  def not_found():
              status = "404 Not Found"
			 response_header = [("Server","PWS/1.1")]
              data = "not found"
              return status,response_header,data
              
  def handle_request(env):
              request_path = env["request_path"]
              print("动态资源请求的地址："，request_path)
              print(route_list)
              
              for path , func in route_list:
              	if request_path == path：
              		result = func()
              		return result
              else:
              	result = not_found()
              	return result
              
   if __name__ == '__main__':
         center_data()
  
       
  
      #############logging 日志
              
       1-->5
       DEBUG
   	   INFO
       WARNING
       ERROR
       CRITICAL
       
              
  import logging
              
    logging.debug('这是一个debug级别的日志信息')
    logging.info('这是一个info级别的日志信息')
    logging.warning('这是一个warning级别的日志信息')
    logging.error('这是一个error级别的日志信息')
    logging.critical('这是一个critical级别的日志信息')

  
       
  import logging
              
  logging.basicConfig(level = logging.DEBUG,
                     format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s : %(message)s')
              
     logging.debug('这是一个debug级别的日志信息')
    logging.info('这是一个info级别的日志信息')
    logging.warning('这是一个warning级别的日志信息')
    logging.error('这是一个error级别的日志信息')
    logging.critical('这是一个critical级别的日志信息')             

level 表示设置的日志等级
format 表示日志的输出格式, 参数说明:
%(levelname)s: 打印日志级别名称
%(filename)s: 打印当前执行程序名
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(message)s: 打印日志信息
  
       
项目中使用：
              
              
   import logging
              
   logging.basicConfig(level= logging.DEBUG,
                      format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s",
                       filename ="log.txt"
                       filemode="w"
                      )
              
  INFO级别的日志输出，示例代码:       
   if request_path.endswith(".html"):
     """这里是动态资源请求，把请求信息交给框架处理"""
     logging.info("动态资源请求:" + request_path)
     ...
 else:
     """这里是静态资源请求"""
     logging.info("静态资源请求:" + request_path)
     ...  
       
 WARNING级别的日志输出，示例代码:

 if len(sys.argv) != 2:
     print("执行命令如下: python3 xxx.py 9000")
     logging.warning("用户在命令行启动程序参数个数不正确!")
     return
              
 if not sys.argv[1].isdigit():
     print("执行命令如下: python3 xxx.py 9000")
     logging.warning("用户在命令行启动程序参数不是数字字符串!")
     return  
              
              
 ERROR级别的日志输出，示例代码:
 def handle_request(env):
     
     request_path = env["request_path"]
     print("接收到的动态资源请求:", request_path)

     for path, func in route_list:
         if request_path == path:
             result = func()
             return result
     else:
         logging.error("没有设置相应的路由:" + request_path)
        
         result = not_found()
         return result       
              
              
              
  ####正则表达式
              
  在业务处理时经常需要在数据的读取和存入前对数据进行预处理，通过@property和@*.setter两个装饰器就可以方便的实现。

 

#@property

　　python中的@property装饰器可以总结为两个作用：

让函数可以像普通变量一样使用
对要读取的数据进行预处理
              
# @*.setter

　　python中的@*.setter装饰器可以总结为两个作用：

对要存入的数据进行预处理
设置可读属性(不可修改)
　　注意：@*.setter装饰器必须在@property装饰器的后面，且两个被修饰的函数的名称必须保持一致，* 即为函数名称。             
              
 
property	英[ˈprɒpəti]
美[ˈprɑːpərti]
n.	所有物; 财产; 财物; 不动产; 房地产; 房屋及院落; 庄园; 性质;
              
定义property属性有两种方式:
装饰器方式
类属性方式
              
装饰器方式:
@property 修饰获取值的方法
@方法名.setter 修饰设置值的方法
              
类属性方式:
类属性 = property(获取值方法, 设置值方法)
              
 @property
 def get_age():
              xxxxx
 @age.setter
  def set_age():
				xxxx
           
    2\
              age = property(get_age,set_age)
              
              
              
      with(oprn('1.txt','w'))as f:
              f.write("xxx")
              
              
       __enter__
       __exit__
       
              
       根据程序员制定的规则循环生成数据，当条件不成立时则生成数据结束。数据不是一次性全部生成处理，而是使用一个，再生成一个，可以节约大量的内存       
     yield 关键字:

只要在def函数里面看到有 yield 关键字那么就是生成器  
              
              
 浅拷贝使用copy.copy函数
深拷贝使用copy.deepcopy函数             
              
  # 正则表达式是匹配符合某些规则的字符串数据           
              
              
   import re
   
 	result = re.match(正则表达式，str)
    
  	result.group()
   
              #eg:
              import re
              
              result = re.match("itcast","itcast.cn")
              
              info = result.group()
              print(info)
              
              
              
              
              
代码	功能
.	匹配任意1个字符（除了\n）
[ ]	匹配[ ]中列举的字符
\d	匹配数字，即0-9
\D	匹配非数字，即不是数字
\s	匹配空白，即 空格，tab键
\S	匹配非空白
\w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
\W	匹配特殊字符，即非字母、非数字、非汉字
              
  *	匹配前一个字符出现0次或者无限次，即可有可无
+	匹配前一个字符出现1次或者无限次，即至少有1次
?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	匹配前一个字符出现m次
{m,n}	匹配前一个字符出现从m到n次            
              
^	匹配字符串开头
$	匹配字符串结尾              
              
              
  |	匹配左右任意一个表达式
(ab)	将括号中字符作为一个分组
\num	引用分组num匹配到的字符串
(?P<name>)	分组起别名
(?P=name)	引用别名为name分组匹配到的字符串            
              
              
 #需求：匹配出163、126、qq等邮箱             
   import re
   
              match_obj = re.match("[a-zA-Z0-9_]{4,9}@(163|126|qq|sina|yahoo)\.com","hello@163.com")
              if match_obj:
              	print(match_obj.group())
              	print(match_obj.group(1))
             else:
              	print("匹配失败")
             
              
              
              
              
              
              
              
              
              
              
              
              
       





```

# 二. 公共方法

| 函数                    | 描述                                                         |
| ----------------------- | ------------------------------------------------------------ |
| len()                   | 计算容器中元素个数                                           |
| del 或 del()            | 删除                                                         |
| max()                   | 返回容器中元素最大值                                         |
| min()                   | 返回容器中元素最小值                                         |
| range(start, end, step) | 生成从start到end的数字，步长为 step，供for循环使用           |
| enumerate()             | 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。 |

## 

# 

- 文件操作步骤

  - 打开

  ``` python
  文件对象 = open(目标文件, 访问模式)
  ```

  - 操作

    - 读

    ``` python
    文件对象.read()
    文件对象.readlines()
    文件对象.readline()
    ```

    - 写

    ``` python
    文件对象.write()
    ```

    - seek()

  - 关闭

  ``` python
  文件对象.close()
  ```


- 主访问模式
  - w：写，文件不存在则新建该文件
  - r：读，文件不存在则报错
  - a：追加

- 文件和文件夹操作
  - 重命名：os.rename()
  - 获取当前目录：os.getcwd()
  - 获取目录列表：os.listdir()

# 

- `__init__()`: 初始化
- `__str__()`:输出对象信息
- `__del__()`:删除对象时调用

- 继承的特点

  - 子类默认拥有父类的所有属性和方法
  - 子类重写父类同名方法和属性
  - 子类调用父类同名方法和属性

- super()方法快速调用父类方法

- 私有权限

  - 不能继承给子类的属性和方法需要添加私有权限
  - 语法

  ``` python
  class 类名():
    # 私有属性
    __属性名 = 值
  
    # 私有方法
    def __函数名(self):
      代码
  ```

  - import 模块名
  - from 模块名 import 功能名
  - from 模块名 import *
  - import 模块名 as 别名
  - from 模块名 import 功能名 as 别名


### 1. 进程和线程的对比的三个方向

1. 关系对比
2. 区别对比
3. 优缺点对比

### 2. 关系对比

1. 线程是依附在进程里面的，没有进程就没有线程。
2. 一个进程默认提供一条线程，进程可以创建多个线程。
### 2. 区别对比

1. 进程之间不共享全局变量
2. 线程之间共享全局变量，但是要注意资源竞争的问题，解决办法: 互斥锁或者线程同步
3. 创建进程的资源开销要比创建线程的资源开销要大
4. 进程是操作系统资源分配的基本单位，线程是CPU调度的基本单位
5. 线程不能够独立执行，必须依存在进程中
6. 多进程开发比单进程多线程开发稳定性要强

### 3. 优缺点对比

- 进程优缺点:
  - 优点：可以用多核
  - 缺点：资源开销大
- 线程优缺点:
  - 优点：资源开销小
  - 缺点：不能使用多核

### 4. 小结

- 进程和线程都是完成多任务的一种方式
- 多进程要比多线程消耗的资源多，但是多进程开发比单进程多线程开发稳定性要强，某个进程挂掉不会影响其它进程。
- 多进程可以使用cpu的多核运行，多线程可以共享全局变量。
- 线程不能单独执行必须依附在进程里面







**python中装饰器是随着程序的加载运行而自动加载的，跟调不调用方法没有关系.所以只要是装饰器内部函数以外的部分都会自动加载执行，不用调用。**

- DEBUG：程序调试bug时使用
- INFO：程序正常运行时使用
- WARNING：程序未按预期运行时使用，但并不是错误，如:用户登录密码错误
- ERROR：程序出错误时使用，如:IO操作失败
- CRITICAL：特别严重的问题，导致程序不能再继续运行时使用，如:磁盘空间为空，一般很少使用
- 默认的是WARNING等级，当在WARNING或WARNING之上等级的才记录日志信息。
- 日志等级从低到高的顺序是: DEBUG < INFO < WARNING < ERROR < CRITICAL

- 浅拷贝使用copy.copy函数
- 深拷贝使用copy.deepcopy函数
- 不管是给对象进行深拷贝还是浅拷贝，只要拷贝成功就会开辟新的内存空间存储拷贝的对象。
- 浅拷贝和深拷贝的区别是:
  - 浅拷贝最多拷贝对象的一层，深拷贝可能拷贝对象的多层。
