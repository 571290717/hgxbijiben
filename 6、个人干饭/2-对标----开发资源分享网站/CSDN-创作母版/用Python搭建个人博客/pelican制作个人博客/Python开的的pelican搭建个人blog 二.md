

# Python开的的pelican搭建个人blog 二



我们已经成功地在本地搭建了一个博客网站，它使用的是`pelican`默认的`notmyidea`主题；

> 如果你不太记得了，可以再看看这篇文章：[一、从零开始搭建自己的静态博客 -- 基础篇](https://www.cnblogs.com/luizyao/p/11910504.html)；

其实，`pelican`拥有众多的开源主题库，我们可以在[`pelican`主题仓库](https://github.com/getpelican/pelican-themes)上选择一个自己喜欢的主题应用到项目中；

> http://pelicanthemes.com/网站提供在线预览主题的功能；

我选择的是[pelican-alchemy](https://github.com/nairobilug/pelican-alchemy)主题，它的在线`Demo`是：https://nairobilug.github.io/pelican-alchemy/；

下面，我们来一步一步的将其应用到我们的项目中；

# 1. 下载主题

我粗略的浏览了一下`pelican-alchemy`的文档和`issue`列表，考虑到后续有可能会做一些修改，所以我决定先将其`fork`到自己的仓库；

然后，我在项目根目录新建一个目录`themes/`用于存放所有下载的主题，然后将`fork`后的`pelican-alchemy`作为一个独立的子仓库克隆到目录下：



```
λ mkdir themes
λ git submodule add git@github.com:luizyao/pelican-alchemy.git themes/pelican-alchemy
```

> 注意：
>
> `git submodule add <url> <path>`命令是将一个仓库添加到指定的目录下作为独立的子仓库；
>
> 如果你仔细观察，会发现我们的根目录下多了一个文件：`.gitmodules`，它记录了子仓库的信息；
>
> 例如：我们项目中这个文件的内容是：
>
> 
>
> ```
> [submodule "themes/pelican-alchemy"]
>     path = themes/pelican-alchemy
>     url = git@github.com:luizyao/pelican-alchemy.git
> ```
>
> 常用的和子仓库的相关的操作有下面几个：
>
> - 克隆父仓库时，连同子仓库一起克隆：
>
>   
>
>   ```
>   git clone --recurse-submodules <URL> <directory>
>   ```
>
> - 查看父仓库中所有子仓库的状态：
>
>   
>
>   ```
>   λ git submodule status
>   3381c5031bf30d3b1212619b662898f178d695f1 themes/pelican-alchemy (v2.1-43-g3381c50)
>   ```
>
>   `3381c5031bf30d3b1212619b662898f178d695f1`是对当前`Commit Id`的`SHA-1`加密字串；
>
> - 删除子仓库：
>
>   
>
>   ```
>   git rm <submodule path> && git commit
>   ```
>
>   再手动删除`.git/modules/<name>/`目录
>
> 如果你想了解更多关于`git submodule`的内容，可以通过`git submodule --help`阅读它的官方文档；

------

# 2. 使用主题

## 2.1. 基本配置



```
# pelicanconf.py

# 主题所在的相对目录
THEME = 'themes/pelican-alchemy/alchemy'

# 副标题
SITESUBTITLE = '戒骄戒躁 砥砺前行'

# 头像
SITEIMAGE = '/images/profile.png width=200 height=200'

# 友链
LINKS = (
    ('pytest-chinese-doc', 'https://luizyao.github.io/pytest-chinese-doc/'),
)

# 代码高亮的样式
PYGMENTS_STYLE = 'friendly'

# 使用 Bootswatch 样式：https://bootswatch.com/
BOOTSTRAP_CSS = 'https://cdn.bootcss.com/bootswatch/4.3.1/lux/bootstrap.min.css'

# 生成 sitemap.xml 文件，它是一个对爬虫友好的文件，方便搜索引擎抓取网站页面
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'

# 构建后的 html 文件路径和 URL 标识
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
DRAFTS_URL = 'drafts/{date:%Y}/{date:%m}/{slug}.html'
DRAFTS_SAVE_AS = ARTICLE_URL
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL

# RSS 订阅
FEED_ALL_RSS = 'feeds/all.rss.xml'
```

> 具体细节可以参考：https://github.com/nairobilug/pelican-alchemy/wiki/Settings

## 2.2. 高级配置

### 2.2.1. 配置网站图标

通过在线工具https://realfavicongenerator.net/可以生成适配各种平台和浏览器的`favicon`文件：

下载上面生成的`favicon`包，并解压到项目`content/extras`目录下：



```
λ ls content/extras/
android-chrome-192x192.png  favicon.ico         safari-pinned-tab.svg
android-chrome-384x384.png  favicon-16x16.png   site.webmanifest
apple-touch-icon.png        favicon-32x32.png
browserconfig.xml           mstile-150x150.png
```

修改模版中的`base.html`文件：



```
<!-- themes/pelican-alchemy/alchemy/templates/base.html --> 

{% if RFG_FAVICONS %}
  <link rel="apple-touch-icon" href="{{ SITEURL }}/apple-touch-icon.png" sizes="180x180">
  <link rel="icon" type="image/png" href="{{ SITEURL }}/favicon-32x32.png" sizes="32x32">
  <link rel="icon" type="image/png" href="{{ SITEURL }}/favicon-16x16.png" sizes="16x16">
  <link rel="manifest" href="{{ SITEURL }}/manifest.json">
  <meta name="theme-color" content="#333333">
{% endif %}

<!-- 改成 --> 

{% if RFG_FAVICONS %}
  <link rel="apple-touch-icon" href="{{ SITEURL }}/apple-touch-icon.png" sizes="180x180">
  <link rel="icon" type="image/png" href="{{ SITEURL }}/favicon-32x32.png" sizes="32x32">
  <link rel="icon" type="image/png" href="{{ SITEURL }}/favicon-16x16.png" sizes="16x16">
  <link rel="manifest" href="{{ SITEURL }}/site.webmanifest">
  <link rel="mask-icon" href="{{ SITEURL }}/safari-pinned-tab.svg" color="#5bbad5">
  <meta name="msapplication-TileColor" content="#da532c">
  <meta name="theme-color" content="#ffffff">
{% endif %}
```

修改`pelicanconf.py`配置文件：



```
# pelicanconf.py

# 在构建中，它们会无损的拷贝到 output 的同名目录下
STATIC_PATHS = ['extras', 'images', 'css']

# 构建时，extras/android-chrome-192x192.png文件，拷贝到output/android-chrome-192x192.png，不再是output/extras/android-chrome-192x192.png
EXTRA_PATH_METADATA = {
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/manifest.json': {'path': 'manifest.json'},
    'extras/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extras/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
    # 自定义样式
    'css/custom.css': {'path': 'theme/css/custom.css'},
}

# 自定义样式的URL目录
THEME_CSS_OVERRIDES = ('theme/css/custom.css',)

RFG_FAVICONS = True
```

### 2.2.2. 更新`Font Awesome`的版本

`pelican-alchemy`使用`Font Awesome 4.7.0`版本，并且使用的是静态资源的相对引用；

我们将其修改为最新的`5.11.2`版本的`CDN`引入，修改主题模版中的`base.html`文件：



```
<!-- themes/pelican-alchemy/alchemy/templates/base.html --> 

<link rel="stylesheet" href="{{ SITEURL }}/theme/css/font-awesome.min.css">

<!-- 改成 --> 

<link href="https://cdn.bootcss.com/font-awesome/5.11.2/css/fontawesome.min.css" rel="stylesheet">
<link href="https://cdn.bootcss.com/font-awesome/5.11.2/css/solid.css" rel="stylesheet">
<link href="https://cdn.bootcss.com/font-awesome/5.11.2/css/brands.css" rel="stylesheet">
```

除了上面的步骤，我们还有一个额外的工作要做：**因为`5.x`的版本已经不使用`fa`前缀，取而代之的是`fas`（[`Solid`样式](https://fontawesome.com/icons?s=solid)）和`fab`（[`Brands`样式](https://fontawesome.com/icons?s=brands)）；**

所以，对于主题中那些类似`class="fa fa-github"`的样式，应该修改为`class="fab fa-github"`，主要涉及`article.html`、`index.html`和`header.html`这些文件；

最后，修改`pelicanconf.py`文件中关于`ICONS`配置的格式，需要额外指定样式类别：



```
# pelicanconf.py

# 社交属性，请到<https://fontawesome.com/icons>网站确定图标样式的类别
ICONS = [
    ('fab', 'github', 'https://github.com/luizyao'),
    ('fas', 'blog', 'https://www.cnblogs.com/luizyao/'),
    ('fas', 'rss', 'feeds/all.rss.xml')
]
```

> `pelican-alchemy`有一个`open`的`issue`：https://github.com/nairobilug/pelican-alchemy/issues/69是关于`Font Awesome`版本的，后续可能会更新到`5.x`版本，目前`issue`处于接收反馈的状态；
>
> 至于为什么不使用`CDN`，貌似还和伟大的防火墙有关呢。。。
>
> > I'm sure you've heard of the Great Firewall of China; India, Russia, some African countries are doing similar things. You never know which URL or IP might become inaccessible

### 2.2.3. 使用`Bootstrap`的样式

我们可以为特定类型的元素添加`Bootstrap`的官方样式；例如：为每个`img`元素添加`class = "img-fluid"`的样式；

首先，安装依赖包：



```
# beautifulsoup4为插件所依赖的第三方包
λ pipenv install beautifulsoup4
```

然后，下载[Bootstrapify](https://github.com/ingwinlu/pelican-bootstrapify)插件：



```
λ mkdir plugins
λ git submodule add git@github.com:ingwinlu/pelican-bootstrapify.git plugins/pelican-bootstrapify
```

最后，修改`pelicanconf.py`配置文件：



```
# 到哪里寻找插件
PLUGIN_PATHS = ['plugins']

# 想要使用的插件名
PLUGINS = ['pelican-bootstrapify']

# 想要添加的 Bootstrap 样式
BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
}
```

## 2.3. 定制主题

下面我们为`pelican-alchemy`做一些定制化的操作，添加一些新的功能；

### 2.3.1. 添加返回顶部链接

修改`base.html`文件，在`<head>`中添加如下部分：



```
<!-- themes/pelican-alchemy/alchemy/templates/base.html --> 

<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdn.bootcss.com/scrollup/2.4.1/jquery.scrollUp.min.js"></script>

<script>
  $(function () {
    $.scrollUp({
      scrollText: '<i class="fas fa-2x fa-chevron-circle-up"></i>'
    });
  });
</script>
```

### 2.3.2. 支持目录

我自己写了一个的插件，用于替代`pelican`默认的`MarkdownReader`，它有以下功能：

- 使用增强的`markdown`解析

  - [pymdownx.extra](https://facelessuser.github.io/pymdown-extensions/extensions/extra/)代替`markdown.extensions.extra`；
  - [pymdownx.highlight](https://facelessuser.github.io/pymdown-extensions/extensions/highlight/)代替`markdown.extensions.codehilite`；

- 支持以下方式生成文章目录：

  1. 在`markdown`文本内的`[TOC]`标记处生成目录；

  2. 通过元数据`toc`自定义目录样式；例如：

     

     ```
     {% if article.toc %}
       <aside class="col-md-4">
         <div class="widget widget-content">
           <h3 class="widget-title">文章目录</h3>
           <div class="toc">
             <ul>
               {{ article.toc | safe }}
             </ul>
           </div>
         </div>
       </aside>
     {% endif %}
     ```

- 如果没配`summary`或者`summary`为空，支持自动截取开头部分字符作为摘要；

使用方法：

1. 作为一个子仓库下载

   

   ```
   # 项目根目录创建目录
   λ mkdir plugins
   # 下载
   λ git submodule add git@github.com:luizyao/pelican-md-reader.git plugins/pelican-md-reader
   ```

2. 修改`pelicanconf.py`配置文件

   

   ```
   # pelicanconf.py
   
   # 到哪里寻找插件
   PLUGIN_PATHS = ['plugins']
   
   # 想要使用的插件名
   PLUGINS = ['pelican-md-reader']
   ```

> 更多细节可以参考：[pelican-md-reader](https://github.com/luizyao/pelican-md-reader)

### 2.3.3. 汉化

主要关键字汉化；

------

# 3. 完整的`pelicanconf.py`文件



```
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'luizyao'
SITENAME = "luizyao's blog"
SITEURL = ''

PATH = 'content'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# 修改时区
TIMEZONE = 'Asia/Shanghai'

# 修改默认的时间格式（'%a %d %B %Y'）
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M"

# 为元数据定义默认值
DEFAULT_METADATA = {
    # 默认发布的文章都是草稿，除非在文章元数据中明确指定：Status: published
    'status': 'draft',
}

# pelican-alchemy 原有的配置

# 主题所在的相对目录
THEME = 'themes/pelican-alchemy/alchemy'

# 副标题
SITESUBTITLE = '戒骄戒躁 砥砺前行'

# 头像
SITEIMAGE = '/images/profile.png width=200 height=200'

# 友链
LINKS = (
    ('pytest-chinese-doc', 'https://luizyao.github.io/pytest-chinese-doc/'),
)

# 代码高亮的样式
PYGMENTS_STYLE = 'friendly'

# 使用 Bootswatch 样式：https://bootswatch.com/
BOOTSTRAP_CSS = 'https://cdn.bootcss.com/bootswatch/4.3.1/lux/bootstrap.min.css'

# 生成 sitemap.xml 文件
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'

# 构建后的 html 文件路径和 URL 标识
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
DRAFTS_URL = 'drafts/{date:%Y}/{date:%m}/{slug}.html'
DRAFTS_SAVE_AS = ARTICLE_URL
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL

# RSS 订阅
FEED_ALL_RSS = 'feeds/all.rss.xml'

# 在构建中，它们会无损的拷贝到 output 的同名目录下
STATIC_PATHS = ['extras', 'images', 'css']

# 构建时，extras/android-chrome-192x192.png文件，拷贝到output/android-chrome-192x192.png，不再是output/extras/android-chrome-192x192.png
EXTRA_PATH_METADATA = {
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/manifest.json': {'path': 'manifest.json'},
    'extras/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extras/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
    # 自定义样式
    'css/custom.css': {'path': 'theme/css/custom.css'},
}

# 自定义样式的URL目录
THEME_CSS_OVERRIDES = ('theme/css/custom.css',)

RFG_FAVICONS = True

# 到哪里寻找插件
PLUGIN_PATHS = ['plugins']

# 想要使用的插件名
PLUGINS = ['pelican-bootstrapify', 'pelican-md-reader']

# 想要添加的 Bootstrap 样式
BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
}

# 社交属性，请到<https://fontawesome.com/icons>网站确定图标样式的类别
ICONS = [
    ('fab', 'github', 'https://github.com/luizyao'),
    ('fas', 'blog', 'https://www.cnblogs.com/luizyao/'),
    ('fas', 'rss', 'feeds/all.rss.xml')
]
```

------

# 4. 预览

[https://blog.luizyao.com](https://blog.luizyao.com/)

> Github: https://github.com/luizyao/pelican-blog