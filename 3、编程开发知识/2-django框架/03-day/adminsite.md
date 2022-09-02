# Admin站点 {#admin站点}

假设我们要设计一个新闻网站，我们需要编写展示给用户的页面，网页上展示的新闻信息是从哪里来的呢？**是从数据库中查找到新闻的信息，然后把它展示在页面上**。但是我们的网站上的新闻每天都要更新，这就意味着对数据库的增、删、改、查操作，那么我们需要每天写sql语句操作数据库吗? 如果这样的话，是不是非常繁琐，所以我们可以设计一个页面，通过对这个页面的操作来实现对新闻数据库的增删改查操作。那么问题来了，老板说我们需要在建立一个新网站，是不是还要设计一个页面来实现对新网站数据库的增删改查操作，但是这样的页面具有一个很大的重复性，那有没有一种方法能够让我们很快的生成管理数据库表的页面呢？**有，那就是我们接下来要给大家讲的Django的后台管理**。Django能够根据定义的模型类自动地生成管理页面。

使用Django的管理模块，需要按照如下步骤操作：

1. 管理界面本地化
2. 创建管理员
3. 注册模型类
4. 自定义管理页面

## 1 管理界面本地化 {#1--管理界面本地化}

在settings.py中设置语言和时区

```
#设置中文
LANGUAGE_CODE = 'zh-Hans'
#亚洲上海时区
TIME_ZONE = 'Asia/Shanghai'
```

## 2 创建超级管理员 {#2--创建超级管理员}

创建管理员的命令如下，按提示输入用户名、邮箱、密码。

```
python manage.py createsuperuser
```

![](/assets/创建站点管理员.png)

打开浏览器，在地址栏中输入如下地址后回车。

```
http://127.0.0.1:8000/admin/
```

输入前面创建的用户名、密码完成登录。

![](/assets/登陆站点.png "登录")

登录成功后界面如下，但是并没有我们自己应用模型的入口，接下来进行第三步操作。

![](/assets/登陆站点成功.png "admin默认首页")

## 3 注册模型类 {#3--注册模型类}

登录后台管理后，默认没有我们创建的应用中定义的模型类，需要在自己应用中的admin.py文件中注册，才可以在后台管理中看到，并进行增删改查操作。

打开booktest/admin.py文件，编写如下代码：

```
from django.contrib import admin
#导入模型
from book.models import BookInfo,PeopleInfo
# Register your models here.
#注册书籍模型
admin.site.register(BookInfo)
#注册人物模型
admin.site.register(PeopleInfo)
```

到浏览器中刷新页面，可以看到模型类BookInfo和PeopleInfo的管理了。

![](/assets/show.png)

点击类名称"BookInfo"（图书）可以进入列表页，默认只有一列。

![](/assets/admin_one.png)

在列表页中点击"增加"可以进入增加页，Django会根据模型类的不同，生成不同的表单控件，按提示填写表单内容后点击"保存"，完成数据创建，创建成功后返回列表页。

![](/assets/admin_add.png)

在列表页中点击某行的第一列可以进入修改页。

![](/assets/admin_show.png)

按照提示进行内容的修改，修改成功后进入列表页。在修改页点击“删除”可以删除一项。

![](/assets/admin_delete.png)

删除：在列表页勾选想要删除的复选框，可以删除多项。

![](/assets/delete.png)

点击执行后进入确认页面，删除后回来列表页面。

![](/assets/delete_confirm.png)

## 4 定义与使用Admin管理类 {#4--定义与使用admin管理类}

Django提供的Admin站点的展示效果可以通过自定义**ModelAdmin**类来进行控制。

定义管理类需要继承自**admin.ModelAdmin**类，如下

```
from django.contrib import admin

class BookInfoAdmin(admin.ModelAdmin):
    pass
```

使用管理类有两种方式：

* 注册参数

  ```
  admin.site.register(BookInfo,BookInfoAdmin)
  ```

* 装饰器

  ```
  @admin.register(BookInfo)
  class BookInfoAdmin(admin.ModelAdmin):
      pass
  ```



