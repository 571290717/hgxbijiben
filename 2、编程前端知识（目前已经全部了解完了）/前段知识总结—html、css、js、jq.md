# 前段知识总结



### 2. html的定义

HTML 的全称为：HyperText Mark-up Language, 指的是超文本标记语言。 标记：就是标签, `<标签名称> </标签名称>`, 比如: `<html></html>、<h1></h1>` 等，标签大多数都是成对出现的。

所谓超文本，有两层含义:

1. 因为网页中还可以图片、视频、音频等内容(超越文本限制)
2. 它还可以在网页中跳转到另一个网页，与世界各地主机的网页链接(超链接文本)

### 3. html的作用

html是用来开发网页的，它是开发网页的语言。

- html是开发网页的语言
- html中的标签大多数都是成对出现的, 格式: `<标签名></标签名>`

### 1. 结构代码

```html
<!DOCTYPE html>
<html>
    <head>            
        <meta charset="UTF-8">
        <title>网页标题</title>
    </head>
    <body>
          网页显示内容
    </body>
</html>
```

1. 第一行`<!DOCTYPE html>`是文档声明, 用来指定页面所使用的html的版本, 这里声明的是一个html5的文档。
2. `<html>...</html>`标签是开发人员在告诉浏览器，整个网页是从`<html>`这里开始的，到`<html>`结束,也就是html文档的开始和结束标签。
3. `<head>...</head>`标签用于定义文档的头部,是负责对网页进行设置标题、编码格式以及引入css和js文件的。
4. `<body>...</body>`标签是编写网页上显示的内容。
5. 

| 标签                                                         | 描述                                               |
| ------------------------------------------------------------ | -------------------------------------------------- |
| <!--...-->                                                   | 定义注释。                                         |
| <[!DOCTYPE](https://baike.baidu.com/item/!DOCTYPE?fromModule=lemma_inlink)> | 定义文档类型。                                     |
| <a>                                                          | 定义锚。                                           |
| <abbr>                                                       | 定义缩写。                                         |
| <acronym>                                                    | 定义只取首字母的缩写。                             |
| <address>                                                    | 定义文档作者或拥有者的联系信息。                   |
| <applet>                                                     | 不赞成使用。定义嵌入的 applet。                    |
| <area>                                                       | 定义图像映射内部的区域。                           |
| <article>                                                    | 定义文章。                                         |
| <aside>                                                      | 定义页面内容之外的内容。                           |
| <audio>                                                      | 定义声音内容。                                     |
| <b>                                                          | 定义粗体字。                                       |
| <base>                                                       | 定义页面中所有链接的默认地址或默认目标。           |
| <basefont>                                                   | 不赞成使用。定义页面中文本的默认字体、颜色或尺寸。 |
| <bdi>                                                        | 定义文本的文本方向，使其脱离其周围文本的方向设置。 |
| <bdo>                                                        | 定义文字方向。                                     |
| <big>                                                        | 定义大号文本。                                     |
| <blockquote>                                                 | 定义长的引用。                                     |
| <body>                                                       | 定义文档的主体。                                   |
| <br>                                                         | 定义简单的折行。                                   |
| <button>                                                     | 定义按钮 (push button)。                           |
| <canvas>                                                     | 定义图形。                                         |
| <caption>                                                    | 定义表格标题。                                     |
| <center>                                                     | 不赞成使用。定义居中文本。                         |
| <cite>                                                       | 定义引用(citation)。                               |
| <code>                                                       | 定义计算机代码文本。                               |
| <col>                                                        | 定义表格中一个或多个列的属性值。                   |
| <colgroup>                                                   | 定义表格中供格式化的列组。                         |
| <command>                                                    | 定义命令按钮。                                     |
| <datalist>                                                   | 定义下拉列表。                                     |
| <dd>                                                         | 定义定义列表中项目的描述。                         |
| <del>                                                        | 定义被删除文本。                                   |
| <details>                                                    | 定义元素的细节。                                   |
| <dir>                                                        | 不赞成使用。定义目录列表。                         |
| <div>                                                        | 定义文档中的节。                                   |
| <dfn>                                                        | 定义定义项目。                                     |
| <dialog>                                                     | 定义对话框或窗口。                                 |
| <dl>                                                         | 定义定义列表。                                     |
| <dt>                                                         | 定义定义列表中的项目。                             |
| <em>                                                         | 定义强调文本。                                     |
| <embed>                                                      | 定义外部交互内容或插件。                           |
| <fieldset>                                                   | 定义围绕表单中元素的边框。                         |
| <figcaption>                                                 | 定义 figure 元素的标题。                           |
| <figure>                                                     | 定义媒介内容的分组，以及它们的标题。               |
| <font>                                                       | 不赞成使用。定义文字的字体、尺寸和颜色。           |
| <footer>                                                     | 定义 section 或 page 的页脚。                      |
| <form>                                                       | 定义供用户输入的 HTML 表单。                       |
| <frame>                                                      | 定义框架集的窗口或框架。                           |
| <frameset>                                                   | 定义框架集。                                       |
| <h1> to <h6>                                                 | 定义 HTML 标题，可以改变标题的大小。               |
| <head>                                                       | 定义关于文档的信息。                               |
| <header>                                                     | 定义 section 或 page 的页眉。                      |
| <hr>                                                         | 定义水平线。                                       |
| <html>                                                       | 定义 HTML 文档。                                   |
| <i>                                                          | 定义斜体字。                                       |
| <iframe>                                                     | 定义内联框架。                                     |
| <img>                                                        | 定义图像。                                         |
| <input>                                                      | 定义输入控件。                                     |
| <ins>                                                        | 定义被插入文本。                                   |
| <isindex>                                                    | 不赞成使用。定义与文档相关的可搜索索引。           |
| <kbd>                                                        | 定义键盘文本。                                     |
| <keygen>                                                     | 定义生成密钥。                                     |
| <label>                                                      | 定义 input 元素的标注。                            |
| <legend>                                                     | 定义 fieldset 元素的标题。                         |
| <li>                                                         | 定义列表的项目。                                   |
| <link>                                                       | 定义文档与外部资源的关系。                         |
| <map>                                                        | 定义图像映射。                                     |
| <mark>                                                       | 定义有记号的文本。                                 |
| <menu>                                                       | 定义菜单列表。                                     |
| <meta>                                                       | 定义关于 HTML 文档的元信息。                       |
| <meter>                                                      | 定义预定义范围内的度量。                           |
| <nav>                                                        | 定义导航链接。                                     |
| <noframes>                                                   | 定义针对不支持框架的用户的替代内容。               |
| <noscript>                                                   | 定义针对不支持客户端脚本的用户的替代内容。         |
| <object>                                                     | 定义内嵌对象。                                     |
| <ol>                                                         | 定义有序列表。                                     |
| <optgroup>                                                   | 定义选择列表中相关选项的组合。                     |
| <option>                                                     | 定义选择列表中的选项。                             |
| <output>                                                     | 定义输出的一些类型。                               |
| <p>                                                          | 定义段落。                                         |
| <param>                                                      | 定义对象的参数。                                   |
| <pre>                                                        | 定义预格式文本。                                   |
| <progress>                                                   | 定义任何类型的任务的进度。                         |
| <q>                                                          | 定义短的引用。                                     |
| <rp>                                                         | 定义若浏览器不支持 ruby 元素显示的内容。           |
| <rt>                                                         | 定义 ruby 注释的解释。                             |
| <ruby>                                                       | 定义 ruby 注释。                                   |
| <s>                                                          | 定义加删除线的文本。                               |
| <samp>                                                       | 定义计算机代码样本。                               |
| <script>                                                     | 定义客户端脚本。                                   |
| <section>                                                    | 定义 section。                                     |
| <select>                                                     | 定义选择列表（下拉列表）。                         |
| <small>                                                      | 定义小号文本。                                     |
| <source>                                                     | 定义媒介源。                                       |
| <span>                                                       | 定义文档中的节。                                   |
| <strike>                                                     | 不赞成使用。定义加删除线文本。                     |
| <strong>                                                     | 定义强调文本。                                     |
| <style>                                                      | 定义文档的样式信息。                               |
| <sub>                                                        | 定义下标文本。                                     |
| <summary>                                                    | 为 <details> 元素定义可见的标题。                  |
| <sup>                                                        | 定义上标文本。                                     |
| <table>                                                      | 定义表格。                                         |
| <tbody>                                                      | 定义表格中的主体内容。                             |
| <td>                                                         | 定义表格中的单元。                                 |
| <textarea>                                                   | 定义多行的文本输入控件。                           |
| <tfoot>                                                      | 定义表格中的表注内容（脚注）。                     |
| <th>                                                         | 定义表格中的表头单元格。                           |
| <thead>                                                      | 定义表格中的表头内容。                             |
| <time>                                                       | 定义日期/时间。                                    |
| <title>                                                      | 定义文档的标题。                                   |
| <tr>                                                         | 定义表格中的行。                                   |
| <track>                                                      | 定义用在媒体播放器中的文本轨道。                   |
| <tt>                                                         | 定义打字机文本。                                   |
| <u>                                                          | 定义下划线文本。                                   |
| <ul>                                                         | 定义无序列表。                                     |
| <var>                                                        | 定义文本的变量部分。                               |
| <video>                                                      | 定义视频。                                         |
| <wbr>                                                        | 定义视频。                                         |
| <xmp>                                                        | 定义预格式文本。                                   |

### 1. 常用的 html 标签

```html
<!-- 1、成对出现的标签：-->

<h1>h1标题</h1>
<div>这是一个div标签</div>
<p>这个一个段落标签</p>


<!-- 2、单个出现的标签： -->
<br>
<img src="images/pic.jpg" alt="图片">
<hr>

<!-- 3、带属性的标签，如src、alt 和 href等都是属性 -->
<img src="images/pic.jpg" alt="图片">
<a href="http://www.baidu.com">百度网</a>

<!-- 4、标签的嵌套 -->
<div>
    <img src="images/pic.jpg" alt="图片">
    <a href="http://www.baidu.com">百度网</a>
</div>
```

**提示:**

1. 标签不区分大小写，但是推荐使用小写。
2. 根据标签的书写形式，标签分为双标签(闭合标签)和单标签(空标签)
   2.1 双标签是指由开始标签和结束标签组成的一对标签，这种标签允许嵌套和承载内容，比如: div标签
   2.2 单标签是一个标签组成，没有标签内容， 比如: img标签

### 2. 小结

- 学习 html 语言就是学习标签的用法，常用的标签有20多个。
- 编写 html 标签建议使用小写
- 根据书写形式，html 标签分为双标签和单标签
- 单标签没有标签内容，双标签可以嵌套其它标签和承载文本内容

当我们使用img标签显示图片的时候，需要指定图片的资源路径，比如:

```html
<img src="images/logo.png">
```

这里的src属性就是设置图片的资源路径的，资源路径可以分为**相对路径和绝对路径**。

### 1. 相对路径

> 从当前操作 html 的文档所在目录算起的路径叫做相对路径

**示例代码:**

```html
<!-- 相对路径方式1 -->
<img src="./images/logo.png">
<!-- 相对路径方式2 -->
<img src="images/logo.png">
```

### 2. 绝对路径

> 从根目录算起的路径叫做绝对路径，Windows 的根目录是指定的盘符，mac OS 和Linux 是/

**示例代码:**

```html
<!-- 绝对路径 -->
<img src="/Users/apple/Desktop/demo/hello/images/logo.png">
<img src="C:\demo\images\001.jpg">
```

**提示:**

一般都会使用相对路径，绝对路径的操作在其它电脑上打开会有可能出现资源文件找不到的问题

### 3. 小结

- 相对路径和绝对路径是 html 标签使用资源文件的两种方式，一般使用相对路径。
- 相对路径是从当前操作的 html 文档所在目录算起的路径
- 绝对 路径是从根目录算起的路径

# 列表标签

**学习目标**

- 能够知道列表标签的种类

- 列表标签有无序列表标签(ul标签)和有序列表标签(ol标签)
- 列表项目对顺序有要求的时候使用ol标签
- 列表项目对顺序无要求的时候使用ul标签

# 表格标签

**学习目标**

- 能够知道表格的边线合并

------

### 1. 表格的结构

> 表格是由行和列组成，好比一个excel文件

### 2. 表格标签

- `<table>`标签：表示一个表格
  - `<tr>`标签：表示表格中的一行
    - `<td>`标签：表示表格中的列
    - `<th>`标签：表示表格中的表头

**示例代码:**

```html
<table>
    <tr>
        <th>姓名</th>
        <th>年龄</th>
    </tr>
    <tr>
        <td>张三</td>
        <td>18</td> 
    </tr>
</table>
```

**表格边线合并:**

border-collapse 设置表格的边线合并，如：border-collapse:collapse;

# 表单标签

**学习目标**

- 能够知道表单中常用的表单元素标签

------

### 1. 表单的介绍

> 表单用于搜集不同类型的用户输入(用户输入的数据)，然后可以把用户数据提交到web服务器 。

### 2. 表单相关标签的使用

1. `<form>`标签 表示表单标签，定义整体的表单区域
2. `<label>`标签 表示表单元素的文字标注标签，定义文字标注
3. `<input>`标签 表示表单元素的用户输入标签，定义不同类型的用户输入数据方式
   - type属性
     - type="text" 定义单行文本输入框
     - type="password" 定义密码输入框
     - type="radio" 定义单选框
     - type="checkbox" 定义复选框
     - type="file" 定义上传文件
     - type="submit" 定义提交按钮
     - type="reset" 定义重置按钮
     - type="button" 定义一个普通按钮
4. `<textarea>`标签 表示表单元素的多行文本输入框标签 定义多行文本输入框
5. `<select>`标签 表示表单元素的下拉列表标签 定义下拉列表
   - `<option>`标签 与`<select>`标签配合，定义下拉列表中的选项

**示例代码:**

```html
<form>
    <p>
        <label>姓名：</label><input type="text">
    </p>
    <p>
        <label>密码：</label><input type="password">
    </p>
    <p>
        <label>性别：</label>
        <input type="radio"> 男
        <input type="radio"> 女
    </p>
    <p>
        <label>爱好：</label>
        <input type="checkbox"> 唱歌
        <input type="checkbox"> 跑步
        <input type="checkbox"> 游泳
    </p>
    <p>
        <label>照片：</label>
        <input type="file">
    </p>
    <p>
        <label>个人描述：</label>
        <textarea></textarea>
    </p>
    <p>
        <label>籍贯：</label>
        <select>
            <option>北京</option>
            <option>上海</option>
            <option>广州</option>
            <option>深圳</option>
        </select>
    </p>
    <p>
        <input type="submit" value="提交">
        <input type="reset" value="重置">
    </p>
</form>
```

### 3. 小结

- 表单标签是`<form>`标签
- 常用的表单元素标签有: `<label>`、`<input>`、 `<textarea>`、`<select>` 等标签

# 表单提交

**学习目标**

- 能够知道表单的提交方式
- 能够知道表单中action属性的作用

------

### 1. 表单属性设置

`<form>`标签 表示表单标签，定义整体的表单区域

- action属性 设置表单数据提交地址
- method属性 设置表单提交的方式，一般有“GET”方式和“POST”方式, 不区分大小写

### 2. 表单元素属性设置

- name属性 设置表单元素的名称，该名称是提交数据时的参数名
- value属性 设置表单元素的值，该值是提交数据时参数名所对应的值

### 3. 示例代码

```html
 <form action="https://www.baidu.com" method="GET">
    <p>
        <label>姓名：</label><input type="text" name="username" value="11" />
    </p>
    <p>
        <label>密码：</label><input type="password" name="password" />
    </p>
    <p>
        <label>性别：</label>
        <input type="radio" name="gender" value="0" /> 男
        <input type="radio" name="gender" value="1" /> 女
    </p>
    <p>
        <label>爱好：</label>
        <input type="checkbox" name="like" value="sing" /> 唱歌
        <input type="checkbox" name="like" value="run" /> 跑步
        <input type="checkbox" name="like" value="swiming" /> 游泳
    </p>
    <p>
        <label>照片：</label>
        <input type="file" name="person_pic">
    </p>
    <p>
        <label>个人描述：</label>
        <textarea name="about"></textarea>
    </p>
    <p>
        <label>籍贯：</label>
        <select name="site">
            <option value="0">北京</option>
            <option value="1">上海</option>
            <option value="2">广州</option>
            <option value="3">深圳</option>
        </select>
    </p>
    <p>
        <input type="submit" name="" value="提交">
        <input type="reset" name="" value="重置">
    </p>
</form>
```

### 小结

- 表单标签的作用就是可以把用户输入数据一起提交到web服务器。
- 表单属性设置
  - action: 是设置表单数据提交地址
  - method: 是表单提交方式，提交方式有GET和POST
- 表单元素属性设置
  - name: 表单元素的名称，用于作为提交表单数据时的参数名
  - value: 表单元素的值，用于作为提交表单数据时参数名所对应的值

# css 的介绍

**学习目标**

- 能够知道css的作用

------

### 1. css 的定义

> css(Cascading Style Sheet)层叠样式表，它是用来美化页面的一种语言。

**没有使用css的效果图**

![图片1](imgs/css1.png)

**使用css的效果图**

![图片1](imgs/css2.png)

### 2. css 的作用

1. 美化界面, 比如: 设置标签文字大小、颜色、字体加粗等样式。
2. 控制页面布局, 比如: 设置浮动、定位等样式。

### 3. css 的基本语法

选择器{

样式规则

}

样式规则：

属性名1：属性值1;

属性名2：属性值2;

属性名3：属性值3;

...

选择器:**是用来选择标签的，选出来以后给标签加样式。**

**代码示例:**

```html
div{ 
    width:100px; 
    height:100px; 
    background:gold; 
}
```

**说明**

css 是由两个主要的部分构成：**选择器和一条或多条样式规则**，注意:**样式规则需要放到大括号里面。**

### 4. 小结

- css 是层叠样式表，它是用来美化网页和控制页面布局的。
- 定义 css 的语法格式是: 选择器{样式规则}



# css 的引入方式

**学习目标**

- 能够知道 css 的引入三种方式

------

**css的三种引入方式**

1. 行内式
2. 内嵌式（内部样式）
3. 外链式

### 1. 行内式

> 直接在标签的 style 属性中添加 css 样式

**示例代码:**

```html
<div style="width:100px; height:100px; background:red ">hello</div>
```

优点：方便、直观。 缺点：缺乏可重用性。

### 2. 内嵌式（内部样式）

> 在`<head>`标签内加入`<style>`标签，在`<style>`标签中编写css代码。

**示例代码:**

```html
<head>
   <style type="text/css">
      h3{
         color:red;
      }
   </style>
</head>
```

优点：在同一个页面内部便于复用和维护。 缺点：在多个页面之间的可重用性不够高。

### 3. 外链式

> 将css代码写在一个单独的.css文件中，在`<head>`标签中使用`<link>`标签直接引入该文件到页面中。

**示例代码:**

```html
<link rel="stylesheet" type="text/css" href="css/main.css">
```

优点：使得css样式与html页面分离，便于整个页面系统的规划和维护，可重用性高。 缺点：css代码由于分离到单独的css文件，容易出现css代码过于集中，若维护不当则极容易造成混乱。

### 4. css引入方式选择

1. 行内式几乎不用
2. 内嵌式在学习css样式的阶段使用
3. 外链式在公司开发的阶段使用，可以对 css 样式和 html 页面分别进行开发。

### 5. 小结

- css 的引入有三种方式, 分别是行内式、内嵌式、外链式。
- 外链式是在公司开发的时候会使用，最能体现 div+css 的标签内容与显示样式分离的思想， 也最易改版维护，代码看起来也是最美观的一种。

# css 选择器

**学习目标**

- 能够说出 css 选择器的种类

------

### 1. css 选择器的定义

css 选择器是用来选择标签的，选出来以后给标签加样式。

### 2. css 选择器的种类

1. 标签选择器
2. 类选择器
3. 层级选择器(后代选择器)
4. id选择器
5. 组选择器
6. 伪类选择器

### 3. 标签选择器

根据标签来选择标签，**以标签开头**，此种选择器影响范围大，一般用来做一些通用设置。

**示例代码**

```html
<style type="text/css">
    p{
        color: red;
    }
</style>

<div>hello</div>
<p>hello</p>
```

### 4. 类选择器

根据类名来选择标签，**以 . 开头**, 一个类选择器可应用于多个标签上，一个标签上也可以使用多个类选择器，多个类选择器需要使用空格分割，应用灵活，可复用，是css中应用最多的一种选择器。

**示例代码**

```
<style type="text/css">
    .blue{color:blue}
    .big{font-size:20px}
    .box{width:100px;height:100px;background:gold} 
</style>

<div class="blue">这是一个div</div>
<h3 class="blue big box">这是一个标题</h3>
<p class="blue box">这是一个段落</p>
```

### 5. 层级选择器(后代选择器)

根据层级关系选择后代标签，**以选择器1 选择器2开头**，主要应用在标签嵌套的结构中，减少命名。

**示例代码**

```
<style type="text/css">
    div p{
        color: red;
    }
    .con{width:300px;height:80px;background:green}
    .con span{color:red}
    .con .pink{color:pink}
    .con .gold{color:gold}    
</style>

<div>
    <p>hello</p>
</div>

<div class="con">
    <span>哈哈</span>
    <a href="#" class="pink">百度</a>
    <a href="#" class="gold">谷歌</a>
</div>
<span>你好</span>
<a href="#" class="pink">新浪</a>
```

**注意点: 这个层级关系不一定是父子关系，也有可能是祖孙关系，只要有后代关系都适用于这个层级选择器**

### 6. id选择器

根据id选择标签，以#开头, 元素的id名称不能重复，所以id选择器只能对应于页面上一个元素，不能复用，id名一般给程序使用，所以不推荐使用id作为选择器。

**示例代码**

```
<style type="text/css">
    #box{color:red} 
</style>

<p id="box">这是一个段落标签</p>   <!-- 对应以上一条样式，其它元素不允许应用此样式 -->
<p>这是第二个段落标签</p> <!-- 无法应用以上样式，每个标签只能有唯一的id名 -->
<p>这是第三个段落标签</p> <!-- 无法应用以上样式，每个标签只能有唯一的id名  -->
```

**注意点: 虽然给其它标签设置id=“box”也可以设置样式，但是不推荐这样做，因为id是唯一的，以后js通过id只能获取一个唯一的标签对象。**

### 7. 组选择器

根据组合的选择器选择不同的标签，**以 , 分割开**, 如果有公共的样式设置，可以使用组选择器。

**示例代码**

```
<style type="text/css">
    .box1,.box2,.box3{width:100px;height:100px}
    .box1{background:red}
    .box2{background:pink}
    .box2{background:gold}
</style>

<div class="box1">这是第一个div</div>
<div class="box2">这是第二个div</div>
<div class="box3">这是第三个div</div>
```

### 8. 伪类选择器

用于向选择器添加特殊的效果, **以 : 分割开**, 当用户和网站交互的时候改变显示效果可以使用伪类选择器

**示例代码**

```
<style type="text/css">
    .box1{width:100px;height:100px;background:gold;}
    .box1:hover{width:300px;}
</style>

<div class="box1">这是第一个div</div>
```

### 9. 小结

- css 选择器就是用来选择标签设置样式的
- 常用的 css 选择器有六种，分别是:
  1. 标签选择器
  2. 类选择器
  3. 层级选择器(后代选择器)
  4. id选择器
  5. 组选择器
  6. 伪类选择器

# css 属性

**学习目标**

- 能够知道常用的样式属性

------

我们知道 css 作用是美化 HTML 网页和控制页面布局的,接下来我们来学习一下经常使用一些样式属性。

### 1. 布局常用样式属性

- width 设置元素(标签)的宽度，如：width:100px;
- height 设置元素(标签)的高度，如：height:200px;
- background 设置元素背景色或者背景图片，如：background:gold; 设置元素的背景色, background: url(images/logo.png); 设置元素的背景图片。
- border 设置元素四周的边框，如：border:1px solid black; 设置元素四周边框是1像素宽的黑色实线
- 以上也可以拆分成四个边的写法，分别设置四个边的：
- border-top 设置顶边边框，如：border-top:10px solid red;
- border-left 设置左边边框，如：border-left:10px solid blue;
- border-right 设置右边边框，如：border-right:10px solid green;
- border-bottom 设置底边边框，如：border-bottom:10px solid pink;
- padding 设置元素包含的内容和元素边框的距离，也叫内边距，如padding:20px;padding是同时设置4个边的，也可以像border一样拆分成分别设置四个边:padding-top、padding-left、padding-right、padding-bottom。
- margin 设置元素和外界的距离，也叫外边距，如margin:20px;margin是同时设置4个边的，也可以像border一样拆分成分别设置四个边:margin-top、margin-left、margin-right、margin-bottom。
- float 设置元素浮动，浮动可以让块元素排列在一行，浮动分为左浮动：float:left; 右浮动：float:right;

### 2. 文本常用样式属性

- color 设置文字的颜色，如： color:red;
- font-size 设置文字的大小，如：font-size:12px;
- font-family 设置文字的字体，如：font-family:'微软雅黑';为了避免中文字不兼容，一般写成：font-family:'Microsoft Yahei';
- font-weight 设置文字是否加粗，如：font-weight:bold; 设置加粗 font-weight:normal 设置不加粗
- line-height 设置文字的行高，如：line-height:24px; 表示文字高度加上文字上下的间距是24px，也就是每一行占有的高度是24px
- text-decoration 设置文字的下划线，如：text-decoration:none; 将文字下划线去掉
- text-align 设置文字水平对齐方式，如text-align:center 设置文字水平居中
- text-indent 设置文字首行缩进，如：text-indent:24px; 设置文字首行缩进24px

### 3. 布局常用样式属性示例代码

```html
<style>

    .box1{
        width: 200px; 
        height: 200px; 
        background:yellow; 
        border: 1px solid black;
    }

    .box2{
        /* 这里是注释内容 */
        /* 设置宽度 */
        width: 100px;
        /* 设置高度 */
        height: 100px;
        /* 设置背景色 */
        background: red;
        /* 设置四边边框 */
        /* border: 10px solid black; */
        border-top: 10px solid black;
        border-left: 10px solid black;
        border-right: 10px solid black;
        border-bottom: 10px solid black;
        /* 设置内边距， 内容到边框的距离，如果设置四边是上右下左 */
        /* padding: 10px;   */
        padding-left: 10px;
        padding-top: 10px;
        /* 设置外边距，设置元素边框到外界元素边框的距离 */
        margin: 10px;
        /* margin-top: 10px;
        margin-left: 10px; */
        float: left;
    }

    .box3{
        width: 48px; 
        height: 48px; 
        background:pink; 
        border: 1px solid black;
        float: left;
    }

</style>

<div class="box1">
    <div class="box2">
        padding 设置元素包含的内容和元素边框的距离
    </div>
    <div class="box3">
    </div>
</div>
```

### 4. 文本常用样式属性示例

```html
<style>
    p{
       /* 设置字体大小  浏览器默认是 16px */
       font-size:20px;
       /* 设置字体 */
       font-family: "Microsoft YaHei"; 
       /* 设置字体加粗 */
       font-weight: bold;
       /* 设置字体颜色 */
       color: red;
       /* 增加掉下划线 */
       text-decoration: underline;
       /* 设置行高  */
       line-height: 100px;
       /* 设置背景色 */
       background: green;
       /* 设置文字居中 */
       /* text-align: center; */
       text-indent: 40px;
    }

    a{
        /* 去掉下划线 */
        text-decoration: none;
    }
</style>

<a href="#">连接标签</a>
<p>
    你好，世界!
</p>
```

### 5. 小结

- 设置不同的样式属性会呈现不同网页的显示效果
- 样式属性的表现形式是: **属性名:属性值;**

# css 元素溢出

**学习目标**

- 能够说出元素溢出的解决办法

------

### 1. 什么是 css 元素溢出

当**子元素(标签)的尺寸超过父元素(标签)的尺寸时**，此时需要设置父元素显示溢出的子元素的方式，设置的方法是通过**overflow属性**来完成。

**overflow的设置项：**

1. visible 默认值, 显示子标签溢出部分。
2. hidden 隐藏子标签溢出部分。
3. auto 如果子标签溢出，则可以滚动查看其余的内容。

### 2. 示例代码

```
<style>
    .box1{
        width: 100px;
        height: 200px;
        background: red;
        /* 在父级上设置子元素溢出的部分如何显示 */
        /* overflow: hidden; */
        overflow: auto;
    }
    .box2{
        width: 50px;
        height: 300px;
        background: yellow;
    }
</style>

<div class="box1">
    <div class="box2">hello</div>
</div>
```

### 3. 小结

- overflow样式属性是设置子标签溢出的显示方式
- 常用使用**overflow:hidden;**来解决元素溢出

# css 显示特性

**学习目标**

- 能够说出标签隐藏设置

------

### 1. display 属性的使用

display 属性是用来设置元素的类型及隐藏的，常用的属性有：

- none 元素隐藏且不占位置
- inline 元素以行内元素显示
- block 元素以块元素显示

### 2. 示例代码

```
<style>
    .box{
        /* 将块元素转化为行内元素 */
        display:inline;
    } 

    .link01{
        /* 将行内元素转化为块元素 */
        display:block;
        background: red;

    }

    .con{
        width:200px;
        height:200px;
        background:gold;

        /* 将元素隐藏 */
        display:none;
    }

</style>

<div class="con"></div>
<div class="box">这是第一个div</div>
<div class="box">这是第二个div</div>
<a href="#" class="link01">这是第一个链接</a>
<a href="#" class="link01">这是第二个链接</a>
```

**说明:**

行内元素不能设置宽高， 块元素或者行内块元素可以设置宽高。

### 3. 小结

- 通常隐藏元素使用 `display:none`

# 盒子模型

**学习目标**

- 能够知道盒子模型中的各个属性

------

### 1. 盒子模型的介绍

所谓的盒子模型就是把HTML页面的元素看作一个矩形盒子，矩形盒子是由内容(content)、内边距(padding)、边框(border)、外边距(margin)四部分组成。

**盒子模型示意图如下：**

![图片](imgs/hzmx.png)

### 2. 盒子模型相关样式属性

- 盒子的内容宽度(width)，注意：不是盒子的宽度
- 盒子的内容高度(height)，注意：不是盒子的高度
- 盒子的边框(border)
- 盒子内的内容和边框之间的间距(padding)
- 盒子与盒子之间的间距(margin)

**设置宽高：**

设置盒子的宽高，此宽高是指盒子内容的宽高，不是盒子整体宽高

```
width:200px;  /* 设置盒子的宽度，此宽度是指盒子内容的宽度，不是盒子整体宽度(难点) */ 
height:200px; /* 设置盒子的高度，此高度是指盒子内容的高度，不是盒子整体高度(难点) */
```

**设置边框:**

设置一边的边框，比如顶部边框，可以按如下设置：

```
border-top:10px solid red;
```

说明:

其中10px表示线框的粗细；solid表示线性；red表示边框的颜色

设置其它三个边的方法和上面一样，把上面的'top'换成'left'就是设置左边，换成'right'就是设置右边，换成'bottom'就是设置底边。

四个边如果设置一样，可以将四个边的设置合并成一句：

```
border:10px solid red;
```

**设置内间距padding**

设置盒子四边的内间距，可设置如下：

```
padding-top：20px;     /* 设置顶部内间距20px */ 
padding-left:30px;     /* 设置左边内间距30px */ 
padding-right:40px;    /* 设置右边内间距40px */ 
padding-bottom:50px;   /* 设置底部内间距50px */
```

上面的设置可以简写如下：

```
padding：20px 40px 50px 30px; /* 四个值按照顺时针方向，分别设置的是 上 右 下 左  
四个方向的内边距值。 */
```

padding后面还可以跟3个值，2个值和1个值，它们分别设置的项目如下：

```
padding：20px 40px 50px; /* 设置顶部内边距为20px，左右内边距为40px，底部内边距为50px */ 
padding：20px 40px; /* 设置上下内边距为20px，左右内边距为40px*/ 
padding：20px; /* 设置四边内边距为20px */
```

**设置外间距margin**

外边距的设置方法和padding的设置方法相同，将上面设置项中的'padding'换成'margin'就是外边距设置方法。

**盒子的真实尺寸**

盒子的width和height值固定时，如果盒子增加border和padding，盒子整体的尺寸会变大，所以盒子的真实尺寸为：

- 盒子宽度 = width + padding左右 + border左右
- 盒子高度 = height + padding上下 + border上下

### 小结

- 盒子模型的5个主要样式属性
  - width：内容的宽度(不是盒子的宽度)
  - height：内容的高度(不是盒子的高度)
  - padding：内边距。
  - border：边框。
  - margin：外边距
- 盒子的真实尺寸只会受到宽度、高度、边框、内边距四个属性的影响，不会受到外边距属性的影响。

# JavaScript的介绍

**学习目标**

- 能够知道JavaScript的作用

------

### 1. JavaScript的定义

JavaScript是运行在浏览器端的脚步语言, 是由浏览器解释执行的, 简称js, 它能够让网页和用户有交互功能, 增加良好的用户体验效果。

**前端开发三大块** 1、HTML：负责网页结构 2、CSS：负责网页样式 3、JavaScript：负责网页行为， 比如:网页与用户的交互效果

### 2. 小结

- JavaScript是运行在浏览器端的脚步语言，它的作用就是负责网页和用户的交互效果。

# JavaScript的使用方式

**学习目标**

- 能够知道JavaScript的使用方式

------

### 1. 行内式（主要用于事件）

```html
<input type="button" name="" onclick="alert('ok！');">
```

### 2. 内嵌式

```html
<script type="text/javascript">        
    alert('ok！');
</script>
```

### 3. 外链式

```html
<script type="text/javascript" src="js/index.js"></script>
```

### 4. 小结

- JavaScript的使用方式有三种，分别是:

  - 行内式
  - 内嵌式
  - 外链式

  

# 变量和数据类型

**学习目标**

- 能够说出常用的数据类型

------

### 1. 定义变量

JavaScript 是一种弱类型语言，也就是说不需要指定变量的类型，JavaScript的变量类型由它的值来决定， 定义变量需要用关键字 'var', 一条JavaScript语句应该以“;”结尾

**定义变量的语法格式:**

var 变量名 = 值;

```javascript
 var iNum = 123;
 var sTr = 'asd';

 //同时定义多个变量可以用","隔开，公用一个‘var’关键字

 var iNum = 45,sTr='qwe',sCount='68';
```

### 2. JavaScript注释

JavaScript的注释分为单行注释(//注释内容)和多行注释(/*多行注释*/)

```javascript
<script type="text/javascript">    

// 单行注释
var iNum = 123;
/*  
    多行注释
    1、...
    2、...
*/
var sTr = 'abc123';
</script>
```

### 3. 数据类型

js中有六种数据类型，包括五种基本数据类型和一种复杂数据类型(object)。

5种基本数据类型：
1、number 数字类型
2、string 字符串类型
3、boolean 布尔类型 true 或 false
4、undefined undefined类型，变量声明未初始化，它的值就是undefined
5、null null类型，表示空对象，如果定义的变量将来准备保存对象，可以将变量初始化为null,在页面上获取不到对象，返回的值就是null

1种复合类型：
1、object 后面学习的**数组、函数和JavaScript对象**都属于复合类型

```js
//1.1 数字 number
var iOne = 10.1;

//1.2 字符串 string
var sStr = '1234';

//1.3 布尔 boolean; 
var bIsTrue = false;

//1.4 未定义 undefined
var unData;

//1.5 null 表示空对象
var nullData = null;

//1.6 object 表示对象类型
var oObj = {
   name:"隔壁老王",
   age:88
}
// 获取变量的类型
var type = typeof(oObj);
alert(type);
// 获取对象的name属性
alert(oObj.name);
```

### 4. 变量命名规范

1、区分大小写
2、第一个字符必须是字母、下划线（_）或者美元符号（$）
3、其他字符可以是字母、下划线、美元符或数字

### 5. 匈牙利命名风格

对象o Object 比如：oDiv
数组a Array 比如：aItems
字符串s String 比如：sUserName
整数i Integer 比如：iItemCount
布尔值b Boolean 比如：bIsComplete
浮点数f Float 比如：fPrice
函数fn Function 比如：fnHandler

### 6. 小结

- js中有六种数据类型，分别是:
  - number
  - string
  - boolean
  - undefined
  - null
  - object

# 函数定义和调用

**学习目标**

- 能够写出函数的定义和调用方式

------

### 1. 函数定义

函数就是可以**重复使用的代码块**, 使用关键字 **function** 定义函数。

```javascript
<script type="text/javascript">
    // 函数定义
    function fnAlert(){
        alert('hello!');
    }
</script>
```

### 2. 函数调用

函数调用就是**函数名加小括号**，比如:函数名(参数[参数可选])

```javascript
<script type="text/javascript">
    // 函数定义
    function fnAlert(){
        alert('hello!');
    }
    // 函数调用
    fnAlert();
</script>
```

### 3. 定义有参数有返回值的函数

定义函数时，函数如果有参数，**参数放到小括号里面**，函数如果有返回值，返回值通过 **return** 关键字来返回

```javascript
<script type="text/javascript">
function fnAdd(iNum01,iNum02){
    var iRs = iNum01 + iNum02;
    return iRs;
    alert('here!');
}

var iCount = fnAdd(3,4);
alert(iCount);  //弹出7
</script>
```

**函数中'return'关键字的作用:**
1、返回函数中的值
2、执行完return函数执行结束

### 4. 小结

- 函数的定义

  ```js
    function 函数名(参数[参数可选]){  
        // 函数的代码实现  
        ...  
    }
  ```

- 函数的调用

  ```js
    函数名(参数[参数可选])
  ```

# 变量作用域

**学习目标**

- 能够知道变量的使用范围

------

### 1. 变量作用域的介绍

变量作用域就是变量的使用范围，变量分为:

- 局部变量
- 全局变量

### 2. 局部变量

局部变量就是在函数内使用的变量，只能在函数内部使用。

```javascript
<script type="text/javascript">
    function myalert()
    {
        // 定义局部变量
        var b = 23;
        alert(b);
    }
    myalert(); // 弹出23
    alert(b);  // 函数外使用出错
</script>
```

### 3. 全局变量

全局变量就是在函数外定义的变量，可以在不同函数内使用。

```javascript
<script type="text/javascript">
    // 定义全局变量
    var a = 12;
    function myalert()
    {
        // 修改全局变量
        a++;
    }
    myalert();
    alert(a);  // 弹出13    
</script>
```

### 4. 小结

- 局部变量只能在函数内部使用
- 全局变量可以在不同函数内使用

# 条件语句

**学习目标**

- 能够写出多条件判断的条件语句

------

### 1. 条件语句的介绍

条件语句就是通过条件来控制程序的走向

### 2. 条件语句语法

1. if 语句 - 只有当指定条件为 true 时，使用该语句来执行代码
2. if...else 语句 - 当条件为 true 时执行代码，当条件为 false 时执行其他代码
3. if...else if....else 语句 - 使用该语句来判断多条件，执行条件成立的语句

### 3. 比较运算符

假如 x = 5, 查看比较后的结果:

| 比较运算符 | 描述           | 例子                                |
| :--------- | :------------- | :---------------------------------- |
| ==         | 等于           | x == 8 为 false                     |
| ===        | 全等(值和类型) | x === 5 为 true; x === "5" 为 false |
| !=         | 不等于         | x != 8 为 true                      |
| >          | 大于           | x > 8 为 false                      |
| <          | 小于           | x < 8 为 true                       |
| >=         | 大于或等于     | x >= 8 为 false                     |
| <=         | 小于或等于     | x <= 8 为 true                      |

**比较运算符示例代码:**

```js
var iNum01 = 12;
var sNum01 = '12';

if(iNum01==12){
    alert('相等！');
}
else{
    alert('不相等！')
}

// "==" 符号默认会将符号两边的变量转换成数字再进行对比，这个叫做隐式转换
if(sNum01==12){
    alert('相等！');
}
else{
    alert('不相等！')
}

// "===" 符号不会转换符号两边的数据类型
if(sNum01===12){
    alert('相等！');
}
else{
    alert('不相等！')
}

// 多条件判断
var sFruit = "苹果";
if (sFruit == "苹果") {
    alert("您选择的水果是苹果");
} else if (sFruit == "鸭梨") {
    alert("您选择的水果是鸭梨");
} else {
    alert("对不起，您选择的水果不存在!")
}
```

### 4. 逻辑运算符

假如 x=6, y=3, 查看比较后的结果:

| 比较运算符 | 描述 | 例子                      |
| :--------- | :--- | :------------------------ |
| &&         | and  | (x < 10 && y > 1) 为 true |
| \|\|       | or   | (x==5 \|\| y==5) 为 false |
| !          | not  | !(x==y) 为 true           |

**逻辑运算符示例代码:**

```js
var x = 6;
var y = 3;

if(x < 10 && y > 1){
    alert('都大于');
}
else{
    alert('至少有一个不大于');
}

if(x > 5 || y > 7 ){
    alert('至少有一个大于');
}
else{
    alert('都不大于');
}

if(!(x == y)){
    alert('等于')
}
else{
    alert('不等于')
}
```

### 5. 小结

- 条件语句三种写法
  - if 语句 适用于单条件判断
  - if else 语句 适用于两种条件的判断(成立和不成立条件判断)。
  - if else if else 语句 适用于多条件判断

# 获取标签元素

**学习目标**

- 能够写出获取标签元素的操作

------

### 1. 获取标签元素

可以使用**内置对象 document** 上的 **getElementById 方法**来获取页面上设置了id属性的标签元素，获取到的是一个html对象，然后将它赋值给一个变量，比如：

```js
<script type="text/javascript">
    var oDiv = document.getElementById('div1');
    alert(oDiv);
</script>
<div id="div1">这是一个div元素</div>
```

**说明:**
上面的代码，如果把javascript写在元素的上面，就会出错，因为页面上从上往下加载执行的，javascript去页面上获取元素div1的时候，元素div1还没有加载。

**解决方法有两种:**

第一种方法：将javascript放到页面最下边

```js
<div id="div1">这是一个div元素</div>

<script type="text/javascript">
    var oDiv = document.getElementById('div1');
    alert(oDiv);
</script>
```

第二种方法：设置页面加载完成执行的函数，在执行函数里面获取标签元素。

```js
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementById('div1');
    }
</script>
```

**说明:**
onload是页面所有元素加载完成的事件，给onload设置函数时，当事件触发就会执行设置的函数。

### 2. 小结

- 获取标签元素需要等待页面加载完成，使用**document.getElementById('标签id');**

# 操作标签元素属性

**学习目标**

- 能够知道获取和设置标签元素属性

------

### 1. 属性的操作

首先获取的页面标签元素，然后就可以对页面标签元素的属性进行操作，属性的操作包括:

- 属性的读取
- 属性的设置

**属性名在js中的写法**

1. html的属性和js里面属性大多数写法一样，但是“class” 属性写成 “className”
2. “style” 属性里面的属性，有横杠的改成驼峰式，比如：“font-size”，改成”style.fontSize”

```html
<style>
    .sty01{
        font-size:20px;
        color:red;
    }
    .sty02{
        font-size:30px;
        color:pink;
        text-decoration:none;
    }

</style>

<script type="text/javascript">

    window.onload = function(){
        var oInput = document.getElementById('input1');
        var oA = document.getElementById('link1');
        // 读取属性值
        var sValue = oInput.value;
        var sType = oInput.type;
        var sName = oInput.name;
        var sLinks = oA.href;

        // 操作class属性,需要写成“className”
        oA.className = 'sty02';

        // 写(设置)属性
        oA.style.color = 'red';
        oA.style.fontSize = sValue;
    }

</script>

<input type="text" name="setsize" id="input1" value="20px">
<a href="#" id="link01" class="sty01">这是一个链接</a>
```

### 2. innerHTML

innerHTML可以读取或者设置标签包裹的内容

```html
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementById('div1');
        //读取
        var sTxt = oDiv.innerHTML;
        alert(sTxt);
        //写入
        oDiv.innerHTML = '<a href="http://www.itcast.cn">传智播客<a/>';
    }
</script>


<div id="div1">这是一个div元素</div>
```

### 3. 小结

标签属性的获取和设置:

1. var 标签对象 = document.getElementById('id名称'); -> 获取标签对象
2. var 变量名 = 标签对象.属性名 -> 读取属性
3. 标签对象.属性名 = 新属性值 -> 设置属性

- 数组的定义使用一对中括号
- 获取数组的长度使用length属性
- 从数组最后添加元素使用push方法
- 从数组最后删除元素使用pop方法
- 根据下标添加和删除元素使用splice方法

- js中循环语句有:
  - for
  - while
  - do-while

- **"+"** 运算符能够实现字符串的拼接操作

- 定时器的创建
  - 只执行一次函数的定时器, 对应的代码是setTimeout函数
  - 反复执行函数的定时器, 对应的代码是setInterval函数
- 清除定时器
  - 清除只执行一次函数的定时器, 对应的代码是clearTimeout函数
  - 清除清除反复执行的定时器, 对应的代码是clearInterval函数

### 1. jQuery的定义

jQuery是对JavaScript的封装，它是免费、开源的JavaScript函数库，jQuery 极大地简化了 JavaScript 编程。

### 2. jQuery的作用

jQuery和JavaScript它们的作用一样，都是负责网页行为操作，增加网页和用户的交互效果的，只不过jQuery简化了JavaScript编程，jQuery实现交互效果更简单。

### 3. jQuery的优点

- jQuery兼容了现在主流的浏览器，增加了程序员的开发效率。
- jQuery简化了 JavaScript 编程，代码编写更加简单。

### 4. 小结

- jQuery是一个免费、开源的JavaScript函数库
- jQuery的作用和JavaScript一样，都是负责网页和用户的交互效果。
- jQuery的优点就是兼容主流浏览器，代码编写更加简单。

### 1. jQuery的引入

```js
<script src="js/jquery-1.12.4.min.js"></script>
```

### 3. 小结

- 引入jQuery

- 获取标签元素需要在入口函数来完成，它的速度比原生的 window.onload 更快

- jQuery入口函数有两种写法:

  ```js
    // 完整写法
    $(document).ready(function(){
         ...
    });
  
    // 简化写法
    $(function(){
         ...
    });
  ```

- jQuery选择器就是选择标签的
- 标签选择器是**根据标签名来选择标签**
- 类选择器是**根据类名来选择标签**
- id选择器是**根据id来选择标签**
- 层级选择器是**根据层级关系来选择标签**
- 属性选择器是**根据属性名来选择标签**

- 选择集过滤可以使用has方法和eq方法来完成
- jquery给标签设置样式使用css方法

- prev() 表示获取上一个同级元素
- prevAll() 表示获取上面所有同级元素
- next() 表示获取下一个同级元素
- nextAll() 表示获取下面所有同级元素
- parent() 表示获取父元素
- children() 表示获取所有的子元素
- siblings() 表示获取其它同级元素
- find("选择器名称") 表示获取指定选择器的元素

- 获取和设置元素的内容使用: html方法
- 给指定元素追加html内容使用: append方法

- 获取和设置元素属性的操作可以通过prop方法来完成
- 获取和设置元素的value属性可以通过val方法来完成，更加简单和方便

jQuery常用事件:

- click() 鼠标单击
- blur() 元素失去焦点
- focus() 元素获得焦点
- mouseover() 鼠标进入（进入子元素也触发）
- mouseout() 鼠标离开（离开子元素也触发）
- ready() DOM加载完成

- 事件代理就是使用父元素来代理子元素的事件，好处是减少事件的绑定次数，提高性能。
- 使用场景当多个相同的子元素绑定同一个事件，可以使用事件代理。
- 事件代理使用是使用delegate方法来完成

创建自定义javascript对象有两种方式:

- Object
- 字面量

### 1. json的介绍

json是 JavaScript Object Notation 的首字母缩写，翻译过来就是javascript对象表示法，这里说的json就是**类似于javascript对象的字符串**，它同时是一种**数据格式**，目前这种数据格式比较流行，逐渐替换掉了传统的xml数据格式。

- json就是一个javascript对象表示法，json本质上是一个字符串。
- json有两种格式：1. 对象格式, 2. 数组格式

### 1. ajax的介绍

ajax 是 Asynchronous JavaScript and XML的简写，ajax一个前后台配合的技术，它可以**让 javascript 发送异步的 http 请求，与后台通信进行数据的获取**，ajax 最大的优点是**实现局部刷新**，ajax可以发送http请求，当获取到后台数据的时候更新页面显示数据实现局部刷新，在这里大家只需要记住，**当前端页面想和后台服务器进行数据交互就可以使用ajax了。**

这里提示一下大家, **在html页面使用ajax需要在web服务器环境下运行, 一般向自己的web服务器发送ajax请求。**

**$.get和$.post方法的参数说明:**

$.get(url,data,success(data, status, xhr),dataType).error(func)
$.post(url,data,success(data, status, xhr),dataType).error(func)

1. url 请求地址
2. data 设置发送给服务器的数据，没有参数不需要设置
3. success 设置请求成功后的回调函数
   - data 请求的结果数据
   - status 请求的状态信息, 比如: "success"
   - xhr 底层发送http请求XMLHttpRequest对象
4. dataType 设置返回的数据格式
   - "xml"
   - "html"
   - "text"
   - "json"
5. error 表示错误异常处理
   - func 错误异常回调函数

### 3. 小结

- ajax 是发送http请求获取后台服务器数据的技术
- ajax的简写方式可以使用$.get和$.post方法来完成