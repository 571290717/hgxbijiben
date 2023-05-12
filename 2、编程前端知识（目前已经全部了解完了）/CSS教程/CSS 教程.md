# CSS 教程

[❮ 首页](https://www.w3schools.cn/default.html)[下一节 ❯](https://www.w3schools.cn/css/css_intro.html)

**CSS**

CSS 是一种描述 HTML 文档样式的语言。

CSS 描述应该如何显示 HTML 元素。

本教程将从零起点的基础教程开始，一直到 CSS3 高级教程，为您提供全面系统地讲解。

[现在开始学习 CSS »](https://www.w3schools.cn/css/css_intro.html)

------

## 每章中的实例

本 CSS 教程包含数百个 CSS 实例。

通过使用我们的在线编辑器（w3schools TIY），您可以编辑 CSS，然后单击运行按钮来查看结果。

### CSS 实例

```css
body {
 background-color: lightblue;
}

h1 {
 color: white;
 text-align: center;
}

p {
 font-family: verdana;
 font-size: 20px;
}
```

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_default)

**点击 "亲自试一试" 按钮查看运行结果。**

------

## CSS 实例

从 300 多个实例中学习！使用我们的在线编辑器，您可以编辑 CSS，然后单击运行按钮来查看结果。

[访问 CSS 实例!](https://www.w3schools.cn/css/css_examples.html)

------

## 使用菜单

我们建议按照菜单中列出的顺序阅读本教程。

如果你有一个大屏幕，菜单将始终出现在左边。

如果屏幕很小，请单击顶部的菜单标志打开菜单 ☰.

------

## CSS 模板

我们已经创建了一些响应式 W3.CSS 的模板供您使用。

您可以在所有项目中自由修改、保存、共享和使用它们。

[免费 CSS 模板！](https://www.w3schools.cn/css/css_rwd_templates.html)

------

------

## CSS 习题和测试

在 W3Schools 测试您的 CSS 技能！

[开始 CSS 实验!](https://www.w3schools.cn/css/css_exercises.html)

[开始 CSS 测试!](https://www.w3schools.cn/css/css_quiz.html)

------

## CSS 参考手册

在 W3School，您将找到所有属性和选择器的完整 CSS 参考手册，包括语法、示例、浏览器支持等。

[CSS 属性参考](https://www.w3schools.cn/cssref/default.html)

[CSS 选择器参考](https://www.w3schools.cn/cssref/css_selectors.html)

[CSS 函数参考](https://www.w3schools.cn/cssref/css_functions.html)

[CSS 动画参考](https://www.w3schools.cn/cssref/css_animatable.html)

[CSS 听觉参照](https://www.w3schools.cn/cssref/css_ref_aural.html)

[CSS 样式表单位](https://www.w3schools.cn/cssref/css_units.html)

[CSS 颜色参考](https://www.w3schools.cn/cssref/css_colors.html)

[CSS 默认值](https://www.w3schools.cn/cssref/css_default_values.html)

[CSS 浏览器支持](https://www.w3schools.cn/cssref/css3_browsersupport.html)



# CSS 简介

[❮ 上一节](https://www.w3schools.cn/css/default.html)[下一节 ❯](https://www.w3schools.cn/css/css_syntax.html)

------

## 什么是 CSS?

- **CSS** 指的是层叠样式表* (**C**ascading **S**tyle **S**heets)
- CSS 描述了**如何在屏幕、纸张或其他媒体上显示 HTML 元素**
- CSS **节省了大量工作**。它可以同时控制多张网页的布局
- 外部样式表存储在 **CSS 文件**中

**注释**： 也称级联样式表。

------

## CSS 演示 - 一张 HTML 页面 - 多个样式！

下面是一张提供了四个不同样式表的 HTML 页面。请单击下面的样式表链接，来查看不同的样式：

<iframe src="https://www.w3schools.cn/css/demo_default.htm" style="box-sizing: inherit; width: 803.672px; height: 800px; background: rgb(255, 255, 255); border: none;"></iframe>

------

------

## 为何使用 CSS？

CSS 用于定义网页的样式，包括针对不同设备和屏幕尺寸的设计和布局。

### CSS 实例

```css
body {
 background-color: lightblue;
}

h1 {
 color: white;
 text-align: center;
}

p {
 font-family: verdana;
 font-size: 20px;
}
```

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_default)

------

## CSS 解决了一个大问题

HTML 从未打算包含用于格式化网页的标签！

创建 HTML 的目的是**描述网页**的内容，例如：

```html
<h1>这是一个标题。</h1>
<p>这是一个段落。</p>
```

将 <font> 之类的标签和 color 属性添加到 HTML 3.2 规范后，Web 开发人员的噩梦开始了。大型网站的开发将字体和颜色信息添加到每个页面中，这演变为一个漫长而昂贵的过程。

为了解决这个问题，万维网联盟（W3C）创建了 CSS。

CSS 从 HTML 页面中删除了样式格式！

如果您不知道 HTML 是什么，建议您阅读 [HTML 教程](https://www.w3schools.cn/html/default.html)。

------

## CSS 节省了大量工作！

样式定义通常保存在外部 .css 文件中。

通过使用外部样式表文件，您只需更改一个文件即可更改整个网站的外观！



[❮ 上一节](https://www.w3schools.cn/css/default.html)[下一节 ❯](https://www.w3schools.cn/css/css_syntax.html)



# CSS 语法

[❮ 上一节](https://www.w3schools.cn/css/css_intro.html)[下一节 ❯](https://www.w3schools.cn/css/css_selectors.html)

------

## 语法

CSS 规则集（rule-set）由选择器和声明块组成：

![CSS selector](https://www.w3schools.cn/css/selector.gif)

选择器指向您需要设置样式的 HTML 元素。

声明块包含一条或多条用分号分隔的声明。

每条声明都包含一个 CSS 属性名称和一个值，以冒号分隔。

多条 CSS 声明用分号分隔，声明块用花括号括起来。

### 实例

在此例中，所有 <p> 元素都将居中对齐，并带有红色文本颜色：

```css
p {
 color: red;
 text-align: center;
}
```

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax1)

#### 实例解析

- `p` 是 CSS 中的**选择器**（它指向要设置样式的 HTML 元素：<p>）。
- `color` 是属性，`red` 是属性值
- `text-align` 是属性，`center` 是属性值

在下一章中，您将学到更多关于 CSS 选择器和 CSS 属性的知识。



# CSS 选择器

[❮ 上一节](https://www.w3schools.cn/css/css_syntax.html)[下一节 ❯](https://www.w3schools.cn/css/css_howto.html)

------

## CSS 选择器

CSS 选择器用于"查找"（或选取）要设置样式的 HTML 元素。

我们可以将 CSS 选择器分为五类：

- 简单选择器（根据名称、id、类来选取元素）
- [组合器选择器](https://www.w3schools.cn/css/css_combinators.html)（根据它们之间的特定关系来选取元素）
- [伪类选择器](https://www.w3schools.cn/css/css_pseudo_classes.html)（根据特定状态选取元素）
- [伪元素选择器](https://www.w3schools.cn/css/css_pseudo_elements.html)（选取元素的一部分并设置其样式）
- [属性选择器](https://www.w3schools.cn/css/css_attribute_selectors.html)（根据属性或属性值来选取元素）

此页会讲解最基本的 CSS 选择器。

------

## CSS 元素选择器

元素选择器根据元素名称来选择 HTML 元素。

### 实例

在这里，页面上的所有 <p> 元素都将居中对齐，并带有红色文本颜色：

```css
p {
 text-align: center;
 color: red;
}
```

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax_element)

------

## CSS id 选择器

id 选择器使用 HTML 元素的 id 属性来选择特定元素。

元素的 id 在页面中是唯一的，因此 id 选择器用于选择一个唯一的元素！

要选择具有特定 id 的元素，请写一个井号（＃），后跟该元素的 id。

### 实例

这条 CSS 规则将应用于 id="para1" 的 HTML 元素：

```css
\#para1 {
 text-align: center;
 color: red;
}
```

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax_id)

**注释:** id 名称不能以数字开头。

------

------

## CSS 类选择器

类选择器选择有特定 class 属性的 HTML 元素。

如需选择拥有特定 class 的元素，请写一个句点（.）字符，后面跟类名。

### 实例

在此例中，所有带有 class="center" 的 HTML 元素将为红色且居中对齐：

```css
.center {
 text-align: center;
 color: red;
}
```

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax_class)

您还可以指定只有特定的 HTML 元素会受类的影响。

### 实例

在这个例子中，只有具有 class="center" 的 <p> 元素会居中对齐：

```css
p.center {
 text-align: center;
 color: red;
}
```

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax_element_class)

HTML 元素也可以引用多个类。

### 实例

在这个例子中，<p> 元素将根据 class="center" 和 class="large" 进行样式设置：

<p class="center large">This paragraph refers to two classes.</p>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax_element_class2)

**注释:** 类名不能以数字开头！

------

## CSS 通用选择器

通用选择器（*）选择页面上的所有的 HTML 元素。

### 实例

下面的 CSS 规则会影响页面上的每个 HTML 元素：

```css
\* {
 text-align: center;
 color: blue;
}
```

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax_universal)

------

## CSS 分组选择器

分组选择器选取所有具有相同样式定义的 HTML 元素。

请看下面的 CSS 代码（h1、h2 和 p 元素具有相同的样式定义）：

```css
h1 {
 text-align: center;
 color: red;
}

h2 {
 text-align: center;
 color: red;
}

p {
 text-align: center;
 color: red;
}
```

最好对选择器进行分组，以最大程度地缩减代码。

如需对选择器进行分组，请用逗号来分隔每个选择器。

### 实例

在这个例子中，我们对上述代码中的选择器进行分组：

```css
h1, h2, p {
 text-align: center;
 color: red;
}
```

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grouping)

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_selectors1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_selectors2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_selectors3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_selectors4)

------

## 所有简单的 CSS 选择器

| 选择器                                                       | 实例       | 实例描述                             |
| :----------------------------------------------------------- | :--------- | :----------------------------------- |
| [.*class*](https://www.w3schools.cn/cssref/sel_class.html)   | .intro     | 选取所有 class="intro" 的元素。      |
| [#*id*](https://www.w3schools.cn/cssref/sel_id.html)         | #firstname | 选取 id="firstname" 的那个元素。     |
| [*](https://www.w3schools.cn/cssref/sel_all.html)            | *          | 选取所有元素。                       |
| *[element](https://www.w3schools.cn/cssref/sel_element.html)* | p          | 选取所有 <p> 元素。                  |
| *[element,element,..](https://www.w3schools.cn/cssref/sel_element_comma.html)* | div, p     | 选取所有 <div> 元素和所有 <p> 元素。 |



[❮ 上一节](https://www.w3schools.cn/css/css_syntax.html)[下一节 ❯](https://www.w3schools.cn/css/css_howto.html)



# CSS 如何使用

[❮ 上一节](https://www.w3schools.cn/css/css_selectors.html)[下一节 ❯](https://www.w3schools.cn/css/css_comments.html)

------

当浏览器读到样式表时，它将根据样式表中的信息来格式化 HTML 文档。

------

## 三种使用 CSS 的方法

有三种插入样式表的方法：

- 外部 CSS
- 内部 CSS
- 行内 CSS

------

## 外部 CSS

通过使用外部样式表，您只需修改一个文件即可改变整个网站的外观！

每张 HTML 页面必须在 head 部分的 <link> 元素内包含对外部样式表文件的引用。

### 实例

外部样式在 HTML 页面 <head> 部分内的 <link> 元素中进行定义：

<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="mystyle.css">
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_howto_external)

外部样式表可以在任何文本编辑器中编写，并且必须以 .css 扩展名保存。

外部 .css 文件不应包含任何 HTML 标签。

"mystyle.css" 是这样的：

### "mystyle.css"

body {
 background-color: lightblue;
}

h1 {
 color: navy;
 margin-left: 20px;
}

**注释:** 请勿在属性值和单位之间添加空格（例如 margin-left: 20 px;）。正确的写法是：margin-left: 20px;

------

------

## 内部 CSS

如果一张 HTML 页面拥有唯一的样式，那么可以使用内部样式表。

内部样式是在 head 部分的 <style> 元素中进行定义。

### 实例

内部样式在 HTML 页面的 <head> 部分内的 <style> 元素中进行定义：

<!DOCTYPE html>
<html>
<head>
<style>
body {
 background-color: linen;
}

h1 {
 color: maroon;
 margin-left: 40px;
}
</style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_howto_internal)

------

## 行内 CSS

行内样式（也称内联样式）可用于为单个元素应用唯一的样式。

如需使用行内样式，请将 style 属性添加到相关元素。style 属性可包含任何 CSS 属性。

### 实例

行内样式在相关元素的 "style" 属性中定义：

<!DOCTYPE html>
<html>
<body>

<h1 style="color:blue;text-align:center;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>

</body>
</html>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_howto_inline)

**提示:** 行内样式失去了样式表的许多优点（通过将内容与呈现混合在一起）。请谨慎使用此方法。

------

## 多个样式表

如果在不同样式表中为同一选择器（元素）定义了一些属性，则将使用最后读取的样式表中的值。

假设某个**外部样式表**为 <h1> 元素设定的如下样式：

h1 {
 color: navy;
}

然后，假设某个**内部样式表**也为 <h1> 元素设置了如下样式：

h1 {
 color: orange;  
}

### 实例

如果内部样式是在链接到外部样式表**之后**定义的，则 <h1> 元素将是橙色：

<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
<style>
h1 {
 color: orange;
}
</style>
</head>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_howto_multiple)

### 实例

不过，如果在链接到外部样式表**之前**定义了内部样式，则 <h1> 元素将是深蓝色：

<head>
<style>
h1 {
 color: orange;
}
</style>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_howto_multiple2)

------

## 层叠顺序

当为某个 HTML 元素指定了多个样式时，会使用哪种样式呢？

页面中的所有样式将按照以下规则"层叠"为新的"虚拟"样式表，其中第一优先级最高：

1. 行内样式（在 HTML 元素中）
2. 外部和内部样式表（在 head 部分）
3. 浏览器默认样式

因此，行内样式具有最高优先级，并且将覆盖外部和内部样式以及浏览器默认样式。

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_howto_cascade)

------

## CSS 习题和测验

# CSS 注释

[❮ 上一节](https://www.w3schools.cn/css/css_howto.html)[下一节 ❯](https://www.w3schools.cn/css/css_colors.html)

------

## CSS 注释

注释用于解释代码，以后在您编辑源代码时可能会有所帮助。

浏览器会忽略注释。

位于 元素内的 CSS 注释，以 开始，以 结束：`<style>``/*``*/`

### 实例

/* 这是一条单行注释 */
p {
 color: red;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_comments)

您可以在代码中的任何位置添加注释：

### 实例

p {
 color: red; /* 将文本颜色设置为红色 */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_comments2)

注释能横跨多行：

### 实例

/* 这是 一条多行的 注释 */

p {
 color: red;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_comments3)

------

## HTML 和 CSS 注释

从 HTML 教程中，您学习到可以使用 语法在 HTML 源代码中添加注释。`<!--...-->`

在下面的例子中，我们结合使用了 HTML 和 CSS 注释：

### 实例

<!DOCTYPE html><html><head><style>p {  color: red; /* Set text color to red */}</style></head><body><h2>My Heading</h2><!-- These paragraphs will be red --><p>Hello World!</p><p>This paragraph is styled with CSS.</p><p>CSS comments are not shown in the output.</p></body></html>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_comments4)



# CSS 颜色

[❮ 上一节](https://www.w3schools.cn/css/css_comments.html)[下一节 ❯](https://www.w3schools.cn/css/css_colors_rgb.html)

------

指定颜色是通过使用预定义的颜色名称，或 RGB、HEX、HSL、RGBA、HSLA 值。

------

## CSS 颜色名

在 CSS 中，可以使用颜色名称来指定颜色：

Tomato

Orange

DodgerBlue

MediumSeaGreen

Gray

SlateBlue

Violet

LightGray

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_names)

CSS/HTML 支持 [140 种标准颜色名](https://www.w3schools.cn/colors/colors_names.html)。

------

## CSS 背景色

您可以为 HTML 元素设置背景色：

Hello World




Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.



### 实例

<h1 style="background-color:DodgerBlue;">Hello World</h1>
<p style="background-color:Tomato;">Lorem ipsum...</p>


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_background)

------

## CSS 文本颜色

您可以设置文本的颜色：

### Hello World

Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.

### 实例

<h1 style="color:Tomato;">Hello World</h1>
<p style="color:DodgerBlue;">Lorem ipsum...</p>
<p style="color:MediumSeaGreen;">Ut wisi enim...</p>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_text)

------

## CSS 边框颜色

您可以设置边框的颜色：

## Hello World

## Hello World

## Hello World

### 实例

<h1 style="border:2px solid Tomato;">Hello World</h1>
<h1 style="border:2px solid DodgerBlue;">Hello World</h1>
<h1 style="border:2px solid Violet;">Hello World</h1>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_border)

------

## CSS 颜色值

在 CSS 中，还可以使用 RGB 值、HEX 值、HSL 值、RGBA 值或者 HSLA 值来指定颜色：

与颜色名 "Tomato" 等效：

rgb(255, 99, 71)

\#ff6347

hsl(9, 100%, 64%)

与颜色名 "Tomato" 等效，但是透明度为 50%：

rgba(255, 99, 71, 0.5)

hsla(9, 100%, 64%, 0.5)

### 实例

<h1 style="background-color:rgb(255, 99, 71);">...</h1>
<h1 style="background-color:#ff6347;">...</h1>
<h1 style="background-color:hsl(9, 100%, 64%);">...</h1>

<h1 style="background-color:rgba(255, 99, 71, 0.5);">...</h1>
<h1 style="background-color:hsla(9, 100%, 64%, 0.5);">...</h1>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_values)

了解有关颜色值的更多信息

在下一章中，您将学习有关 [RGB](https://www.w3schools.cn/css/css_colors_rgb.html), [HEX](https://www.w3schools.cn/css/css_colors_hex.html) 和 [HSL](https://www.w3schools.cn/css/css_colors_hsl.html) 的更多知识。



# CSS RGB 颜色

[❮ 上一节](https://www.w3schools.cn/css/css_colors.html)[下一节 ❯](https://www.w3schools.cn/css/css_colors_hex.html)

------

## RGB 值

在 CSS 中，可以使用下面的公式将颜色指定为 RGB 值：

rgb(**red,** **green**, **blue**)

每个参数 (*red*、*green* 以及 *blue*) 定义了 0 到 255 之间的颜色强度。

例如，rgb(255, 0, 0) 显示为红色，因为红色设置为最大值（255），其他设置为 0。

要显示黑色，请将所有颜色参数设置为 0，如下所示：rgb(0, 0, 0)。

要显示白色，请将所有颜色参数设置为 255，如下所示：rgb(255, 255, 255)。

请通过混合以下 RGB 值来进行实验：

rgb(255, 99, 71)

RED

255

GREEN

99

BLUE

71

### 实例

rgb(255, 0, 0)

rgb(0, 0, 255)

rgb(60, 179, 113)

rgb(238, 130, 238)

rgb(255, 165, 0)

rgb(106, 90, 205)


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_rgb2)

通常为所有 3 个光源使用相等的值来定义灰色阴影：

### 实例

rgb(0, 0, 0)

rgb(60, 60, 60)

rgb(120, 120, 120)

rgb(180, 180, 180)

rgb(240, 240, 240)

rgb(255, 255, 255)


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_rgb_gray)

------

## RGBA 值

RGBA 颜色值是具有 alpha 通道的 RGB 颜色值的扩展 - 它指定了颜色的不透明度。

RGBA 颜色值指定为：

rgba(**red,** **green**, **blue, alpha**)

*alpha* 参数是介于 0.0（完全透明）和 1.0（完全不透明）之间的数字：

请通过混合以下 RGBA 值来进行实验：

rgba(255, 99, 71, 0.5)

RED

255

GREEN

99

BLUE

71

ALPHA

0.5

### 实例

rgba(255, 99, 71, 0)

rgba(255, 99, 71, 0.2)

rgba(255, 99, 71, 0.4)

rgba(255, 99, 71, 0.6)

rgba(255, 99, 71, 0.8)

rgba(255, 99, 71, 1)


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_rgba2)



```css
style="color:rgb(0, 0, 0)"
```

# CSS HEX 颜色

[❮ 上一节](https://www.w3schools.cn/css/css_colors_rgb.html)[下一节 ❯](https://www.w3schools.cn/css/css_colors_hsl.html)

------

## HEX 值

在 CSS 中，可以使用以下格式的十六进制值指定颜色：

\#**rrggbb**

其中 rr（红色）、gg（绿色）和 bb（蓝色）是介于 00 和 ff 之间的十六进制值（与十进制 0-255 相同）。

例如，#ff0000 显示为红色，因为红色设置为最大值（ff），其他设置为最小值（00）。

请通过混合以下十六进制值来进行实验：

\#ff6347

RED

ff

GREEN

63

BLUE

47

### 实例

\#ff0000

\#0000ff

\#3cb371

\#ee82ee

\#ffa500

\#6a5acd


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_hex2)

通常为所有 3 个光源使用相等的值来定义灰色阴影：

### 实例

\#000000

\#3c3c3c

\#787878

\#b4b4b4

\#f0f0f0

\#ffffff


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_hex_gray)

# CSS HSL 颜色

[❮ 上一节](https://www.w3schools.cn/css/css_colors_hex.html)[下一节 ❯](https://www.w3schools.cn/css/css_background.html)

------

## HSL 值

在 CSS 中，可以使用色相、饱和度和明度（HSL）来指定颜色，格式如下：

hsl(**hue**, **saturation**, **lightness**)

色相（*hue*）是色轮上从 0 到 360 的度数。0 是红色，120 是绿色，240 是蓝色。

饱和度（*saturation*）是一个百分比值，0％ 表示灰色阴影，而 100％ 是全色。

亮度（*lightness*）也是百分比，0％ 是黑色，50％ 是既不明也不暗，100％是白色。

请通过混合以下 HSL 值来进行实验：

hsl(0, 100%, 50%)

HUE

0

SATURATION

100%

LIGHTNESS

50%

### 实例

hsl(0, 100%, 50%)

hsl(240, 100%, 50%)

hsl(147, 50%, 47%)

hsl(300, 76%, 72%)

hsl(39, 100%, 50%)

hsl(248, 53%, 58%)


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_hsl2)

------

## 饱和度

饱和度可以描述为颜色的强度。

100％ 是纯色，没有灰色阴影

50％ 是 50％ 灰色，但是您仍然可以看到颜色。

0％ 是完全灰色，您无法再看到颜色。

### 实例

hsl(0, 100%, 50%)

hsl(0, 80%, 50%)

hsl(0, 60%, 50%)

hsl(0, 40%, 50%)

hsl(0, 20%, 50%)

hsl(0, 0%, 50%)


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_hsl_saturation)

------

## 亮度

颜色的明暗度可以描述为要赋予颜色多少光，其中 0％ 表示不亮（黑色），50％ 表示 50％ 亮（既不暗也不亮），100％ 表示全明（白）。

### 实例

hsl(0, 100%, 0%)

hsl(0, 100%, 25%)

hsl(0, 100%, 50%)

hsl(0, 100%, 75%)

hsl(0, 100%, 90%)

hsl(0, 100%, 100%)


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_hsl_lightness)

------

通常通过将色调和饱和度设置为 0 来定义灰色阴影，并将亮度从 0％ 到 100％ 进行调整可以得到更深/更浅的阴影：

### 实例

hsl(0, 0%, 0%)

hsl(0, 0%, 24%)

hsl(0, 0%, 47%)

hsl(0, 0%, 71%)

hsl(0, 0%, 94%)

hsl(0, 0%, 100%)


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_hsl_gray)

------

## HSLA 值

HSLA 颜色值是带有 Alpha 通道的 HSL 颜色值的扩展 - 它指定了颜色的不透明度。

HSLA 颜色值指定为：

hsla(**hue,** **saturation**, **lightness, alpha**)

*alpha* 参数是介于 0.0（完全透明）和 1.0（完全不透明）之间的数字：

请通过混合以下 HSLA 值进行实验：

hsla(0, 100%, 50%, 0.5)

HUE

0

SATURATION

100%

LIGHTNESS

50%

ALPHA

0.5

### 实例

hsla(9, 100%, 64%, 0)

hsla(9, 100%, 64%, 0.2)

hsla(9, 100%, 64%, 0.4)

hsla(9, 100%, 64%, 0.6)

hsla(9, 100%, 64%, 0.8)

hsla(9, 100%, 64%, 1)


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_hsla2)

# CSS 背景颜色

[❮ 上一节](https://www.w3schools.cn/css/css_colors_hsl.html)[下一节 ❯](https://www.w3schools.cn/css/css_background_image.html)



CSS 背景属性用于定义元素的背景效果。

在这些章节中，您将学习如下 CSS 背景属性：

- background-color
- background-image
- background-repeat
- background-attachment
- background-position

------

## CSS background-color

`background-color` 属性指定元素的背景色。

### 实例

页面的背景色设置如下：

body {
 background-color: lightblue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-color_body)

通过 CSS，颜色通常由以下方式指定：

- 有效的颜色名称 - 比如 "red"
- 十六进制值 - 比如 "#ff0000"
- RGB 值 - 比如 "rgb(255,0,0)"

请查看 [CSS 颜色值](https://www.w3schools.cn/cssref/css_colors_legal.html)，获取可能颜色值的完整列表。

------

## 其他元素

您可以为任何 HTML 元素设置背景颜色：

### 实例

在这里，<h1>、<p> 和 <div> 元素将拥有不同的背景色：

h1 {
 background-color: green;
}

div {
 background-color: lightblue;
}

p {
 background-color: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-color_elements)

------

## 不透明度 / 透明度

`opacity` 属性指定元素的不透明度/透明度。取值范围为 0.0 - 1.0。值越低，越透明：

opacity 1

opacity 0.6

opacity 0.3

opacity 0.1

### 实例

div {
 background-color: green;
 opacity: 0.3;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background_opacity)

**注释:** 使用 `opacity` 属性为元素的背景添加透明度时，其所有子元素都继承相同的透明度。这可能会使完全透明的元素内的文本难以阅读。

------

## 使用 RGBA 的透明度

如果您不希望对子元素应用不透明度，例如上面的例子，请使用 **RGBA** 颜色值。下面的例子设置背景色而不是文本的不透明度：

100% opacity

60% opacity

30% opacity

10% opacity

您从我们的[CSS 颜色](https://www.w3schools.cn/css/css_colors.html) 章节中学到了可以将 RGB 用作颜色值。除 RGB 外，还可以将 RGB 颜色值与 **alpha** 通道一起使用（RGB**A**） - 该通道指定颜色的不透明度。

RGBA 颜色值指定为：rgba(*red*, *green*, *blue*, *alpha*)。*alpha* 参数是介于 0.0（完全透明）和 1.0（完全不透明）之间的数字。

**提示:** 您可在我们的 [CSS 颜色](https://www.w3schools.cn/css/css3_colors.html) 一章中学到有关 RGBA 颜色的更多知识。

### 实例

div {
 background: rgba(0, 128, 0, 0.3) /* 不透明度为 30% 的绿色背景 */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background_opacity2)

------

# CSS 背景图像

[❮ 上一节](https://www.w3schools.cn/css/css_background.html)[下一节 ❯](https://www.w3schools.cn/css/css_background_repeat.html)

------

## CSS 背景图像

`background-image` 属性指定用作元素背景的图像。

默认情况下，图像会重复，以覆盖整个元素。

### 实例

页面的背景图像可以像这样设置：

body {
 background-image: url("paper.gif");
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image)

### 实例

本例展示了文本和背景图像的**错误组合**。文字难以阅读：

body {
 background-image: url("bgdesert.jpg");
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_bad)

**注释:** 使用背景图像时，请使用不会干扰文本的图像。

------



[❮ 上一节](https://www.w3schools.cn/css/css_background.html)[下一节 ❯](https://www.w3schools.cn/css/css_background_repeat.html)

# CSS 背景重复

[❮ 上一节](https://www.w3schools.cn/css/css_background_image.html)[下一节 ❯](https://www.w3schools.cn/css/css_background_attachment.html)

------

## CSS background-repeat

默认情况下，`background-image` 属性在水平和垂直方向上都重复图像。

某些图像应只适合水平或垂直方向上重复，否则它们看起来会很奇怪，如下所示：

### 实例

body {
 background-image: url("gradient_bg.png");
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_gradient1)

如果上面的图像仅在水平方向重复 (`background-repeat: repeat-x;`)，则背景看起来会更好：

### 实例

body {
 background-image: url("gradient_bg.png");
 background-repeat: repeat-x;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_gradient2)

**提示:** 如需垂直重复图像，请设置 `background-repeat: repeat-y;`

------

## CSS background-repeat: no-repeat

`background-repeat` 属性还可指定只显示一次背景图像：

### 实例

背景图像仅显示一次：

body {
 background-image: url("img_tree.png");
 background-repeat: no-repeat;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_norepeat)

在上例中，背景图像与文本放置在同一位置。我们想要更改图像的位置，以免图像过多干扰文本。

------

## CSS background-position

`background-position` 属性用于指定背景图像的位置。

### 实例

把背景图片放在右上角：

body {
 background-image: url("img_tree.png");
 background-repeat: no-repeat;
 background-position: right top;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_position)

------

# CSS 背景重复

[❮ 上一节](https://www.w3schools.cn/css/css_background_image.html)[下一节 ❯](https://www.w3schools.cn/css/css_background_attachment.html)

------

## CSS background-repeat

默认情况下，`background-image` 属性在水平和垂直方向上都重复图像。

某些图像应只适合水平或垂直方向上重复，否则它们看起来会很奇怪，如下所示：

### 实例

body {
 background-image: url("gradient_bg.png");
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_gradient1)

如果上面的图像仅在水平方向重复 (`background-repeat: repeat-x;`)，则背景看起来会更好：

### 实例

body {
 background-image: url("gradient_bg.png");
 background-repeat: repeat-x;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_gradient2)

**提示:** 如需垂直重复图像，请设置 `background-repeat: repeat-y;`

------

## CSS background-repeat: no-repeat

`background-repeat` 属性还可指定只显示一次背景图像：

### 实例

背景图像仅显示一次：

body {
 background-image: url("img_tree.png");
 background-repeat: no-repeat;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_norepeat)

在上例中，背景图像与文本放置在同一位置。我们想要更改图像的位置，以免图像过多干扰文本。

------

## CSS background-position

`background-position` 属性用于指定背景图像的位置。

### 实例

把背景图片放在右上角：

body {
 background-image: url("img_tree.png");
 background-repeat: no-repeat;
 background-position: right top;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_position)

------





# CSS 背景附着

[❮ 上一节](https://www.w3schools.cn/css/css_background_repeat.html)[下一节 ❯](https://www.w3schools.cn/css/css_background_shorthand.html)

------

## CSS background-attachment

`background-attachment` 属性指定背景图像是应该滚动还是固定的（不会随页面的其余部分一起滚动）：

### 实例

指定应该固定背景图像：

body {
 background-image: url("img_tree.png");
 background-repeat: no-repeat;
 background-position: right top;
 background-attachment: fixed;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_attachment)

### 实例

指定背景图像应随页面的其余部分一起滚动：

body {
 background-image: url("img_tree.png");
 background-repeat: no-repeat;
 background-position: right top;
 background-attachment: scroll;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_attachment2)

# CSS 简写背景

[❮ 上一节](https://www.w3schools.cn/css/css_background_attachment.html)[下一节 ❯](https://www.w3schools.cn/css/css_border.html)

------

## CSS 简写背景

如需缩短代码，也可以在一个属性中指定所有背景属性。它被称为简写属性。

而不是这样写：

body {
 background-color: #ffffff;
 background-image: url("img_tree.png");
 background-repeat: no-repeat;
 background-position: right top;
}

您能够使用简写属性 `background`：

### 实例

使用简写属性在一条声明中设置背景属性：

body {
 background: #ffffff url("img_tree.png") no-repeat right top;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background_shorthand)

在使用简写属性时，属性值的顺序为：

- `background-color`
- `background-image`
- `background-repeat`
- `background-attachment`
- `background-position`

属性值之一缺失并不要紧，只要按照此顺序设置其他值即可。请注意，在上面的例子中，我们没有使用 background-attachment 属性，因为它没有值。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_background1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_background2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_background3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_background4)[测验 5 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_background5)

------

## 所有 CSS 背景属性

| 属性                                                         | 描述                                               |
| :----------------------------------------------------------- | :------------------------------------------------- |
| [background](https://www.w3schools.cn/cssref/css3_pr_background.html) | 在一条声明中设置所有背景属性的简写属性。           |
| [background-attachment](https://www.w3schools.cn/cssref/pr_background-attachment.html) | 设置背景图像是固定的还是与页面的其余部分一起滚动。 |
| [background-clip](https://www.w3schools.cn/cssref/css3_pr_background-clip.html) | 规定背景的绘制区域。                               |
| [background-color](https://www.w3schools.cn/cssref/pr_background-color.html) | 设置元素的背景色。                                 |
| [background-image](https://www.w3schools.cn/cssref/pr_background-image.html) | 设置元素的背景图像。                               |
| [background-origin](https://www.w3schools.cn/cssref/css3_pr_background-origin.html) | 规定在何处放置背景图像。                           |
| [background-position](https://www.w3schools.cn/cssref/pr_background-position.html) | 设置背景图像的开始位置。                           |
| [background-repeat](https://www.w3schools.cn/cssref/pr_background-repeat.html) | 设置背景图像是否及如何重复。                       |
| [background-size](https://www.w3schools.cn/cssref/css3_pr_background-size.html) | 规定背景图像的尺寸。                               |





# CSS 边框

[❮ 上一节](https://www.w3schools.cn/css/css_background_shorthand.html)[下一节 ❯](https://www.w3schools.cn/css/css_border_width.html)

------

## CSS 边框样式

CSS `border` 属性指定要显示的边框类型。

我的所有边都有边框。



我有一条红色的下边框。



我有圆角边框。



我有一条蓝色的左边框。

------

## CSS 边框样式

`border-style` 属性指定要显示的边框类型。

允许以下值：

- dotted - 定义点线边框
- dashed - 定义虚线边框
- solid - 定义实线边框
- double - 定义双边框
- groove - 定义 3D 坡口边框。效果取决于 border-color 值
- ridge - 定义 3D 脊线边框。效果取决于 border-color 值
- inset - 定义 3D inset 边框。效果取决于 border-color 值
- outset - 定义 3D outset 边框。效果取决于 border-color 值
- none - 定义无边框
- hidden - 定义隐藏边框

border-style 属性可以设置一到四个值（用于上边框、右边框、下边框和左边框）。

### 实例

演示不同的边框样式：

p.dotted {border-style: dotted;}
p.dashed {border-style: dashed;}
p.solid {border-style: solid;}
p.double {border-style: double;}
p.groove {border-style: groove;}
p.ridge {border-style: ridge;}
p.inset {border-style: inset;}
p.outset {border-style: outset;}
p.none {border-style: none;}
p.hidden {border-style: hidden;}
p.mix {border-style: dotted dashed solid double;}

结果:

点状边框。

虚线边框。

实线边框。

双线边框。

凹槽边框。其效果取决于 border-color 的值。

垄状边框。其效果取决于 border-color 的值。

3D inset 边框。其效果取决于 border-color 的值。

3D outset 边框。其效果取决于 border-color 的值。

无边框。

隐藏边框。

混合边框。

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-style)

**注释:** 除非设置了 border-style 属性，否则其他 CSS 边框属性（将在下一章中详细讲解）都不会有任何作用！

# CSS 边框宽度

[❮ 上一节](https://www.w3schools.cn/css/css_border.html)[下一节 ❯](https://www.w3schools.cn/css/css_border_color.html)

------

## CSS 边框宽度

border-width 属性指定四个边框的宽度。

可以将宽度设置为特定大小（以 px、pt、cm、em 计），也可以使用以下三个预定义值之一：thin、medium 或 thick：

### 实例

演示不同的边框宽度：

p.one {
 border-style: solid;
 border-width: 5px;
}

p.two {
 border-style: solid;
 border-width: medium;
}

p.three {
 border-style: dotted;
 border-width: 2px;
}

p.four {
 border-style: dotted;
 border-width: thick;
}

结果:

5px border-width

medium border-width

2px border-width

thick border-width

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-width)

------

## 特定边的宽度

border-width 属性可以设置一到四个值（用于上边框、右边框、下边框和左边框）：

### 实例

p.one {
 border-style: solid;
 border-width: 5px 20px; /* 上边框和下边框为 5px，其他边为 20px */
}

p.two {
 border-style: solid;
 border-width: 20px 5px; /* 上边框和下边框为 20px，其他边为 5px */
}

p.three {
 border-style: solid;
 border-width: 25px 10px 4px 35px; /* 上边框 25px，右边框 10px，下边框 4px，左边框 35px */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-width2)

# CSS 边框颜色

[❮ 上一节](https://www.w3schools.cn/css/css_border_width.html)[下一节 ❯](https://www.w3schools.cn/css/css_border_sides.html)

------

## CSS 边框颜色

border-color 属性用于设置四个边框的颜色。

可以通过以下方式设置颜色：

- name - 指定颜色名，比如 "red"
- HEX - 指定十六进制值，比如 "#ff0000"
- RGB - 指定 RGB 值，比如 "rgb(255,0,0)"
- HSL - 指定 HSL 值，比如 "hsl(0, 100%, 50%)"
- transparent

**注释:** 如果未设置 `border-color` ，则它将继承元素的颜色。

### 实例

演示不同的边框颜色：

p.one {
 border-style: solid;
 border-color: red;
}

p.two {
 border-style: solid;
 border-color: green;
}

p.three {
 border-style: dotted;
 border-color: blue;
}

结果:

红色实线边框

绿色实线边框

蓝色点状边框

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-color1)

------

## 特定边框的颜色

border-color 属性可以设置一到四个值（用于上边框、右边框、下边框和左边框）。

### 实例

p.one {
 border-style: solid;
 border-color: red green blue yellow; /* 上红、右绿、下蓝、左黄 */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-color2)

------

## HEX 值

边框的颜色也可以使用十六进制值（HEX）来指定：

### 实例

p.one {
 border-style: solid;
 border-color: #ff0000; /* red */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-color-hex)

------

## RGB 值

或者使用 RGB 值：

### 实例

p.one {
 border-style: solid;
 border-color: rgb(255, 0, 0); /* red */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-color-rgb)

------

## HSL 值

也可以使用 HSL 值：

### 实例

p.one {
 border-style: solid;
 border-color: hsl(0, 100%, 50%); /* red */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-color-hsl)

您可以在我们的 [CSS 颜色](https://www.w3schools.cn/css/css_colors.html) 章节中学到有关 HEX、RGB 和 HSL 值的更多知识。





# CSS 边框各边

[❮ 上一节](https://www.w3schools.cn/css/css_border_color.html)[下一节 ❯](https://www.w3schools.cn/css/css_border_shorthand.html)

------

## CSS 边框 - 单独的边

从上一章的例子中，您已经看到可以为每一侧指定不同的边框。

在 CSS 中，还有一些属性可用于指定每个边框（顶部、右侧、底部和左侧）：

### 实例

p {
 border-top-style: dotted;
 border-right-style: solid;
 border-bottom-style: dotted;
 border-left-style: solid;
}

结果:

不同的边框样式

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-side)

上例的结果与此相同：

### 实例

p {
 border-style: dotted solid;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-side2)

### 它的工作原理是这样的：

如果 border-style 属性设置四个值：

- 上边框是虚线
- 右边框是实线
- 下边框是双线
- 左边框是虚线

如果 border-style 属性设置三个值：

- 上边框是虚线
- 右和左边框是实线
- 下边框是双线

如果 border-style 属性设置两个值：

- 上和下边框是虚线
- 右和左边框是实线

如果 border-style 属性设置一个值：

- 四条边均为虚线

### 实例

/* 四个值 */
p {
 border-style: dotted solid double dashed;
}

/* 三个值 */
p {
 border-style: dotted solid double;
}

/* 两个值 */
p {
 border-style: dotted solid;
}

/* 一个值 */
p {
 border-style: dotted;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-side3)

上例中使用的是 border-style 属性。但 border-width 和 border-color 也同样适用。

# CSS 简写边框属性

[❮ 上一节](https://www.w3schools.cn/css/css_border_sides.html)[下一节 ❯](https://www.w3schools.cn/css/css_border_rounded.html)

------

## CSS Border - 简写属性

就像您在上一章中所见，处理边框时要考虑许多属性。

为了缩减代码，也可以在一个属性中指定所有单独的边框属性。

`border` 属性是以下各个边框属性的简写属性：

- `border-width`
- `border-style`（必需）
- `border-color`

### 实例

p {
 border: 5px solid red;
}

结果:

Some text

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border)

您还可以只为一个边指定所有单个边框属性：

### 左边框

p {
 border-left: 6px solid red;
 background-color: lightgrey;
}

结果:

Some text

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border_left)

### 下边框

p {
 border-bottom: 6px solid red;
 background-color: lightgrey;
}

结果:

Some text

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border_bottom)





# CSS 圆角边框

[❮ 上一节](https://www.w3schools.cn/css/css_border_shorthand.html)[下一节 ❯](https://www.w3schools.cn/css/css_margin.html)

------

## CSS 圆角边框

border-radius 属性用于向元素添加圆角边框：

普通边框

圆角边框

圆角边框

圆角边框

### 实例

p {
 border: 2px solid red;
 border-radius: 5px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border_round)

------

## 更多实例

[一个声明中的所有上边框属性](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-top)
本例演示简写属性，用于在一条声明中设置上边框的所有属性。

[设置下边框的样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-bottom-style)
本例演示如何设置下边框的样式。

[设置左边框的宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-left-width)
本例演示如何设置左边框的宽度。

[设置四条边框的颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-color)
本例演示如何设置四条边框的颜色。它可以拥有一到四

[设置右边框的颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-right-color)
本例演示如何设置右边框的颜

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_border1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_border2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_border3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_border4)

------

## 所有 CSS 边框属性

| 属性                                                         | 描述                                                  |
| :----------------------------------------------------------- | :---------------------------------------------------- |
| [border](https://www.w3schools.cn/cssref/pr_border.html)     | 简写属性，在一条声明中设置所有边框属性。              |
| [border-bottom](https://www.w3schools.cn/cssref/pr_border-bottom.html) | 简写属性，在一条声明中设置所有下边框属性。            |
| [border-bottom-color](https://www.w3schools.cn/cssref/pr_border-bottom_color.html) | 设置下边框的颜色。                                    |
| [border-bottom-style](https://www.w3schools.cn/cssref/pr_border-bottom_style.html) | 设置下边框的样式。                                    |
| [border-bottom-width](https://www.w3schools.cn/cssref/pr_border-bottom_width.html) | 设置下边框的宽度。                                    |
| [border-color](https://www.w3schools.cn/cssref/pr_border-color.html) | 简写属性，设置四条边框的颜色。                        |
| [border-left](https://www.w3schools.cn/cssref/pr_border-left.html) | 简写属性，在一条声明中设置所有左边框属性。            |
| [border-left-color](https://www.w3schools.cn/cssref/pr_border-left_color.html) | 设置左边框的颜色。                                    |
| [border-left-style](https://www.w3schools.cn/cssref/pr_border-left_style.html) | 设置左边框的样式。                                    |
| [border-left-width](https://www.w3schools.cn/cssref/pr_border-left_width.html) | 设置左边框的宽度。                                    |
| [border-radius](https://www.w3schools.cn/cssref/css3_pr_border-radius.html) | 简写属性，可设置圆角的所有四个 border-*-radius 属性。 |
| [border-right](https://www.w3schools.cn/cssref/pr_border-right.html) | 简写属性，在一条声明中设置所有右边框属性。            |
| [border-right-color](https://www.w3schools.cn/cssref/pr_border-right_color.html) | 设置右边框的颜色。                                    |
| [border-right-style](https://www.w3schools.cn/cssref/pr_border-right_style.html) | 设置右边框的样式。                                    |
| [border-right-width](https://www.w3schools.cn/cssref/pr_border-right_width.html) | 设置右边框的宽度。                                    |
| [border-style](https://www.w3schools.cn/cssref/pr_border-style.html) | 简写属性，设置四条边框的样式。                        |
| [border-top](https://www.w3schools.cn/cssref/pr_border-top.html) | 简写属性，在一条声明中设置所有上边框属性。            |
| [border-top-color](https://www.w3schools.cn/cssref/pr_border-top_color.html) | 设置上边框的颜色。                                    |
| [border-top-style](https://www.w3schools.cn/cssref/pr_border-top_style.html) | 设置上边框的样式。                                    |
| [border-top-width](https://www.w3schools.cn/cssref/pr_border-top_width.html) | 设置上边框的宽度。                                    |
| [border-width](https://www.w3schools.cn/cssref/pr_border-width.html) | 简写属性，设置四条边框的宽度。                        |





# CSS 外边距

[❮ 上一节](https://www.w3schools.cn/css/css_border_rounded.html)[下一节 ❯](https://www.w3schools.cn/css/css_margin_collapse.html)

------

此元素的外边距为 70px。

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_intro)

------

## CSS 外边距

CSS margin 属性用于在任何定义的边框之外，为元素周围创建空间。

通过 CSS，您可以完全控制外边距。有一些属性可用于设置元素每侧（上、右、下和左）的外边距。

![img](https://www.w3schools.cn/css/css_margin.png)

------

## Margin - 单独的边

CSS 拥有用于为元素的每一侧指定外边距的属性：

- `margin-top`
- `margin-right`
- `margin-bottom`
- `margin-left`

所有外边距属性都可以设置以下值：

- auto - 浏览器来计算外边距
- *length* - 以 px、pt、cm 等单位指定外边距
- % - 指定以包含元素宽度的百分比计的外边距
- inherit - 指定应从父元素继承外边距

**提示:** 允许负值。

### 实例

为 <p> 元素的所有四个边设置不同的外边距：

p {
 margin-top: 100px;
 margin-bottom: 100px;
 margin-right: 150px;
 margin-left: 80px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_sides)

------

------

## Margin - 简写属性

为了缩减代码，可以在一个属性中指定所有外边距属性。

`margin` 属性是以下各外边距属性的简写属性：

- `margin-top`
- `margin-right`
- `margin-bottom`
- `margin-left`

### 工作原理是这样的：

如果 margin 属性有四个值：

- margin: 25px 50px 75px 100px;

- - 上外边距是 25px
  - 右外边距是 50px
  - 下外边距是 75px
  - 左外边距是 100px

### 实例

margin 简写属性设置四个值：

p {
 margin: 25px 50px 75px 100px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_shorthand_4val)

如果 margin 属性设置三个值：

- margin: 25px 50px 75px;

- - 上外边距是 25px
  - 右和左外边距是 50px
  - 下外边距是 75px

### 实例

使用已设置三个值的 margin 简写属性：

p {
 margin: 25px 50px 75px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_shorthand_3val)

如果 margin 属性设置两个值：

- margin: 25px 50px;

- - 上和下外边距是 25px
  - 右和左外边距是 50px

### 实例

使用设置了两个值的 margin 简写属性：

p {
 margin: 25px 50px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_shorthand_2val)

如果 `margin` 属性设置了一个值：

- margin: 25px;

- - 所有四个外边距都是 25px

### 实例

使用设置一个值的 margin 简写属性：

p {
 margin: 25px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_shorthand_1val)

------

## auto 值

您可以将 margin 属性设置为 auto，以使元素在其容器中水平居中。

然后，该元素将占据指定的宽度，并且剩余空间将在左右边界之间平均分配。

### 实例

使用 margin: auto:

div {
 width: 300px;
 margin: auto;
 border: 1px solid red;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_auto)

------

## inherit 值

本例使 <p class="ex1"> 元素的左外边距继承自父元素（<div>）：

### 实例

使用 inherit 值：

div {
 border: 1px solid red;
 margin-left: 100px;
}

p.ex1 {
 margin-left: inherit;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin-left_inherit)





# CSS 外边距合并

[❮ 上一节](https://www.w3schools.cn/css/css_margin.html)[下一节 ❯](https://www.w3schools.cn/css/css_padding.html)

------

## 外边距合并

外边距合并指的是，当两个垂直外边距相遇时，它们将形成一个外边距。

合并后的外边距的高度等于两个发生合并的外边距的高度中的较大者。

请看以下示例：

### 实例

演示外边距合并:

h1 {
 margin: 0 0 50px 0;
}

h2 {
 margin: 20px 0 0 0;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_collapse)

在上面的例子中， <h1> 元素的下边距为50px， <h2> 元素的上边距设置为20px。

常识似乎表明， <h1> 和 <h2> 之间的垂直边距总计为 70px （50px+20px）。 但由于外边距合并，实际间距为 50px.

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_margin1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_margin2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_margin3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_margin4)

------

## 所有 CSS 外边距属性

| 属性                                                         | 描述                                       |
| :----------------------------------------------------------- | :----------------------------------------- |
| [margin](https://www.w3schools.cn/cssref/pr_margin.html)     | 用于在一条声明中设置外边距属性的简写属性。 |
| [margin-bottom](https://www.w3schools.cn/cssref/pr_margin-bottom.html) | 设置元素的下外边距。                       |
| [margin-left](https://www.w3schools.cn/cssref/pr_margin-left.html) | 设置元素的左外边距。                       |
| [margin-right](https://www.w3schools.cn/cssref/pr_margin-right.html) | 设置元素的右外边距。                       |
| [margin-top](https://www.w3schools.cn/cssref/pr_margin-top.html) | 设置元素的上外边距。                       |



# CSS 内边距

[❮ 上一节](https://www.w3schools.cn/css/css_margin_collapse.html)[下一节 ❯](https://www.w3schools.cn/css/css_dimension.html)

------

此元素的内边距为 70px。


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_intro)

------

## CSS 内边距

CSS padding 属性用于在任何定义的边界内的元素内容周围生成空间。

通过 CSS，您可以完全控制内边距（填充）。有一些属性可以为元素的每一侧（上、右、下和左侧）设置内边距。

------

## Padding - 单独的边

CSS 拥有用于为元素的每一侧指定内边距的属性：

- `padding-top`
- `padding-right`
- `padding-bottom`
- `padding-left`

所有内边距属性都可以设置以下值：

- *length* - 以 px、pt、cm 等单位指定内边距
- % - 指定以包含元素宽度的百分比计的内边距
- inherit - 指定应从父元素继承内边距

**注释:** 不允许负值。

### 实例

为 <div> 元素的所有四个边设置不同的内边距：

div {
 padding-top: 50px;
 padding-right: 30px;
 padding-bottom: 50px;
 padding-left: 80px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_sides)

------

------

## Padding - 简写属性

为了缩减代码，可以在一个属性中指定所有内边距属性。

`padding` 属性是以下各内边距属性的简写属性：

- `padding-top`
- `padding-right`
- `padding-bottom`
- `padding-left`

### 工作原理是这样的：

如果 padding 属性有四个值：

- padding: 25px 50px 75px 100px;
  - 上内边距是 25px
  - 右内边距是 50px
  - 下内边距是 75px
  - 左内边距是 100px

### 实例

使用设置了四个值的 padding 简写属性：

div {
 padding: 25px 50px 75px 100px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_shorthand_4val)

如果 padding 属性设置了三个值：

- padding: 25px 50px 75px;
  - 上内边距是 25px
  - right and left paddings are 50px
  - 下内边距是 75px

### 实例

使用设置了三个值的 padding 简写属性：

div {
 padding: 25px 50px 75px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_shorthand_3val)

如果 padding 属性设置了两个值：

- padding: 25px 50px;

- - 上和下内边距是 25px
  - 右和左内边距是 50px

### 实例

使用设置了两个值的 padding 简写属性：

div {
 padding: 25px 50px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_shorthand_2val)

如果 padding 属性设置了一个值：

- padding: 25px;

- - 所有四个内边距都是 25px

### 实例

使用设置了一个值的 padding 简写属性：

div {
 padding: 25px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_shorthand_1val)

------

## 内边距和元素宽度

CSS width 属性指定元素内容区域的宽度。内容区域是元素（盒模型）的内边距、边框和外边距内的部分。

因此，如果元素拥有指定的宽度，则添加到该元素的内边距会添加到元素的总宽度中。这通常是不希望的结果。

### 实例

在这里，<div> 元素的宽度为 300px。但是，<div> 元素的实际宽度将是 350px（300px + 左内边距 25px + 右内边距 25px）：

div {
 width: 300px;
 padding: 25px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_width)

若要将宽度保持为 300px，无论填充量如何，那么您可以使用 box-sizing 属性。这将导致元素保持其宽度。如果增加内边距，则可用的内容空间会减少。

### 实例

使用 box-sizing 属性将宽度保持为 300px，无论填充量如何：

div {
 width: 300px;
 padding: 25px;
 box-sizing: border-box;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_width2)

------

## 更多实例

[设置左内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding-left)
本例演示如何设置 <p> 元素的左内边距

[设置右内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding-right)
本例演示如何设置 <p> 元素的右内边距。

[设置上内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding-top)
本例演示如何设置 <p> 元素的上内边距。

[设置下内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding-bottom)
本例演示如何设置 <p> 元素的下内边距

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_padding1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_padding2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_padding3)

------

## 所有 CSS 内边距属性

| 属性                                                         | 描述                                           |
| :----------------------------------------------------------- | :--------------------------------------------- |
| [padding](https://www.w3schools.cn/cssref/pr_padding.html)   | 用于在一条声明中设置所有内边距属性的简写属性。 |
| [padding-bottom](https://www.w3schools.cn/cssref/pr_padding-bottom.html) | 设置元素的下内边距。                           |
| [padding-left](https://www.w3schools.cn/cssref/pr_padding-left.html) | 设置元素的左内边距。                           |
| [padding-right](https://www.w3schools.cn/cssref/pr_padding-right.html) | 设置元素的右内边距。                           |
| [padding-top](https://www.w3schools.cn/cssref/pr_padding-top.html) | 设置元素的上内边距。                           |



# CSS 高度和宽度

[❮ 上一节](https://www.w3schools.cn/css/css_padding.html)[下一节 ❯](https://www.w3schools.cn/css/css_boxmodel.html)

------

此元素的宽度为 100％。


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_height_width_intro)

------

## CSS 设置高度和宽度

height 和 width 属性用于设置元素的高度和宽度。

height 和 width 属性不包括内边距、边框或外边距。它设置的是元素内边距、边框以及外边距内的区域的高度或宽度。

------

## CSS 高度和宽度值

height 和 width 属性可设置如下值：

- auto - 默认。浏览器计算高度和宽度。
- *length* - 以 px、cm 等定义高度/宽度。
- % - 以包含块的百分比定义高度/宽度。
- initial - 将高度/宽度设置为默认值。
- inherit - 从其父值继承高度/宽度。

------

## CSS 高度和宽度实例

此元素的高度为 200 像素，宽度为 50％

### 实例

设置 <div> 元素的高度和宽度：

div {
 height: 200px;
 width: 50%;
 background-color: powderblue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_height_width2)

此元素的高度为 100 像素，宽度为 500 像素。

### 实例

设置另一个 <div> 元素的高度和宽度：

div {
 height: 100px;
 width: 500px;
 background-color: powderblue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_height_width)

**注释:** 请记住，height 和 width 属性不包括内边距、边框或外边距！它们设置的是元素的内边距、边框和外边距内的区域的高度/宽度！

------

------

## 设置 max-width

max-width 属性用于设置元素的最大宽度。

可以用长度值（例如 px、cm 等）或包含块的百分比（％）来指定 max-width（最大宽度），也可以将其设置为 none（默认值。意味着没有最大宽度）。

当浏览器窗口小于元素的宽度（500px）时，会发生之前那个 <div> 的问题。然后，浏览器会将水平滚动条添加到页面。

在这种情况下，使用 max-width 能够改善浏览器对小窗口的处理。

提示：将浏览器窗口拖动到小于500px的宽度，以查看两个 div 之间的区别！

此元素的高度为 100 像素，最大宽度为 500 像素。

此元素的高度为 100 像素，最大宽度为 500 像素。

注释：`max-width` 属性的值将覆盖 `width`（宽度）。

### 实例

这个 <div> 元素的高度为 100 像素，最大宽度为 500 像素：

div {
 max-width: 500px;
 height: 100px;
 background-color: powderblue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_max_width)

------

## 更多实例

[设置元素的高度和宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_height)
本例演示如何设置不同元素的高度和宽度。

[使用百分比设置图像的高度和宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_height_percent)
本例演示如何使用百分比值设置图像的高度和宽度。

[设置元素的最小宽度和最大宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_max-width)
本例演示如何使用像素值设置元素的最小宽度和最大宽度。

[设置元素的最小高度和最大高度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_max-height)
本例演示如何使用像素值设置元素的最小高度和最大高度。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_dimension1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_dimension2)

------

## 设置 CSS 尺寸属性

| 属性                                                         | 描述                 |
| :----------------------------------------------------------- | :------------------- |
| [height](https://www.w3schools.cn/cssref/pr_dim_height.html) | 设置元素的高度。     |
| [max-height](https://www.w3schools.cn/cssref/pr_dim_max-height.html) | 设置元素的最大高度。 |
| [max-width](https://www.w3schools.cn/cssref/pr_dim_max-width.html) | 设置元素的最大宽度。 |
| [min-height](https://www.w3schools.cn/cssref/pr_dim_min-height.html) | 设置元素的最小高度。 |
| [min-width](https://www.w3schools.cn/cssref/pr_dim_min-width.html) | 设置元素的最小宽度。 |
| [width](https://www.w3schools.cn/cssref/pr_dim_width.html)   | 设置元素的宽度。     |

# CSS 盒子模型

[❮ 上一节](https://www.w3schools.cn/css/css_dimension.html)[下一节 ❯](https://www.w3schools.cn/css/css_outline.html)

------

## CSS 盒子模型

所有 HTML 元素都可以视为方框。在 CSS 中，在谈论设计和布局时，会使用术语"盒模型"或"框模型"。

CSS 框模型实质上是一个包围每个 HTML 元素的框。它包括：外边距、边框、内边距以及实际的内容。下图展示了框模型：

对不同部分的说明：

- **Content** - 框的内容，其中显示文本和图像。
- **Padding** - 清除内容周围的区域。内边距是透明的。
- **Border** - 围绕内边距和内容的边框。
- **Margin** - 清除边界外的区域。外边距是透明的。

框模型允许我们在元素周围添加边框，并定义元素之间的空间。

### 实例

盒子模型的演示：

div {
 width: 300px;
 border: 15px solid green;
 padding: 50px;
 margin: 20px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_boxmodel)

------

------

## 元素的宽度和高度

为了在所有浏览器中正确设置元素的宽度和高度，您需要了解框模型如何工作。

**重要事项:** 使用 CSS 设置元素的 width 和 height 属性时，只需设置内容区域的宽度和高度。要计算元素的完整大小，还必须把内边距、边框和外边距加起来。

### 实例

<div> 元素的总宽度将是 350px：

div {
 width: 320px;
 padding: 10px;
 border: 5px solid gray;
 margin: 0;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_boxmodel_width)

计算如下：

320px(宽度) + 20px（左+右内边距） + 10px（左+右边框） + 0px（左+右外边距） **= 350px**

元素的总宽度应该这样计算：

元素总宽度 = 宽度 + 左内边距 + 右内边距 + 左边框 + 右边框 + 左外边距 + 右外边距

元素的总高度应该这样计算：

元素总高度 = 高度 + 上内边距 + 下内边距 + 上边框 + 下边框 + 上外边距 + 下外边距

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_boxmodel1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_boxmodel2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_boxmodel3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_boxmodel4)

------

# CSS 轮廓

[❮ 上一节](https://www.w3schools.cn/css/css_boxmodel.html)[下一节 ❯](https://www.w3schools.cn/css/css_outline_width.html)

------

此元素拥有黑色边框和蓝色轮廓，宽度为 10px


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline_intro)

------

## CSS 轮廓

轮廓是在元素周围绘制的一条线，在边框之外，以凸显元素。

CSS 拥有如下轮廓属性：

- `outline-style`
- `outline-color`
- `outline-width`
- `outline-offset`
- `outline`

**注释:** 轮廓与 [边框](https://www.w3schools.cn/css/css_border.html) 不同！不同之处在于：轮廓是在元素边框之外绘制的，并且可能与其他内容重叠。同样，轮廓也不是元素尺寸的一部分；元素的总宽度和高度不受轮廓线宽度的影响。

------

## CSS 轮廓样式

`outline-style` 属性指定轮廓的样式，并可设置如下值：

- dotted - 定义点状的轮廓。
- dashed - 定义虚线的轮廓。
- solid - 定义实线的轮廓。
- double - 定义双线的轮廓。
- groove - 定义 3D 凹槽轮廓。
- ridge - 定义 3D 凸槽轮廓。
- inset - 定义 3D 凹边轮廓。
- outset - 定义 3D 凸边轮廓。
- none - 定义无轮廓。
- hidden - 定义隐藏的轮廓。

下例展示了不同的 `outline-style` 值：

### 实例

演示不同的轮廓样式：

p.dotted {outline-style: dotted;}
p.dashed {outline-style: dashed;}
p.solid {outline-style: solid;}
p.double {outline-style: double;}
p.groove {outline-style: groove;}
p.ridge {outline-style: ridge;}
p.inset {outline-style: inset;}
p.outset {outline-style: outset;}

结果:

点状轮廓。

虚线轮廓。

实线轮廓。

双线轮廓。

3D 凹槽轮廓。此效果取决于 outline-color 值。

3D 凸槽轮廓。此效果取决于 outline-color 值。

3D 凹边轮廓。此效果取决于 outline-color 值。

3D 凸边轮廓。此效果取决于 outline-color 值。

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-style)

**注释:** 除非设置了 `outline-style` 属性，否则其他轮廓属性（在下一章中将详细介绍）都不会有任何作用！





# CSS 轮廓宽度

[❮ 上一节](https://www.w3schools.cn/css/css_outline.html)[下一节 ❯](https://www.w3schools.cn/css/css_outline_color.html)

------

## CSS 轮廓宽度

outline-width 属性指定轮廓的宽度，并可设置如下值之一：

- thin（通常为 1px）
- medium（通常为 3px）
- thick （通常为 5px）
- 特定尺寸（以 px、pt、cm、em 计）

下例展示了一些不同宽度的轮廓：

细的轮廓。

中等的轮廓。

粗的轮廓。

4 像素的粗轮廓。

### 实例

p.ex1 {
 border: 1px solid black;
 outline-style: solid;
 outline-color: red;
 outline-width: thin;
}

p.ex2 {
 border: 1px solid black;
 outline-style: solid;
 outline-color: red;
 outline-width: medium;
}

p.ex3 {
 border: 1px solid black;
 outline-style: solid;
 outline-color: red;
 outline-width: thick;
}

p.ex4 {
 border: 1px solid black;
 outline-style: solid;
 outline-color: red;
 outline-width: 4px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-width)



[❮ 上一节](https://www.w3schools.cn/css/css_outline.html)[下一节 ❯](https://www.w3schools.cn/css/css_outline_color.html)



# CSS 轮廓颜色

[❮ 上一节](https://www.w3schools.cn/css/css_outline_width.html)[下一节 ❯](https://www.w3schools.cn/css/css_outline_shorthand.html)

------

## CSS 轮廓颜色

outline-color 属性用于设置轮廓的颜色。

可以通过以下方式设置颜色：

- *name* - 指定颜色名，比如 "red"
- HEX - 指定十六进制值，比如 "#ff0000"
- RGB - 指定 RGB 值，比如 "rgb(255,0,0)"
- HSL - 指定 HSL 值，比如 "hsl(0, 100%, 50%)"
- invert - 执行颜色反转（确保轮廓可见，无论是什么颜色背景）

下例展示了一些不同颜色的不同轮廓样式。请注意，这些元素在轮廓内还有黑色细边框：

红色的实线轮廓。

蓝色的点状轮廓。

灰色的凸边轮廓。

### 实例

p.ex1 {
 border: 2px solid black;
 outline-style: solid;
 outline-color: red;
}

p.ex2 {
 border: 2px solid black;
 outline-style: dotted;
 outline-color: blue;
}

p.ex3 {
 border: 2px solid black;
 outline-style: outset;
 outline-color: grey;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-color)

------

## HEX 值

您也可以使用十六进制值（HEX）指定轮廓颜色：

### 实例

p.ex1 {
 outline-style: solid;
 outline-color: #ff0000; /* red */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-color-hex)

------

## RGB 值

或者通过使用 RGB 值：

### 实例

p.ex1 {
 outline-style: solid;
 outline-color: rgb(255, 0, 0); /* red */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-color-rgb)

------

## HSL 值

您还可以使用 HSL 值：

### 实例

p.ex1 {
 outline-style: solid;
 outline-color: hsl(0, 100%, 50%); /* red */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-color-hsl)

您可以在我们的 [CSS 颜色](https://www.w3schools.cn/css/css_colors.html) 章节中学习有关 HEX、RGB 和 HSL 值的更多知识。

------

## 反转颜色

下例使用 outline-color: invert，执行了颜色反转。这样可以确保无论颜色背景如何，轮廓都是可见的：

反转颜色的实线轮廓。

### 实例

p.ex1 {
 border: 1px solid yellow;
 outline-style: solid;
 outline-color: invert;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-color_invert)



# CSS 轮廓简写属性

[❮ 上一节](https://www.w3schools.cn/css/css_outline_color.html)[下一节 ❯](https://www.w3schools.cn/css/css_outline_offset.html)

------

## CSS Outline - 简写属性

outline 属性是用于设置以下各个轮廓属性的简写属性：

- outline-width
- outline-style（必需）
- outline-color

从上面的列表中，outline 属性可指定一个、两个或三个值。值的顺序无关紧要。

下例展示了用简写的 `outline` 属性指定的一些轮廓：

虚线轮廓。

红色的虚线轮廓。

5 像素的黄色实线轮廓。

粗的粉色凸槽轮廓。

### 实例

p.ex1 {outline: dashed;}
p.ex2 {outline: dotted red;}
p.ex3 {outline: 5px solid yellow;}
p.ex4 {outline: thick ridge pink;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline)



[❮ 上一节](https://www.w3schools.cn/css/css_outline_color.html)[下一节 ❯](https://www.w3schools.cn/css/css_outline_offset.html)





# CSS 轮廓偏移

[❮ 上一节](https://www.w3schools.cn/css/css_outline_shorthand.html)[下一节 ❯](https://www.w3schools.cn/css/css_text.html)

------

## CSS 轮廓偏移

outline-offset 属性在元素的轮廓与边框之间添加空间。元素及其轮廓之间的空间是透明的。

下例指定边框边缘外 15px 的轮廓：

此段落的边框外有 15px 的轮廓。

### 实例

p {
 margin: 30px;
 border: 1px solid black;
 outline: 1px solid red;
 outline-offset: 15px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-offset)

下例显示元素与其轮廓之间的空间是透明的：

本段在边框边缘外的轮廓为 15px。

### 实例

p {
 margin: 30px;
 background: yellow;
 border: 1px solid black;
 outline: 1px solid red;
 outline-offset: 15px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-offset2)

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_outline1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_outline2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_outline3)

------

## 所有 CSS 轮廓属性

| 属性                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [outline](https://www.w3schools.cn/cssref/pr_outline.html)   | 简写属性，在一条声明中设置 outline-width、outline-style 以及 outline-color。 |
| [outline-color](https://www.w3schools.cn/cssref/pr_outline-color.html) | 设置轮廓的颜色。                                             |
| [outline-offset](https://www.w3schools.cn/cssref/css3_pr_outline-offset.html) | 指定轮廓与元素的边缘或边框之间的空间。                       |
| [outline-style](https://www.w3schools.cn/cssref/pr_outline-style.html) | 设置轮廓的样式。                                             |
| [outline-width](https://www.w3schools.cn/cssref/pr_outline-width.html) | 设置轮廓的宽度。                                             |



[❮ 上一节](https://www.w3schools.cn/css/css_outline_shorthand.html)[下一节 ❯](https://www.w3schools.cn/css/css_text.html)





# CSS 文本

[❮ 上一节](https://www.w3schools.cn/css/css_outline_offset.html)[下一节 ❯](https://www.w3schools.cn/css/css_text_align.html)



# 文本格式

此文本使用某些文本格式属性设置样式。标题使用文本对齐、文本转换和颜色属性。 段落缩进、对齐，并指定字符之间的间距。下划线已从此彩色[“自己尝试”](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text)链接中删除。


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text)

------

## 文本颜色

color 属性用于设置文本的颜色。颜色由以下值指定：

- 颜色名 - 比如 “red”
- 十六进制值 - 比如 “#ff0000”
- RGB 值 - 比如 “rgb（255，0，0）”

查看 CSS 颜色值，以获取可能[颜色值](https://www.w3schools.cn/cssref/css_colors_legal.html)的完整列表。

页面的默认文本颜色是在 body 选择器中定义的。

### 实例

body {
 color: blue;
}

h1 {
 color: green;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color)

**注释：**对于符合 W3C 标准的 CSS： 如果您定义了 color 属性，则还必须定义 background-color 属性。

------

## 文本颜色和背景色

在本例中，我们定义了 background-color 属性和 color 属性：

### 实例

body {
 background-color: lightgrey;
 color: blue;
}

h1 {
 background-color: black;
 color: white;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_bg)

------



[❮ 上一节](https://www.w3schools.cn/css/css_outline_offset.html)[下一节 ❯](https://www.w3schools.cn/css/css_text_align.html)



# CSS 文本

[❮ 上一节](https://www.w3schools.cn/css/css_outline_offset.html)[下一节 ❯](https://www.w3schools.cn/css/css_text_align.html)



# 文本格式

此文本使用某些文本格式属性设置样式。标题使用文本对齐、文本转换和颜色属性。 段落缩进、对齐，并指定字符之间的间距。下划线已从此彩色[“自己尝试”](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text)链接中删除。


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text)

------

## 文本颜色

color 属性用于设置文本的颜色。颜色由以下值指定：

- 颜色名 - 比如 “red”
- 十六进制值 - 比如 “#ff0000”
- RGB 值 - 比如 “rgb（255，0，0）”

查看 CSS 颜色值，以获取可能[颜色值](https://www.w3schools.cn/cssref/css_colors_legal.html)的完整列表。

页面的默认文本颜色是在 body 选择器中定义的。

### 实例

body {
 color: blue;
}

h1 {
 color: green;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color)

**注释：**对于符合 W3C 标准的 CSS： 如果您定义了 color 属性，则还必须定义 background-color 属性。

------

## 文本颜色和背景色

在本例中，我们定义了 background-color 属性和 color 属性：

### 实例

body {
 background-color: lightgrey;
 color: blue;
}

h1 {
 background-color: black;
 color: white;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_bg)

------



[❮ 上一节](https://www.w3schools.cn/css/css_outline_offset.html)[下一节 ❯](https://www.w3schools.cn/css/css_text_align.html)

# CSS 文本修饰

[❮ 上一节](https://www.w3schools.cn/css/css_text_align.html)[下一节 ❯](https://www.w3schools.cn/css/css_text_transformation.html)

------

## 文本修饰

text-decoration 属性用于设置或删除文本装饰。

text-decoration: none; 通常用于从链接上删除下划线：

### 实例

a {
 text-decoration: none;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text-decoration_link)

其他 text-decoration 值用于装饰文本：

### 实例

h1 {
 text-decoration: overline;
}

h2 {
 text-decoration: line-through;
}

h3 {
 text-decoration: underline;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text-decoration)

**注释:** 建议不要在非链接文本加下划线，因为这经常会使读者感到困惑。

------



[❮ 上一节](https://www.w3schools.cn/css/css_text_align.html)[下一节 ❯](https://www.w3schools.cn/css/css_text_transformation.html)



# CSS 文本修饰

[❮ 上一节](https://www.w3schools.cn/css/css_text_align.html)[下一节 ❯](https://www.w3schools.cn/css/css_text_transformation.html)

------

## 文本修饰

text-decoration 属性用于设置或删除文本装饰。

text-decoration: none; 通常用于从链接上删除下划线：

### 实例

a {
 text-decoration: none;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text-decoration_link)

其他 text-decoration 值用于装饰文本：

### 实例

h1 {
 text-decoration: overline;
}

h2 {
 text-decoration: line-through;
}

h3 {
 text-decoration: underline;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text-decoration)

**注释:** 建议不要在非链接文本加下划线，因为这经常会使读者感到困惑。

------



[❮ 上一节](https://www.w3schools.cn/css/css_text_align.html)[下一节 ❯](https://www.w3schools.cn/css/css_text_transformation.html)

# CSS 文本间距

[❮ 上一节](https://www.w3schools.cn/css/css_text_transformation.html)[下一节 ❯](https://www.w3schools.cn/css/css_text_shadow.html)

------

## 文字缩进

text-indent 属性用于指定文本第一行的缩进：

### 实例

p {
 text-indent: 50px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text-indent)

------

## 字母间距

letter-spacing 属性用于指定文本中字符之间的间距。

下例演示如何增加或减少字符之间的间距：

### 实例

h1 {
 letter-spacing: 3px;
}

h2 {
 letter-spacing: -3px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_letter-spacing)

------

## 行高

line-height 属性用于指定行之间的间距：

### 实例

p.small {
 line-height: 0.8;
}

p.big {
 line-height: 1.8;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_line-height)

------

## 字间距

word-spacing 属性用于指定文本中单词之间的间距。

下例演示如何增加或减少单词之间的间距：

### 实例

h1 {
 word-spacing: 10px;
}

h2 {
 word-spacing: -5px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text_word-spacing)

------

## 空白

white-space 属性指定元素内部空白的处理方式。

此例演示如何禁用元素内的文本换行：

### 实例

p {
 white-space: nowrap;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text_white-space)

# CSS 文本阴影

[❮ 上一节](https://www.w3schools.cn/css/css_text_spacing.html)[下一节 ❯](https://www.w3schools.cn/css/css_font.html)

------

## 文本阴影

text-shadow 属性为文本添加阴影。

最简单的用法是只指定水平阴影（2px）和垂直阴影（2px）：

## 文字阴影效果!

### 实例

h1 {
 text-shadow: 2px 2px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow1)

接下来，向阴影添加颜色（红色）：

## 文字阴影效果！实例h1 {  text-shadow: 2px 2px red; }[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow2)然后，向阴影添加模糊效果（5px）：

## 文字阴影效果！

### 实例

h1 {
 text-shadow: 2px 2px 5px red;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow3)

**提示:** 请访问 [CSS 字体](https://www.w3schools.cn/css/css_font.html) 一章，学习如何更改字体、文本大小和文本样式。

**提示:** 请访问 [CSS 文本效果](https://www.w3schools.cn/css/css3_text_effects.html) 一章，学习如何实现不同的文本效果。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_text1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_text2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_text3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_text4)[测验 5 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_text5)

------

## 所有 CSS 文本属性

| 属性                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [color](https://www.w3schools.cn/cssref/pr_text_color.html)  | 设置文本颜色。                                               |
| [direction](https://www.w3schools.cn/cssref/pr_text_direction.html) | 指定文本的方向 / 书写方向。                                  |
| [letter-spacing](https://www.w3schools.cn/cssref/pr_text_letter-spacing.html) | 设置字符间距。                                               |
| [line-height](https://www.w3schools.cn/cssref/pr_dim_line-height.html) | 设置行高。                                                   |
| [text-align](https://www.w3schools.cn/cssref/pr_text_text-align.html) | 指定文本的水平对齐方式。                                     |
| [text-decoration](https://www.w3schools.cn/cssref/pr_text_text-decoration.html) | 指定添加到文本的装饰效果。                                   |
| [text-indent](https://www.w3schools.cn/cssref/pr_text_text-indent.html) | 指定文本块中首行的缩进。                                     |
| [text-shadow](https://www.w3schools.cn/cssref/css3_pr_text-shadow.html) | 指定添加到文本的阴影效果。                                   |
| [text-transform](https://www.w3schools.cn/cssref/pr_text_text-transform.html) | 控制文本的大小写。                                           |
| [text-overflow](https://www.w3schools.cn/cssref/css3_pr_text-overflow.html) | 指定应如何向用户示意未显示的溢出内容。                       |
| [unicode-bidi](https://www.w3schools.cn/cssref/pr_text_unicode-bidi.html) | 与 [direction](https://www.w3schools.cn/cssref/pr_text_direction.html) 属性一起使用，设置或返回是否应重写文本来支持同一文档中的多种语言。 |
| [vertical-align](https://www.w3schools.cn/cssref/pr_pos_vertical-align.html) | 指定文本的垂直对齐方式。                                     |
| [white-space](https://www.w3schools.cn/cssref/pr_text_white-space.html) | 指定如何处理元素内的空白。                                   |
| [word-spacing](https://www.w3schools.cn/cssref/pr_text_word-spacing.html) | 设置单词间距。                                               |



# CSS 字体

[❮ 上一节](https://www.w3schools.cn/css/css_text_shadow.html)[下一节 ❯](https://www.w3schools.cn/css/css_font_style.html)

------

CSS 字体属性定义字体系列、粗体、大小和文本样式。为您的网站选择正确的字体很重要！

------

## 字体选择很重要

选择正确的字体会对网站的用户体验产生巨大影响。

正确的字体可以为您的品牌创造强有力的形象。

使用易于阅读的字体很重要。字体为您的文本增加了价值。为字体选择正确的颜色和文本大小也很重要。

------

## Serif 和 Sans-serif 字体之间的区别

![Serif vs. Sans-serif](https://www.w3schools.cn/css/serif.gif)

------

## CSS 字体系列

在 CSS 中，有两种类型的字体系列：

- **通用系列** - 一组外观相似的字体系列 (如 "Serif" 或 "Monospace")
- **font family** - 特定的字体系列 (如 "Times New Roman" 或 "Arial")

| 通用字体族 | 字体名称实例               | 描述                                                         |
| :--------- | :------------------------- | :----------------------------------------------------------- |
| Serif      | Times New Roman Georgia    | 衬线字体（Serif）- 在每个字母的边缘都有一个小的笔触。它们营造出一种形式感和优雅感。 |
| Sans-serif | Arial Verdana              | 无衬线字体（Sans-serif）- 字体线条简洁（没有小笔画）。它们营造出现代而简约的外观。 |
| Monospace  | Courier New Lucida Console | 等宽字体（Monospace）- 这里所有字母都有相同的固定宽度。它们创造出机械式的外观。 |

**注释:** 在计算机屏幕上，无衬线字体被认为比衬线字体更易于阅读。

------

## Font Family 属性

文本的字体族是使用 `font-family` 属性设置的。

`font-family` 属性应包含多个字体名称作为"后备"系统，以确保浏览器/操作系统之间的最大兼容性。

请以您需要的字体开始，并以通用系列结束（如果没有其他可用字体，则让浏览器选择通用系列中的相似字体）。字体名称应以逗号分隔。

**注释：** 如果字体名称不止一个单词，则必须用引号引起来，例如： "Times New Roman".

在逗号分隔的列表中指定了多个字体系列：

### 实例

为三个段落规定不同的字体：

.serif {
 font-family: "Times New Roman", Times, serif;
}

.sansserif {
 font-family: Arial, Helvetica, sans-serif;
}

.monospace {
 font-family: "Lucida Console", Courier, monospace;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-family)

### 实例

指定段落 "Impact" 字体：

p.impact {
 font-family: Impact, Charcoal, sans-serif;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-family2)

对于常用的字体组合，请查看我们的 [Web 安全字体](https://www.w3schools.cn/cssref/css_websafe_fonts.html)。



# CSS 字体样式

[❮ 上一节](https://www.w3schools.cn/css/css_font.html)[下一节 ❯](https://www.w3schools.cn/css/css_font_size.html)

------

## 字体样式

font-style 属性主要用于指定斜体文本。

此属性可设置三个值：

- normal - 文字正常显示
- italic - 文本以斜体显示
- oblique - 文本为"倾斜"（倾斜与斜体非常相似，但支持较少）

### 实例

p.normal {
 font-style: normal;
}

p.italic {
 font-style: italic;
}

p.oblique {
 font-style: oblique;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-style)

------

## 字体粗细

font-weight 属性指定字体的粗细：

### 实例

p.normal {
 font-weight: normal;
}

p.thick {
 font-weight: bold;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-weight)

------

## 字体变体

font-variant 属性指定是否以 small-caps 字体（小型大写字母）显示文本。

在 small-caps 字体中，所有小写字母都将转换为大写字母。但是，转换后的大写字母的字体大小小于文本中原始大写字母的字体大小。

### 实例

p.normal {
 font-variant: normal;
}

p.small {
 font-variant: small-caps;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-variant)

------



[❮ 上一节](https://www.w3schools.cn/css/css_font.html)[下一节 ❯](https://www.w3schools.cn/css/css_font_size.html)





[报告错误](javascript:void(0);)

[打印](javascript:void(0);)

[关于](https://www.w3schools.cn/about/default.html)

[学习路线](https://www.w3schools.cn/about/about_learnpath.html)



# CSS 字体大小

[❮ 上一节](https://www.w3schools.cn/css/css_font_style.html)[下一节 ❯](https://www.w3schools.cn/css/css_font_google.html)

------

## 字体大小

font-size 属性设置文本的大小。

在网页设计中，能够管理文本大小很重要。但是，不应使用调整字体大小来使段落看起来像标题，或是使标题看起来像段落。

请始终使用正确的 HTML 标签，例如 <h1> - <h6> 用于标题，而 <p> 仅用于段落。

font-size 值可以是绝对或相对大小。

绝对尺寸：

- 将文本设置为指定大小
- 不允许用户在所有浏览器中更改文本大小（可访问性不佳）
- 当输出的物理尺寸已知时，绝对尺寸很有用

相对尺寸：

- 设置相对于周围元素的大小
- 允许用户在浏览器中更改文本大小

**注释:** 如果您没有指定字体大小，则普通文本（如段落）的默认大小为 16px（16px = 1em）。

------

## 以像素设置字体大小

使用像素设置文本大小可以完全控制文本大小：

### 实例

h1 {
 font-size: 40px;
}

h2 {
 font-size: 30px;
}

p {
 font-size: 14px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-size_px)

**提示:** 如果您使用了像素，则仍然可以使用缩放工具来调整整个页面的大小。

------

## 用 em 设置字体大小

为了允许用户调整文本大小（在浏览器菜单中），许多开发人员使用 em 而不是像素。

W3C 建议使用 em 尺寸单位。

1em 等于当前字体大小。浏览器中的默认文本大小为 16px。因此，默认大小 1em 为 16px。

可以使用这个公式从像素到 em 来计算大小：pixels/16=em。

### 实例

h1 {
 font-size: 2.5em; /* 40px/16=2.5em */
}

h2 {
 font-size: 1.875em; /* 30px/16=1.875em */
}

p {
 font-size: 0.875em; /* 14px/16=0.875em */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-size_em)

在上例中，em 单位的文本大小与上一个例子中的像素大小相同。但是，若使用 em 尺寸，则可以在所有浏览器中调整文本大小。

不幸的是，旧版本的 Internet Explorer 仍然存在问题。放大文本时它比应该大的尺寸更大，缩小文本时会更小。

------

## 使用百分比和 Em 的组合

适用于所有浏览器的解决方案是为 <body> 元素设置默认字体大小（以百分比为单位）:

### 实例

body {
 font-size: 100%;
}

h1 {
 font-size: 2.5em;
}

h2 {
 font-size: 1.875em;
}

p {
 font-size: 0.875em;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-size_percent_em)

我们的代码目前运行良好！它在所有浏览器中显示相同的文本大小，并允许所有浏览器缩放或调整文本大小！

------

## 响应式字体大小

可以使用 vw 单位设置文本大小，它的意思是"视口宽度"（"viewport width"）。

这样，文本大小将遵循浏览器窗口的大小，请调整浏览器窗口的大小，以查看字体大小如何缩放：

# Hello World

调整浏览器窗口大小以查看字体大小如何缩放。

### 实例

<h1 style="**font-size:10vw**">Hello World</h1>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font_responsive)

视口（Viewport）是浏览器窗口的大小。 1vw = 视口宽度的 1％。如果视口为 50 厘米宽，则 1vw 为 0.5 厘米。



# CSS 谷歌字体

[❮ 上一节](https://www.w3schools.cn/css/css_font_size.html)[下一节 ❯](https://www.w3schools.cn/css/css_font_shorthand.html)

------

## 谷歌字体

如果您不想使用 HTML 中的任何标准字体，则可以使用 Google Fonts API 向页面添加数百种其他字体。

只需添加一个样式表链接并引用您选择的字体系列：

### 实例

<!DOCTYPE html>
<html>
<head>
**<link rel="stylesheet" href="/fonts/css.asp?family=Sofia">**
<style>
body {
 **font-family: "Sofia";**
 font-size: 22px;
}
</style>
</head>
<body>

<h1>Sofia Font</h1>
<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</p>

</body>
</html>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-google)

如需所有可用的 Google 字体列表，请访问我们的 [如何使用 Google 字体 教程](https://www.w3schools.cn/howto/howto_google_fonts.html)。

------



[❮ 上一节](https://www.w3schools.cn/css/css_font_size.html)[下一节 ❯](https://www.w3schools.cn/css/css_font_shorthand.html)





[报告错误](javascript:void(0);)

[打印](javascript:void(0);)

[关于](https://www.w3schools.cn/about/default.html)

[学习路线](https://www.w3schools.cn/about/about_learnpath.html)



# CSS 字体属性

[❮ 上一节](https://www.w3schools.cn/css/css_font_google.html)[下一节 ❯](https://www.w3schools.cn/css/css_icons.html)

------

## 字体属性

为了缩短代码，也可以在一个属性中指定所有单个字体属性。

font 属性是以下属性的简写属性：

- `font-style`
- `font-variant`
- `font-weight`
- `font-size/line-height`
- `font-family`

### 实例

使用简写声明设置一些字体属性：

p.a {
 font: 20px Arial, sans-serif;
}

p.b {
 font: italic small-caps bold 12px/30px Georgia, serif;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font)

**注释:** >font-size 和 font-family 的值是必需的。如果缺少其他值之一，则会使用其默认值。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_font1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_font2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_font3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_font4)[测验 5 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_font5)

------

## 所有 CSS 字体属性

| 属性                                                         | 描述                                     |
| :----------------------------------------------------------- | :--------------------------------------- |
| [font](https://www.w3schools.cn/cssref/pr_font_font.html)    | 简写属性。在一条声明中设置所有字体属性。 |
| [font-family](https://www.w3schools.cn/cssref/pr_font_font-family.html) | 规定文本的字体系列（字体族）。           |
| [font-size](https://www.w3schools.cn/cssref/pr_font_font-size.html) | 规定文本的字体大小。                     |
| [font-style](https://www.w3schools.cn/cssref/pr_font_font-style.html) | 规定文本的字体样式。                     |
| [font-variant](https://www.w3schools.cn/cssref/pr_font_font-variant.html) | 规定是否以小型大写字母的字体显示文本。   |
| [font-weight](https://www.w3schools.cn/cssref/pr_font_weight.html) | 规定字体的粗细。                         |



# CSS 图标

[❮ 上一节](https://www.w3schools.cn/css/css_font_shorthand.html)[下一节 ❯](https://www.w3schools.cn/css/css_link.html)

------

 

 

 

------

## 如何添加图标

向 HTML 页面添加图标的最简单方法是使用图标库，比如 Font Awesome。

将指定的图标类的名称添加到任何行内 HTML 元素（如 <i> 或 <span>）。

下面的图标库中的所有图标都是可缩放矢量，可以使用 CSS进行自定义（大小、颜色、阴影等）。

------

## Font Awesome 图标

如需使用 Font Awesome 图标，请访问 fontawesome.com，登录并获取代码添加到 HTML 页面的 <head> 部分：

```
<script src="https://kit.fontawesome.com/yourcode.js"></script>
```

请在我们的 Font Awesome 5 教程中，阅读有关如何开始使用 [Font Awesome](https://www.w3schools.cn/icons/fontawesome5_intro.html) 的更多内容。

**注释：** 无需下载或安装！

### 实例

<!DOCTYPE html><html><head><script src="https://kit.fontawesome.com/a076d05399.js"></script></head><body><i class="fas fa-cloud"></i><i class="fas fa-heart"></i><i class="fas fa-car"></i><i class="fas fa-file"></i><i class="fas fa-bars"></i></body></html>

结果:

  

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_icons_fa)

有关所有 Font Awesome 图标的完整参考，请访问我们的 [Icon 图标参考](https://www.w3schools.cn/icons/icons_reference.html)。

------

------

## Bootstrap 图标

如需使用 Bootstrap glyphicons，请在 HTML 页面的 <head> 部分内添加这行：

```
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
```

**注释：** 无需下载或安装！

### 实例

<!DOCTYPE html><html><head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"></head><body><i class="glyphicon glyphicon-cloud"></i><i class="glyphicon glyphicon-remove"></i><i class="glyphicon glyphicon-user"></i><i class="glyphicon glyphicon-envelope"></i><i class="glyphicon glyphicon-thumbs-up"></i></body></html>

结果:

<iframe src="https://www.w3schools.cn/css/trycss_icons_bs_ifr.htm" style="box-sizing: inherit; width: 837.984px; border: none; height: 25px; overflow: hidden; padding-top: 5px;"></iframe>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_icons_bs)

------

## Google 图标

如需使用 Google 图标，请在HTML页面的 <head> 部分中添加以下行：

```
<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
```

**注释:** 无需下载或安装！

### 实例

<!DOCTYPE html><html><head><link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons"></head><body><i class="material-icons">cloud</i><i class="material-icons">favorite</i><i class="material-icons">attachment</i><i class="material-icons">computer</i><i class="material-icons">traffic</i></body></html>

结果:

<iframe src="https://www.w3schools.cn/css/trycss_icons_google_ifr.htm" style="box-sizing: inherit; width: 869.984px; border: none; height: 50px; overflow: hidden; padding-left: 6px; padding-top: 6px;"></iframe>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_icons_google)

有关所有图标的完整列表，请访问我们的 [Icon 教程](https://www.w3schools.cn/icons/default.html)。



[❮ 上一节](https://www.w3schools.cn/css/css_font_shorthand.html)[下一节 ❯](https://www.w3schools.cn/css/css_link.html)





[报告错误](javascript:void(0);)

[打印](javascript:void(0);)

[关于](https://www.w3schools.cn/about/default.html)

[学习路线](https://www.w3schools.cn/about/about_learnpath.html)

------

W3Schools 在线教程提供的内容仅用于学习和测试，不保证内容的正确性。通过使用本站内容随之而来的风险与本站无关。



# CSS 样式链接

[❮ 上一节](https://www.w3schools.cn/css/css_icons.html)[下一节 ❯](https://www.w3schools.cn/css/css_list.html)

------

通过 CSS，可以用不同的方式设置链接的样式。

[Text Link](javascript:void(0)) [Text Link](javascript:void(0)) [Link Button](javascript:void(0)) [Link Button](javascript:void(0))

------

## 设置链接样式

链接可以使用任何 CSS 属性（例如 color、font-family、background 等）来设置样式。

### 实例

a {
 color: hotpink;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link_all)

此外，可以根据链接处于什么状态来设置链接的不同样式。

四种链接状态分别是：

- a:link - 正常的，未访问的链接
- a:visited - 用户访问过的链接
- a:hover - 用户将鼠标悬停在链接上时
- a:active - 链接被点击时

### 实例

/* 未被访问的链接 */
a:link {
 color: red;
}

/* 已被访问的链接 */
a:visited {
 color: green;
}

/* 将鼠标悬停在链接上 *
a:hover {
 color: hotpink;
}

/* 被选择的链接 */
a:active {
 color: blue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link)

如果为多个链接状态设置样式，请遵循如下顺序规则：

- a:hover 必须 a:link 和 a:visited 之后
- a:active 必须在 a:hover 之后

------

------

## 文本装饰

text-decoration 属性主要用于从链接中删除下划线：

### 实例

a:link {
 text-decoration: none;
}

a:visited {
 text-decoration: none;
}

a:hover {
 text-decoration: underline;
}

a:active {
 text-decoration: underline;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link_decoration)

------

## 背景色

background-color 属性可用于指定链接的背景色：

### 实例

a:link {
 background-color: yellow;
}

a:visited {
 background-color: cyan;
}

a:hover {
 background-color: lightgreen;
}

a:active {
 background-color: hotpink;
} 

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link_background)

------

## 链接按钮

本例演示了一个更高级的例子，其中我们组合了多个 CSS 属性，将链接显示为框/按钮：

### 实例

a:link, a:visited {
 background-color: #f44336;
 color: white;
 padding: 14px 25px;
 text-align: center;
 text-decoration: none;
 display: inline-block;
}

a:hover, a:active {
 background-color: red;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link_advanced)

------

## 更多实例

[为超链接添加不同的样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link2)
本例演示如何向超链接添加其他

[高级 - 创建带边框的链接按钮](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link_advanced2)
这是如何创建链接框/按钮的另一个例子。

[改变光标](https://www.w3schools.cn/css/tryit.asp?filename=trycss_cursor)
cursor 属性指定要显示的光标类型。本例演示了不同类型的光标（对链接有用）。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_link1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_link2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_link3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_link4)



[❮ 上一节](https://www.w3schools.cn/css/css_icons.html)[下一节 ❯](https://www.w3schools.cn/css/css_list.html)





[报告错误](javascript:void(0);)

[打印](javascript:void(0);)

[关于](https://www.w3schools.cn/about/default.html)

[学习路线](https://www.w3schools.cn/about/about_learnpath.html)

------

W3Schools 在线教程提供的内容仅用于学习和测试，不保证内容的正确性。通过使用本站内容随之而来的风险与本站无关。

Copyright 2

# CSS 样式列表

[❮ 上一节](https://www.w3schools.cn/css/css_link.html)[下一节 ❯](https://www.w3schools.cn/css/css_table.html)

------

## 无序列表：

- Coffee
- Tea
- Coca Cola

- Coffee
- Tea
- Coca Cola

## 有序列表：

1. Coffee
2. Tea
3. Coca Cola

1. Coffee
2. Tea
3. Coca Cola

------

## HTML 列表和 CSS 列表属性

在 HTML 中，列表主要有两种类型：

- 无序列表（<ul>）- 列表项用的是项目符号标记
- 有序列表（<ol>）- 列表项用的是数字或字母标记

CSS 列表属性使您可以：

- 为有序列表设置不同的列表项标记
- 为无序列表设置不同的列表项标记
- 将图像设置为列表项标记
- 为列表和列表项添加背景色

------

## 不同的列表项目标记

list-style-type 属性指定列表项标记的类型。

下例显示了一些可用的列表项标记：

### 实例

ul.a {
 list-style-type: circle;
}

ul.b {
 list-style-type: square;
}

ol.c {
 list-style-type: upper-roman;
}

ol.d {
 list-style-type: lower-alpha;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style-type_ex)

**注意：**有些值用于无序列表，有些值用于有序列表。

------

------

## 图像作为列表项标记

list-style-image 属性将图像指定为列表项标记：

### 实例

ul {
 list-style-image: url('sqpurple.gif');
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style-image)

------

## 定位列表项标记

list-style-position 属性指定列表项标记（项目符号）的位置。

"list-style-position: outside;" 表示项目符号点将在列表项之外。列表项每行的开头将垂直对齐。这是默认的：

- Coffee - A brewed drink prepared from roasted coffee beans...
- Tea
- Coca-cola

"list-style-position: inside;" 表示项目符号将在列表项内。由于它是列表项的一部分，因此它将成为文本的一部分，并在开头推开文本：

- Coffee - A brewed drink prepared from roasted coffee beans...
- Tea
- Coca-cola

### 实例

ul.a {
 list-style-position: outside;
}

ul.b {
 list-style-position: inside;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style-position)

------

## 删除默认设置

list-style-type:none 属性也可以用于删除标记/项目符号。请注意，列表还拥有默认的外边距和内边距。要删除此内容，请在 <ul> 或 <ol> 中添加 margin:0 和 padding:0 ：

### 实例

ul {
 list-style-type: none;
 margin: 0;
 padding: 0;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style_none)

------

## 列表 - 简写属性

list-style 属性是一种简写属性。它用于在一条声明中设置所有列表属性：

### 实例

ul {
 list-style: square inside url("sqpurple.gif");
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style)

在使用简写属性时，属性值的顺序为：

- list-style-type（如果指定了 list-style-image，那么在由于某种原因而无法显示图像时，会显示这个属性的值）
- list-style-position（指定列表项标记应显示在内容流的内部还是外部）
- list-style-image（将图像指定为列表项标记）

如果缺少上述属性值之一，则将插入缺失属性的默认值（如果有）。

------

## 设置列表的颜色样式

我们还可以使用颜色设置列表样式，使它们看起来更有趣。

添加到 <ol> 或 <ul> 标记的任何样式都会影响整个列表，而添加到 <li> 标记的属性将影响各个列表项：

### 实例

ol {
 background: #ff9999;
 padding: 20px;
}

ul {
 background: #3399ff;
 padding: 20px;
}

ol li {
 background: #ffe5e5;
 padding: 5px;
 margin-left: 35px;
}

ul li {
 background: #cce5ff;
 margin: 5px;
}

结果:

1. Coffee
2. Tea
3. Coca Cola

- Coffee
- Tea
- Coca Cola

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style_colors)

------

## 更多实例

[带红色左边框的自定义列表](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style-red-border)
本例演示如何创建带有红色左边框的列表。

[全屏宽度的边框列表](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style-border)
本例演示如何创建没有项目符号的带边框列表。

[列表的所有不同列表项标记](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style-type_all)
本例演示了 CSS 中所有不同的列表项标记。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_list1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_list2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_list3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_list4)

------

## 所有 CSS 列表属性

| 属性                                                         | 描述                                       |
| :----------------------------------------------------------- | :----------------------------------------- |
| [list-style](https://www.w3schools.cn/cssref/pr_list-style.html) | 简写属性。在一条声明中设置列表的所有属性。 |
| [list-style-image](https://www.w3schools.cn/cssref/pr_list-style-image.html) | 指定图像作为列表项标记。                   |
| [list-style-position](https://www.w3schools.cn/cssref/pr_list-style-position.html) | 规定列表项标记（项目符号）的位置。         |
| [list-style-type](https://www.w3schools.cn/cssref/pr_list-style-type.html) | 规定列表项标记的类型。                     |



[❮ 上一节](https://www.w3schools.cn/css/css_link.html)[下一节 ❯](https://www.w3schools.cn/css/css_table.html)





[报告错误](javascript:void(0);)

[打印](javascript:void(0);)

[关于](https://www.w3schools.cn/about/default.html)

[学习路线](https://www.w3schools.cn/about/about_learnpath.html)

------

W3Schools 在线教程提供的内容仅用于学习和测试，不保证内容的正确性。通过使用本站内容随之而来的风险与本站无关。



# CSS 表格

[❮ 上一节](https://www.w3schools.cn/css/css_list.html)[下一节 ❯](https://www.w3schools.cn/css/css_display_visibility.html)

------

**使用 CSS 可以极大地改善 HTML 表格的外观：**

| Company                      | Contact            | Country |
| :--------------------------- | :----------------- | :------ |
| Alfreds Futterkiste          | Maria Anders       | Germany |
| Berglunds snabbköp           | Christina Berglund | Sweden  |
| Centro comercial Moctezuma   | Francisco Chang    | Mexico  |
| Ernst Handel                 | Roland Mendel      | Austria |
| Island Trading               | Helen Bennett      | UK      |
| Königlich Essen              | Philip Cramer      | Germany |
| Laughing Bacchus Winecellars | Yoshi Tannamuri    | Canada  |
| Magazzini Alimentari Riuniti | Giovanni Rovelli   | Italy   |


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_fancy)

------

## 表格边框

如需在 CSS 中设置表格边框，请使用 border 属性。

下例为 <table>、<th> 和 <td> 元素规定了黑色边框：

<iframe src="https://www.w3schools.cn/css/trycss_table_border_iframe.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: none; height: 106px;"></iframe>



### 实例

table, th, td {
 border: 1px solid black;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_border)

注意：上例中的表格拥有双边框。这是因为 table 和 <th> 和 <td> 元素都有单独的边框。

------

## 合并表格边框

border-collapse 属性设置是否将表格边框折叠为单一边框：

<iframe src="https://www.w3schools.cn/css/trycss_table_border-collapse_iframe.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: none; height: 96px;"></iframe>



### 实例

table {
 border-collapse: collapse;
}

table, th, td {
 border: 1px solid black;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_border-collapse)

如果只希望表格周围有边框，则仅需为 <table> 指定 border 属性：

<iframe src="https://www.w3schools.cn/css/trycss_table_border2_iframe.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: none; height: 96px;"></iframe>



### 实例

table {
 border: 1px solid black;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_border2)

------

------

## 表格宽度和高度

表格的宽度和高度由 width 和 height 属性定义。

下例将表的宽度设置为 100％，将 <th> 元素的高度设置为 50px：

<iframe src="https://www.w3schools.cn/css/trycss_table_width_iframe.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: none; width: 869.984px; height: 147px;"></iframe>



### 实例

table {
 width: 100%;
}

th {
 height: 50px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_width)

------

## 水平对齐

text-align 属性设置 <th> 或 <td> 中内容的水平对齐方式（左、右或居中）。

默认情况下，<th> 元素的内容居中对齐，而 <td> 元素的内容左对齐。

要使 <td> 元素的内容也居中对齐，请使用 text-align: center：

<iframe src="https://www.w3schools.cn/css/trycss_table_align_iframe.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: none; width: 869.984px; height: 120px;"></iframe>



### 实例

th {
 text-align: left;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_align)

------

## 垂直对齐

vertical-align 属性设置 <th> 或 <td> 中内容的垂直对齐方式（上、下或居中）。

默认情况下，表中内容的垂直对齐是居中（<th> 和 <td> 元素都是）。

下例将 <td> 元素的垂直文本对齐方式设置为下对齐：

<iframe src="https://www.w3schools.cn/css/trycss_table_vertical-align_iframe.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: none; width: 869.984px; height: 206px;"></iframe>



### 实例

td {
 height: 50px;
 vertical-align: bottom;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_vertical-align)

------

## 表格内边距

如需控制边框和表格内容之间的间距，请在 <td> 和 <th> 元素上使用 padding 属性：

<iframe src="https://www.w3schools.cn/css/trycss_table_border-padding_iframe.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: none; width: 869.984px; height: 231px;"></iframe>



### 实例

th, td {
 padding: 15px;
 text-align: left;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_padding)

------

## 水平分隔线

| First Name | Last Name | Savings |
| :--------- | :-------- | :------ |
| Peter      | Griffin   | $100    |
| Lois       | Griffin   | $150    |
| Joe        | Swanson   | $300    |

向 <th> 和 <td> 添加 border-bottom 属性，以实现水平分隔线：

### 实例

th, td {
 border-bottom: 1px solid #ddd;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_border_divider)

------

## 可悬停表格

在 <tr> 元素上使用 :hover 选择器，以突出显示鼠标悬停时的表格行：

| First Name | Last Name | Savings |
| :--------- | :-------- | :------ |
| Peter      | Griffin   | $100    |
| Lois       | Griffin   | $150    |
| Joe        | Swanson   | $300    |

### 实例

tr:hover {background-color: #f5f5f5;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_hover)

------

## 条状表格

| First Name | Last Name | Savings |
| :--------- | :-------- | :------ |
| Peter      | Griffin   | $100    |
| Lois       | Griffin   | $150    |
| Joe        | Swanson   | $300    |

为了实现斑马纹表格效果，请使用 nth-child() 选择器，并为所有偶数（或奇数）表行添加 background-color：

### 实例

tr:nth-child(even) {background-color: #f2f2f2;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_striped)

------

## 表格颜色

下例指定了 <th> 元素的背景颜色和文本颜色：

| First Name | Last Name | Savings |
| :--------- | :-------- | :------ |
| Peter      | Griffin   | $100    |
| Lois       | Griffin   | $150    |
| Joe        | Swanson   | $300    |

### 实例

th {
 background-color: #4CAF50;
 color: white;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_color)

------

## 响应式表格

如果屏幕太小而无法显示全部内容，则响应式表格会显示水平滚动条：

| First Name | Last Name | Points | Points | Points | Points | Points | Points | Points | Points | Points | Points | Points | Points |
| :--------- | :-------- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- |
| Jill       | Smith     | 50     | 50     | 50     | 50     | 50     | 50     | 50     | 50     | 50     | 50     | 50     | 50     |
| Eve        | Jackson   | 94     | 94     | 94     | 94     | 94     | 94     | 94     | 94     | 94     | 94     | 94     | 94     |
| Adam       | Johnson   | 67     | 67     | 67     | 67     | 67     | 67     | 67     | 67     | 67     | 67     | 67     | 67     |

在 <table> 元素周围添加带有 overflow-x:auto 的容器元素（例如 <div>），以实现响应式效果：

### 实例

<div style="overflow-x:auto;"><table>... table content ...</table></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_responsive)

**注释:** 在 OS X Lion（在 Mac 上）中，滚动条默认情况下是隐藏的，并且仅在使用时显示（即使设置了 "overflow:scroll"）。

------

## 更多实例

[做一张花式表格](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_fancy)
本例演示如何创建花式表格。

[设置表格标题的位置](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_caption-side)
本例演示了如何放置表格标题。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_table1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_table2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_table3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_table4)[测验 5 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_table5)[测验 6 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_table6)

------

## CSS 表格属性

| 属性                                                         | 描述                                           |
| :----------------------------------------------------------- | :--------------------------------------------- |
| [border](https://www.w3schools.cn/cssref/pr_border.html)     | 简写属性。在一条声明中设置所有边框属性。       |
| [border-collapse](https://www.w3schools.cn/cssref/pr_border-collapse.html) | 规定是否应折叠表格边框。                       |
| [border-spacing](https://www.w3schools.cn/cssref/pr_border-spacing.html) | 规定相邻单元格之间的边框的距离。               |
| [caption-side](https://www.w3schools.cn/cssref/pr_tab_caption-side.html) | 规定表格标题的位置。                           |
| [empty-cells](https://www.w3schools.cn/cssref/pr_tab_empty-cells.html) | 规定是否在表格中的空白单元格上显示边框和背景。 |
| [table-layout](https://www.w3schools.cn/cssref/pr_tab_table-layout.html) | 设置用于表格的布局算法。                       |



[❮ 上一节](https://www.w3schools.cn/css/css_list.html)[下一节 ❯](https://www.w3schools.cn/css/css_display_visibility.html)



# CSS 布局 - display 属性

[❮ 上一节](https://www.w3schools.cn/css/css_table.html)[下一节 ❯](https://www.w3schools.cn/css/css_max-width.html)

------

`display` 属性是用于控制布局的最重要的 CSS 属性。

------

## display 属性

display 属性规定是否/如何显示元素。

每个 HTML 元素都有一个默认的 display 值，具体取决于它的元素类型。大多数元素的默认 display 值为 block 或 inline。

点击显示面板

------

## 块级元素（block element）

块级元素总是从新行开始，并占据可用的全部宽度（尽可能向左和向右伸展）。

这个 <div> 元素属于块级元素。

块级元素的一些例子：

- <div>
- <h1> - <h6>
- <p>
- <form>
- <header>
- <footer>
- <section>

------

## 行内元素（inline element）

内联元素不从新行开始，仅占用所需的宽度。

这是段落中的 a行内 <span> 元素。

行内元素的一些例子：

- <span>
- <a>
- <img>

------

## Display: none;

display: none; 通常与 JavaScript 一起使用，以隐藏和显示元素，而无需删除和重新创建它们。如果您想知道如何实现此目标，请查看本页面上的最后一个实例。

默认情况下，<script> 元素使用 display: none;。

------

------

## 覆盖默认的 Display 值

如前所述，每个元素都有一个默认 display 值。但是，您可以覆盖它。

将行内元素更改为块元素，反之亦然，对于使页面以特定方式显示同时仍遵循 Web 标准很有用。

一个常见的例子是为实现水平菜单而生成行内的 <li> 元素：

### 实例

li {
 display: inline;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_display_inline_list)

**注释:** 设置元素的 display 属性仅会更改**元素的显示方式**，而不会更改元素的种类。因此，带有 display: block; 的行内元素不允许在其中包含其他块元素。

下例将 <span> 元素显示为块元素：

### 实例

span {
 display: block;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_display_block)

下例将 <a> 元素显示为块元素：

### 实例

a {
 display: block;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_display_block_a)

------

## 隐藏元素 - display:none 还是 visibility:hidden？

```
display:none
```

![Italy](https://www.w3schools.cn/css/img_5terre.jpg)

Remove

```
visibility:hidden
```

![Forest](https://www.w3schools.cn/css/img_forest.jpg)

Hide

Reset

![Lights](https://www.w3schools.cn/css/img_lights.jpg)

Reset All

通过将 display 属性设置为 none 可以隐藏元素。该元素将被隐藏，并且页面将显示为好像该元素不在其中：

### 实例

h1.hidden {
 display: none;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_display_none)

visibility:hidden; 也可以隐藏元素。

但是，该元素仍将占用与之前相同的空间。元素将被隐藏，但仍会影响布局：

### 实例

h1.hidden {
 visibility: hidden;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_visibility_hidden)

------

## 更多实例

[display: none; 与 visibility: hidden; 之间的差异](https://www.w3schools.cn/css/tryit.asp?filename=trycss_display)
本例演示 display: none; VS visibility: hidden;

[结合使用 CSS 和 JavaScript 来显示内容](https://www.w3schools.cn/css/tryit.asp?filename=trycss_display_js)
本例演示如何使用 CSS 和 JavaScript 在单击时显示元素。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_display_visibility1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_display_visibility2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_display_visibility3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_display_visibility4)

------

## CSS Display/Visibility 属性

| 属性                                                         | 描述                   |
| :----------------------------------------------------------- | :--------------------- |
| [display](https://www.w3schools.cn/cssref/pr_class_display.html) | 指定应如何显示元素。   |
| [visibility](https://www.w3schools.cn/cssref/pr_class_visibility.html) | 指定元素是否应该可见。 |



[❮ 上一节](https://www.w3schools.cn/css/css_table.html)[下一节 ❯](https://www.w3schools.cn/css/css_max-width.html)





[报告错误](javascript:void(0);)

[打印](javascript:void(0);)

[关于](https://www.w3schools.cn/about/default.html)

[学习路线](https://www.w3schools.cn/about/about_learnpath.html)

------

W3Schools 在线教程提供的内容仅用于学习和测试，不保证内容的正确性。通过使用本站内容随之而来的风险与本站无关。



# CSS 布局 - width 和 max-width

[❮ 上一节](https://www.w3schools.cn/css/css_display_visibility.html)[下一节 ❯](https://www.w3schools.cn/css/css_positioning.html)

------

## 使用 width、max-width 和 margin: auto;

如上一章所述，块级元素始终占用可用的全部宽度（尽可能向左和向右伸展）。

设置块级元素的 width 将防止其延伸到其容器的边缘。然后，您可以将外边距设置为 auto，以将元素在其容器中水平居中。元素将占用指定的宽度，剩余空间将在两个外边距之间平均分配：

这个 <div> 元素的宽度为 500px，外边距设置为 auto。



**注释:** 当浏览器窗口小于元素的宽度时，上面这个 <div> 会发生问题。浏览器会将水平滚动条添加到页面。

在这种情况下，使用 max-width 可以改善浏览器对小窗口的处理。为了使网站在小型设备上可用，这一点很重要：

这个 <div> 元素的最大宽度为 500px，外边距设置为 auto。



**提示:** 请将浏览器窗口的大小调整为小于 500 像素，以查看两个 div 之间的区别！

这是上面两个 div 的例子：

### 实例

div.ex1 {
 width: 500px;
 margin: auto;
 border: 3px solid #73AD21;
}

div.ex2 {
 max-width: 500px;
 margin: auto;
 border: 3px solid #73AD21;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_max-width)



[❮ 上一节](https://www.w3schools.cn/css/css_display_visibility.html)[下一节 ❯](https://www.w3schools.cn/css/css_positioning.html)



# CSS 布局 - 定位属性

[❮ 上一节](https://www.w3schools.cn/css/css_max-width.html)[下一节 ❯](https://www.w3schools.cn/css/css_overflow.html)

------

`position` 属性规定应用于元素的定位方法的类型（static、relative、fixed、absolute 或 sticky）。

------

## position 属性

position 属性规定应用于元素的定位方法的类型。

有五个不同的位置值：

- `static`
- `relative`
- `fixed`
- `absolute`
- `sticky`

元素其实是使用 top、bottom、left 和 right 属性定位的。但是，除非首先设置了 position 属性，否则这些属性将不起作用。根据不同的 position 值，它们的工作方式也不同。

------

## position: static;

HTML 元素默认情况下的定位方式为 static（静态）。

静态定位的元素不受 top、bottom、left 和 right 属性的影响。

position: static; 的元素不会以任何特殊方式定位；它始终根据页面的正常流进行定位：

这个 <div> 元素设置了 position: static;

这是所用的 CSS：

### 实例

div.static {
 position: static;
 border: 3px solid #73AD21;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_static)

------

## position: relative;

position: relative; 的元素相对于其正常位置进行定位。

设置相对定位的元素的 top、right、bottom 和 left 属性将导致其偏离其正常位置进行调整。不会对其余内容进行调整来适应元素留下的任何空间。

这个 <div> 元素设置了 position: relative;

这是所用的 CSS：

### 实例

div.relative {
 position: relative;
 left: 30px;
 border: 3px solid #73AD21;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_relative)

------

------

## position: fixed;

position: fixed; 的元素是相对于视口定位的，这意味着即使滚动页面，它也始终位于同一位置。 top、right、bottom 和 left 属性用于定位此元素。

固定定位的元素不会在页面中通常应放置的位置上留出空隙。

请注意页面右下角的这个固定元素。这是所用的 CSS：

### 实例

div.fixed {
 position: fixed;
 bottom: 0;
 right: 0;
 width: 300px;
 border: 3px solid #73AD21;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_fixed)

这个 <div> 元素设置了 position: fixed;

------

## position: absolute;

position: absolute; 的元素相对于最近的定位祖先元素进行定位（而不是相对于视口定位，如 fixed）。

然而，如果绝对定位的元素没有祖先，它将使用文档主体（body），并随页面滚动一起移动。

**注释:** "被定位的"元素是其位置除 static 以外的任何元素。

这是一个简单的例子：

这个 <div> 元素设置了 position: relative;

这个 <div> 元素设置了 position: absolute;

这是所用的 CSS：

### 实例

div.relative {
 position: relative;
 width: 400px;
 height: 200px;
 border: 3px solid #73AD21;
}

div.absolute {
 position: absolute;
 top: 80px;
 right: 0;
 width: 200px;
 height: 100px;
 border: 3px solid #73AD21;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_absolute)

------

## position: sticky;

position: sticky; 的元素根据用户的滚动位置进行定位。

粘性元素根据滚动位置在相对（relative）和固定（fixed）之间切换。起先它会被相对定位，直到在视口中遇到给定的偏移位置为止 - 然后将其"粘贴"在适当的位置（比如 position:fixed）。

<iframe src="https://www.w3schools.cn/css/trycss_position_sticky_ifr.htm" class="w3-padding" style="box-sizing: inherit; padding: 8px 16px !important; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; width: 869.984px; border: 4px solid rgb(229, 229, 229);"></iframe>



**注意:** Internet Explorer、Edge 15 以及更早的版本不支持粘性定位。 Safari 需要 -webkit- 前缀（请参见下面的实例）。您还必须至少指定 top、right、bottom 或 left 之一，以便粘性定位起作用。

在此例中，在到达其滚动位置时，sticky 元素将停留在页面顶部（top: 0）。

### 实例

div.sticky {
 position: -webkit-sticky; /* Safari */
 position: sticky;
 top: 0;
 background-color: green;
 border: 2px solid #4CAF50;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_sticky)

------

## 重叠元素

在对元素进行定位时，它们可以与其他元素重叠。

z-index 属性指定元素的堆栈顺序（哪个元素应放置在其他元素的前面或后面）。

元素可以设置正或负的堆叠顺序：

# This is a heading

![img](https://www.w3schools.cn/css/w3css.gif)

Because the image has a z-index of -1, it will be placed behind the text.

### 实例

img {
 position: absolute;
 left: 0px;
 top: 0px;
 z-index: -1;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_zindex)

具有较高堆叠顺序的元素始终位于具有较低堆叠顺序的元素之前。

**注释:** 如果两个定位的元素重叠而未指定 z-index，则位于 HTML 代码中最后的元素将显示在顶部。

------

## 定位图像中的文本

如何在图片上放置文字：

### 实例

![Cinque Terre](https://www.w3schools.cn/css/img_5terre_wide.jpg)

Bottom Left

Top Left

Top Right

Bottom Right

Centered

在线实例:

[Top Left »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_top_left) [Top Right »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_top_right) [Bottom Left »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_bottom_left) [Bottom Right »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_bottom_right) [Centered »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_center)

------

## 更多实例

[设置元素的形状](https://www.w3schools.cn/css/tryit.asp?filename=trycss_clip)
本例演示如何设置元素的形状。元素被裁剪为这种形状并显示。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_positioning1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_positioning2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_positioning3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_positioning4)[测验 5 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_positioning5)

------

## 所有 CSS 定位属性

| 属性                                                         | 描述                         |
| :----------------------------------------------------------- | :--------------------------- |
| [bottom](https://www.w3schools.cn/cssref/pr_pos_bottom.html) | 设置定位框的底部外边距边缘。 |
| [clip](https://www.w3schools.cn/cssref/pr_pos_clip.html)     | 剪裁绝对定位的元素。         |
| [left](https://www.w3schools.cn/cssref/pr_pos_left.html)     | 设置定位框的左侧外边距边缘。 |
| [position](https://www.w3schools.cn/cssref/pr_class_position.html) | 规定元素的定位类型。         |
| [right](https://www.w3schools.cn/cssref/pr_pos_right.html)   | 设置定位框的右侧外边距边缘。 |
| [top](https://www.w3schools.cn/cssref/pr_pos_top.html)       | 设置定位框的顶部外边距边缘。 |
| [z-index](https://www.w3schools.cn/cssref/pr_pos_z-index.html) | 设置元素的堆叠顺序。         |

。

# CSS 布局 - 溢出

[❮ 上一节](https://www.w3schools.cn/css/css_positioning.html)[下一节 ❯](https://www.w3schools.cn/css/css_float.html)

------

The CSS `overflow` 属性控制对太大而区域无法容纳的内容的处理方式。

This text is really long and the height of its container is only 100 pixels. Therefore, a scrollbar is added to help the reader to scroll the content. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Typi non habent claritatem insitam; est usus legentis in iis qui facit eorum claritatem.


[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_overflow_intro)

------

## CSS Overflow

overflow 属性指定在元素的内容太大而无法放入指定区域时是剪裁内容还是添加滚动条。

overflow 属性可设置以下值：

- visible - 默认。溢出没有被剪裁。内容在元素框外渲染
- hidden - 溢出被剪裁，其余内容将不可见
- scroll - 溢出被剪裁，同时添加滚动条以查看其余内容
- auto - 与 scroll 类似，但仅在必要时添加滚动条

**注释:** `overflow` 属性仅适用于具有指定高度的块元素。

**注释:** 在 OS X Lion（在 Mac 上）中，滚动条默认情况下是隐藏的，并且仅在使用时显示（即使设置了 "overflow:scroll"）。

------

## overflow: visible

默认情况下，溢出是可见的(visible)，这意味着它不会被裁剪，而是在元素框外渲染：

当您希望更好地控制布局时，可以使用 overflow 属性。overflow 属性指定如果内容溢出元素框会发生什么。

### 实例

div {
 width: 200px;
 height: 50px;
 background-color: #eee;
 overflow: visible;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_overflow_visible)

------

------

## overflow: hidden

如果使用 hidden 值，溢出会被裁剪，其余内容被隐藏：

当您希望更好地控制布局时，可以使用 overflow 属性。overflow 属性指定如果内容溢出元素框会发生什么。

### 实例

div {
 overflow: hidden;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_overflow_hidden)

------

## overflow: scroll

如果将值设置为 scroll，溢出将被裁剪，并添加滚动条以便在框内滚动。请注意，这将在水平和垂直方向上添加一个滚动条（即使您不需要它）：

当您希望更好地控制布局时，可以使用 overflow 属性。overflow 属性指定如果内容溢出元素框会发生什么。

### 实例

div {
 overflow: scroll;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_overflow_scroll)

------

## overflow: auto

auto 值类似于 scroll，但是它仅在必要时添加滚动条：

当您希望更好地控制布局时，可以使用 overflow 属性。overflow 属性指定如果内容溢出元素框会发生什么。

### 实例

div {
 overflow: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_overflow_auto)

------

## overflow-x 和 overflow-y

overflow-x 和 overflow-y 属性规定是仅水平还是垂直地（或同时）更改内容的溢出：

- overflow-x 指定如何处理内容的左/右边缘。
- overflow-y 指定如何处理内容的上/下边缘。

当您希望更好地控制布局时，可以使用 overflow 属性。overflow 属性指定如果内容溢出元素框会发生什么。

### 实例

div {
 overflow-x: hidden; /* 隐藏水平滚动条 */
 overflow-y: scroll; /* 添加垂直滚动条 */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_overflow_xy)

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_overflow1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_overflow2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_overflow3)

------

## 所有 CSS Overflow 属性

| 属性                                                         | 描述                                                |
| :----------------------------------------------------------- | :-------------------------------------------------- |
| [overflow](https://www.w3schools.cn/cssref/pr_pos_overflow.html) | 规定如果内容溢出元素框会发生什么情况。              |
| [overflow-x](https://www.w3schools.cn/cssref/css3_pr_overflow-x.html) | 规定在元素的内容区域溢出时如何处理内容的左/右边缘。 |
| [overflow-y](https://www.w3schools.cn/cssref/css3_pr_overflow-y.html) | 指定在元素的内容区域溢出时如何处理内容的上/下边缘。 |



# CSS 布局 - 浮动和清除

[❮ 上一节](https://www.w3schools.cn/css/css_overflow.html)[下一节 ❯](https://www.w3schools.cn/css/css_float_clear.html)

------

CSS float 属性规定元素如何浮动。

CSS clear 属性规定哪些元素可以在清除的元素旁边以及在哪一侧浮动。





------

## float 属性

float 属性用于定位和格式化内容，例如让图像向左浮动到容器中的文本那里。

float 属性可以设置以下值之一：

- left - 元素浮动到其容器的左侧
- right - 元素浮动在其容器的右侧
- none - 元素不会浮动（将显示在文本中刚出现的位置）。默认值。
- inherit - 元素继承其父级的 float 值

最简单的用法是， `float` 属性可实现（报纸上）文字包围图片的效果。

------

## 实例 - float: right;

下例指定图像应在文本中向右浮动：

![Pineapple](https://www.w3schools.cn/css/pineapple.jpg)Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor. Maecenas nisl est, ultrices nec congue eget, auctor vitae massa. Fusce luctus vestibulum augue ut aliquet. Mauris ante ligula, facilisis sed ornare eu, lobortis in odio. Praesent convallis urna a lacus interdum ut hendrerit risus congue. Nunc sagittis dictum nisi, sed ullamcorper ipsum dignissim ac...

### 实例

img {
 float: right;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_layout_float)

------

## 实例 - float: left;

下例指定图像应在文本中**向左**浮动：

![Pineapple](https://www.w3schools.cn/css/pineapple.jpg)Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor. Maecenas nisl est, ultrices nec congue eget, auctor vitae massa. Fusce luctus vestibulum augue ut aliquet. Mauris ante ligula, facilisis sed ornare eu, lobortis in odio. Praesent convallis urna a lacus interdum ut hendrerit risus congue. Nunc sagittis dictum nisi, sed ullamcorper ipsum dignissim ac...

### 实例

img {
 float: left;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_layout_float2)

------

## 实例 - No float

在下例中，图像将显示在文本中刚出现的位置（float: none;）：

![Pineapple](https://www.w3schools.cn/css/pineapple.jpg) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor. Maecenas nisl est, ultrices nec congue eget, auctor vitae massa. Fusce luctus vestibulum augue ut aliquet. Mauris ante ligula, facilisis sed ornare eu, lobortis in odio. Praesent convallis urna a lacus interdum ut hendrerit risus congue. Nunc sagittis dictum nisi, sed ullamcorper ipsum dignissim ac...

### 实例

img {
 float: none;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_layout_float_none)

------



[❮ 上一节](https://www.w3schools.cn/css/css_overflow.html)[下一节 ❯](https://www.w3schools.cn/css/css_float_clear.html)



# CSS 布局 - clear 和 clearfix

[❮ 上一节](https://www.w3schools.cn/css/css_float.html)[下一节 ❯](https://www.w3schools.cn/css/css_float_examples.html)

------

## clear 属性

clear 属性指定哪些元素可以浮动于被清除元素的旁边以及哪一侧。

clear 属性可设置以下值之一：

- none - 允许两侧都有浮动元素。默认值
- left - 左侧不允许浮动元素
- right- 右侧不允许浮动元素
- both - 左侧或右侧均不允许浮动元素
- inherit - 元素继承其父级的 clear 值

使用 clear 属性的最常见用法是在元素上使用了 float 属性之后。

在清除浮动时，应该对清除与浮动进行匹配：如果某个元素浮动到左侧，则应清除左侧。您的浮动元素会继续浮动，但是被清除的元素将显示在其下方。

下例将清除向左的浮动。表示在（div 的）左侧不允许出现浮动元素：

### 实例

div {
 clear: left;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_layout_clear)

------

## clearfix Hack

如果一个元素比包含它的元素高，并且它是浮动的，它将"溢出"到其容器之外：

### Without Clearfix

![img](https://w3schools.cn/howto/clearfix_prob.jpg)

### With Clearfix

![img](https://w3schools.cn/howto/clearfix_solution.jpg)

然后我们可以向包含元素添加 overflow: auto;，来解决此问题：

### 实例

.clearfix {
 overflow: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_layout_clearfix)

只要您能够控制外边距和内边距（否则您可能会看到滚动条），`overflow: auto` clearfix 就会很好地工作。但是，新的现代 clearfix hack 技术使用起来更安全，以下代码被应用于多数网站：

### 实例

.clearfix::after {
 content: "";
 clear: both;
 display: table;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_layout_clearfix2)

您将在稍后的章节学到 ::after 伪元素。

------



[❮ 上一节](https://www.w3schools.cn/css/css_float.html)[下一节 ❯](https://www.w3schools.cn/css/css_float_examples.html)

# CSS 布局 - 浮动实例

[❮ 上一节](https://www.w3schools.cn/css/css_float_clear.html)[下一节 ❯](https://www.w3schools.cn/css/css_inline-block.html)

------

本页提供常见的浮动案例。

------

## 网格 / 等宽的框

Box 1

Box 2



Box 1

Box 2

Box 3

通过使用 float 属性，可以轻松地并排浮动内容框：

### 实例

\* {
 box-sizing: border-box;
}

.box {
 float: left;
 width: 33.33%; /* 三个盒子（四个用 25%，两个用 50%，等等） */
 padding: 50px; /* 如果你想要图像之间的空间 */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float_boxes)

## 什么是 box-sizing？

您可以轻松地并排创建三个浮动框。但是，当您添加一些内容来扩大每个框的宽度（例如，内边距或边框）时，这个框会损坏。 box-sizing 属性允许我们在框的总宽度（和高度）中包括内边距和边框，确保内边距留在框内而不会破裂。

您可以在我们的 [CSS Box Sizing](https://www.w3schools.cn/css/css3_box-sizing.html) 这一章中学习有关 box-sizing 属性的更多知识。

------

## 图像并排

![Italy](https://www.w3schools.cn/css/img_5terre.jpg)

![Forest](https://www.w3schools.cn/css/img_forest.jpg)

![Mountains](https://www.w3schools.cn/css/img_mountains.jpg)

这种框格（The grid of boxes）也可以用来并排显示图像：

### 实例

.img-container {
 float: left;
 width: 33.33%; /* 三个容器（四个使用 25%，两个使用 50%，等等）*/
 padding: 5px; /* 如果你想要图像之间的空间 */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float_images_side)

------

## 等高的框

在上例中，您学习了如何以相等的宽度并排浮动框。但是，创建具有相同高度的浮动框并不容易。不过，快速解决方案是设置一个固定的高度，如下例所示：

## Box 1

一些内容，一些内容，一些内容

## Box 2

一些内容，一些内容，一些内容

一些内容，一些内容，一些内容

一些内容，一些内容，一些内容

### 实例

.box {
 height: 500px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float_boxes_height)

但是，这么做就失去了弹性。如果可以保证框中始终有相同数量的内容，那是可以的。但是很多时候，内容是不一样的。如果您在手机上尝试上例，则会看到第二个框的内容将显示在框的外部。这是 CSS3 Flexbox 派上用场的地方 - 因为它可以自动拉伸框使其与最长的框一样长：

### 实例

使用 Flexbox 创建弹性框：

Box 1 - 这是一些文本，以确保内容变得非常高。 这是一些文本，以确保内容变得非常高。 这是一些文本，以确保内容变得非常高。

Box 2 - 此高度将跟随 Box 1。

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float_boxes_flex)

Flexbox 的唯一问题是它在 Internet Explorer 10 或更早版本中不起作用。您可以在我们的 [CSS Flexbox](https://www.w3schools.cn/css/css3_flexbox.html) 章节中学习有关 Flexbox 布局模块的更多知识。

------

## 导航菜单

将 float 与超链接列表一起使用，来创建水平菜单：

### 实例

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float5)

------

## Web 布局实例

使用 float 属性完成整个 Web 布局也很常见：

<iframe src="https://www.w3schools.cn/css/trycss_layout_cols.htm" class="w3-hide-small" style="box-sizing: inherit; width: 869.984px; border: 1px solid rgb(241, 241, 241); height: 420px; padding: 5px; overflow: auto;"></iframe>

### 实例

.header, .footer {
 background-color: grey;
 color: white;
 padding: 15px;
}

.column {
 float: left;
 padding: 15px;
}

.clearfix::after {
 content: "";
 clear: both;
 display: table;
}

.menu {
 width: 25%;
}

.content {
 width: 75%;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_layout_cols)

------

## 更多实例

[带有边框和外边距的图像浮动到段落的右侧](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float2)
让图像浮动到段落的右侧。在图像上添加边框和

[带标题的图像浮动到右侧](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float3)
让带有标题的图像向右浮

[让段落的第一个字母向左浮动](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float4)
让段落的第一个字母向左浮动并设置该字母的样式。

[用浮动创建一个网站](https://www.w3schools.cn/css/tryit.asp?filename=trycss_layout_webpage)
使用浮动创建带有水平导航栏、页眉、页脚、左侧导航栏和主要内容的首页。

------

## 所有 CSS 浮动属性

| 属性                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [box-sizing](https://www.w3schools.cn/cssref/css3_pr_box-sizing.html) | 定义元素的宽度和高度的计算方式：它们是否应包含内边距和边框。 |
| [clear](https://www.w3schools.cn/cssref/pr_class_clear.html) | 指定哪些元素可以在被清除的元素旁边以及在哪一侧浮动。         |
| [float](https://www.w3schools.cn/cssref/pr_class_float.html) | 指定元素应如何浮动。                                         |
| [overflow](https://www.w3schools.cn/cssref/pr_pos_overflow.html) | 指定如果内容溢出元素框会发生什么情况。                       |
| [overflow-x](https://www.w3schools.cn/cssref/css3_pr_overflow-x.html) | 指定当溢出元素的内容区域时，如何处理内容的左/右边缘。        |
| [overflow-y](https://www.w3schools.cn/cssref/css3_pr_overflow-y.html) | 指定当溢出元素的内容区域时，如何处理内容的上/下边缘。        |



[❮ 上一节](https://www.w3schools.cn/css/css_float_clear.html)[下一节 ❯](https://www.w3schools.cn/css/css_inline-block.html)

# CSS 布局 - display: inline-block

[❮ 上一节](https://www.w3schools.cn/css/css_float_examples.html)[下一节 ❯](https://www.w3schools.cn/css/css_align.html)

------

## display: inline-block

与 display: inline 相比，主要区别在于 display: inline-block 允许在元素上设置宽度和高度。

同样，如果设置了 display: inline-block，将保留上下外边距/内边距，而 display: inline 则不会。

与 display: block 相比，主要区别在于 display：inline-block 在元素之后不添加换行符，因此该元素可以位于其他元素旁边。

下例展示 display: inline、display: inline-block 以及 display: block 的不同行为：

### 实例

span.a {
 display: inline; /* 跨度的默认值 */
 width: 100px;
 height: 100px;
 padding: 5px;
 border: 1px solid blue;
 background-color: yellow;
}

span.b {
 display: inline-block;
 width: 100px;
 height: 100px;
 padding: 5px;
 border: 1px solid blue;
 background-color: yellow;
}

span.c {
 display: block;
 width: 100px;
 height: 100px;
 padding: 5px;
 border: 1px solid blue;
 background-color: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_inline-block_span1)

------

## 使用 inline-block 来创建导航链接

display 的一种常见用法：inline-block 用于水平而不是垂直地显示列表项。下例创建了一个水平导航链接：

### 实例

.nav {
 background-color: yellow;
 list-style-type: none;
 text-align: center; 
 padding: 0;
 margin: 0;
}

.nav li {
 display: inline-block;
 font-size: 20px;
 padding: 20px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_inline-block_nav)

# CSS 布局 - 水平和垂直对齐

[❮ 上一节](https://www.w3schools.cn/css/css_inline-block.html)[下一节 ❯](https://www.w3schools.cn/css/css_combinators.html)



▲▼

◀►

## 水平和垂直居中的元素

------

## 居中对齐元素

要使块元素（例如 <div> ）水平居中，请使用 margin: auto;。

设置元素的宽度将防止其延伸到容器的边缘。

然后，元素将占用指定的宽度，剩余空间将在两个外边距之间平均分配：

这个 div 元素是居中的

### 实例

.center {
 margin: auto;
 width: 50%;
 border: 3px solid green;
 padding: 10px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_container)

**注释:** 如果未设置 width 属性（或将其设置为 100％），则居中对齐无效。

------

## 居中对齐文本

如果仅需在元素内居中文本，请使用 text-align: center;：

这段文本是居中的。

### 实例

.center {
 text-align: center;
 border: 3px solid green;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_text)

**提示:** 有关如何对齐文本的更多例子，请参见 [CSS 文本](https://www.w3schools.cn/css/css_text.html) 这一章。

------

------

## 居中对齐图像

如需居中图像，请将左右外边距设置为 auto，并将其设置为块元素：

![Paris](https://www.w3schools.cn/css/paris.jpg)

### 实例

img {
 display: block;
 margin-left: auto;
 margin-right: auto;
 width: 40%;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_image)

------

## 左和右对齐 - 使用 position

对齐元素的一种方法是使用 position: absolute; :

In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.

### 实例

.right {
 position: absolute;
 right: 0px;
 width: 300px;
 border: 3px solid #73AD21;
 padding: 10px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_pos)

**注释:** 绝对定位的元素将从正常流中删除，并可能出现元素重叠。

------

## 左和右对齐 - 使用 float

对齐元素的另一种方法是使用 float 属性：

### 实例

.right {
 float: right;
 width: 300px;
 border: 3px solid #73AD21;
 padding: 10px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_float)

**注释:** 如果一个元素比包含它的元素高，并且它是浮动的，它将溢出其容器。您可以使用 **clearfix hack** 来解决此问题（请看下面的例子）。

------

## clearfix hack

### 没有 Clearfix

![img](https://w3schools.cn/howto/clearfix_prob.jpg)

### 使用 Clearfix

![img](https://w3schools.cn/howto/clearfix_solution.jpg)

然后我们可以向包含元素添加 overflow: auto;，来解决此问题：

### 实例

.clearfix {
 overflow: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_layout_clearfix)

------

## 垂直对齐 - 使用 padding

有很多方法可以在 CSS 中垂直对齐元素。一个简单的解决方案是使用上下内边距：

我是垂直居中的。

### 实例

.center {
 padding: 70px 0;
 border: 3px solid green;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_padding)

如需同时垂直和水平对齐，请使用 padding 和 text-align: center;：

我是水平和垂直居中的。

### 实例

.center {
 padding: 70px 0;
 border: 3px solid green;
 text-align: center;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_padding2)

------

## 垂直对齐 - 使用 line-height

另一个技巧是使用**其值**等于 height 属性值的 line-height 属性：

我是水平和垂直居中的。

### 实例

.center {
 line-height: 200px;
 height: 200px;
 border: 3px solid green;
 text-align: center;
}

/* 如果文本有多行，添加以下内容: */
.center p {
 line-height: 1.5;
 display: inline-block;
 vertical-align: middle;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_line-height)

------

## 垂直对齐 - 使用 position 和 transform

如果您的选择不是 padding 和 line-height，则另一种解决方案是使用 `position` 和 transform 属性：

我是水平和垂直居中的。

### 实例

.center {
 height: 200px;
 position: relative;
 border: 3px solid green;
}

.center p {
 margin: 0;
 position: absolute;
 top: 50%;
 left: 50%;
 transform: translate(-50%, -50%);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_transform)

**提示:** 在我们的 [2D 转换](https://www.w3schools.cn/css/css3_2dtransforms.html) 一章中，您将了解有关 transform 属性的更多信息。

------

## 垂直对齐 - 使用 Flexbox

您还可以使用 flexbox 将内容居中。请注意，IE10 以及更早的版本不支持 flexbox：

我是水平和垂直居中的

### 实例

.center {
 display: flex;
 justify-content: center;
 align-items: center;
 height: 200px;
 border: 3px solid green;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_align_flex)

**提示:** 您将在我的 [CSS Flexbox](https://www.w3schools.cn/css/css3_flexbox.html) 这一章中学到更多关于 Flexbox 的知识。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_align1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_align2)



[❮ 上一节](https://www.w3schools.cn/css/css_inline-block.html)[下一节 ❯](https://www.w3schools.cn/css/css_combinators.html)

# CSS 组合器

[❮ 上一节](https://www.w3schools.cn/css/css_align.html)[下一节 ❯](https://www.w3schools.cn/css/css_pseudo_classes.html)

------

## CSS 组合器

组合器是解释选择器之间关系的某种机制。

CSS 选择器可以包含多个简单选择器。在简单选择器之间，我们可以包含一个组合器。

CSS 中有四种不同的组合器：

- 后代选择器 (空格)
- 子选择器 (>)
- 相邻兄弟选择器 (+)
- 通用兄弟选择器 (~)

------

## 后代选择器

后代选择器匹配属于指定元素后代的所有元素。

下面的例子选择 <div> 元素内的所有 <p> 元素：

### 实例

div p {
 background-color: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_element_element)

------

## 子选择器

子选择器匹配属于指定元素子元素的所有元素。

下面的例子选择属于 <div> 元素子元素的所有 <p> 元素：

### 实例

div > p {
 background-color: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_element_gt)

------

------

## 相邻兄弟选择器

相邻兄弟选择器匹配所有作为指定元素的相邻同级的元素。

兄弟（同级）元素必须具有相同的父元素，"相邻"的意思是"紧随其后"。

下面的例子选择紧随 <div> 元素之后的所有 <p> 元素：

### 实例

div + p {
 background-color: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_element_pluss)

------

## 通用兄弟选择器

通用兄弟选择器匹配属于指定元素的同级元素的所有元素。

下面的例子选择属于 <div> 元素的同级元素的所有 <p> 元素：

### 实例

div ~ p {
 background-color: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_element_tilde)

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_combinators1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_combinators2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_combinators3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_combinators4)

------

## 所有 CSS 组合选择器

| 选择器                                                       | 实例    | 实例描述                                   |
| :----------------------------------------------------------- | :------ | :----------------------------------------- |
| [*element* *element*](https://www.w3schools.cn/cssref/sel_element_element.html) | div p   | 选择 <div> 元素内的所有 <p> 元素。         |
| [*element*>*element*](https://www.w3schools.cn/cssref/sel_element_gt.html) | div > p | 选择其父元素是 <div> 元素的所有 <p> 元素。 |
| [*element*+*element*](https://www.w3schools.cn/cssref/sel_element_pluss.html) | div + p | 选择所有紧随 <div> 元素之后的 <p> 元素。   |
| [*element1*~*element2*](https://www.w3schools.cn/cssref/sel_gen_sibling.html) | p ~ ul  | 选择前面有 <p> 元素的每个 <ul> 元素。      |









# CSS 伪类

[❮ 上一节](https://www.w3schools.cn/css/css_combinators.html)[下一节 ❯](https://www.w3schools.cn/css/css_pseudo_elements.html)

------

## 什么是伪类？

伪类用于定义元素的特殊状态。

例如，它可以用于：

- 设置鼠标悬停在元素上时的样式
- 为已访问和未访问链接设置不同的样式
- 设置元素获得焦点时的样式

请将鼠标悬停在我上面



------

## 语法

伪类的语法：

selector:pseudo-class {
 property: value;
}

------

## 锚伪类

链接能够以不同的方式显示：

### 实例

/* 未访问的链接 */
a:link {
 color: #FF0000;
}

/* 访问过的链接 */
a:visited {
 color: #00FF00;
}

/* 鼠标悬停在链接上 */
a:hover {
 color: #FF00FF;
}

/* 选择的链接 */
a:active {
 color: #0000FF;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link)

**注释:** `a:hover` 必须在 CSS 定义中的 `a:link` 和 `a:visited` 之后，才能生效！`a:active` 必须在 CSS 定义中的 `a:hover` 之后才能生效！伪类名称对大小写不敏感。

------

------

## 伪类和 CSS 类

伪类可以与 CSS 类结合使用：

当您将鼠标悬停在例子中的链接上时，它会改变颜色：

### 实例

a.highlight:hover {
 color: #ff0000;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_pseudo-class)

------

## 悬停在 <div> 上

在 <div> 元素上使用 :hover 伪类的实例：

### 实例

div:hover {
 background-color: blue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_pseudo-class_hover_div)

------

## 简单的工具提示悬停

把鼠标悬停到 <div> 元素以显示 <p> 元素（类似工具提示的效果）：

**悬停到我上面来显示 <p> 元素。**

### 实例

p {
 display: none;
 background-color: yellow;
 padding: 20px;
}

div:hover p {
 display: block;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_pseudo-class_hover_tooltip)

------

## CSS - :first-child 伪类

:first-child 伪类与指定的元素匹配：该元素是另一个元素的第一个子元素。

匹配首个 <p> 元素

在下面的例子中，选择器匹配作为任何元素的第一个子元素的任何 <p> 元素：

### 实例

p:first-child {
 color: blue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_first-child1)

------

## 匹配所有 <p> 元素中的首个 <i> 元素

在下面的例子中，选择器匹配所有 <p> 元素中的第一个 <i> 元素：

### 实例

p i:first-child {
 color: blue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_first-child2)

------

## 匹配所有首个 <p> 元素中的所有 <i> 元素

在下面的例子中，选择器匹配作为另一个元素的第一个子元素的 <p> 元素中的所有 <i> 元素：

### 实例

p:first-child i {
 color: blue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_first-child3)

------

## CSS - :lang 伪类

:lang 伪类允许您为不同的语言定义特殊的规则。

在下面的例子中，:lang 为属性为 lang="en" 的 <q> 元素定义引号：

### 实例

<html>
<head>
<style>
q:lang(no) {
 quotes: "~" "~";
}
</style>
</head>
<body>

<p>Some text <q lang="no">A quote in a paragraph</q> Some text.</p>

</body>
</html>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_lang)

------

## 更多实例

[为超链接添加不同样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link2)
本例演示如何向超链接添加其他样式。

[使用 :focus](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link_focus)
本例演示如何使用 :focus 伪类。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_pseudo_classes1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_pseudo_classes2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_pseudo_classes3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_pseudo_classes4)

------

## 所有 CSS 伪类

<

| 选择器                                                       | 实例                  | 实例描述                                                     |
| :----------------------------------------------------------- | :-------------------- | :----------------------------------------------------------- |
| [:active](https://www.w3schools.cn/cssref/sel_active.html)   | a:active              | 选择活动的链接。                                             |
| [:checked](https://www.w3schools.cn/cssref/sel_checked.html) | input:checked         | 选择每个被选中的 <input> 元素。                              |
| [:disabled](https://www.w3schools.cn/cssref/sel_disabled.html) | input:disabled        | 选择每个被禁用的 <input> 元素。                              |
| [:empty](https://www.w3schools.cn/cssref/sel_empty.html)     | p:empty               | 选择没有子元素的每个 <p> 元素。                              |
| [:enabled](https://www.w3schools.cn/cssref/sel_enabled.html) | input:enabled         | 选择每个已启用的 <input> 元素。                              |
| [:first-child](https://www.w3schools.cn/cssref/sel_firstchild.html) | p:first-child         | 选择作为其父的首个子元素的每个 <p> 元素。                    |
| [:first-of-type](https://www.w3schools.cn/cssref/sel_first-of-type.html) | p:first-of-type       | 选择作为其父的首个 <p> 元素的每个 <p> 元素。                 |
| [:focus](https://www.w3schools.cn/cssref/sel_focus.html)     | input:focus           | 选择获得焦点的 <input> 元素。                                |
| [:hover](https://www.w3schools.cn/cssref/sel_hover.html)     | a:hover               | 选择鼠标悬停其上的链接。                                     |
| [:in-range](https://www.w3schools.cn/cssref/sel_in-range.html) | input:in-range        | 选择具有指定范围内的值的 <input> 元素。                      |
| [:invalid](https://www.w3schools.cn/cssref/sel_invalid.html) | input:invalid         | 选择所有具有无效值的 <input> 元素。                          |
| [:lang(*language*)](https://www.w3schools.cn/cssref/sel_lang.html) | p:lang(it)            | 选择每个 lang 属性值以 "it" 开头的 <p> 元素。                |
| [:last-child](https://www.w3schools.cn/cssref/sel_last-child.html) | p:last-child          | 选择作为其父的最后一个子元素的每个 <p> 元素。                |
| [:last-of-type](https://www.w3schools.cn/cssref/sel_last-of-type.html) | p:last-of-type        | 选择作为其父的最后一个 <p> 元素的每个 <p> 元素。             |
| [:link](https://www.w3schools.cn/cssref/sel_link.html)       | a:link                | 选择所有未被访问的链接。                                     |
| [:not(selector)](https://www.w3schools.cn/cssref/sel_not.html) | :not(p)               | 选择每个非 <p> 元素的元素。                                  |
| [:nth-child(n)](https://www.w3schools.cn/cssref/sel_nth-child.html) | p:nth-child(2)        | 选择作为其父的第二个子元素的每个 <p> 元素。                  |
| [:nth-last-child(n)](https://www.w3schools.cn/cssref/sel_nth-last-child.html) | p:nth-last-child(2)   | 选择作为父的第二个子元素的每个<p>元素，从最后一个子元素计数。 |
| [:nth-last-of-type(n)](https://www.w3schools.cn/cssref/sel_nth-last-of-type.html) | p:nth-last-of-type(2) | 选择作为父的第二个<p>元素的每个<p>元素，从最后一个子元素计数 |
| [:nth-of-type(n)](https://www.w3schools.cn/cssref/sel_nth-of-type.html) | p:nth-of-type(2)      | 选择作为其父的第二个 <p> 元素的每个 <p> 元素。               |
| [:only-of-type](https://www.w3schools.cn/cssref/sel_only-of-type.html) | p:only-of-type        | 选择作为其父的唯一 <p> 元素的每个 <p> 元素。                 |
| [:only-child](https://www.w3schools.cn/cssref/sel_only-child.html) | p:only-child          | 选择作为其父的唯一子元素的 <p> 元素。                        |
| [:optional](https://www.w3schools.cn/cssref/sel_optional.html) | input:optional        | 选择不带 "required" 属性的 <input> 元素。                    |
| [:out-of-range](https://www.w3schools.cn/cssref/sel_out-of-range.html) | input:out-of-range    | 选择值在指定范围之外的 <input> 元素。                        |
| [:read-only](https://www.w3schools.cn/cssref/sel_read-only.html) | input:read-only       | 选择指定了 "readonly" 属性的 <input> 元素。                  |
| [:read-write](https://www.w3schools.cn/cssref/sel_read-write.html) | input:read-write      | 选择不带 "readonly" 属性的 <input> 元素。                    |
| [:required](https://www.w3schools.cn/cssref/sel_required.html) | input:required        | 选择指定了 "required" 属性的 <input> 元素。                  |
| [:root](https://www.w3schools.cn/cssref/sel_root.html)       | root                  | 选择元素的根元素。                                           |
| [:target](https://www.w3schools.cn/cssref/sel_target.html)   | #news:target          | 选择当前活动的 #news 元素（单击包含该锚名称的 URL）。        |
| [:valid](https://www.w3schools.cn/cssref/sel_valid.html)     | input:valid           | 选择所有具有有效值的 <input> 元素。                          |
| [:visited](https://www.w3schools.cn/cssref/sel_visited.html) | a:visited             | 选择所有已访问的链接。                                       |

## 所有 CSS 伪元素

| 选择器                                                       | 实例            | 实例描述                      |
| :----------------------------------------------------------- | :-------------- | :---------------------------- |
| [::after](https://www.w3schools.cn/cssref/sel_after.html)    | p::after        | 在每个 <p> 元素之后插入内容。 |
| [::before](https://www.w3schools.cn/cssref/sel_before.html)  | p::before       | 在每个 <p> 元素之前插入内容。 |
| [::first-letter](https://www.w3schools.cn/cssref/sel_firstletter.html) | p::first-letter | 选择每个 <p> 元素的首字母。   |
| [::first-line](https://www.w3schools.cn/cssref/sel_firstline.html) | p::first-line   | 选择每个 <p> 元素的首行。     |
| [::selection](https://www.w3schools.cn/cssref/sel_selection.html) | p::selection    | 选择用户选择的元素部分。      |



# CSS 伪元素

[❮ 上一节](https://www.w3schools.cn/css/css_pseudo_classes.html)[下一节 ❯](https://www.w3schools.cn/css/css_image_transparency.html)

------

## 什么是伪元素？

CSS 伪元素用于设置元素指定部分的样式。

例如，它可用于：

- 设置元素的首字母、首行的样式
- 在元素的内容之前或之后插入内容

------

## 语法

伪元素的语法：

selector::pseudo-element {
 property: value;
}

------

## ::first-line 伪元素

::first-line 伪元素用于向文本的首行添加特殊样式。

下面的例子为所有 <p> 元素中的首行添加样式：

### Example 

p::first-line {
 color: #ff0000;
 font-variant: small-caps;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_firstline)

**注释:** `::first-line` 伪元素只能应用于块级元素。

以下属性适用于 ::first-line 伪元素：

- 字体属性
- 颜色属性
- 背景属性
- word-spacing
- letter-spacing
- text-decoration
- vertical-align
- text-transform
- line-height
- clear

请注意**双冒号表示法** - ::first-line 对比 :first-line

在 CSS3 中，双冒号取代了伪元素的单冒号表示法。这是 W3C 试图区分**伪类**和**伪元素**的尝试。

在 CSS2 和 CSS1 中，伪类和伪元素都使用了单冒号语法。

为了向后兼容，CSS2 和 CSS1 伪元素可接受单冒号语法。

------

------

## ::first-letter 伪元素

::first-letter 伪元素用于向文本的首字母添加特殊样式。

下面的例子设置所有 <p> 元素中文本的首字母格式：

### 实例

p::first-letter {
 color: #ff0000;
 font-size: xx-large;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_firstletter)

**注释:** `::first-letter` 伪元素只适用于块级元素。

下面的属性适用于 ::first-letter 伪元素：

- 字体属性
- 颜色属性
- 背景属性
- 外边距属性
- 内边距属性
- 边框属性
- text-decoration
- vertical-align（仅当 "float" 为 "none"）
- text-transform
- line-height
- float
- clear

------

## 伪元素和 CSS 类

伪元素可以与 CSS 类结合使用：

### 实例

p.intro::first-letter {
 color: #ff0000;
 font-size: 200%;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_pseudo-element)

上面的例子将以红色和较大的字体显示 class="intro" 的段落的首字母。

------

## 多个伪元素

也可以组合几个伪元素。

在下面的例子中，段落的第一个字母将是红色，字体大小为 xx-large。第一行的其余部分将变为蓝色，并使用小型大写字母。该段的其余部分将是默认的字体大小和颜色：

### 实例

p::first-letter {
 color: #ff0000;
 font-size: xx-large;
}

p::first-line {
 color: #0000ff;
 font-variant: small-caps;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_firstline_letter)

------

## CSS - ::before 伪元素

::before 伪元素可用于在元素内容之前插入一些内容。

下面的例子在每个 <h1> 元素的内容之前插入一幅图像：

### 实例

h1::before {
 content: url(smiley.gif);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_before)

------

## CSS - ::after 伪元素

::after 伪元素可用于在元素内容之后插入一些内容。

下面的例子在每个 <h1> 元素的内容之后插入一幅图像：

### 实例

h1::after {
 content: url(smiley.gif);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_after)

------

## CSS - ::selection 伪元素

::selection 伪元素匹配用户选择的元素部分。

以下 CSS 属性可以应用于 ::selection：

- color
- background
- cursor
- outline

下例使所选文本在黄色背景上显示为红色：

### 实例

::selection {
 color: red;
 background: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_selection)

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_pseudo_elements1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_pseudo_elements2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_pseudo_elements3)

------

## 所有 CSS 伪元素

| 选择器                                                       | 实例            | 实例描述                      |
| :----------------------------------------------------------- | :-------------- | :---------------------------- |
| [::after](https://www.w3schools.cn/cssref/sel_after.html)    | p::after        | 在每个 <p> 元素之后插入内容。 |
| [::before](https://www.w3schools.cn/cssref/sel_before.html)  | p::before       | 在每个 <p> 元素之前插入内容。 |
| [::first-letter](https://www.w3schools.cn/cssref/sel_firstletter.html) | p::first-letter | 选择每个 <p> 元素的首字母。   |
| [::first-line](https://www.w3schools.cn/cssref/sel_firstline.html) | p::first-line   | 选择每个 <p> 元素的首行。     |
| [::selection](https://www.w3schools.cn/cssref/sel_selection.html) | p::selection    | 选择用户选择的元素部分。      |

## 所有 CSS 伪类

<

| 选择器                                                       | 实例                  | 实例描述                                                     |
| :----------------------------------------------------------- | :-------------------- | :----------------------------------------------------------- |
| [:active](https://www.w3schools.cn/cssref/sel_active.html)   | a:active              | 选择活动的链接。                                             |
| [:checked](https://www.w3schools.cn/cssref/sel_checked.html) | input:checked         | 选择每个被选中的 <input> 元素。                              |
| [:disabled](https://www.w3schools.cn/cssref/sel_disabled.html) | input:disabled        | 选择每个被禁用的 <input> 元素。                              |
| [:empty](https://www.w3schools.cn/cssref/sel_empty.html)     | p:empty               | 选择没有子元素的每个 <p> 元素。                              |
| [:enabled](https://www.w3schools.cn/cssref/sel_enabled.html) | input:enabled         | 选择每个已启用的 <input> 元素。                              |
| [:first-child](https://www.w3schools.cn/cssref/sel_firstchild.html) | p:first-child         | 选择作为其父的首个子元素的每个 <p> 元素。                    |
| [:first-of-type](https://www.w3schools.cn/cssref/sel_first-of-type.html) | p:first-of-type       | 选择作为其父的首个 <p> 元素的每个 <p> 元素。                 |
| [:focus](https://www.w3schools.cn/cssref/sel_focus.html)     | input:focus           | 选择获得焦点的 <input> 元素。                                |
| [:hover](https://www.w3schools.cn/cssref/sel_hover.html)     | a:hover               | 选择鼠标悬停其上的链接。                                     |
| [:in-range](https://www.w3schools.cn/cssref/sel_in-range.html) | input:in-range        | 选择具有指定范围内的值的 <input> 元素。                      |
| [:invalid](https://www.w3schools.cn/cssref/sel_invalid.html) | input:invalid         | 选择所有具有无效值的 <input> 元素。                          |
| [:lang(*language*)](https://www.w3schools.cn/cssref/sel_lang.html) | p:lang(it)            | 选择每个 lang 属性值以 "it" 开头的 <p> 元素。                |
| [:last-child](https://www.w3schools.cn/cssref/sel_last-child.html) | p:last-child          | 选择作为其父的最后一个子元素的每个 <p> 元素。                |
| [:last-of-type](https://www.w3schools.cn/cssref/sel_last-of-type.html) | p:last-of-type        | 选择作为其父的最后一个 <p> 元素的每个 <p> 元素。             |
| [:link](https://www.w3schools.cn/cssref/sel_link.html)       | a:link                | 选择所有未被访问的链接。                                     |
| [:not(selector)](https://www.w3schools.cn/cssref/sel_not.html) | :not(p)               | 选择每个非 <p> 元素的元素。                                  |
| [:nth-child(n)](https://www.w3schools.cn/cssref/sel_nth-child.html) | p:nth-child(2)        | 选择作为其父的第二个子元素的每个 <p> 元素。                  |
| [:nth-last-child(n)](https://www.w3schools.cn/cssref/sel_nth-last-child.html) | p:nth-last-child(2)   | 选择作为父的第二个子元素的每个<p>元素，从最后一个子元素计数。 |
| [:nth-last-of-type(n)](https://www.w3schools.cn/cssref/sel_nth-last-of-type.html) | p:nth-last-of-type(2) | 选择作为父的第二个<p>元素的每个<p>元素，从最后一个子元素计数 |
| [:nth-of-type(n)](https://www.w3schools.cn/cssref/sel_nth-of-type.html) | p:nth-of-type(2)      | 选择作为其父的第二个 <p> 元素的每个 <p> 元素。               |
| [:only-of-type](https://www.w3schools.cn/cssref/sel_only-of-type.html) | p:only-of-type        | 选择作为其父的唯一 <p> 元素的每个 <p> 元素。                 |
| [:only-child](https://www.w3schools.cn/cssref/sel_only-child.html) | p:only-child          | 选择作为其父的唯一子元素的 <p> 元素。                        |
| [:optional](https://www.w3schools.cn/cssref/sel_optional.html) | input:optional        | 选择不带 "required" 属性的 <input> 元素。                    |
| [:out-of-range](https://www.w3schools.cn/cssref/sel_out-of-range.html) | input:out-of-range    | 选择值在指定范围之外的 <input> 元素。                        |
| [:read-only](https://www.w3schools.cn/cssref/sel_read-only.html) | input:read-only       | 选择指定了 "readonly" 属性的 <input> 元素。                  |
| [:read-write](https://www.w3schools.cn/cssref/sel_read-write.html) | input:read-write      | 选择不带 "readonly" 属性的 <input> 元素。                    |
| [:required](https://www.w3schools.cn/cssref/sel_required.html) | input:required        | 选择指定了 "required" 属性的 <input> 元素。                  |
| [:root](https://www.w3schools.cn/cssref/sel_root.html)       | root                  | 选择元素的根元素。                                           |
| [:target](https://www.w3schools.cn/cssref/sel_target.html)   | #news:target          | 选择当前活动的 #news 元素（单击包含该锚名称的 URL）。        |
| [:valid](https://www.w3schools.cn/cssref/sel_valid.html)     | input:valid           | 选择所有具有有效值的 <input> 元素。                          |
| [:visited](https://www.w3schools.cn/cssref/sel_visited.html) | a:visited             | 选择所有已访问的链接。                                       |

# CSS 图像不透明度 / 透明度

[❮ 上一节](https://www.w3schools.cn/css/css_pseudo_elements.html)[下一节 ❯](https://www.w3schools.cn/css/css_navbar.html)

------

`opacity` 属性指定元素的不透明度/透明度。

------

## 透明图像

opacity 属性的取值范围为 0.0-1.0。值越低，越透明：

![Forest](https://www.w3schools.cn/css/img_forest.jpg)

opacity 0.2

![Forest](https://www.w3schools.cn/css/img_forest.jpg)

opacity 0.5

![Forest](https://www.w3schools.cn/css/img_forest.jpg)

opacity 1
(default)

### 实例

img {
 opacity: 0.5;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_opacity)

------

## 透明悬停效果

opacity 属性通常与 :hover 选择器一同使用，这样就可以在鼠标悬停时更改不透明度：

![Northern Lights](https://www.w3schools.cn/css/img_lights.jpg)

![Mountains](https://www.w3schools.cn/css/img_mountains.jpg)

![Italy](https://www.w3schools.cn/css/img_5terre.jpg)

### 实例

img {
 opacity: 0.5;
}

img:hover {
 opacity: 1.0;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_transparency)

### 实例解析

第一个 CSS 块类似于实例 1 中的代码。此外，我们还添加了当用户将鼠标悬停在其中一个图像上时的效果。在这种情况下，当用户将鼠标悬停在图像上时，我们希望图像不透明。这条 CSS 是 opacity:1;。

当鼠标指针离开图像时，图像将再次透明。

反向悬停效果的例子：

![Northern Lights](https://www.w3schools.cn/css/img_lights.jpg)

![Mountains](https://www.w3schools.cn/css/img_mountains.jpg)

![Italy](https://www.w3schools.cn/css/img_5terre.jpg)

### 实例

img:hover {
 opacity: 0.5;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_transparency2)

------

------

## 透明盒

使用 opacity 属性为元素的背景添加透明度时，其所有子元素都继承相同的透明度。这可能会使完全透明的元素内的文本难以阅读：

opacity 1

opacity 0.6

opacity 0.3

opacity 0.1

### 实例

div {
 opacity: 0.3;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_opacity_box)

------

## 使用 RGBA 的透明度

如果您不希望对子元素应用不透明度，如上面的例子，请使用 RGBA 颜色值。下面的例子设置背景色而不是文本的不透明度：

100% opacity

60% opacity

30% opacity

10% opacity

您已经从我们的 [CSS 颜色](https://www.w3schools.cn/css/css_colors.html) 这一章中学到了可以将 RGB 用作颜色值。除 RGB 外，还可以将 RGB 颜色值与 alpha 通道（RGBA）一起使用 - 该通道规定颜色的不透明度。

RGBA 颜色值指定为：rgba(*red*, *green*, *blue*, *alpha*)。 *alpha* 参数是介于 0.0（完全透明）和 1.0（完全不透明）之间的数字。

提示：您将在我们的 [CSS 颜色](https://www.w3schools.cn/css/css3_colors.html) 这一章中学到有关 RGBA 颜色的更多知识。

### 实例

div {
 background: rgba(76, 175, 80, 0.3) /* 不透明度为 30% 的绿色背景 */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_opacity_box2)

------

## 透明盒中的文本

这是一些位于透明框中的文本。

### 实例

<html><head><style>div.background {  background: url(klematis.jpg) repeat;  border: 2px solid black;}div.transbox {  margin: 30px;  background-color: #ffffff;  border: 1px solid black;  opacity: 0.6;}div.transbox p {  margin: 5%;  font-weight: bold;  color: #000000;}</style></head><body><div class="background">  <div class="transbox">    <p>This is some text that is placed in the transparent box.</p>  </div></div></body></html>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_transparency)

## 实例说明

首先，我们创建一个带有背景图像和边框的 <div> 元素（class="background"）。

然后，我们在第一个 <div> 中创建另一个 <div>（class="transbox"）。

<div class="transbox"> 有背景色和边框 - 这个 div 是透明的。

在透明的 <div> 内，我们在 <p> 元素内添加了一些文本。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_image_transparency1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_image_transparency2)



# CSS 导航栏

[❮ 上一节](https://www.w3schools.cn/css/css_image_transparency.html)[下一节 ❯](https://www.w3schools.cn/css/css_navbar_vertical.html)

------

## Demo：导航栏

垂直导航栏

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

水平导航栏

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))



- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

------

## 导航栏

易用的导航对于任何网站都很重要。

通过使用 CSS，您可以将无聊的 HTML 菜单转换为美观的导航栏。

------

## 导航栏 = 链接列表

导航栏需要标准 HTML 作为基础。

在我们的实例中，将用标准的 HTML 列表构建导航栏。

导航栏基本上就是链接列表，因此使用 <ul> 和 <li> 元素会很有意义：

### 实例

<ul>  <li><a href="default.asp">Home</a></li>  <li><a href="news.asp">News</a></li>  <li><a href="contact.asp">Contact</a></li>  <li><a href="about.asp">About</a></li></ul>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_basic_html)

现在，从列表中删除项目符号以及外边距和内边距（填充）：

### 实例

ul {
 list-style-type: none;
 margin: 0;
 padding: 0;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_basic_css)

实例说明:

- list-style-type: none; - 删除项目符号。导航条不需要列表项标记。
- 设置 margin: 0; 和 padding: 0; 删除浏览器的默认设置。

上例中的代码是垂直和水平导航栏中使用的标准代码，您将在下一章中学习更多内容。

------

# CSS 垂直导航栏

[❮ 上一节](https://www.w3schools.cn/css/css_navbar.html)[下一节 ❯](https://www.w3schools.cn/css/css_navbar_horizontal.html)

------

## 垂直导航栏

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

如需构建垂直导航栏，除了上一章中的代码外，还可以在列表中设置 <a> 元素的样式：

### 实例

li a {
 display: block;
 width: 60px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_vertical)

实例说明:

- display: block; - 将链接显示为块元素可以使整个链接区域都可以被单击（而不仅仅是文本），我们还可以指定宽度（如果需要，还可以指定内边距、外边距、高度等）。
- width: 60px; - 默认情况下，块元素会占用全部可用宽度。我们需要指定 60 像素的宽度。

您还可以设置 <ul> 的宽度，并删除 <a> 的宽度，因为当显示为块元素时，它们将占据可用的全部宽度。这将导致与我们之前的例子相同的结果：

### 实例

ul {
 list-style-type: none;
 margin: 0;
 padding: 0;
 width: 60px;
}

li a {
 display: block;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_vertical2)

------

## 垂直导航栏实例

创建背景色为灰色的基础垂直导航栏，并在用户将鼠标移到链接上时改变链接的背景色：

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

### 实例

ul {
 list-style-type: none;
 margin: 0;
 padding: 0;
 width: 200px;
 background-color: #f1f1f1;
}

li a {
 display: block;
 color: #000;
 padding: 8px 16px;
 text-decoration: none;
}

/* 更改悬停时的链接颜色 */
li a:hover {
 background-color: #555;
 color: white;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_vertical_gray)

### 活动/当前导航链接

向当前链接添加 "active" 类，以使用户知道他/她在哪个页面上：

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

### 实例

.active {
 background-color: #4CAF50;
 color: white;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_vertical_active)

### 居中链接以及添加边框

把 text-align:center 添加到 <li> 或 <a>，使链接居中。

将 border 属性添加到 <ul>，在导航栏周围添加边框。如果您还希望在导航栏内添加边框，请为所有 <li> 元素添加 border-bottom，最后一个元素除外：

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

### 实例

ul {
 border: 1px solid #555;
}

li {
 text-align: center;
 border-bottom: 1px solid #555;
}

li:last-child {
 border-bottom: none;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_vertical_borders)

### 全高固定垂直导航栏

创建全高的"粘性"侧面导航：

<iframe src="https://www.w3schools.cn/css/trycss_navbar_vertical_iframe.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; height: 262px; width: 869.984px; border-top: 3px solid rgb(241, 241, 241); border-right: 3px solid rgb(241, 241, 241); border-bottom: 3px solid rgb(241, 241, 241); border-image: initial; border-left: none;"></iframe>



### 实例

ul {
 list-style-type: none;
 margin: 0;
 padding: 0;
 width: 25%;
 background-color: #f1f1f1;
 height: 100%; /* 全高 */
 position: fixed; /* 使它产生粘性，即使在滚动时 */
 overflow: auto; /* 如果侧栏的内容太多，则启用滚动条 */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_vertical_fixed)

**注释:** 本例在移动设备上可能无法正常工作。

# CSS 水平导航栏

[❮ 上一节](https://www.w3schools.cn/css/css_navbar_vertical.html)[下一节 ❯](https://www.w3schools.cn/css/css_dropdowns.html)

------

## 水平导航栏

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

有两种创建水平导航栏的方法：使用**行内**或**浮动**列表项。

### 行内列表项

构建水平导航栏的一种方法是，除了上一章中的"标准"代码外，还要将 <li> 元素指定为 inline：

### 实例

li {
 display: inline;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal)

实例说明:

- ```
  display: inline;
  ```

   

  \- 默认情况下，<li> 元素是块元素。在这里，我们删除每个列表项之前和之后的换行符，这样它们才能显示在一行。

  

### 浮动列表项

创建水平导航栏的另一种方法是浮动 <li> 元素，并为导航链接规定布局：

### 实例

li {
 float: left;
}

a {
 display: block;
 padding: 8px;
 background-color: #dddddd;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_float)

实例说明:

- float: left; - 使用 float 使块元素滑动为彼此相邻
- display: block; - 将链接显示为块元素可以使整个链接区域都可单击（不仅是文本），而且允许我们指定填充（如果需要，还可以指定高度，宽度，边距等）
- padding: 8px; - 使块元素更美观
- background-color: #dddddd; - 为每个元素添加灰色背景色

**提示:** 如需全宽的背景色，请将 background-color 添加到 <ul> 而不是每个 <a> 元素：

### 实例

ul {
 background-color: #dddddd;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_float2)

------

## 水平导航栏实例

创建具有深色背景色的基础水平导航栏，并在用户将鼠标移到链接上方时改变链接的背景色：

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

### 实例

ul {
 list-style-type: none;
 margin: 0;
 padding: 0;
 overflow: hidden;
 background-color: #333;
}

li {
 float: left;
}

li a {
 display: block;
 color: white;
 text-align: center;
 padding: 14px 16px;
 text-decoration: none;
}

/* 悬停时将链接颜色更改为#111（黑色） */
li a:hover {
 background-color: #111;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_black)

### 活动/当前导航链接

向当前链接添加 "active" 类，这样用户就知道他/她在哪个页面上：

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

### 实例

.active {
 background-color: #4CAF50;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_black_active)

### 右对齐链接

通过将列表项向右浮动来右对齐链接（float:right;）：

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

### 实例

<ul>  <li><a href="#home">Home</a></li>  <li><a href="#news">News</a></li>  <li><a href="#contact">Contact</a></li>  <li style="float:right"><a class="active" href="#about">About</a></li></ul>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_black_right)

### 边框分隔栏

将 border-right 属性添加到 <li>，以创建链接分隔符：

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

### 实例

/* 为所有列表项添加灰色右边框，最后一项（last-child）除
li {
 border-right: 1px solid #bbb;
}

li:last-child {
 border-right: none;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_dividers)

### 固定的导航栏

使导航栏保持在页面的顶部或底部，即使用户滚动页面也是如此：

<iframe src="https://www.w3schools.cn/css/trycss_navbar_horizontal_iframe.htm" style="box-sizing: inherit; height: 262px; width: 408.875px; border: none;"></iframe>

### 固定在顶部

ul {
 position: fixed;
 top: 0;
 width: 100%;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_black_fixed)

<iframe src="https://www.w3schools.cn/css/trycss_navbar_horizontal_iframe2.htm" style="box-sizing: inherit; height: 262px; width: 408.875px; border: none;"></iframe>

### 固定在底部

ul {
 position: fixed;
 bottom: 0;
 width: 100%;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_black_fixed2)

**注释:** 固定定位在移动设备上可能无法正常工作。

### 灰色水平导航栏

带有细灰色边框的灰色水平导航栏的实例

- [Home](javascript:void(0))
- [News](javascript:void(0))
- [Contact](javascript:void(0))
- [About](javascript:void(0))

### 实例

ul {
 border: 1px solid #e7e7e7;
 background-color: #f3f3f3;
}

li a {
 color: #666;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_gray)

### 粘性导航栏

为 <ul> 添加 position: sticky;，以创建粘性导航栏。

粘性元素会根据滚动位置在相对和固定之间切换。它是相对定位的，直到在视口中遇到给定的偏移位置为止 - 然后将其"粘贴"在适当的位置（比如 position:fixed）。

<iframe src="https://www.w3schools.cn/howto/tryhow_js_navbar_sticky.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; width: 869.984px; border: 3px solid rgb(233, 233, 233); height: 400px; padding: 0px;"></iframe>

### 实例

ul {
 position: -webkit-sticky; /* Safari */
 position: sticky;
 top: 0;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_sticky)

**注意:** Internet Explorer、Edge 15 和更早版本不支持粘性定位。 Safari 需要 -webkit- 前缀（请参见上面的例子）。您还必须指定 top、right、bottom 或 left 至少之一，以使粘性定位起作用。

------

## 更多实例

### 响应式的上导航栏

如何使用 CSS 媒体查询来创建响应式顶部导航。

![img](https://www.w3schools.cn/css/navbar_responsive_hor.jpg)

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_responsive)

### 响应式的侧导航栏

如何使用 CSS 媒体查询来创建响应式侧导航。

![img](https://www.w3schools.cn/css/navbar_responsive_ver.jpg)

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_vertical_responsive)

### 下拉式导航栏

如何在导航栏中添加下拉菜单。

<iframe src="https://www.w3schools.cn/css/trycss_dropdown_navbar.htm" style="box-sizing: inherit; width: 869.984px; border: none; height: 200px;"></iframe>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dropdown_navbar)



# CSS 下拉菜单

[❮ 上一节](https://www.w3schools.cn/css/css_navbar_horizontal.html)[下一节 ❯](https://www.w3schools.cn/css/css_image_gallery.html)

------

使用 CSS 创建可悬停的下拉列表。

------

## 演示：下拉式案例

请把鼠标指针移动到下面的例子上：

下拉文本

下拉菜单

Other: ![Cinque Terre](https://www.w3schools.cn/css/img_5terre.jpg)



------

## 基础的下拉菜单

创建当用户将鼠标移到元素上时出现的下拉框。

### 实例

<style>.dropdown {  position: relative;  display: inline-block;}.dropdown-content {  display: none;  position: absolute;  background-color: #f9f9f9;  min-width: 160px;  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);  padding: 12px 16px;  z-index: 1;}.dropdown:hover .dropdown-content {  display: block;}</style><div class="dropdown">  <span>Mouse over me</span>  <div class="dropdown-content">    <p>Hello World!</p>  </div></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dropdown_text)

### 实例解析

#### HTML

使用任何元素打开下拉菜单内容，例如 <span> 或 <button> 元素。

使用容器元素（如 <div>）创建下拉内容，并在其中添加任何内容。

用 <div> 元素包围这些元素，使用 CSS 正确定位下拉内容。

#### CSS

`.dropdown` 类使用 `position:relative`，当我们希望将下拉内容放置在下拉按钮的正下方（使用 `position:absolute`）时，需要使用该类。

.dropdown-content 类保存实际的下拉菜单内容。默认情况下它是隐藏的，并将在悬停时显示（请看下文）。请注意，min-width 设置为 160px。可随时更改此设置。提示：如果您希望下拉内容的宽度与下拉按钮的宽度一样，请将宽度设置为 100％（设置 overflow:auto 可实现在小屏幕上滚动）。

我们用了 CSS box-shadow 属性，而不是边框，这样下拉菜单看起来像一张"卡片"。

当用户将鼠标移到下拉按钮上时，:hover 选择器用于显示下拉菜单。

------

------

## 下拉式菜单

创建一个下拉菜单，并允许用户从列表中选择一个选项：

下拉菜单



本例与上例相似，除了我们在下拉框内添加链接并为其设置了样式，以此匹配下拉按钮的样式：

### 实例

<style>/* 为下拉按钮设置样式 */.dropbtn {  background-color: #4CAF50;  color: white;  padding: 16px;  font-size: 16px;  border: none;  cursor: pointer;}/* 容器 <div> - 需要定位下拉内容 */.dropdown {  position: relative;  display: inline-block;}/* 下拉内容（默认隐藏）*/.dropdown-content {  display: none;  position: absolute;  background-color: #f9f9f9;  min-width: 160px;  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);  z-index: 1;}/* 下拉列表中的链接 */.dropdown-content a {  color: black;  padding: 12px 16px;  text-decoration: none;  display: block;}/* 更改悬停时下拉链接的颜色 */.dropdown-content a:hover {background-color: #f1f1f1}/* 悬停时显示下拉菜单 */.dropdown:hover .dropdown-content {  display: block;}/* 显示下拉内容时更改下拉按钮的背景颜色 */.dropdown:hover .dropbtn {  background-color: #3e8e41;}</style><div class="dropdown">  <button class="dropbtn">Dropdown</button>  <div class="dropdown-content">    <a href="#">Link 1</a>    <a href="#">Link 2</a>    <a href="#">Link 3</a>  </div></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dropdown_button)

------

## 右对齐的下拉菜单内容

Left

Right



如果希望下拉菜单从右到左而不是从左到右，请添加 right: 0;：

### 实例

.dropdown-content {
 right: 0;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dropdown_right)

------

## 更多实例

### 下拉式图像

如何在下拉框中添加图像和其他内容。

请把鼠标指针悬停在图像上：

![Cinque Terre](https://www.w3schools.cn/css/img_5terre.jpg)



[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dropdown_image)

### 下拉式导航

如何在导航栏中添加下拉菜单。

<iframe src="https://www.w3schools.cn/css/trycss_dropdown_navbar.htm" style="box-sizing: inherit; width: 869.984px; border: none; height: 200px;"></iframe>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dropdown_navbar)



[❮ 上一节](https://www.w3schools.cn/css/css_navbar_horizontal.html)[下一节 ❯](https://www.w3schools.cn/css/css_image_gallery.html)

# CSS 图片库

[❮ 上一节](https://www.w3schools.cn/css/css_dropdowns.html)[下一节 ❯](https://www.w3schools.cn/css/css_image_sprites.html)

------

CSS 可用于创建图片库。

[![五渔村](https://www.w3schools.cn/css/img_5terre.jpg)](https://www.w3schools.cn/css/img_5terre.jpg)

在此处添加图片说明

[![森林](https://www.w3schools.cn/css/img_forest.jpg)](https://www.w3schools.cn/css/img_forest.jpg)

在此处添加图片说明

[![北极光](https://www.w3schools.cn/css/img_lights.jpg)](https://www.w3schools.cn/css/img_lights.jpg)

在此处添加图片说明

[![山](https://www.w3schools.cn/css/img_mountains.jpg)](https://www.w3schools.cn/css/img_mountains.jpg)

在此处添加图片说明

------

## 图片库

下面这个图片库是使用 CSS 创建的：

### 实例

<html><head><style>div.gallery {  margin: 5px;  border: 1px solid #ccc;  float: left;  width: 180px;}div.gallery:hover {  border: 1px solid #777;}div.gallery img {  width: 100%;  height: auto;}div.desc {  padding: 15px;  text-align: center;}</style></head><body><div class="gallery">  <a target="_blank" href="img_5terre.jpg">    <img src="img_5terre.jpg" alt="Cinque Terre" width="600" height="400">  </a>  <div class="desc">Add a description of the image here</div></div><div class="gallery">  <a target="_blank" href="img_forest.jpg">    <img src="img_forest.jpg" alt="Forest" width="600" height="400">  </a>  <div class="desc">Add a description of the image here</div></div><div class="gallery">  <a target="_blank" href="img_lights.jpg">    <img src="img_lights.jpg" alt="Northern Lights" width="600" height="400">  </a>  <div class="desc">Add a description of the image here</div></div><div class="gallery">  <a target="_blank" href="img_mountains.jpg">    <img src="img_mountains.jpg" alt="Mountains" width="600" height="400">  </a>  <div class="desc">Add a description of the image here</div></div></body></html>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_gallery)

------

## 更多实例

### 响应式图库

如何使用 CSS 媒体查询创建响应式图库，在台式机、平板电脑和智能手机上看起来都不错。

![img](https://www.w3schools.cn/css/responsiveImgGallery.jpg)

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_gallery_responsive)

# CSS 图像精灵

[❮ 上一节](https://www.w3schools.cn/css/css_image_gallery.html)[下一节 ❯](https://www.w3schools.cn/css/css_attribute_selectors.html)

------

## 图像精灵

图像精灵是单个图像中包含的图像集合。

包含许多图像的网页可能需要很长时间才能加载，同时会生成多个服务器请求。

使用图像精灵将减少服务器请求的数量并节约带宽。

------

## 图像精灵 - 简单的例子

我们使用以下单幅图像（"navsprites.gif"）而不是使用三幅单独的图像：

![navigation images](https://www.w3schools.cn/css/img_navsprites.gif)

通过使用 CSS，我们可以仅显示所需图像的某个部分。

在下面的例子中，CSS 指定了显示 "navsprites.gif" 图像的哪部分：

### 实例

\#home {
 width: 46px;
 height: 44px;
 background: url(img_navsprites.gif) 0 0;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sprites_img)

**实例解析:**

- <img id="home" src="trans.gif"> - 仅定义小的透明图像，因为 src 属性不能为空。而实际显示的图像将是我们在 CSS 中指定的背景图像。
- width: 46px; height: 44px; - 定义我们要使用的图像部分
- background: url(navsprites.gif) 0 0; - 定义背景图片及其位置（left 0px, top 0px）

This is the easiest way to use image sprites, now we want to expand it by using links and hover effects.

------

## 图像精灵 - 创建导航列表

我们希望使用精灵图片（"navsprites.gif"）来创建一个导航列表。

我们将使用 HTML 列表，因为它可以是链接，同时还支持背景图片：

### 实例

\#navlist {
 position: relative;
}

\#navlist li {
 margin: 0;
 padding: 0;
 list-style: none;
 position: absolute;
 top: 0;
}

\#navlist li, #navlist a {
 height: 44px;
 display: block;
}

\#home {
 left: 0px;
 width: 46px;
 background: url('img_navsprites.gif') 0 0;
}

\#prev {
 left: 63px;
 width: 43px;
 background: url('img_navsprites.gif') -47px 0;
}

\#next {
 left: 129px;
 width: 43px;
 background: url('img_navsprites.gif') -91px 0;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sprites_nav)

**实例解析:**

- \#navlist {position:relative;} - 位置设置为相对，以允许在其中进行绝对定位
- \#navlist li {margin:0;padding:0;list-style:none;position:absolute;top:0;} - 外边距和内边距设置为 0，删除 list-style，并且所有列表项都均为绝对定位
- \#navlist li, #navlist a {height:44px;display:block;} - 所有图片的高度均为 44px

现在开始为每个特定部分设置定位和样式：

- \#home {left:0px;width:46px;} - 一直向左定位，图像宽度 46px
- \#home {background:url(navsprites.gif) 0 0;} - 定义背景图片及其位置（left 0px, top 0px）
- \#prev {left:63px;width:43px;} - 向右定位 63px（#home 宽度 46px + 项目之间的一些额外空间），宽度 43px。
- \#prev {background:url('navsprites.gif') -47px 0;} - 定义背景图片向右 47px（#home 宽度 46px + 1px 分隔线）
- \#next {left:129px;width:43px;} - 向右定位 129px（#prev 开始是 63px + #prev 的宽度是 43px + 多余的空格），宽度 43px。
- \#next {background:url('navsprites.gif') -91px 0;} - 定义背景图片向右 91px（#home 宽度 46px + 1px 分隔线+ #prev 宽度 43px + 1px 分隔线）

------

------

## 图像精灵 - 悬停效果

现在，我们要向导航列表中添加悬停效果。

**提示:** `:hover` 选择器可用于所有元素，而不仅限于链接。

not only on links.



我们的新图像（"img_navsprites_hover.gif"）包含三幅导航图像和三幅用于悬停效果的图像：

![navigation images](https://www.w3schools.cn/css/img_navsprites_hover.gif)

因为这是一幅图像，而不是六个单独的文件，所以当用户将鼠标悬停在图像上时，**不会有加载延迟**。

我们仅添加三行代码来实现悬停效果：

### 实例

\#home a:hover {
 background: url('img_navsprites_hover.gif') 0 -45px;
}

\#prev a:hover {
 background: url('img_navsprites_hover.gif') -47px -45px;
}

\#next a:hover {
 background: url('img_navsprites_hover.gif') -91px -45px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sprites_hover_nav)

实例说明:

- \#home a:hover {background: transparent url('img_navsprites_hover.gif') 0 -45px;} - 我们为所有三个悬停图像指定相同的背景位置，仅向下 45 像素



[❮ 上一节](https://www.w3schools.cn/css/css_image_gallery.html)[下一节 ❯](https://www.w3schools.cn/css/css_attribute_selectors.html)



# CSS 属性选择器

[❮ 上一节](https://www.w3schools.cn/css/css_image_sprites.html)[下一节 ❯](https://www.w3schools.cn/css/css_form.html)

------

## 为带有特定属性的 HTML 元素设置样式

我们可以设置带有特定属性或属性值的 HTML 元素的样式。

------

## CSS [attribute] 选择器

[attribute] 选择器用于选取带有指定属性的元素。

下例选择所有带有 target 属性的 <a> 元素；

### 实例

a[target] {
 background-color: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute)

------

## CSS [attribute="value"] 选择器

[attribute="value"] 选择器用于选取带有指定属性和值的元素。

下例选取所有带有 target="_blank" 属性的 <a> 元素：

### 实例

a[target="_blank"] {
 background-color: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute_value)

------

## CSS [attribute~="value"] 选择器

[attribute~="value"] 选择器选取属性值包含指定词的元素。

下例选取 title 属性包含 "flower" 单词的所有元素：

### 实例

[title~="flower"] {
 border: 5px solid yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute_value2)

上面的例子会匹配以下属性的元素：title="flower"、title="summer flower" 以及 title="flower new"，但不匹配：title="my-flower" 或 title="flowers"。

------

------

## CSS [attribute|="value"] 选择器

[attribute|="value"] 选择器用于选取指定属性以指定值开头的元素。

下例选取 class 属性以 "top" 开头的所有元素：

**注释:** 值必须是完整或单独的单词，比如 class="top" 或者后跟连字符的，比如 class="top-text"。

### 实例

[class|="top"] {
 background: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute_hyphen)

------

## CSS [attribute^="value"] 选择器

[attribute^="value"] 选择器用于选取指定属性以指定值开头的元素。

下例选取 class 属性以 "top" 开头的所有元素：

**注释:** 值不必是完整单词！

### 实例

[class^="top"] {
 background: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute_start)

------

## CSS [attribute$="value"] 选择器

[attribute$="value"] 选择器用于选取指定属性以指定值结尾的元素。

下例选取 class 属性以 "test" 结尾的所有元素：

**注释:** 值不必是完整单词！

### 实例

[class$="test"] {
 background: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute_end)

------

## CSS [attribute*="value"] 选择器

[attribute*="value"] 选择器选取属性值包含指定词的元素。

下例选取 class 属性包含 "te" 的所有元素：

**注释:** 值不必是完整单词！

### 实例

[class*="te"] {
 background: yellow;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute_contain)

------

## 设置表单样式

若需为不带 class 或 id 的表单设置样式，属性选择器会很有用：

### 实例

input[type="text"] {
 width: 150px;
 display: block;
 margin-bottom: 10px;
 background-color: yellow;
}

input[type="button"] {
 width: 120px;
 margin-left: 35px;
 display: block;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_attselector_form)

**提示:** 请访问我们的 [CSS 表单教程](https://www.w3schools.cn/css/css_form.html)，学习如何用 CSS 设置表单样式的更多知识。

------

## CSS 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_attribute_selectors1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_attribute_selectors2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_attribute_selectors3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_attribute_selectors4)[测验 5 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_attribute_selectors5)[测验 6 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_attribute_selectors6)

------

## 所有 CSS 属性选择器

| 选择器                                                       | 实例                 | 实例描述                                                |
| :----------------------------------------------------------- | :------------------- | :------------------------------------------------------ |
| [[*attribute*\]](https://www.w3schools.cn/cssref/sel_attribute.html) | [target]             | 选择带有 target 属性的所有元素。                        |
| [[*attribute*=*value*\]](https://www.w3schools.cn/cssref/sel_attribute_value.html) | [target=_blank]      | 选择带有 target="_blank" 属性的所有元素。               |
| [[*attribute*~=*value*\]](https://www.w3schools.cn/cssref/sel_attribute_value_contains.html) | [title~=flower]      | 选择带有包含 "flower" 一词的 title 属性的所有元素。     |
| [[*attribute*\|=*value*\]](https://www.w3schools.cn/cssref/sel_attribute_value_lang.html) | [lang\|=en]          | 选择带有以 "en" 开头的 lang 属性的所有元素。            |
| [[*attribute*^=*value*\]](https://www.w3schools.cn/cssref/sel_attr_begin.html) | a[href^="https"]     | 选择其 href 属性值以 "https" 开头的每个 <a> 元素。      |
| [[*attribute*$=*value*\]](https://www.w3schools.cn/cssref/sel_attr_end.html) | a[href$=".pdf"]      | 选择其 href 属性值以 ".pdf" 结尾的每个 <a> 元素。       |
| [[*attribute**=*value*\]](https://www.w3schools.cn/cssref/sel_attr_contain.html) | a[href*="w3schools"] | 选择其 href 属性值包含子串 "w3school" 的每个 <a> 元素。 |



# CSS 表单

[❮ 上一节](https://www.w3schools.cn/css/css_attribute_selectors.html)[下一节 ❯](https://www.w3schools.cn/css/css_counters.html)

------

通过使用 CSS，可以极大地改善 HTML 表单的外观：

First Name Last Name Country    Australia   Canada   USA  [亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_forms)

------

## 设置输入字段的样式

使用 width 属性来确定输入字段的宽度：

First Name

 



### 实例

input {
 width: 100%;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_width)

上例适用于所有 <input> 元素。如果只想设置特定输入类型的样式，则可以使用属性选择器：

- input[type=text] - 将仅选择文本字段
- input[type=password] - 将仅选择密码字段
- input[type=number] - 将仅选择数字字段
- 等等...

------

------

## 填充输入框

使用 padding 属性在文本字段内添加空间。

**提示:** 若有很多输入，那么您可能还需要添加外边距，以便在它们之外添加更多空间：

First Name

 

 

Last Name

 



### 实例

input[type=text] {
 width: 100%;
 padding: 12px 20px;
 margin: 8px 0;
 box-sizing: border-box;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_padding)

请注意，我们已将 box-sizing 属性设置为 border-box。这样可以确保元素的总宽度和高度中包括内边距（填充）和最终的边框。

请在在我们的 [CSS Box Sizing](https://www.w3schools.cn/css/css3_box-sizing.html) 这一章中学习有关 box-sizing 属性的更多知识。

------

## 带边框的输入框

请使用 border 属性更改边框的粗细和颜色，并使用 border-radius 属性添加圆角：

First Name

 



### 实例

input[type=text] {
 border: 2px solid red;
 border-radius: 4px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_border)

如果仅需要下边框，请使用 border-bottom 属性：

First Name

 



### 实例

input[type=text] {
 border: none;
 border-bottom: 2px solid red;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_border2)

------

## 彩色的输入框

请使用 background-color 属性为输入添加背景色，并使用 color 属性更改文本颜色：



### 实例

input[type=text] {
 background-color: #3CBC8D;
 color: white;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_color)

------

## 获得焦点的输入框

默认情况下，某些浏览器在获得焦点（单击）时会在输入框周围添加蓝色轮廓。您可以通过向输入添加 outline: none; 来消除此行为。

使用 :focus 选择器可以在输入字段获得焦点时为其设置样式：

### 实例

input[type=text]:focus {
 background-color: lightblue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_focus)

### 实例

input[type=text]:focus {
 border: 3px solid #555;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_focus2)

------

## 带有图标/图像的输入框

如果希望在输入框中包含图标，请使用 background-image 属性，并将其与 background-position 属性一起设置。还要注意，我们添加了一个较大的左内边距（padding-left）来留出图标的空间：



### 实例

input[type=text] {
 background-color: white;
 background-image: url('searchicon.png');
 background-position: 10px 10px;
 background-repeat: no-repeat;
 padding-left: 40px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_icon)

------

## 带动画效果的搜索输入框

在本例中，我们使用 CSS transition 属性为搜索输入框获得焦点时的宽度变化设置动画。稍后，您将在我们的 [CSS 过渡](https://www.w3schools.cn/css/css3_transitions.html) 一章中学到更多有关 transition 属性的知识。



### 实例

input[type=text] {
 transition: width 0.4s ease-in-out;
}

input[type=text]:focus {
 width: 100%;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_search_anim)

------

## 设置文本域的样式

**提示:** 使用 resize 属性可防止对 textareas 调整大小（禁用右下角的"抓取器"）：



### 实例

textarea {
 width: 100%;
 height: 150px;
 padding: 12px 20px;
 box-sizing: border-box;
 border: 2px solid #ccc;
 border-radius: 4px;
 background-color: #f8f8f8;
 resize: none;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_textarea)

------

## 设置选择菜单的样式

   Australia   Canada   USA  

### 实例

select {
 width: 100%;
 padding: 16px 20px;
 border: none;
 border-radius: 4px;
 background-color: #f1f1f1;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_select)

------

## 设置输入按钮的样式

 



### 实例

input[type=button], input[type=submit], input[type=reset] {
 background-color: #4CAF50;
 border: none;
 color: white;
 padding: 16px 32px;
 text-decoration: none;
 margin: 4px 2px;
 cursor: pointer;
}

/* 提示：对全宽按钮使用 **width: 100%** */

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_button)

有关如何使用 CSS 设置按钮样式的更多知识，请学习我们的 [CSS 按钮](https://www.w3schools.cn/css/css3_buttons.html) 教程。

------

## 响应式菜单

请调整 TIY 编辑器窗口的大小来查看效果。当屏幕的宽度小于 600 像素时，使两列上下堆叠而不是左右堆叠。

**高级:** 接下来的例子使用 [媒体查询](https://www.w3schools.cn/css/css3_mediaqueries.html) 来创建响应式表单。在下一章中，您将学到更多相关知识。

<iframe src="https://www.w3schools.cn/css/trycss_form_responsive_ifr.htm" class="myfr" style="box-sizing: inherit; height: 450px; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; margin-left: -8px; border: none; width: 869.984px;"></iframe>

 

# CSS 计数器

[❮ 上一节](https://www.w3schools.cn/css/css_form.html)[下一节 ❯](https://www.w3schools.cn/css/css_website_layout.html)

------

### Pizza

### Hamburger

### Hotdogs

CSS 计数器是由 CSS 保持的"变量"，其值可以通过 CSS 规则递增（以跟踪其使用次数）。计数器使您可以根据内容在文档中的位置来调整其外观。

------

## 带计数器的自动编号

CSS 计数器就像"变量"。变量值可以通过 CSS 规则递增（将跟踪它们的使用次数）。

如需使用 CSS 计数器，我们将使用以下属性：

- counter-reset - 创建或重置计数器
- counter-increment - 递增计数器值
- content - 插入生成的内容
- counter() 或 counters() 函数 - 将计数器的值添加到元素

如需使用 CSS 计数器，必须首先使用 counter-reset 创建它。

下面的例子为页面（在 body 选择器中）创建一个计数器，然后为每个 <h2> 元素增加计数器值，并在每个 <h2> 元素的开头添加 "Section <value of the counter>:"：

### 实例

body {
 counter-reset: section;
}

h2::before {
 counter-increment: section;
 content: "Section " counter(section) ": ";
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_counters1)

------

------

## 嵌套计数器

下面的例子为页面（section）创建一个计数器，为每个 <h1> 元素（subsection）创建一个计数器。

"section" 计数器为每个 <h1> 元素计数，同时写入 "Section" 以及 section 计数器的值，"subsection" 计数器为每个 <h2> 元素计数，同时写入 section 计数器的值以及 subsection 计数器的值：

### 实例

body {
 counter-reset: section;
}

h1 {
 counter-reset: subsection;
}

h1::before {
 counter-increment: section;
 content: "Section " counter(section) ". ";
}

h2::before {
 counter-increment: subsection;
 content: counter(section) "." counter(subsection) " ";
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_counters2)

计数器对于创建概述列表也很有用，因为在子元素中会自动创建一个计数器的新实例。在这里，我们使用 counters() 函数在不同级别的嵌套计数器之间插入一个字符串：

### 实例

ol {
 counter-reset: section;
 list-style-type: none;
}

li::before {
 counter-increment: section;
 content: counters(section,".") " ";
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_counters3)

------

## CSS 计数器属性

| 属性                                                         | 描述                                                      |
| :----------------------------------------------------------- | :-------------------------------------------------------- |
| [content](https://www.w3schools.cn/cssref/pr_gen_content.html) | 与 ::before 和 ::after 伪元素一同使用，来插入生成的内容。 |
| [counter-increment](https://www.w3schools.cn/cssref/pr_gen_counter-increment.html) | 递增一个或多个计数器值。                                  |
| [counter-reset](https://www.w3schools.cn/cssref/pr_gen_counter-reset.html) | 创建或重置一个或多个计数器。                              |



# CSS 网站布局

[❮ 上一节](https://www.w3schools.cn/css/css_counters.html)[下一节 ❯](https://www.w3schools.cn/css/css_units.html)

------

## 网站布局

网站通常分为页眉、菜单、内容和页脚：

<iframe src="https://www.w3schools.cn/css/trycss_template_ifr5.htm" style="box-sizing: inherit; border: 0px; width: 837.984px; overflow: hidden; height: 465px;"></iframe>

有很多不同的布局设计可供选择。但是，以上结构是最常见的结构之一，我们将在本教程中对其进行仔细研究。

------

## 页眉

页眉（header）通常位于网站顶部（或顶部导航菜单的正下方）。它通常包含徽标（logo）或网站名称：

### 实例

.header {
 background-color: #F1F1F1;
 text-align: center;
 padding: 20px;
}

Result

## Header

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_website_layout_header)

------

------

## 导航栏

导航栏包含链接列表，以帮助访问者浏览您的网站：

### 实例

/* 导航栏容器 */
.topnav {
 overflow: hidden;
 background-color: #333;
}

/* 导航栏链接 */
.topnav a {
 float: left;
 display: block;
 color: #f2f2f2;
 text-align: center;
 padding: 14px 16px;
 text-decoration: none;
}

/* 链接 - 悬停时改变颜色 */
.topnav a:hover {
 background-color: #ddd;
 color: black;
}

Result

[Link](javascript:void(0))[Link](javascript:void(0))[Link](javascript:void(0))

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_website_layout_navbar)

------

## 内容

使用哪种布局通常取决于您的目标用户。最常见的布局是以下布局之一（或将它们组合在一起）：

- **1-列**布局（通常用于移动浏览器）
- **2-列**布局（通常用于平板电脑和笔记本电脑）
- **3-列**布局 （仅用于台式机）

1-column:

<iframe src="https://www.w3schools.cn/css/trycss_layout_ifr.htm" style="box-sizing: inherit; border: 0px; width: 240.656px; overflow: hidden; height: 177px;"></iframe>

2-column:

<iframe src="https://www.w3schools.cn/css/trycss_layout_ifr2.htm" style="box-sizing: inherit; border: 0px; width: 240.656px; overflow: hidden; height: 177px;"></iframe>

3-column:

<iframe src="https://www.w3schools.cn/css/trycss_layout_ifr3.htm" style="box-sizing: inherit; border: 0px; width: 240.656px; overflow: hidden; height: 177px;"></iframe>

我们将创建 3 列布局，并在较小的屏幕上将其更改为 1 列布局：

### 实例

/* 创建三个彼此相邻浮动的相等列 */
.column {
 float: left;
 width: 33.33%;
}

/* 清除列后的浮动 */
.row:after {
 content: "";
 display: table;
 clear: both;
}

/* 响应式布局 - 使三列堆叠在一起，而不是在较小的屏幕（600px 宽或更小）上彼此相邻 */
@media screen and (max-width: 600px) {
 .column {
  width: 100%;
 }
}

结果：

## Column

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sit amet pretium urna. Vivamus venenatis velit nec neque ultricies, eget elementum magna tristique.

## Column

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sit amet pretium urna. Vivamus venenatis velit nec neque ultricies, eget elementum magna tristique.

## Column

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sit amet pretium urna. Vivamus venenatis velit nec neque ultricies, eget elementum magna tristique.

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_website_layout_grid)

**提示:** 如需创建 2 列布局，请将宽度更改为 50％。如需创建 4 列布局，请使用 25％。

**提示:** 您是否想知道 @media 规则如何工作？请在我们的 [CSS 媒体查询](https://www.w3schools.cn/css/css3_mediaqueries.html) 这一章中学习更多相关知识。

**提示:** ：创建列布局的一种更现代的方法是使用 CSS Flexbox。但是，Internet Explorer 10 和更早版本不支持它。如果需要 IE6-10 支持，请使用浮动（如上所示）。

如需了解有关 Flexible Box 布局模块的更多信息，请阅读我们的 [CSS Flexbox](https://www.w3schools.cn/css/css3_flexbox.html) 教程。

------

## 不相等的栏

主要内容（main content）是您网站上最大、最重要的部分。

列宽不相等的情况很常见，因为大部分空间都为主内容保留。附属内容（如果有）通常用作替代导航或指定与主要内容有关的信息。您可以随意更改宽度，只要记住它的总和应为 100％：

### 实例

.column {
 float: left;
}

/* 左右列 */
.column.side {
 width: 25%;
}

/* 中间列 */
.column.middle {
 width: 50%;
}

/* 响应式布局 - 使三列堆叠在一起而不是彼此相邻 */
@media screen and (max-width: 600px) {
 .column.side, .column.middle {
  width: 100%;
 }
}

结果：

## Side

Lorem ipsum dolor sit amet, consectetur adipiscing elit...

## Main Content

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sit amet pretium urna. Vivamus venenatis velit nec neque ultricies, eget elementum magna tristique. Quisque vehicula, risus eget aliquam placerat, purus leo tincidunt eros, eget luctus quam orci in velit. Praesent scelerisque tortor sed accumsan convallis.

## Side

Lorem ipsum dolor sit amet, consectetur adipiscing elit...

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_website_layout_grid2)

------

## 页脚

页脚位于页面底部。它通常包含诸如版权和联系方式之类的信息：

### 实例

.footer {
 background-color: #F1F1F1;
 text-align: center;
 padding: 10px;
}

结果：

Footer

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_website_layout_footer)

------

## 响应式网站布局

通过使用上面的这些 CSS 代码，我们创建了一个自适应的网站布局，会根据屏幕宽度切换两列与全宽列：

<iframe src="https://www.w3schools.cn/css/trycss_website_layout_blog.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; width: 869.984px; border: 3px solid rgb(221, 221, 221); height: 606px;"></iframe>



[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_website_layout_blog)



# CSS 单位

[❮ 上一节](https://www.w3schools.cn/css/css_website_layout.html)[下一节 ❯](https://www.w3schools.cn/css/css_specificity.html)

------

## CSS 单位

CSS 有几种表示长度的不同单位。

许多 CSS 属性接受"长度"值，诸如 width、margin、padding、font-size 等。

长度是一个后面跟着长度单位的数字，诸如 `10px`、`2em` 等。

数字和单位之间不能出现空格。但是，如果值为 0，则可以省略单位。

对于某些 CSS 属性，允许使用负的长度。

长度单位有两种类型：**绝对单位**和**相对单位**。

------

## 绝对长度

绝对长度单位是固定的，用任何一个绝对长度表示的长度都将恰好显示为这个尺寸。

不建议在屏幕上使用绝对长度单位，因为屏幕尺寸变化很大。但是，如果已知输出介质，则可以使用它们，例如用于打印布局（print layout）。

| 单位 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| cm   | 厘米[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_cm) |
| mm   | 毫米[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_mm) |
| in   | 英寸 (1in = 96px = 2.54cm)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_in) |
| px * | 像素 (1px = 1/96th of 1in)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_px) |
| pt   | 点 (1pt = 1/72 of 1in)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_pt) |
| pc   | 派卡 (1pc = 12 pt)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_pc) |

\* 像素（px）是相对于观看设备的。对于低 dpi 的设备，1px 是显示器的一个设备像素（点）。对于打印机和高分辨率屏幕，1px 表示多个设备像素。

------

## 相对长度

相对长度单位规定相对于另一个长度属性的长度。相对长度单位在不同渲染介质之间缩放表现得更好。

| 单位 | 描述                                                         |                                                              |
| :--- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| em   | 相对于元素的字体大小（font-size）（2em 表示当前字体大小的 2 倍） | [测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_em) |
| ex   | 相对于当前字体的 x-height(极少使用)                          | [测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_ex) |
| ch   | 相对于 "0"（零）的宽度                                       | [测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_ch) |
| rem  | 相对于根元素的字体大小（font-size）                          | [测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_rem) |
| vw   | 相对于视口*宽度的 1%                                         | [测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_vw) |
| vh   | 相对于视口*高度的 1%                                         | [测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_vh) |
| vmin | 相对于视口*较小尺寸的 1％                                    | [测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_vmin) |
| vmax | 相对于视口*较大尺寸的 1％                                    | [测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_vmax) |
| %    | 相对于父元素                                                 | [测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_unit_percentage) |

**提示:** em 和 rem 单元可用于创建完美的可扩展布局！

\* 视口（Viewport）= 浏览器窗口的尺寸。如果视口为 50 厘米宽，则 1vw = 0.5 厘米。

------

------

## 浏览器支持

表格中的数字注明了完全支持该长度单位的首个浏览器版本。

| Length Unit                       |      |               |      |      |      |
| :-------------------------------- | ---- | ------------- | ---- | ---- | ---- |
| em, ex, %, px, cm, mm, in, pt, pc | 1.0  | 3.0           | 1.0  | 1.0  | 3.5  |
| ch                                | 27.0 | 9.0           | 1.0  | 7.0  | 20.0 |
| rem                               | 4.0  | 9.0           | 3.6  | 4.1  | 11.6 |
| vh, vw                            | 20.0 | 9.0           | 19.0 | 6.0  | 20.0 |
| vmin                              | 20.0 | 9.0*          | 19.0 | 6.0  | 20.0 |
| vmax                              | 26.0 | Not supported | 19.0 | 7.0  | 20.0 |

**注释:** Internet Explorer 9 支持使用非标准名称的 vmin: vm.

------

[❮ 上一节](https://www.w3schools.cn/css/css_website_layout.html)[下一节 ❯](https://www.w3schools.cn/css/css_specificity.html)

# CSS 特异性

[❮ 上一节](https://www.w3schools.cn/css/css_units.html)[下一节 ❯](https://www.w3schools.cn/css/css3_tutorial.html)

------

## 什么是特异性？

如果有两条或两条以上指向同一元素的冲突 CSS 规则，则浏览器将遵循一些原则来确定哪一条是最具体的，并因此胜出。

将特异性（specificity）视为得分/等级，能够确定最终将哪些样式声明应用于元素。

通用选择器（*）具有较低的特异性，而 ID 选择器具有较高的特异性！

**注释:** 这种特异性是 CSS 规则不适用于某些元素的常见原因，尽管您可能会认为应该适用。

------

## 特异性层次

每个选择器在特异性层次结构中都有其位置。以下四种类别定义了选择器的特异性级别：

**行内样式** - 行内（内联）样式直接附加到要设置样式的元素。实例：<h1 style="color: #ffffff;">。

**ID** - ID 是页面元素的唯一标识符，例如 #navbar。

**类、属性和伪类** - 此类别包括 .classes、[attributes] 和伪类，例如：:hover、:focus 等。

**元素和伪元素** - 此类别包括元素名称和伪元素，比如 h1、div、:before 和 :after。

------

## 如何计算特异性？

请您牢记计算特异性的方法！

从 0 开始，为 style 属性添加 1000，为每个 ID 添加 100，为每个属性、类或伪类添加 10，为每个元素名称或伪元素添加 1。

请思考以下三个代码片段：

### 实例

A: h1
B: #content h1
C: <div id="content"><h1 style="color: #ffffff">Heading</h1></div>

- A 的特异性为 1（一个元素）
- B 的特异性为 101（一个 ID 引用以及一个元素）
- C 的特异性为 1000（行内样式）

由于 1 < 101 < 1000，因此第三条规则（C）具有更高的特异性，所以将被应用。

------

------

## 特异性规则 1：

**在特异性相同的情况下：最新的规则很重要** - 如果将同一规则两次写入外部样式表，那么样式表中后面的规将更靠近要设置样式的元素，因此会被应用：

### 实例

h1 {background-color: yellow;}
h1 {background-color: red;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_specificity1)

后一条规则始终适用。

------

## 特异性规则 2：

**ID 选择器比属性选择器拥有更高的特异性** - 请看以下三行代码：

### 实例

div#a {background-color: green;}
\#a {background-color: yellow;}
div[id=a] {background-color: blue;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_specificity2)

第一条规则比其他两条更具体，因此将被应用。

------

## 特异性规则 3：

**上下文选择器比单一元素选择器更具体** - 嵌入式样式表更靠近要设置样式的元素。所以在以下情况下：

### 实例

**From external CSS file:**
\#content h1 {background-color: red;}

**In HTML file:**
<style>
\#content h1 {
 background-color: yellow;
}
</style>

将适用后一条规则。

------

## 特异性规则 4：

**类选择器会击败任意数量的元素选择器** - 类选择器（诸如 .intro 会击败 h1、p、div 等）：

### 实例

.intro {background-color: yellow;}
h1 {background-color: red;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_specificity3)

------

此外，**通用选择器以及被继承的值拥有 0** - * 的特异性，body * 及类似拥有 0 的特异性。被继承的值的特异性也为 0。



[❮ 上一节](https://www.w3schools.cn/css/css_units.html)[下一节 ❯](https://www.w3schools.cn/css/css3_tutorial.html)









