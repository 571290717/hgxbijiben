# Python开的的pelican搭建个人blog 一

> 
>
> 
>
> 前几天心血来潮，想要在`GitHub Pages`上搭建一个静态博客；之前，我也曾基于`Django`开发过自己的博客，并买了云主机部署，但是访问量感人，慢慢自己也不打理了，就把云主机退订了（去吃吨好的~~~）；
>
> 虽然搭建静态博客很简单，但是也想记录一下，如果恰好能对你有所帮助或启发，那我也觉的很开心了。

搭建静态博客的工具多种多样，即有流行的[WordPress](https://wordpress.org/)，也有`GitHub Pages`官方推荐的[Jekyll](https://jekyllcn.com/)；其实，选用哪种工具不重要，关键是一步步的理解它，遇到问题、解决问题的思路和过程；

因为我本人对`Python`比较熟悉，所以我选用基于`Python`开发的[pelican](https://blog.getpelican.com/)，它基本满足我的需求：

- 支持`markdown`的格式；
- 提供自动化构建；
- 足够的主题库和插件库，并且支持定制化；
- ...

本文主要涉及`pelican`的基本使用方法，最终在本地搭建一个简陋的博客网站；

# 1. 准备环境

选定工作目录，并使用[pipenv](https://pipenv.readthedocs.io/en/latest/)创建一个虚拟环境：



```
λ mkdir pelican-blog
λ cd pelican-blog

# 创建基于 Python 3 的虚拟环境 
λ pipenv install --three

# 查看虚拟环境中的 Python 版本
λ pipenv run python --version
Python 3.7.3
```

在虚拟环境中安装必要的包：



```
λ pipenv install Markdown pelican

# 查看包之间的依赖关系
λ pipenv graph
Markdown==3.1.1
  - setuptools [required: >=36, installed: 41.6.0]
pelican==4.2.0
  - blinker [required: Any, installed: 1.4]
  - docutils [required: Any, installed: 0.15.2]
  - feedgenerator [required: >=1.9, installed: 1.9]
    - pytz [required: >=0a, installed: 2019.3]
    - six [required: Any, installed: 1.13.0]
  - jinja2 [required: >=2.7, installed: 2.10.3]
    - MarkupSafe [required: >=0.23, installed: 1.1.1]
  - pygments [required: Any, installed: 2.4.2]
  - python-dateutil [required: Any, installed: 2.8.1]
    - six [required: >=1.5, installed: 1.13.0]
  - pytz [required: >=0a, installed: 2019.3]
  - six [required: >=1.4, installed: 1.13.0]
  - unidecode [required: Any, installed: 1.1.1]
```

------

# 2. 新建项目

`pelican`提供了一个命令行工具：`pelican-quickstart`，能够让我们快速地新建一个网站项目；

它在执行的过程中，会交互式的询问一些配置项，如果你现在还不能确定的话，那就大胆的使用默认值吧，后面还可以在配置文件中修改；

[![pelican-quickstart](https://files.cnblogs.com/files/luizyao/pelican-quickstart.gif)](https://files.cnblogs.com/files/luizyao/pelican-quickstart.gif)

命令执行完成后，它会在我们的项目中新建如下的目录和文件：



```
.
├── content         # 目录，存放原始博文和相关静态文件
├── output          # 目录，存放构建后的网站源码
├── Makefile        
├── pelicanconf.py  # 构建相关的配置文件
├── publishconf.py  # 发布相关的配置文件
└── tasks.py
```

其中，`content/`目录存放所有的`markdown`格式的文本，我们还可以再新建一个`content/images/`的子目录，用于存放所有的图片；

> 注意：
>
> 在自动构建的过程中，`content/images/`中的文件会被无损地拷贝到`output/images/`中，通过修改`pelicanconf.py`文件中`STATIC_PATHS`的配置项（默认值为`['images']`）可以改变这种行为；

------

# 3. 第一篇博文

现在我们在`content/`目录下添加第一篇`markdown`格式的文章，就以本文为例；

`pelican`可以很“聪明”地从文章的元数据中提取需要的信息，所以我们以特定的格式编写文章的开头：



```
Title: 一、从零开始搭建自己的静态博客 -- 基础篇
Date: 2019-11-21 14:37
Modified: 2019-11-22 11:09
Category: 工具
Tags: pelican
Author: luizyao
Slug: pelican-blog-chapter-1
Summary: 本文简要的介绍 pelican 的基本用法
Status: published

<开始正文>
```

> 注意：
>
> - 更多元数据以参考：https://docs.getpelican.com/en/stable/content.html#file-metadata；
> - 如果你使用`VSCode`作为你的日常开发工具，那么我建议你使用[psioniq File Header](https://marketplace.visualstudio.com/items?itemName=psioniq.psi-header)插件为不同类型的文件自动生成头信息模版；

------

# 4. 修改配置文件

在正式开始构建之前，我们需要完善一下配置文件`pelicanconf.py`：



```
# pelicanconf.py

# 修改时区
TIMEZONE = 'Asia/Shanghai'

# 添加一个 GitHub 的“丝带”链接
GITHUB_URL = 'https://github.com/luizyao'

# 修改社交账号的展示
SOCIAL = (
    ('GitHub', 'https://github.com/luizyao'),
)

# 修改默认的时间格式（'%a %d %B %Y'）
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M"

# 为元数据定义默认值
DEFAULT_METADATA = {
    # 默认发布的文章都是草稿，除非在文章元数据中明确指定：Status: published
    'status': 'draft',
}
```

------

# 5. 本地构建和访问

我们通过以下命令构建网站并自动适配文件的修改，通过[http://localhost:8000](http://localhost:8000/)访问：



```
λ pipenv run pelican --autoreload --listen content/
```

> 注意：
>
> - 不要忘记把文章元数据中的`Status: draft`改成`Status: published`，不然我们是看不到这篇文章的；
>
> - `pelican`默认使用`notmyidea`这个主题来构建网站；你可以通过`pelican-themes`命令查看已安装的主题：
>
>   
>
>   ```
>   λ pipenv run pelican-themes --list
>   notmyidea
>   simple
>   ```
>
>   然后通过在`pelicanconf.py`中设定`THEME = 'simple'`或者构建时传入`-t 'simple'`选项来使用主题`simple`，实际上和纯文本差不多了；

------

# 6. `markdown`解析异常

- 这是一个列表：

  

  ```
  if 1：
      print('这是一段python代码')
  ```

这个时候，如果你访问我们的网站，你会发现上面的`markdown`代码被展示成下面的形式，根本就不是我们想要的缩进代码块的效果：

[![screenshot_markdown_error](https://files.cnblogs.com/files/luizyao/screenshot_markdown_error.bmp)](https://files.cnblogs.com/files/luizyao/screenshot_markdown_error.bmp)

为什么会这样呢？我们又该如何解决这个问题？

## 6.1. `Markdown`包的实现机制

`pelican`使用[Markdown](https://pypi.org/project/Markdown/)包作为`markdown`文本的解释器，这个包严格实现了[John Gruber’s Markdown](http://daringfireball.net/projects/markdown/)语法，并提供一些扩展；

`John Gruber`是`markdown`语法的发明者，他在`2004`发布了第一个版本的`markdown`语法，这一版本的语法有着明显的特点：

- 不支持三个反引号（`'```'`）包裹代码的写法；
- 不支持表格；
- 定义了严格的嵌套缩进的格式，必须是`4`个空格；
- ...

虽然自从发布了第一版之后，就再也没有更新过，但是现在流行的各种`markdown`语法都是基于它的扩展和补充，例如：[GitHub Markdown](https://help.github.com/categories/writing-on-github/)、[PHP Markdown](https://michelf.ca/projects/php-markdown/)等；

> 注意：
>
> 虽然`Markdown`包严格实现了`John Gruber’s Markdown`语法，但是具体的实现还是有一些差别的，更多细节可以参考：https://python-markdown.github.io/#differences

## 6.2. `pelican`默认使用的`Markdown`扩展

上一节中我们提到，`Markdown`包同样提供一些扩展用于解析更多类型的语法，这些扩展又分为官方扩展和第三方扩展；

通过查阅`pelican`的源码（或官方文档），可以看到其默认使用了以下扩展：



```
# pelican/settings.py

'MARKDOWN': {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
},
```

首先，我们看一下[markdown.extensions.extra](https://python-markdown.github.io/extensions/extra/)扩展：

它主要实现了大多数`PHP Markdown`的语法，是其它`6`个扩展的合集：

| 扩展               | 文档                                                         | 描述               |
| :----------------- | :----------------------------------------------------------- | :----------------- |
| Abbreviations      | https://python-markdown.github.io/extensions/abbreviations/  |                    |
| Attribute Lists    | https://python-markdown.github.io/extensions/attr_list/      |                    |
| Definition Lists   | https://python-markdown.github.io/extensions/definition_lists/ |                    |
| Fenced Code Blocks | https://python-markdown.github.io/extensions/fenced_code_blocks/ | 扩展了代码块的写法 |
| Footnotes          | https://python-markdown.github.io/extensions/footnotes/      |                    |
| Tables             | https://python-markdown.github.io/extensions/tables/         | 支持表格           |

我们重点看一下`Fenced Code Blocks`，因为它支持了我常用的三个反引号包裹代码块的写法：

> GitHub‘s backtick (```) syntax is also supported:
>
> 
>
> ```
> # more python code
> ```

然后，我们再看一下[markdown.extensions.codehilite](https://www.cnblogs.com/luizyao/p/11910504.html)扩展：

它基于[Pygments](http://pygments.org/)包为我们提供了代码的高亮显示，我们主要看一下它的一些可配置选项：

- `linenums`：如果置为`True`，将会为代码块每行标上行号；
- `css_class`：为`<div>`标签加上`class`属性，默认是`codehilite`；在这里，`pelican`使用的是`highlight`;

最后，我们看一下[markdown.extensions.meta](https://python-markdown.github.io/extensions/meta_data/)：

它主要是`pelican`内部使用，还记得我们每个`markdown`文本的开头都要有特定的格式吗？就是通过这个扩展读取的；感兴趣的同学可以自己去看一下，这里我们就不多说了；

## 6.3. 向第三方扩展寻求帮助

看到现在，我们也没有找到想要的解决方案：对列表里缩进嵌套反引号包裹的代码块，进行正确的渲染；

还好我们还有众多的第三方扩展供我们使用：https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions

我们找到一个[pymdownx.extra](https://facelessuser.github.io/pymdown-extensions/extensions/extra/)的扩展貌似可以代替`markdown.extensions.extra`，来一起看一下吧：

它和`markdown.extensions.extra`大部分是一样的，只是有以下不同：

- 新包含了[BetterEm](https://facelessuser.github.io/pymdown-extensions/extensions/betterem/)扩展：优化粗体和斜体的展示（不关心）；
- 新包含了[ExtraRawHTML](https://facelessuser.github.io/pymdown-extensions/extensions/extrarawhtml/)扩展：增加了对原始`HTML`代码的处理（不关心）；
- 使用[SuperFences](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/)扩展代替`Fenced Code Blocks`：加强版的`markdown`语法解析（看来正式我们想要的）；

> 其实，看到`SuperFences`文档的第一句话，我就知道妥了，嘻嘻；
>
> Allowing the nesting of fences under blockquotes, lists, or other block elements (see Limitations for more info).
>
> 文档的内容很丰富，我们就不再这里一一解释了，有兴趣的同学可以自己去看一看，说不定有什么意外的收获呢！！！

## 6.4. 解决问题

现在，我们来实际解决这个问题：

1. 安装必要的包：

   

   ```
   λ pipenv install pymdown-extensions
   ```

2. 修改`pelicanconf.py`文件中`MARKDOWN`的默认配置：

   

   ```
   # 使用第三方扩展来增强对 markdown 语言的解析，但是首先要安装 pymdown-extensions 模块
   MARKDOWN = {
       'extension_configs': {
           'markdown.extensions.codehilite': {'css_class': 'highlight'},
           'pymdownx.extra': {},
           'markdown.extensions.meta': {},
       },
       'output_format': 'html5',
   }
   ```

------

# 7. One more thing

我在浏览`SuperFences`文档时，发现一个很有意思的章节：https://facelessuser.github.io/pymdown-extensions/extensions/superfences/#code-highlighting；

它推荐了[pymdownx.highlight](https://facelessuser.github.io/pymdown-extensions/extensions/highlight/)代替`markdown.extensions.codehilite`，那我们就来看看这到底是个什么鬼？

在它的文档中有一句话大概能说明两者的关系：

> The Highlight extension is inspired by CodeHilite, but differs in features. PyMdown Extensions chooses not to implement special language headers for standard Markdown code blocks like CodeHilite does; PyMdown Extensions takes the position that language headers are better suited in fenced code blocks.

更多实现上的细节，我们不再去深究，主要看看我们可以用来干什么？

比如，为代码块每行加上行号：

咦？`markdown.extensions.codehilite`也可以啊，它不是也有一个`linenums`的选项吗？置成`True`不就行了；

说的对，不过丑。

一般情况下，为代码块添加行号有两种样式：

- `table`：默认的样式，创建一个表，第一列是行号；
- `inline`：在每行代码的开头，但是复制代码会把行号一起复制，不方便；

不过，`pymdownx.highlight`提供了第三种样式：`pymdownx-inline`，它和`inline`很像，只是复制时不会加上行号，因为实际上把行号元素渲染成下面这样：



```
<span class="lineno" data-linenos="1 "></span>
```

然后，我们通过以下的`CSS`样式去“激活”它：



```
[data-linenos]:before {
  content: attr(data-linenos);
}
```

下面，我们来将它具体的应用到我们的项目中吧：

首先，修改`pelicanconf.py`文件中`MARKDOWN`的默认配置：



```
# 使用第三方扩展来增强对 markdown 语言的解析，但是首先要安装 pymdown-extensions 模块
MARKDOWN = {
    'extension_configs': {
        'pymdownx.highlight': {
            'css_class': 'highlight',
            'linenums': True,
            'linenums_style': 'pymdownx-inline',
        },
        'pymdownx.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
```

然后，在`output/theme/css/main.css`文件的末尾加上下面这段代码：



```
[data-linenos]:before {
  content: attr(data-linenos);
}
```

最后重启下服务，就能看到效果了：

[![Screenshot_full_site](https://files.cnblogs.com/files/luizyao/Screenshot_full_site.bmp)](https://files.cnblogs.com/files/luizyao/Screenshot_full_site.bmp)

> 注意：
>
> 这里有个问题，如果我们重新执行构建命令，`output/theme/css/main.css`文件又会被覆盖成原先的内容，我们这个效果就看不到了；
>
> 不过这并不是我们最终的方案，所以我们也不在这里继续深究了。

> GitHub：[https://github.com/luizyao/pelican-blog/tree/chapter-](https://github.com/luizyao/pelican-blog/tree/chapter-1)