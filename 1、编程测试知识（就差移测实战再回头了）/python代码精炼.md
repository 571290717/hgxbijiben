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
#切片  序列【开始位置下标：结束位置下标：步长】
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

## 

    






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
