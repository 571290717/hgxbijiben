# Git——C站最详细的Git教程，一篇学会Git(window\linux通用)



[TOC]



![image-20230519140302851](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/image-20230519140302851.png)



# Git简介



## Git

- Git 是目前世界上最先进的分布式版本控制系统（没有之一）

## 作用

- 源代码管理

## 为什么要进行源代码管理?

- 方便多人协同开发
- 方便版本控制

## Git的诞生

- 作者是 Linux 之父：Linus Benedict Torvalds
- 当初开发 Git 仅仅是为了辅助 Linux 内核的开发（管理源代码）



> git 开发时间表
>
> - git 的产生是 Linux Torvals 在无奈被逼的情况下创造的，我看了一下时间历程：
>   - 2005 年 4 月3 日开始开发 git
>   - 2005 年 4 月 6 日项目发布
>   - 2005 年 4 月 7 日 Git 开始作为自身的版本控制工具
>   - 2005 年 4 月 18 日发生第一个多分支合并
>   - 2005 年 4 月 29 日 Git 的性能达到 Linux 预期
>   - 2005年 7 月 26 日 Linux 功成身退，将 Git 维护权交给 Git 另一个主要贡献者 Junio C Hamano，直到现在
>
> Git 迅速成为最流行的分布式版本控制系统，尤其是 2008 年，GitHub 网站上线了，它为开源项目免费提供 Git 存储，无数开源项目开始迁移至 GitHub，包括 jQuery，PHP，Ruby 等等

## Git管理源代码特点

- 1.`Git`是分布式管理.服务器和客户端都有版本控制能力,都能进行代码的提交、合并、...

  ![](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E5%88%86%E5%B8%83%E5%BC%8F%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6.png)

- 2.`Git`会在根目录下创建一个`.git`隐藏文件夹，作为本地代码仓库

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E6%9C%AC%E5%9C%B0%E4%BB%93%E5%BA%93.png)

## Git操作流程图解

```
Git服务器 --> 本地仓库 --> 客户端 --> 本地仓库 --> Git服务器
```

>git clone xxx
>
>git add . 
>
>git commit -m 'xxx'
>
>git push 





![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/GIT%E6%93%8D%E4%BD%9C%E5%9B%BE%E8%A7%A3.png)



# 工作区暂存区和仓库区



![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E5%B7%A5%E4%BD%9C%E5%8C%BA%E6%9A%82%E5%AD%98%E5%8C%BA%E5%92%8C%E4%BB%93%E5%BA%93%E5%8C%BA-16844667931571.png)

#### 工作区

- 对于`添加`、`修改`、`删除`文件的操作，都发生在工作区中

#### 暂存区

- 暂存区指将工作区中的操作完成小阶段的存储，是版本库的一部分

#### 仓库区

- 仓库区表示个人开发的一个小阶段的完成
  - 仓库区中记录的各版本是可以查看并回退的
  - 但是在暂存区的版本一旦提交就再也没有了



# Git单人本地仓库操作

- 课程目标：学习常用的Git终端命令
- 提示：本地仓库是个`.git`隐藏文件

> 以下为演示Git单人本地仓库操作

## **1.安装git**

> linux上

```

  sudo apt-get install git
  密码：chuanzhi
```

![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E5%AE%89%E8%A3%85Git-16844669628062.png)



> ​	 windows

可以到 GitHub 的页面上下载 exe 安装文件并运行：

安装包下载地址：https://gitforwindows.org/

官网慢，可以用国内的镜像：https://npm.taobao.org/mirrors/git-for-windows/。



## **2.查看git安装结果**

```
  git
```

## **3.创建项目**

- 在桌面创建`test`文件夹，表示是工作项目

  ```
    Desktop/test/
  ```

> windows

![image-20230519113331535](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/image-20230519113331535.png)

## **4.创建本地仓库**

1. 进入到`test`，并创建本地仓库`.git`

2. 新创建的本地仓库`.git`是个空仓库

   ```
     cd Desktop/test/
     git init
   ```

   ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E5%88%9B%E5%BB%BA%E6%9C%AC%E5%9C%B0%E4%BB%93%E5%BA%93-16844672443655.png)

3. 创建本地仓库`.git`后

   ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E7%A9%BA%E4%BB%93%E5%BA%93-16844672496926.png)

> 进入该待显示的文件路径，ctrl + h ，则显示隐藏文件

## **5.配置个人信息**

```
  git config user.name '张三'
  git config user.email 'zhangsan@163.com'
```

![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E9%85%8D%E7%BD%AE%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF-16844672592717.png)

- 配置个人信息后

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E9%85%8D%E7%BD%AE%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF%E5%90%8E-16844672677588.png)

> 默认不配置的话，会使用全局配置里面的用户名和邮箱
> 全局git配置文件路径：~/.gitconfig

## **6.新建py文件**

- 在项目文件`test`里面创建`login.py`文件，用于版本控制演示

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E9%A1%B9%E7%9B%AE%E6%96%87%E4%BB%B6%E8%AF%A6%E6%83%85-16844672825239.png)

## **7.查看文件状态**

- 红色表示新建文件或者新修改的文件,都在工作区.

- 绿色表示文件在暂存区

- 新建的`login.py`文件在工作区，需要添加到暂存区并提交到仓库区

  ```
  git status
  ```

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E6%9F%A5%E7%9C%8B%E6%96%87%E4%BB%B6%E7%8A%B6%E6%80%81-168446729131510.png)

## **8.将工作区文件添加到暂存区**

```
  # 添加项目中所有文件
  git add .
  或者
  # 添加指定文件
  git add login.py
```

![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E6%B7%BB%E5%8A%A0%E5%88%B0%E6%9A%82%E5%AD%98%E5%8C%BA-168446730137111.png)

**9.将暂存区文件提交到仓库区**

- `commit`会生成一条版本记录

- `-m`后面是版本描述信息

  ```
  git commit -m '版本描述'
  ```

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E6%8F%90%E4%BA%A4%E5%88%B0%E4%BB%93%E5%BA%93%E5%8C%BA-168446730896512.png)

## **10.接下来就可以在**`login.py`**文件中编辑代码**

- 代码编辑完成后即可进行`add`和`commit`操作

- 提示：添加和提交合并命令

  ```
    git commit -am "版本描述"
  ```

- 提交两次代码，会有两个版本记录

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E4%B8%A4%E6%AC%A1%E7%89%88%E6%9C%AC%E6%8F%90%E4%BA%A4-168446731720913.png)

> 一般到这里就可以愉快的
>
> git push 推送到远程仓库了
>
> 后面的操作是为了方便修改错了，来回退版本的（push之后也可以回退，可以去服务器上找版本号来回退）





## **11.查看历史版本**

```
  git log
  或者
  git reflog
```

![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E6%9F%A5%E7%9C%8B%E5%8E%86%E5%8F%B2%E8%AE%B0%E5%BD%95log-168446732409214.png)

> git reflog 可以查看所有分支的所有操作记录（包括commit和reset的操作），包括已经被删除的commit记录，git log 则不能察看已经删除了的commit记录

## **12.回退版本**

- **方案一：**

  - `HEAD`表示当前最新版本

  - `HEAD^`表示当前最新版本的前一个版本

  - `HEAD^^`表示当前最新版本的前两个版本，**以此类推...**

  - `HEAD~1`表示当前最新版本的前一个版本

  - `HEAD~10`表示当前最新版本的前10个版本，**以此类推...**

    ```
    git reset --hard HEAD^
    ```

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E5%9B%9E%E9%80%80%E7%89%88%E6%9C%ACHEAD-168446738393319.png)

- **方案二：当版本非常多时可选择的方案**

  - 通过每个版本的版本号回退到指定版本

    ```
      git reset --hard 版本号
    ```

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E5%9B%9E%E9%80%80%E7%89%88%E6%9C%AC%E7%89%88%E6%9C%AC%E5%8F%B7-168446736568018.png)

    

## **13.撤销修改**

- 只能撤销工作区、暂存区的代码,不能撤销仓库区的代码

- 撤销仓库区的代码就相当于回退版本操作

  - 撤销工作区代码

    - 新加代码`num3 = 30`，不`add`到暂存区，保留在工作区

      ```
      git checkout 文件名
      ```

      ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E6%92%A4%E9%94%80%E5%B7%A5%E4%BD%9C%E5%8C%BA%E4%BB%A3%E7%A0%81%E5%89%8D-168446740552620.png)

      ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E6%92%A4%E9%94%80%E5%B7%A5%E4%BD%9C%E5%8C%BA%E4%BB%A3%E7%A0%81%E5%90%8E-168446741063421.png)

  - 撤销暂存区代码

    - 新加代码`num3 = 30`，并`add`到暂存区

      ```
      # 第一步：将暂存区代码撤销到工作区
      git reset HEAD  文件名
      # 第二步：撤销工作区代码
      git checkout 文件名
      ```

      ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/%E6%92%A4%E9%94%80%E6%9A%82%E5%AD%98%E5%8C%BA%E4%BB%A3%E7%A0%81-168446742386822.png)



>学弯路这篇，基本上就会了Git，可以自己去github上注册个人账号了，注册完账号，就可以自己搭建自己个人github主页了
>
>附上作者的github主页链接：https://github.com/571290717

![9c7bc198b36f77679bc7983f2f02810](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E7%9A%84Git%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9AGit.assets/9c7bc198b36f77679bc7983f2f02810.jpg)