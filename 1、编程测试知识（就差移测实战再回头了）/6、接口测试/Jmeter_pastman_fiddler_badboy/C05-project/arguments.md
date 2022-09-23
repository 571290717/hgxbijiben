# 测试用例中测试数据-参数化

------

## 目标

- 给测试用例设计测试数据

------

## 测试数据分类

- 正向：(根据测试用例覆盖面设计正向测试数据)
- 逆向: (根据测试用例覆盖面设计逆向测试数据)

### 正向方法：

```
1. 传入所有可传属性，且格式正确
2. 传入必填属性，且格式正确
```

### 校验方法：

```
1) 为空校验
2) 为空格校验
3) 前后含空格校验
4) 超长校验
5) 类型校验
6) 含特殊字符校验
7) 删除引用校验
8) 唯一不重复属性校验
```

------

## 参数化示例：

### 学院-组合查询参数化示例：

```
Here is Slogan,Test-Master,Test学院,----正向数据
,Test-Master,Test学院,----两个条件组合
,,Test学院,----单个条件
Here is Slogan,,,----正向数据
,Test-Master,,----正向数据
 Here is Slogan ,Test-Master,Test学院,----Here is Slogan前后含空格
Here is Slogan, Test-Master ,Test学院,----Test-Master前后含空格
Here is Slogan,Test-Master, Test学院 ,----Test学院前后含空格
 ,Test-Master,Test学院,----为空格
Here is Slogan, ,Test学院,----为空格
Here is Slogan,Test-Master, ,----为空格
Here is Slogan222,Test-Master,Test学院,----一个条件不存在
Here is Slogan,Test-Master22222222222222222222222222222,Test学院,----超长
Here is Slogan,Test-Master,Test%%%%%%%%%%%%%院,----含特殊字符
,,,----全部为空
```

### 学院-list删除参数化示例：

```
T07,T08,---正确数据
,T08,---一个为空
T07,,---一个为空
T07,T0888,---一个为正常，一个为不存在
 ,T08,---一个为空格
T07, ,---一个为空格
 T07 , T08 ,---前后含空格 
T07%,T08,---一个为格式不正确
T07,T0888888888888888,---一个为超长

`
```

### 学院新增参数化示例：

```
T09,Test学院,Test-Master,Here is Slogan,-----正向数据
---ID存在校验
T09,Test学院,Test-Master,Here is Slogan,-----ID已存在
---为空校验
,Test学院,Test-Master,Here is Slogan,-----depid为空
T09,,Test-Master,Here is Slogan,-----depname为空
T09,Test学院,,Here is Slogan,-----mastername为空
T09,Test学院,Test-Master,,-----slogan为空
---为空格校验
 ,Test学院,Test-Master,Here is Slogan,-----depid为空格
T09, ,Test-Master,Here is Slogan,-----depname为空格
T09,Test学院, ,Here is Slogan,-----mastername为空格
T09,Test学院,Test-Master, ,-----slogan为空格
---含前后空格
 T09 ,Test学院,Test-Master,Here is Slogan,-----depid含前后空格
T09, Test学院 ,Test-Master,Here is Slogan,-----depname含前后空格
T09,Test学院, Test-Master ,Here is Slogan,-----mastername含前后空格
T09,Test学院,Test-Master, Here is Slogan ,-----slogan含前后空格
---含前后#
#T09#,Test学院,Test-Master,Here#is#Slogan,-----depid含前后#
T09,#Test学院#,Test-Master,Here#is#Slogan,-----depname含前后#
T09,Test学院,#Test-Master#,Here#is#Slogan,-----mastername含前后#
T09,Test学院,Test-Master,#Here#is#Slogan#,-----slogan含前后#
---含前后@
@T09@,Test学院,Test-Master,Here@is@Slogan,-----depid含前后@
T09,@Test学院@,Test-Master,Here@is@Slogan,-----depname含前后@
T09,Test学院,@Test-Master@,Here@is@Slogan,-----mastername含前后@
T09,Test学院,Test-Master,@Here@is@Slogan@,-----slogan含前后@
---含前后%
%T09%,Test学院,Test-Master,Here%is%Slogan,-----depid含前后%
T09,%Test学院%,Test-Master,Here%is%Slogan,-----depname含前后%
T09,Test学院,%Test-Master%,Here%is%Slogan,-----mastername含前后%
T09,Test学院,Test-Master,%Here%is%Slogan%,-----slogan含前后%
---超长校验
T091111111111111111111111122222222222222,Test学院,Test-Master,Here%is%Slogan,-----depid含超长
T09,Test学院222222222222222222222,Test-Master,HereisSlogan,-----depname含超长
T09,Test学院,%Test-Master1111111111111111111111,HereisSlogan,-----mastername超长
T09,Test学院,Test-Master,HereisSlogan11111111111111111111,-----slogan超长
```