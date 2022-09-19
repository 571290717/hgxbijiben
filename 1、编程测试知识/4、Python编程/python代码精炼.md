```python
print()

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
	'''request_path = "/index.html"

        try:
            # 动态打开指定文件
            with open("static" + request_path, "rb") as file:
                # 读取文件数据
                file_data = file.read()
        except Exception as e:
            # 请求资源不存在，返回404数据
            # 响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Server: PWS1.0\r\n"
            with open("static/error.html", "rb") as file:
                file_data = file.read()
            # 响应体
            response_body = file_data

            # 拼接响应报文
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            # 发送数据
            new_socket.send(response_data)
        else:
            # 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Server: PWS1.0\r\n"

            # 响应体
            response_body = file_data

            # 拼接响应报文
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            # 发送数据
            new_socket.send(response_data)
        finally:
            # 关闭服务与客户端的套接字
            new_socket.close()
'''
	

	
	
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










