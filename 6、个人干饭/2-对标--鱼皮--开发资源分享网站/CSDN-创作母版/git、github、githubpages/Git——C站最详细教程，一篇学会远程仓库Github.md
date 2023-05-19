# Git——C站最详细教程，一篇学会远程仓库Github

[TOC]

![image-20230519152501007](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/image-20230519152501007-16844811043522.png)

# 创建远程仓库

> 以下操作为演示在Github网站上创建远程仓库

1.登陆注册Github

2.创建仓库入口

- ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/%E8%BF%9C%E7%A8%8B01.png)

  3.编辑仓库信息

  ![image-20230519145704287](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/image-20230519145704287.png)

  4.仓库创建完成

  ![image-20230519145803323](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/image-20230519145803323.png)

  

  

  5.查看仓库地址

  ![image-20230519145910484](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/image-20230519145910484.png)

  

  

  

  > 作者的远程仓库地址 https://github.com/qruihua/info.git



# 配置SSH

选择SSH操作

![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/%E9%80%89%E6%8B%A9SSH.png)

- 如果某台电脑需要与`Github`上的仓库交互，那么就要把这台电脑的SSH公钥添加到这个`Github`账户上

- 1.配置SSH公钥入口

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/SSH%E9%85%8D%E7%BD%AE%E5%85%A5%E5%8F%A301.png)![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/SSH%E9%85%8D%E7%BD%AE%E5%85%A5%E5%8F%A302.png)

- 2.生成SSH公钥

  ```
    ssh-keygen -t rsa -C "qiruihua@itcast.cn"
  ```

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/SSH%E7%94%9F%E6%88%90%E5%85%AC%E9%92%A5.png)

- 3.配置SSH公钥

- ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/ssh01.png)![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/ssh02-16844808295091.png)

- 补充：删除旧的秘钥

  - 删除`~/.ssh`目录，这里存储了旧的密钥
    rm -r .ssh

> SSH操作报错

![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/ssh%E4%B8%8B%E8%BD%BD%E9%97%AE%E9%A2%98.png)

> **解决方案为**
>
> eval "$(ssh-agent -s)"
>
> ssh-add

![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/ssh%E4%B8%8B%E8%BD%BD%E8%A7%A3%E5%86%B3.png)



> !!!!
>
> Windows下配置git的ssh
>
> https://blog.csdn.net/gregcsdn/article/details/125844019



>
>
>下面就是多人协调办公了，如果你的公司有涉及git协调办公或者感兴趣的话就再往下学~
>
>（个人觉得如果是个人开发者不涉及协同办公就算了，等需要学的时候在回来看就完了!  \但是记得先收藏。。。）

# 克隆项目

- 准备经理的文件 `Desktop/manager/`
- 准备张三的文件 `Desktop/zhangsan/`

**经理的工作**

- 立项：克隆远程仓库+配置身份信息+创建项目+推送项目到远程仓库

- 1.克隆远程仓库的命令

  ```
    cd Desktop/manager/
    git clone https://github.com/qruihua/info.git
  ```

- 2.克隆远程仓库到本地

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E5%85%8B%E9%9A%86%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%9302.png)

- 3.克隆成功后查看经理的文件

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E5%85%8B%E9%9A%86%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93%E6%88%90%E5%8A%9F%E5%90%8E.png)

- 4.配置经理身份信息

  ```
    cd Desktop/manager/info/
    git config user.name '经理'
    git config user.email 'manager@itcast.com'
  ```

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E9%85%8D%E7%BD%AE%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF%E5%90%8E.png)

- 5.创建项目

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E5%88%9B%E5%BB%BA%E9%A1%B9%E7%9B%AE.png)

- 6.推送项目到远程仓库

  ```
    # 工作区添加到暂存区
    git add .
    # 暂存区提交到仓库区
    git commit -m '立项'
    # 推送到远程仓库
    git push
  ```

![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E6%8E%A8%E9%80%81%E9%A1%B9%E7%9B%AE%E5%88%B0%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93%E5%90%8E.png)

- 在 push 的时候需要设置账号与密码，该密码则是 github 的账号与密码

  - 如果在每次 push 都需要设置账号与密码，那么可以设置记住密码

    ```
    设置记住密码（默认15分钟）：
    git config --global credential.helper cache
    如果想自己设置时间，可以这样做(1小时后失效)：
    git config credential.helper 'cache --timeout=3600'
    长期存储密码：
    git config --global credential.helper store
    ```

    > 在以后的项目开发过程中，Pycharm 可以自动记住密码

**张三的工作**

- 获取项目：克隆项目到本地、配置身份信息

- 1.克隆项目到本地

  ```
    cd Desktop/zhangsan/
    git clone https://github.com/qruihua/info.git
  ```

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E5%BC%A0%E4%B8%89%E5%85%8B%E9%9A%86%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%9302.png)

- 2.克隆成功后查看张三的文件

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E5%BC%A0%E4%B8%89%E5%85%8B%E9%9A%86%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93%E5%90%8E.png)

- 3.配置张三身份信息

  ```
    cd Desktop/zhangsan/info/
    git config user.name '张三'
    git config user.email 'zhangsan@itcast.com'
  ```

> 张三身份信息配置成功后即可跟经理协同开发同一个项目





# 多人协同开发

- 1.代码编辑界面介绍：此处使用`gedit`做演示

  - 代码编辑界面左边为模拟经理的操作

  - 代码编辑界面右边为模拟张三的操作

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E4%BB%A3%E7%A0%81%E7%BC%96%E8%BE%91%E7%95%8C%E9%9D%A2%E4%BB%8B%E7%BB%8D.png)

- 2.模拟张三先编辑`login.py`文件代码

  - 进入张三本地仓库：`cd Desktop/zhangsan/info`

  - 编辑代码：`num1 = 10`

  - 本地仓库记录版本：`git commit -am '第一个变量'`

  - 推送到远程仓库：`git push`

    

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E5%BC%A0%E4%B8%89%E7%BC%96%E8%BE%91num1.png)

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E5%BC%A0%E4%B8%89%E7%BC%96%E8%BE%91num1git%E6%93%8D%E4%BD%9C.png)![img](file:///D:/hgx%E7%AC%94%E8%AE%B0/hgxbijiben/3%E3%80%81%E7%BC%96%E7%A8%8B%E5%BC%80%E5%8F%91%E7%9F%A5%E8%AF%86/3-git/images/github%E5%BC%A0%E4%B8%89%E7%BC%96%E8%BE%91num1%E6%8E%A8%E9%80%81%E5%90%8E.png)

- 3.模拟经理后编辑`login.py`文件代码

  - 进入经理本地仓库：`cd Desktop/manager/info/`

  - 经理同步服务器代码：`git pull`

  - 编辑代码：`num2 = 20`

  - 本地仓库记录版本：`git commit -am '第二个变量'`

  - 推送到远程仓库：`git push`

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E5%90%8C%E6%AD%A5num1.png)

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E7%BC%96%E8%BE%91num2.png)

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E7%BC%96%E8%BE%91num2git%E6%93%8D%E4%BD%9C.png)

    ![img](file:///D:/hgx%E7%AC%94%E8%AE%B0/hgxbijiben/3%E3%80%81%E7%BC%96%E7%A8%8B%E5%BC%80%E5%8F%91%E7%9F%A5%E8%AF%86/3-git/images/github%E7%BB%8F%E7%90%86%E7%BC%96%E8%BE%91num2%E6%8E%A8%E9%80%81%E5%90%8E.png)

- 4.模拟张三同步服务器代码

  - 本次可以把`num2`同步到张三的本地仓库

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E5%BC%A0%E4%B8%89%E5%90%8C%E6%AD%A5num2.png)

- 5.按照以上`2-3-4`步骤循环操作，即可实现基本的协同开发

- 6.总结：

  - 要使用git命令操作仓库，需要进入到仓库内部
  - 要同步服务器代码就执行：`git pull`
  - 本地仓库记录版本就执行：`git commit -am '版本描述'`
  - 推送代码到服务器就执行：`git push`
  - 编辑代码前要先`pull`，编辑完再`commit`，最后推送是`push`

# 代码冲突

- **提示**：多人协同开发时，避免不了会出现代码冲突的情况
- **原因**：多人同时修改了同一个文件
- **危害**：会影响正常的开发进度
- **注意**：一旦出现代码冲突，必须先解决再做后续开发

**代码冲突演练**

- 1.张三先编辑`login.py`文件代码

  - 进入张三本地仓库：`cd Desktop/zhangsan/info`

  - 拉取服务器最新代码：`git pull`

  - 编辑代码：`num3 = 30`

  - 本地仓库记录版本：`git commit -am '第三个变量'`

  - 推送到服务器仓库：`git push`

  - 张三本地仓库和远程仓库代码如下：

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E6%9F%A5%E7%9C%8B%E5%BC%A0%E4%B8%89%E6%9C%AC%E5%9C%B0%E4%BB%93%E5%BA%93num3.png)

    ![img](file:///D:/hgx%E7%AC%94%E8%AE%B0/hgxbijiben/3%E3%80%81%E7%BC%96%E7%A8%8B%E5%BC%80%E5%8F%91%E7%9F%A5%E8%AF%86/3-git/images/github%E6%9F%A5%E7%9C%8B%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93num3.png)

- 2.经理后编辑`login.py`文件代码

  - 进入经理本地仓库：`cd Desktop/manager/info/`

  - 编辑代码：`num3 = 300`

  - 本地仓库记录版本：`git commit -am '第三个变量'`

  - 推送到服务器仓库：`git push`

  - **以上操作会出现代码冲突**

    - 提示需要先pull

      ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E5%86%B2%E7%AA%81%E6%8F%90%E7%A4%BA%E9%9C%80%E8%A6%81%E5%85%88pull.png)

    - 提示冲突文件

      ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E5%86%B2%E7%AA%81%E6%8F%90%E7%A4%BA%E5%86%B2%E7%AA%81%E6%96%87%E4%BB%B6.png)

    - 冲突代码表现

      ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E5%86%B2%E7%AA%81%E4%BB%A3%E7%A0%81%E8%A1%A8%E7%8E%B0.png)

- 3.解决冲突

  - 原则：谁冲突谁解决，并且一定要协商解决

  - 方案：保留所有代码 或者 保留某一人代码

  - 解决完冲突代码后，依然需要`add`、`commit`、`push`

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E5%86%B2%E7%AA%81%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88.png)

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E5%86%B2%E7%AA%81%E8%A7%A3%E5%86%B3%E6%8E%A8%E9%80%81.png)

  - 提示：如果张三执行`pull`没有影响，就算真正解决了冲突代码

**补充：**

- **容易冲突的操作方式**
  - 多个人同时操作了同一个文件
  - 一个人一直写不提交
  - 修改之前不更新最新代码
  - 提交之前不更新最新代码
  - 擅自修改同事代码
- **减少冲突的操作方式**
  - 养成良好的操作习惯,先`pull`在修改,修改完立即`commit`和`push`
  - 一定要确保自己正在修改的文件是最新版本的
  - 各自开发各自的模块
  - 如果要修改公共文件,一定要先确认有没有人正在修改
  - 下班前一定要提交代码,上班第一件事拉取最新代码
  - 一定不要擅自修改同事的代码

# 标签

- 当某一个大版本完成之后,需要打一个标签

- 作用：

  - 记录大版本

  - 备份大版本代码

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E6%A0%87%E7%AD%BE%E5%9B%BE%E8%A7%A3.png)

**模拟经理打标签**

- 1.进入到经理的本地仓库info

  ```
   cd Desktop/manager/info/
  ```

- 2.经理在本地打标签

  ```
   git tag -a 标签名 -m '标签描述'
   例：
   git tag -a v1.0 -m 'version 1.0'
  ```

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E5%9C%A8%E6%9C%AC%E5%9C%B0%E6%89%93%E6%A0%87%E7%AD%BE.png)

- 3.经理推送标签到远程仓库

  ```
   git push origin 标签名
   例：
   git push origin v1.0
  ```

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E6%8E%A8%E9%80%81%E6%A0%87%E7%AD%BE.png)

- 4.查看打标签结果

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E6%9F%A5%E7%9C%8B%E6%89%93%E6%A0%87%E7%AD%BE%E7%BB%93%E6%9E%9C.png)

- 补充：删除本地和远程标签

  ```
    # 删除本地标签
    git tag -d 标签名
    # 删除远程仓库标签
    git push origin --delete tag 标签名
  ```

# 分支

![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E5%88%86%E6%94%AF.png)

- 作用：
  - 区分生产环境代码以及开发环境代码
  - 研究新的功能或者攻关难题
  - 解决线上bug
- 特点：
  - 项目开发中公用分支包括master、dev
  - 分支master是默认分支，用于发布，当需要发布时将dev分支合并到master分支
  - 分支dev是用于开发的分支，开发完阶段性的代码后，需要合并到master分支

**模拟经理分支操作**

- 对比：操作分支前的代码

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E6%93%8D%E4%BD%9C%E5%88%86%E6%94%AF%E5%89%8D%E4%BB%A3%E7%A0%81.png)

- 1.进入到经理的本地仓库info

  ```
   cd Desktop/manager/info/
  ```

- 2.查看当前分支

  ```
    git branch
  ```

  - 没有创建其他分支时，只有`master`分支

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%9F%A5%E7%9C%8Bmaster%E5%88%86%E6%94%AF.png)

- 3.经理创建并切换到dev分支

  ```
   git checkout -b dev
  ```

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E5%88%9B%E5%BB%BA%E5%B9%B6%E5%88%87%E6%8D%A2%E5%88%B0dev%E5%88%86%E6%94%AF.png)

- 4.设置本地分支跟踪远程指定分支（将分支推送到远程）

  ```
    git push -u origin dev
  ```

- 5.经理在dev分支编辑代码

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86dev%E7%BC%96%E8%BE%91%E4%BB%A3%E7%A0%81num4.png)

- 6.管理dev分支源代码：`add`、`commit`、`push`

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86dev%E7%BC%96%E8%BE%91%E4%BB%A3%E7%A0%81num4%E5%90%8Egit%E6%93%8D%E4%BD%9C.png)

  ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86dev%E7%BC%96%E8%BE%91%E4%BB%A3%E7%A0%81num4%E5%90%8E%E6%8E%A8%E9%80%81.png)

- 7.dev分支合并到master分支

  - 提示：只有当dev分支合并到master分支成功，张三才能获取到`num4`

  - 7.1 先切换到master分支

    ```
      git checkout master
    ```

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E5%90%88%E5%B9%B6%E5%88%86%E6%94%AF%E5%88%87%E6%8D%A2%E5%88%B0master%E5%88%86%E6%94%AF.png)

  - 7.2 dev分支合并到master分支

    ```
      git merge dev
    ```

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E7%BB%8F%E7%90%86%E5%90%88%E5%B9%B6%E5%88%86%E6%94%AFdev%E5%88%B0master.png)

  - 7.3 经理推送合并分支操作到远程仓库

    - 合并分支默认在本地完成，合并后直接推送即可

      ```
      git push
      ```

      ![img](file:///D:/hgx%E7%AC%94%E8%AE%B0/hgxbijiben/3%E3%80%81%E7%BC%96%E7%A8%8B%E5%BC%80%E5%8F%91%E7%9F%A5%E8%AF%86/3-git/images/github%E7%BB%8F%E7%90%86%E5%90%88%E5%B9%B6%E5%88%86%E6%94%AFdev%E5%88%B0master%E6%8E%A8%E9%80%81.png)

- 8.张三同步经理合并后的`num4`

  - 只有当张三同步代码成功，分支合并才算成功

    ```
      cd Desktop/zhangsan/info/
      git pull
    ```

    ![img](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/github%E5%BC%A0%E4%B8%89%E5%90%8C%E6%AD%A5%E5%88%86%E6%94%AF%E5%90%88%E5%B9%B6%E5%90%8Egit%E6%93%8D%E4%BD%9C.png)

    ![img](file:///D:/hgx%E7%AC%94%E8%AE%B0/hgxbijiben/3%E3%80%81%E7%BC%96%E7%A8%8B%E5%BC%80%E5%8F%91%E7%9F%A5%E8%AF%86/3-git/images/github%E5%BC%A0%E4%B8%89%E5%90%8C%E6%AD%A5%E5%88%86%E6%94%AF%E5%90%88%E5%B9%B6%E5%90%8E%E4%BB%A3%E7%A0%81.png)

>

![9c7bc198b36f77679bc7983f2f02810](Git%E2%80%94%E2%80%94C%E7%AB%99%E6%9C%80%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B%EF%BC%8C%E4%B8%80%E7%AF%87%E5%AD%A6%E4%BC%9A%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93Github.assets/9c7bc198b36f77679bc7983f2f02810.jpg)