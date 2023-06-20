# Day25 实战篇 ——Jmeter实现Java测试实战

[TOC]



![image-20230615160217357](https://the-toast.oss-cn-shenzhen.aliyuncs.com/image-20230615160217357.png)







> 1、性能测试过程中，有时候开发想对JAVA代码进行性能测试，Jmeter是支持对Java请求进行性能测试，但是需要自己开发、打包好要测试的代码，就能在Java请求中对该java方法进行性能测试
> 2、本文举的例子是Java实现通过传入两个参数，将值写入到文件中

> - 开发思路
>   1、使用Eclipse创建Maven 项目，配置Pom文件，引入Jmeter开发Java请求所需的依赖包；
>   2、创建输入参数类，和测试类，然后继承JavaSamplerClient，实现四个主方法；
>   3、对编写好的项目进行编译、打包
>   4、把打包好的函数放到jmeter扩展目录，调用Java请求，对封装的Java方法进行测试；

| JDK环境 | Jmeter依赖包版本 | Maven仓库版本 |
| ------- | ---------------- | ------------- |
| 1.8     | 4.0              | 3.5.3         |

Java_Sample完整项目下载方法见文章末尾介绍

## 一、新建Maven项目

1. File》New》Project，选择Maven》Maven Project，一直点击Next
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70.png)
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066254.png)
2. 配置Pom文件，Pom文件配置的Jmeter4.0版本，只要保存了Pom文件，系统就会自动下载和关联相应的jar包，Pom配置文件如下：
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066355.png)保存Pom文件之后，系统会自动下载关联的依赖文件，会用到的为ApacheJMeter_core-4.0.jar和ApacheJMeter_java-4.0.jar如下图：
   保存前：
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/20190827121432189.png)
   保存后：
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066356.png)
3. 此时，由于对pom文件进行了修改，项目顶层会出现一把×，并且编译可能就会报错，需要执行Maven》Update Project更新外部依赖的Jar包
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066357.png)
   更新前：
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066358.png)
   更新后，编译、打包正常：
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066359.png)

## 二、编写输入参数类、测试类

1. 输入参数类，该类就是被测试的java方法，主要是实现将参数写入到文件，代码如下：
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066460.png)
2. 测试类，首先在com.xiet.Java_Sample包下创建一个类，类名为Jmeter_Test，需要继承JavaSamplerClient类，然后实现父类的四个方法，和一个main方法
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066461.png)

> main主方法主要是用来本地调试，用来测试封装的Java方法是否功能正常，如果能实现正常功能，就可以进行编译、打包在Jmeter中进行调用

![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/20190827121552164.png)

> setupTest方法为初始化方法，实际运行时每个线程仅执行一次，在测试方法运行前执行，默认置空即可

![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066462.png)

> runTest方法为测试方法，该方法用来传入输入的参数，然后调用参数类，进行测试

![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/2019082712161585.png)

> teardownTest方法为结束方法，实际运行时每个线程仅执行一次，在测试方法结束后执行，默认置空即可

![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/20190827121626911.png)

3.getDefaultParameters方法为设置传入的参数，可以设置多个，已设置的参数会显示到Jmeter的参数列表中，如下所示：
![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066563.png)



## 三、编译、打包

1. 编写代码完成，就可以进行编译、打包操作了，右键点击项目》Run As》Maven build
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066564.png)
2. 在Goals中输入package，然后点击Apply》Run执行编译，打包操作
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066565.png)
3. 编译打包完成，在target目录会生成一个jar包，如下图所示
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066566.png)
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066567.png)

## 四、验证开发的函数是否正常

1. 首先把Java_Sample_0.1.jar函数放到jmeter的\lib\ext目录
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/20190827121753748.png)
2. 然后启动Jmeter，线程组》添加》Sample》Java请求
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066568.png)
3. 在类名称中选择封装的Java类，为com.xiet.Java_Sample.Jmeter_Test，该类名称为包名+类名
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066669.png)
4. 本次设置2线程，2循环，点击执行按钮，执行结果如下：
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066670.png)
   ![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066671.png)

完整源码如下
![在这里插入图片描述](https://the-toast.oss-cn-shenzhen.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NzA1MTM4,size_16,color_FFFFFF,t_70-168673417066672.png)

***









![9c7bc198b36f77679bc7983f2f02810](https://the-toast.oss-cn-shenzhen.aliyuncs.com/9c7bc198b36f77679bc7983f2f02810.jpg)

































 

