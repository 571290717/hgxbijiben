# Day43 移动端测试详解（3）——ADB常用命令

[TOC]

![image-20230915151707116](images/image-20230915151707116.png)





# 学习目标

- 掌握常用的ADB命令

# 1. ADB命令简介

```
ADB全名Andorid Debug Bridge。 是一个Debug工具。为何称之为Bridge呢? 
因为adb是一个标准的C/S结构的工具, 是要连接开发电脑和调试手机的

包含如下几个部分:
    1.Client端，运行在开发机器中，即你的开发PC机。用来发送adb命令。
    2.Daemon守护进程, 运行在调试设备中, 即的调试手机或模拟器。
    3.Server端, 作为一个后台进程运行在开发机器中, 即你的开发PC机. 用来管理PC中的Client端和手机的Daemon之间的通信。
```

# 2. 常用命令

- adb 帮助

```
adb --help
```

- 启动adb 服务

```
adb start-server
```

- 关闭adb 服务

```
adb kill-server
```

- 获取设备号

```
adb devices
```

- 获取系统版本

```
adb shell getprop ro.build.version.release
```

- 发送文件到手机

```
adb push 电脑端⽂件路径/需要发送的文件,手机端存储的路径

adb push C:\Users\win\Desktop\xx.png /sdcard
```

- 从手机拉取文件

```
adb pull 手机端的路径/拉取文件名 电脑端存储文件路径

adb pull /sdcard/xx.png C:\Users\win\Desktop
```

- 查看手机运行日志

```
adb logcat
```

- 进入到手机终端

```
adb shell
```

- 获取app启动包名和启动名(⚠手机需要先打开对应app)

```
1.Mac/Linux: 'adb shell dumpsys window windows | grep mFocusedApp’
2.在 Windows 终端运⾏ 'adb shell dumpsys window windows | findstr mFocusedApp’
```

- 安装app到手机

```
adb install 路径/xxx.apk
```

- 卸载手机app

```
adb uninstall app
```

- 获取app启动时间

```
adb shell am start -W 包名/.启动名
```



# 3. 主流移动端自动化测试工具



![常用工具](D:/hgx笔记/hgxbijiben/1、编程测试知识（背基础知识）/8、移动测试/appium_jenkins_allure_pytest/day1/img/choice_appium_cause.png)

- Robotium

```
1.支持语言：Java
2.仅支持Android系统
3.不支持跨应用
```

- Macaca

```
1.支持语言：Java，Python，Node.js
2.支持Android和IOS系统
3.支持跨应用
```

- Appium

```
1.支持语言：Java，C#，Python，php，perl，ruby，Node.js
2.支持Android和iOS系统
3.支持跨应用
4.不依赖源码
```

- 自动化工具选择关注点

```
1.是否支持native，webview
2.是否支持获取toast
3.是否支持跨应用
```

![9c7bc198b36f77679bc7983f2f02810](https://the-toast.oss-cn-shenzhen.aliyuncs.com/csdn/blog9c7bc198b36f77679bc7983f2f02810%20(1)-169476214409811.jpg)
