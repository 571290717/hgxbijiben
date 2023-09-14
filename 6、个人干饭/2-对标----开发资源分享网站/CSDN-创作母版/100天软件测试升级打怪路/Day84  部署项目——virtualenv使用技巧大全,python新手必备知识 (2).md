# Day 84  部署项目——virtualenv使用技巧大全,python新手必备知识



## virtualenv使用技巧大全,python新手必备知识



搞Python开发时，总会遇到需要同时运行多个不同软件版本项目的时候。每个项目的依赖需求也不一样，那咋整？这个时候我们就需要用到Virtualenv了。



那么什么是Virtualenv呢？Virtualenv是一个能创建隔绝的独立的Python虚拟环境工具。通过它可以防止各个项目之间因为Python版本不同或第三方库版本不同引起冲突，它能够建立多个相互独立，互不影响的Python工作环境。

Virtualenv的安装很简单，一行命令就能搞定：

```
pip install virtualenv
```



Virtualenv安装好之后，就是给自己的项目创建一个虚拟环境。

```
virtualenv pyweb  #pyweb  为虚拟环境目录名，目录名自定义.
```

当然你也可以使用下面的命令创建指定Python版本的虚拟环境。

```
virtualenv 环境名称 --python=/usr/bin/python3.6    #指定创建一个版本为python3.6的虚拟环境
virtualenv  环境名称 --python='C:\python\python3.8.exe'
```



在哪个目录下创建，就会在该目录下生成一个名为pyweb的文件夹。



至于启动虚拟环境，Windows下和Linux下，略有不同。

**Linux下：**

![1.jpg](https://www.django.cn/media/upimg/1_20180710223628_171.jpg)

我们进入创建的虚拟环境的bin目录下，然后使用如下命令启动

```
source activate
```

启动成功之后就会在命令行前出现一个pyweb

![2.jpg](https://www.django.cn/media/upimg/2_20180710224039_224.jpg)

这就说明虚拟环境启动成功。我们就可以在这个虚拟环境下做自己想要做的事了。



**Windows下：**

进入pyweb目录下的Scripts目录下。

![1.jpg](https://www.django.cn/media/upimg/1_20180710224943_102.jpg)

然后输入：activate 回车，就能启动虚拟环境。

![3.jpg](https://www.django.cn/media/upimg/3_20180710225048_180.jpg)

至于退出虚拟环境，使用如下命令即可！

```
Linux下任意目录
>>>deactivate 

>>>windows cd 进入虚拟环境Scripts目录
>>>deactivate.exe
```



安装virtualenv以后，我们不同的项目只需要安装不同的虚拟环境，在不同的环境下工作，就不再相互影响到。妈妈再也不用担心我们出现各种莫名其妙的坑了。

**温馨提示：**安装virtualenv的时候，一定要留意自己系统默认的Python版本，不同版本安装出来的virtualenv版本可能不一样。

