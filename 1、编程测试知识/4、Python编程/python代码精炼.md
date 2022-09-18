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
