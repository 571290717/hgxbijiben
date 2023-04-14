# Django知识

1、django框架搭建

2、django URL路由

3、django模型层

4、django视图层

5、django模板层

6、django常用web工具

7、django的其他核心功能



### 1、django框架搭建

```python
pip install django==2.2.*  

python -m django --version

django-admin startproject myweb

python manage.py runserver

python manage.py startapp myapp
 #添加子应用
    
#设置中文
LANGUAGE_CODE = 'zh-Hans'
#亚洲上海时区
TIME_ZONE = 'Asia/Shanghai'
#在应用同级目录下,创建templates模板文件夹
#项目中匹配urls


pip install  mysqlclient

python manage.py migrate

或者
#pip install PyMySQL

#在Django的工程同名子目录的__init__.py文件中添加如下语句

#import pymysql

#pymysql.install_as_MySQLdb()

#修改DATABASES配置信息

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'book'  # 数据库名字
    }
}


#1）生成迁移文件

python manage.py makemigrations
#2）同步到数据库中

python manage.py migrate


python manage.py shell


#示例views.py：

from django.http import HttpResponse
from django.views import View

class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
    
    
    
# 示例urls.py：   
from django.urls import path

from myapp.views import MyView

urlpatterns = [
    path('mine/', MyView.as_view(), name='my-view'),
]

# 其中as_view()是接受请求并返回响应的可调用视图['get', 'post', 'put', 'patch', 'delete, 'options'.]
```



### 7、django的其他核心功能

```python

静态文件
配置静态文件
1.在settings 文件中定义静态内容
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

2.在项目根目录下创建static目录，再创建当前应用名称的目录
mysite/static/myapp/

3.在模板中可以使用硬编码
/static/my_app/myexample.jpg

4.在模板中可以使用static编码
{ % load static from staticfiles % }
...
<img src="{ % static "my_app/myexample.jpg" % }" alt="My image"/>


##Csrf
csrf的使用

csrf的使用
在django的模板中，提供了防止跨站攻击的方法，使用步骤如下：

step1：在settings.py中启用'django.middleware.csrf.CsrfViewMiddleware'中间件，此项在创建项目时，默认被启用

step2：在HTML的表单中添加标签

<form>
{ % csrf_token % }
...
</form>


取消保护
如果某些视图不需要保护，可以使用装饰器csrf_exempt，模板中也不需要写标签，修改csrf2的视图如下 from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def csrf2(request):
    uname=request.POST['uname'] 
    return render(request,'booktest/csrf2.html',{'uname':uname}) 
    运行上面的两个请求，发现都可以请求
    
    
##    保护原理
加入标签后，可以查看源代码，发现多了如下代码

<input type='hidden' name='csrfmiddlewaretoken' value='nGjAB3Md9ZSb4NmG1sXDolPmh3bR2g59' />
在浏览器的调试工具中，通过network标签可以查看cookie信息

本站中自动添加了cookie信息，如下图csrf3

查看跨站的信息，并没有cookie信息，即使加入上面的隐藏域代码，发现又可以访问了

结论：django的csrf不是完全的安全

当提交请求时，中间件'django.middleware.csrf.CsrfViewMiddleware'会对提交的cookie及隐藏域的内容进行验证，如果失败则返回403错误

##Ajax CSRF 认证
GET 请求不需要 CSRF 认证，POST 请求需要正确认证才能得到正确的返回结果。

如果使用Ajax调用的时候，就要麻烦一些。需要注意以下几点：

在视图中使用render （而不要使用 render_to_response）
使用 jQuery 的 ajax 或者 post 之前 加入这个 js 代码

jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
#或者 #更为优雅简洁的代码（不能写在 .js 中，要直接写在模板文件中）：

$.ajaxSetup({
    data: {csrfmiddlewaretoken: '{ { csrf_token } }' },
});
这样之后，就可以像原来一样的使用 jQuery.ajax() 和 jQuery.post()了
    
    
    
    
    
## 状态保持
HTTP协议是无状态的：每次请求都是一次新的请求，不会记得之前通信的状态
客户端与服务器端的一次通信，就是一次会话
实现状态保持的方式：在客户端或服务器端存储与会话有关的数据
存储方式包括cookie、session，会话一般指session对象
使用cookie，所有数据存储在客户端，注意不要存储敏感信息
推荐使用sesison方式，所有数据存储在服务器端，在客户端cookie中存储session_id
状态保持的目的是在一段时间内跟踪请求者的状态，可以实现跨页面访问当前请求者的数据
注意：不同的请求者之间不会共享这个数据，与请求者一一对应
开启session
使用django-admin startproject创建的项目默认启用
禁用会话：删除下面指定的两个值，禁用会话将节省一些性能消耗
Django 中session需要依赖数据库,因此需要确认数据库中是否存在 与session相关的 表
在settings.py文件中

* 项INSTALLED_APPS列表中添加：
* 'django.contrib.sessions',

* 项MIDDLEWARE_CLASSES列表中添加：
* 'django.contrib.sessions.middleware.SessionMiddleware',
使用session
启用会话后，每个HttpRequest对象将具有一个session属性，它是一个类字典对象
get(key, default=None)：根据键获取会话的值
clear()：清除所有会话
flush()：删除当前的会话数据并删除会话的Cookie
del request.session['member_id']：删除会话
示例:

#session设置
 request.session[key] = value

#session获取
 request.session.get(key,default=Node)

#session删除

# 删除单个key 不存在时报错
 del request.session['a'] 

#清除所有会话,但不会删除数据
 request.session.clear() 

#删除当前的会话数据
 request.session.flush()
    
    
    
##中间件
中间件是一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，修改Django的输入或输出
激活：添加到Django配置文件中的MIDDLEWARE_CLASSES元组中
使用中间件，可以干扰整个处理过程，每次请求中都会执行中间件的这个方法
验证用户是否登陆示例
在应用中创建AdminLoginMiddleware.py文件

from django.shortcuts import render
from django.http import HttpResponse
import re

class AdminLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):


        # 检测当前的请求是否已经登录,如果已经登录,.则放行,如果未登录,则跳转到登录页
        # 获取当前用户的请求路径  /admin/开头  但不是 /admin/login/  /admin/dologin/   /admin/verifycode
        urllist = ['/admin/login','/admin/dologin','/admin/vcode']
        # 判断是否进入了后台,并且不是进入登录页面
        if re.match('/admin/',request.path) and request.path not in urllist:

            # 检测session中是否存在 adminlogin的数据记录
            if request.session.get('Vuser','') == '':
                # 如果在session没有记录,则证明没有登录,跳转到登录页面
                return HttpResponse('<script>alert("请先登录");location.href="/admin/login";</script>')



        response = self.get_response(request)
        return response
##配置中间件
在settings.py文件中修改MIDDLEWARE_CLASSES选项

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #自定义的中间件
    'myadmin.AdminMiddleware.AdminLoginMiddleware'
]
    

    
    
#使用Django中提供的密码方案
该django.contrib.auth.hashers模块提供了一组函数来创建和验证散列密码。您可以独立于User模型使用它们。

 # from django.contrib.auth.hashers import make_password, check_password

 # 对密码进行加密操作
 # upass = make_password(request.POST['password'], None, 'pbkdf2_sha256')
 # upass = check_password('1234567','pbkdf2_sha256$36000$197nqXM6yxYv$Zxh/Vsns8qszkvUmY81BgrjCeLPXhCHLEilP6VO+Rnc=')
python中的MD5加密
#获取密码并md5
import hashlib
m = hashlib.md5() 
m.update(bytes(request.POST['password'],encoding="utf8"))
print(m.hexdigest())

```





