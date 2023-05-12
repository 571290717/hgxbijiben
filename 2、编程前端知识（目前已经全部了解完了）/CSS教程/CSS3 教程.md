# CSS3 教程

[❮ 首页](https://www.w3schools.cn/css/css_specificity.html)[下一节 ❯](https://www.w3schools.cn/css/css3_intro.html)

CSS3 是最新的 CSS 标准。

CSS 描述应该如何显示 HTML 元素。

本教程向您讲解 CSS3 中的新特性。

[现在开始学习 CSS3 »](https://www.w3schools.cn/css/css3_intro.html)

------

2D rotate

3D rotate

------

### CSS3 实例

div {
 transform: rotate(20deg);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_rotate)

**点击 "亲自试一试" 按钮查看运行结果。**

------

## CSS3 参考手册

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



# CSS3 简介

[❮ 上一节](https://www.w3schools.cn/css/css3_tutorial.html)[下一节 ❯](https://www.w3schools.cn/css/css3_borders.html)

------

CSS3 已完全向后兼容，所以你就不必改变现有的设计。

------

## CSS3 模块

CSS3 被拆分为"模块"。旧规范已拆分成小块，还增加了新的。

一些最重要 CSS3 模块如下：

- 选择器
- 盒模型
- 背景和边框
- 文字特效
- 2D/3D转换
- 动画
- 多列布局
- 用户界面

------

## CSS3 建议

W3C 的 CSS3 规范仍在开发。

但是，现在新的浏览器已经都支持 CSS3 属性。

# CSS3 圆角

[❮ 上一节](https://www.w3schools.cn/css/css3_intro.html)[下一节 ❯](https://www.w3schools.cn/css/css3_border_images.html)

------

## CSS3 圆角

通过 CSS border-radius 属性，可以实现任何元素的"圆角"样式。

------

## CSS3 border-radius 属性

CSS border-radius 属性定义元素角的半径。

提示：您可以使用此属性为元素添加圆角！

这里有三个例子：

\1. 带有指定背景颜色的元素的圆角：

圆角！

\2. 带边框元素的圆角：

圆角！

\3. 带有背景图像的元素的圆角：

圆角！

这是代码：

### 实例

\#rcorners1 {
 border-radius: 25px;
 background: #73AD21;
 padding: 20px;
 width: 200px;
 height: 150px;
}

\#rcorners2 {
 border-radius: 25px;
 border: 2px solid #73AD21;
 padding: 20px;
 width: 200px;
 height: 150px;
}

\#rcorners3 {
 border-radius: 25px;
 background: url(paper.gif);
 background-position: left top;
 background-repeat: repeat;
 padding: 20px;
 width: 200px;
 height: 150px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_border-radius)

**提示:** border-radius 属性实际上是以下属性的简写属性：

- border-top-left-radius
- border-top-right-radius
- border-bottom-right-radius
- border-bottom-left-radius

------

------

## CSS3 border-radius - 指定每个角

border-radius 属性可以接受一到四个值。规则如下：

border-radius 属性可以接受一到四个值。规则如下：

**四个值 - border-radius: 15px 50px 30px 5px;**（依次分别用于：左上角、右上角、右下角、左下角）：

**三个值 - border-radius: 15px 50px 30px;**（第一个值用于左上角，第二个值用于右上角和左下角，第三个用于右下角）：

**两个值 - border-radius: 15px 50px;**（第一个值用于左上角和右下角，第二个值用于右上角和左下角）：

**一个值 - border-radius: 15px;**（该值用于所有四个角，圆角都是一样的）：

这是代码：

### 实例

\#rcorners1 {
 border-radius: 15px 50px 30px 5px;
 background: #73AD21;
 padding: 20px;
 width: 200px;
 height: 150px;
}

\#rcorners2 {
 border-radius: 15px 50px 30px;
 background: #73AD21;
 padding: 20px;
 width: 200px;
 height: 150px;
}

\#rcorners3 {
 border-radius: 15px 50px;
 background: #73AD21;
 padding: 20px;
 width: 200px;
 height: 150px;
}

\#rcorners4 {
 border-radius: 15px;
 background: #73AD21;
 padding: 20px;
 width: 200px;
 height: 150px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_border-radius2)

您还可以创建椭圆角：

### 实例

\#rcorners1 {
 border-radius: 50px / 15px;
 background: #73AD21;
 padding: 20px;
 width: 200px;
 height: 150px;
}

\#rcorners2 {
 border-radius: 15px / 50px;
 background: #73AD21;
 padding: 20px;
 width: 200px;
 height: 150px;
}

\#rcorners3 {
 border-radius: 50%;
 background: #73AD21;
 padding: 20px;
 width: 200px;
 height: 150px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_border-radius3)

------

## CSS3 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_borders1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_borders2)

------

## CSS3 圆角属性

| 属性                                                         | 描述                                                |
| :----------------------------------------------------------- | :-------------------------------------------------- |
| [border-radius](https://www.w3schools.cn/cssref/css3_pr_border-radius.html) | 用于设置所有四个 border-*-*-radius 属性的简写属性。 |
| [border-top-left-radius](https://www.w3schools.cn/cssref/css3_pr_border-top-left-radius.html) | 定义左上角边框的形状。                              |
| [border-top-right-radius](https://www.w3schools.cn/cssref/css3_pr_border-top-right-radius.html) | 定义右上角边框的形状。                              |
| [border-bottom-right-radius](https://www.w3schools.cn/cssref/css3_pr_border-bottom-right-radius.html) | 定义右下角边框的形状。                              |
| [border-bottom-left-radius](https://www.w3schools.cn/cssref/css3_pr_border-bottom-left-radius.html) | 定义左下角边框的形状。                              |



[❮ 上一节](https://www.w3schools.cn/css/css3_intro.html)[下一节 ❯](https://www.w3schools.cn/css/css3_border_images.html)

# CSS3 边框图像

[❮ 上一节](https://www.w3schools.cn/css/css3_borders.html)[下一节 ❯](https://www.w3schools.cn/css/css3_backgrounds.html)

------

## CSS3 边框图像

通过使用 CSS border-image 属性，可以设置图像用作围绕元素的边框。

------

## CSS3 border-image 属性

CSS border-image 属性允许您指定要使用的图像，而不是包围普通边框。

该属性有三部分：

1. 用作边框的图像
2. 在哪里裁切图像
3. 定义中间部分应重复还是拉伸

我们将使用这幅图像（"border.png"）

![Border](https://www.w3schools.cn/css/border.png)

border-image 属性接受图像，并将其切成九部分，就像井字游戏板。然后，将拐角放置在拐角处，并根据您的设置重复或拉伸中间部分。

**注释:** 为了使 border-image 起作用，该元素还需要设置 border 属性！

此处，重复图像的中间部分以创建边框：

图像作为边框！

这是代码：

### 实例

\#borderimg {
 border: 10px solid transparent;
 padding: 15px;
 border-image: url(border.png) 30 round;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_border-image)

此处，图像的中间部分被拉伸以创建边框：

图像作为边框！

这是代码：

### 实例

\#borderimg {
 border: 10px solid transparent;
 padding: 15px;
 border-image: url(border.png) 30 stretch;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_border-image2)

**提示:** border-image 属性实际上是以下属性的简写属性：

- border-image-source
- border-image-slice
- border-image-width
- border-image-outset
- border-image-repeat

------

------

## CSS3 border-image - 不同的裁切值

不同的裁切值会完全改变边框的外观：

### 实例 1：

border-image: url(border.png) 50 round;

### 实例 2：

border-image: url(border.png) 20% round;

### 实例 3：

border-image: url(border.png) 30% round;

这是代码：

### 实例

\#borderimg1 {
 border: 10px solid transparent;
 padding: 15px;
 border-image: url(border.png) 50 round;
}

\#borderimg2 {
 border: 10px solid transparent;
 padding: 15px;
 border-image: url(border.png) 20% round;
}

\#borderimg3 {
 border: 10px solid transparent;
 padding: 15px;
 border-image: url(border.png) 30% round;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_border-image3)

------

## CSS3 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_border_images1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_border_images2)

------

## CSS3 边框图像属性

| 属性                                                         | 描述                                         |
| :----------------------------------------------------------- | :------------------------------------------- |
| [border-image](https://www.w3schools.cn/cssref/css3_pr_border-image.html) | 用于设置所有 border-image-* 属性的简写属性。 |
| [border-image-source](https://www.w3schools.cn/cssref/css3_pr_border-image-source.html) | 规定用作边框的图像的路径。                   |
| [border-image-slice](https://www.w3schools.cn/cssref/css3_pr_border-image-slice.html) | 规定如何裁切边框图像。                       |
| [border-image-width](https://www.w3schools.cn/cssref/css3_pr_border-image-width.html) | 规定边框图像的宽度。                         |
| [border-image-outset](https://www.w3schools.cn/cssref/css3_pr_border-image-outset.html) | 规定边框图像区域超出边框盒的量。             |
| [border-image-repeat](https://www.w3schools.cn/cssref/css3_pr_border-image-repeat.html) | 规定边框图像应重复、圆角、还是拉伸。         |

# CSS3 多重背景

[❮ 上一节](https://www.w3schools.cn/css/css3_border_images.html)[下一节 ❯](https://www.w3schools.cn/css/css3_colors.html)

------

在本章中，您将学习如何将多个背景图像添加到一个元素。

您还将学到以下属性：

- `background-size`
- `background-origin`
- `background-clip`

------

## CSS3 多重背景

CSS 允许您通过 background-image 属性为一个元素添加多幅背景图像。

不同的背景图像用逗号隔开，并且图像会彼此堆叠，其中的第一幅图像最靠近观看者。

下面的例子有两幅背景图像，第一幅图像是花朵（与底部和右侧对齐），第二幅图像是纸张背景（与左上角对齐）：

### 实例

\#example1 {
 background-image: url(img_flwr.gif), url(paper.gif);
 background-position: right bottom, left top;
 background-repeat: no-repeat, repeat;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background_multiple)

多重背景图像可以使用单独的背景属性（如上所述）或 background 简写属性来指定。

下面的例子使用 background 简写属性（结果与上例相同）：

### 实例

\#example1 {
 background: url(img_flwr.gif) right bottom no-repeat, url(paper.gif) left top repeat;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background_multiple2)

------

------

## CSS3 背景尺寸

CSS background-size 属性允许您指定背景图像的大小。

可以通过长度、百分比或使用以下两个关键字之一来指定背景图像的大小：`contain` 或 `cover`。

下面的例子将背景图像的大小调整为比原始图像小得多（使用像素）：

## Lorem Ipsum Dolor

Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.

这是代码：

### 实例

\#div1 {
 background: url(img_flower.jpg);
 background-size: 100px 80px;
 background-repeat: no-repeat;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background-size)

background-size 的其他两个可能的值是 contain 和 cover。

contain 关键字将背景图像缩放为尽可能大的尺寸（但其宽度和高度都必须适合内容区域）。这样，取决于背景图像和背景定位区域的比例，可能存在一些未被背景图像覆盖的背景区域。

cover 关键字会缩放背景图像，以使内容区域完全被背景图像覆盖（其宽度和高度均等于或超过内容区域）。这样，背景图像的某些部分可能在背景定位区域中不可见。

下面的例子展示了 contain 和 cover 的用法：

### 实例

\#div1 {
 background: url(img_flower.jpg);
 background-size: contain;
 background-repeat: no-repeat;
}

\#div2 {
 background: url(img_flower.jpg);
 background-size: cover;
 background-repeat: no-repeat;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background-size_contain)

------

## 定义多个背景图像的尺寸

在处理多重背景时，background-size 属性还可以接受多个设置背景尺寸的值（使用逗号分隔的列表）。

下面的例子指定了三幅背景图像，每幅图像有不同的 background-size 值：

### 实例

\#example1 {
 background: url(img_tree.gif) left top no-repeat, url(img_flwr.gif) right bottom no-repeat, url(paper.gif) left top repeat;
 background-size: 50px, 130px, auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background_multiple3)

------

## 全尺寸背景图像

现在，我们希望网站上的背景图像始终覆盖整个浏览器窗口。

具体要求如下：

- 用图像填充整个页面（无空白）
- 根据需要缩放图像
- 在页面上居中图像
- 不引发滚动条

下面的例子显示了如何实现它：使用 <html> 元素（<html> 元素始终至少是浏览器窗口的高度）。然后在其上设置固定且居中的背景。最后使用 background-size 属性调整其大小：

### 实例

html {
 background: url(img_man.jpg) no-repeat center fixed;
 background-size: cover;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background_full)

------

## Hero Image

您还可以在 <div> 上使用不同的背景属性来创建 Hero Image（带有文本的大图像），并将其放置在您希望的位置上。

### 实例

.hero-image {
 background: url(img_man.jpg) no-repeat center;
 background-size: cover;
 height: 500px;
 position: relative;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background_hero)

------

## CSS3 background-origin 属性

CSS background-origin 属性指定背景图像的位置。

该属性接受三个不同的值：

- border-box - 背景图片从边框的左上角开始
- padding-box -背景图像从内边距边缘的左上角开始（默认）
- content-box - 背景图片从内容的左上角开始

下面的示例展示了 background-origin 属性：

### 实例

\#example1 {
 border: 10px solid black;
 padding: 35px;
 background: url(img_flwr.gif);
 background-repeat: no-repeat;
 background-origin: content-box;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background-origin)

------

## CSS3 background-clip 属性

CSS background-clip 属性指定背景的绘制区域。

该属性接受三个不同的值：

- border-box - 背景绘制到边框的外部边缘（默认）
- padding-box - 背景绘制到内边距的外边缘
- content-box - 在内容框中绘制背景

下面的例子展示了 background-clip 属性：

### 实例

\#example1 {
 border: 10px dotted black;
 padding: 35px;
 background: yellow;
 background-clip: content-box;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background-clip)

------

## CSS3 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_backgrounds1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_backgrounds2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_backgrounds3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_backgrounds4)[测验 5 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_backgrounds5)

------

## CSS3 高级背景属性

| 属性                                                         | 描述                                         |
| :----------------------------------------------------------- | :------------------------------------------- |
| [background](https://www.w3schools.cn/cssref/css3_pr_background.html) | 用于在一条声明中设置所有背景属性的简写属性。 |
| [background-clip](https://www.w3schools.cn/cssref/css3_pr_background-clip.html) | 规定背景的绘制区域。                         |
| [background-image](https://www.w3schools.cn/cssref/pr_background-image.html) | 为一个元素指定一幅或多幅背景图像。           |
| [background-origin](https://www.w3schools.cn/cssref/css3_pr_background-origin.html) | 规定背景图像的放置位置。                     |
| [background-size](https://www.w3schools.cn/cssref/css3_pr_background-size.html) | 规定背景图像的大小。                         |



[❮ 上一节](https://www.w3schools.cn/css/css3_border_images.html)[下一节 ❯](https://www.w3schools.cn/css/css3_colors.html)

# CSS3 颜色

[❮ 上一节](https://www.w3schools.cn/css/css3_backgrounds.html)[下一节 ❯](https://www.w3schools.cn/css/css3_gradients.html)

------

CSS 支持 [140 多种颜色名称](https://www.w3schools.cn/css/css_colors.html)，以及十六进制值、RGB 值、RGBA 值、HSL 值、HSLA 值和不透明度。

------

## RGBA 颜色

RGBA 颜色值是 RGB 颜色值的扩展，带有 alpha 通道 - 该通道规定颜色的不透明度。

RGBA 颜色值是这样规定的：rgba(*red*, *green*, *blue*, *alpha*)。 *alpha* 参数是介于 0.0（完全透明）和 1.0（完全不透明）之间的数字。

rgba(255, 0, 0, 0.2);

rgba(255, 0, 0, 0.4);

rgba(255, 0, 0, 0.6);

rgba(255, 0, 0, 0.8);

下面的例子定义了不同的 RGBA 颜色：

### 实例

\#p1 {background-color: rgba(255, 0, 0, 0.3);} /* 不透明的红色 */
\#p2 {background-color: rgba(0, 255, 0, 0.3);}  /* 不透明的绿色 */
\#p3 {background-color: rgba(0, 0, 255, 0.3);}  /* 不透明的蓝色 */

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_color_rgba)

------

------

## HSL 颜色

HSL 指的是色相、饱和度和亮度（Hue、Saturation 以及 Lightness）。

HSL 颜色值是这样规定的：hsl(hue, saturation, lightness)。

1. 色相是色轮上的度数（从 0 到 360）：
   - 0（或 360）是红色
   - 120 是绿色
   - 240 是蓝色
2. 饱和度是一个百分比值：100％ 是全色。
3. 亮度也是一个百分比值：0％ 是深色（黑色），而 100％ 是白色。

hsl(0, 100%, 30%);

hsl(0, 100%, 50%);

hsl(0, 100%, 70%);

hsl(0, 100%, 90%);

下面的例子定义了不同的 HSL 颜色：

### 实例

\#p1 {background-color: hsl(120, 100%, 50%);} /* green */
\#p2 {background-color: hsl(120, 100%, 75%);} /* 浅绿色 */
\#p3 {background-color: hsl(120, 100%, 25%);} /* 深绿色 */
\#p4 {background-color: hsl(120, 60%, 70%);}  /* 柔和的绿色 */

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_color_hsl)

------

## HSLA 颜色

HSLA 颜色值是带有 Alpha 通道的 HSL 颜色值的扩展 - 它规定了颜色的不透明度。

HSLA 颜色值由以下参数规定：hsla(hue, saturation, lightness, alpha)，其中 alpha 参数定义不透明度。 alpha 参数是介于 0.0（完全透明）和 1.0（完全不透明）之间的数字。

hsla(0, 100%, 30%, 0.3);

hsla(0, 100%, 50%, 0.3);

hsla(0, 100%, 70%, 0.3);

hsla(0, 100%, 90%, 0.3);

下面的例子定义了不同的 HSLA 颜色：

### 实例

\#p1 {background-color: hsla(120, 100%, 50%, 0.3);} /* 不透明的绿色 */
\#p2 {background-color: hsla(120, 100%, 75%, 0.3);}  /* 不透明的浅绿色 */
\#p3 {background-color: hsla(120, 100%, 25%, 0.3);}  /* 不透明的深绿色 */
\#p4 {background-color: hsla(120, 60%, 70%, 0.3);}  /* 带有不透明度的柔和绿色 */

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_color_hsla)

------

## 不透明度

CSS opacity 属性设置整个元素的不透明度（背景颜色和文本都将是不透明/透明的）。

opacity 属性值必须是介于 0.0（完全透明）和 1.0（完全不透明）之间的数字。

rgb(255, 0, 0);opacity:0.2;

rgb(255, 0, 0);opacity:0.4;

rgb(255, 0, 0);opacity:0.6;

rgb(255, 0, 0);opacity:0.8;

请注意，上面的文本也将是透明/不透明的！

下面的例子显示了带有不透明度的不同元素：

### 实例

\#p1 {background-color:rgb(255,0,0);opacity:0.6;} /* 不透明的红色 */
\#p2 {background-color:rgb(0,255,0);opacity:0.6;} /* 不透明的绿色 */
\#p3 {background-color:rgb(0,0,255);opacity:0.6;} /* 不透明的蓝色 */

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_color_opacity)

------

## CSS3 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_colors1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_colors2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_colors3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_colors4)

# CSS3 渐变

[❮ 上一节](https://www.w3schools.cn/css/css3_colors.html)[下一节 ❯](https://www.w3schools.cn/css/css3_gradients_radial.html)

------

渐变背景

------

CSS 渐变使您可以显示两种或多种指定颜色之间的平滑过渡。

CSS 定义了两种渐变类型：

- **线性渐变**（向下/向上/向左/向右/对角线）
- **径向渐变**（由其中心定义）

------

## CSS3 线性渐变

如需创建线性渐变，您必须定义至少两个色标。色标是您要呈现平滑过渡的颜色。您还可以设置起点和方向（或角度）以及渐变效果。

### 语法

background-image: linear-gradient(**direction**, **color-stop1**, **color-stop2, ...**);

### 线性渐变 - 从上到下（默认）

下面的例子显示了从顶部开始的线性渐变。它从红色开始，过渡到黄色：

从上到下（默认）

### 实例

\#grad {
 background-image: linear-gradient(red, yellow);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear)

### 线性渐变 - 从左到右

下面的例子展示了从左开始的线性渐变。它从红色开始，过渡到黄色：

从左到右

### 实例

\#grad {
 background-image: linear-gradient(to right, red , yellow);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_ltr)

### 线性渐变 - 对角线

您可以通过指定水平和垂直起始位置来实现对角渐变。

下面的例子展示了从左上角开始（到右下角）的线性渐变。它从红色开始，过渡到黄色：

左上到下右

### 实例

\#grad {
 background-image: linear-gradient(to bottom right, red, yellow);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_diagonal)

------

------

## 使用角度

如果希望对渐变角度做更多的控制，您可以定义一个角度，来取代预定义的方向（向下、向上、向右、向左、向右下等等）。值 0deg 等于向上（to top）。值 90deg 等于向右（to right）。值 180deg 等于向下（to bottom）。

### 语法

background-image: linear-gradient(**angle**, **color-stop1**, **color-stop2**);

下面的例子展示了如何在线性渐变上使用角度：

180deg

### 实例

\#grad {
 background-image: linear-gradient(180deg, red, yellow);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_angles)

------

## 使用多个色标

下面的例子展示了带有多个色标的线性渐变（从上到下）：

### 实例

\#grad {
 background-image: linear-gradient(red, yellow, green);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_cs)

下面的例子展示了如何使用彩虹色和一些文本创建线性渐变（从左到右）：

Rainbow Background

### 实例

\#grad {
 background-image: linear-gradient(to right, red,orange,yellow,green,blue,indigo,violet);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_rainbow)

------

## 使用透明度

CSS 渐变还支持透明度，也可用于创建渐变效果。

如需添加透明度，我们使用 rgba() 函数来定义色标。 rgba() 函数中的最后一个参数可以是 0 到 1 的值，它定义颜色的透明度：0 表示全透明，1 表示全彩色（无透明）。

下面的例子展示了从左开始的线性渐变。它开始完全透明，然后过渡为全色红色：

### 实例

\#grad {
 background-image: linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1));
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_trans)

------

## 重复线性渐变

repeating-linear-gradient() 函数用于重复线性渐变：

### 实例

A repeating linear gradient:

\#grad {
 background-image: repeating-linear-gradient(red, yellow 10%, green 20%);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_repeating)

# CSS3 径向渐变

[❮ 上一节](https://www.w3schools.cn/css/css3_gradients.html)[下一节 ❯](https://www.w3schools.cn/css/css3_shadows.html)

------

## CSS3 径向渐变

径向渐变由其中心定义。

如需创建径向渐变，您还必须定义至少两个色标。

### 语法

background-image: radial-gradient(**shape size** at **position, start-color, ..., last-color**);

默认地，*shape* 为椭圆形，*size* 为最远角，*position* 为中心。

### 径向渐变-均匀间隔的色标（默认）

下面的例子展示了带有均匀间隔的色标的径向渐变：

### 实例

\#grad {
 background-image: radial-gradient(red, yellow, green);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-radial)

### 径向渐变-不同间距的色标

下面的例子展示了一个径向渐变，其色标之间的间隔不同：

### 实例

\#grad {
 background-image: radial-gradient(red 5%, yellow 15%, green 60%);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-radial2)

------

## 设置形状

*shape* 参数定义形状。它可接受 circle 或 ellipse 值。默认值为 ellipse（椭圆）。

下面的例子展示了一个圆形的径向渐变：

### 实例

\#grad {
 background-image: radial-gradient(circle, red, yellow, green);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-radial_shape)

------

## 使用大小不同的关键字

*size* 参数定义渐变的大小。它可接受四个值：

- **closest-side**
- **farthest-side**
- **closest-corner**
- **farthest-corner**

### 实例

设置了不同 size 关键词的径向渐变：

\#grad1 {
 background-image: radial-gradient(closest-side at 60% 55%, red, yellow, black);
}

\#grad2 {
 background-image: radial-gradient(farthest-side at 60% 55%, red, yellow, black);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-radial_size)

------

## 重复径向渐变

repeating-radial-gradient() 函数用于重复径向渐变：

### 实例

A repeating radial gradient:

\#grad {
 background-image: repeating-radial-gradient(red, yellow 10%, green 15%);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-radial_repeating)

------

## CSS3 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_gradients1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_gradients2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_gradients3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_gradients4)[测验 5 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_gradients5)[测验 6 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_gradients6)[测验 7 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_gradients7)

------

## CSS3 渐变属性

下表列出了 CSS 渐变属性：

| 属性                                                         | 描述                               |
| :----------------------------------------------------------- | :--------------------------------- |
| [background-image](https://www.w3schools.cn/cssref/pr_background-image.html) | 为一个元素设置一幅或多幅背景图像。 |

# CSS3 阴影效果

[❮ 上一节](https://www.w3schools.cn/css/css3_gradients_radial.html)[下一节 ❯](https://www.w3schools.cn/css/css3_shadows_box.html)

------

![Norway](https://www.w3schools.cn/css/rock600x400.jpg)

Shadows

用 CSS 创建阴影效果！

在我上面悬停！

------

## CSS3 阴影效果

通过使用 CSS，您可以在文本和元素上添加阴影。

在我们的教程中，您将学习如下属性：

- text-shadow
- box-shadow

------

## CSS3 文字阴影

CSS text-shadow 属性为文本添加阴影。

最简单的用法是只指定水平阴影（2px）和垂直阴影（2px）：

## 文字阴影效果！

### 实例

h1 {
 text-shadow: 2px 2px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow1)

接下来，为阴影添加颜色：

## 文字阴影效果！

### 实例

h1 {
 text-shadow: 2px 2px red;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow2)

然后，向阴影添加模糊效果：

## 文字阴影效果！

### 实例

h1 {
 text-shadow: 2px 2px 5px red;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow3)

下面的例子展示了带有黑色阴影的白色文本：

## 文字阴影效果！

### 实例

h1 {
 color: white;
 text-shadow: 2px 2px 4px #000000;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow4)

下面的例子展示了红色的霓虹发光阴影：

## 文字阴影效果！

### 实例

h1 {
 text-shadow: 0 0 3px #FF0000;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow5)

------

## 多个阴影

如需在文本中添加多个阴影，您可以添加以逗号分隔的阴影列表。

下面的例子展示了红色和蓝色的霓虹灯发光阴影：

## 文字阴影效果！

### 实例

h1 {
 text-shadow: 0 0 3px #FF0000, 0 0 5px #0000FF;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow6)

下面的例子展示了带有黑色、蓝色和深蓝色阴影的白色文本：

## 文字阴影效果！

### 实例

h1 {
 color: white;
 text-shadow: 1px 1px 2px black, 0 0 25px blue, 0 0 5px darkblue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow7)

您还可以使用 text-shadow 属性在文本周围创建纯边框（无阴影）：

## 包围文本的边框！

### 实例

h1 {
 color: yellow;
 text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow_border)

# CSS3 Box 盒子阴影

[❮ 上一节](https://www.w3schools.cn/css/css3_shadows.html)[下一节 ❯](https://www.w3schools.cn/css/css3_text_effects.html)

------

## CSS3 box-shadow 属性

CSS box-shadow 属性应用阴影于元素。

最简单的用法是只指定水平阴影和垂直阴影：

带有黑色 box-shadow 的黄色 <div> 元素

### 实例

div {
 box-shadow: 10px 10px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-shadow)

接下来，为阴影添加颜色：

带有灰色 box-shadow 的黄色 <div> 元素

### 实例

div {
 box-shadow: 10px 10px grey;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-shadow2)

接下来，向阴影添加模糊效果：

黄色的 <div> 元素，带有模糊的 box-shadow

### 实例

div {
 box-shadow: 10px 10px 5px grey;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-shadow3)

------

## 卡片

您还可以使用 box-shadow 属性创建纸质卡片效果：

# 1

January 1, 2016

![Norway](https://www.w3schools.cn/css/rock600x400.jpg)

Hardanger, Norway

### 实例

div.card {
 width: 250px;
 box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
 text-align: center;
}

[Try it (Text Card) »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-shadow4) [Try it (Image Card) »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-shadow5)

------

## CSS3 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_shadows1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_shadows2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_shadows3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_shadows4)[测验 5 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_shadows5)

------

## CSS3 阴影属性

下表列出了 CSS 的阴影属性：

| 属性                                                         | 描述                           |
| :----------------------------------------------------------- | :----------------------------- |
| [box-shadow](https://www.w3schools.cn/cssref/css3_pr_box-shadow.html) | 向一个元素添加一个或多个阴影。 |
| [text-shadow](https://www.w3schools.cn/cssref/css3_pr_text-shadow.html) | 在文本中添加一个或多个阴影。   |



[❮ 上一节](https://www.w3schools.cn/css/css3_shadows.html)[下一节 ❯](https://www.w3schools.cn/css/css3_text_effects.html)

# CSS3 文本效果

[❮ 上一节](https://www.w3schools.cn/css/css3_shadows_box.html)[下一节 ❯](https://www.w3schools.cn/css/css3_fonts.html)

------

## CSS3 文本溢出、整字换行、换行规则以及书写模式

在本章中，您将学习如下属性：

- `text-overflow`
- `word-wrap`
- `word-break`
- `writing-mode`

------

## CSS3 文字溢出

CSS text-overflow 属性规定应如何向用户呈现未显示的溢出内容。

可以被裁剪：

This is some long text that will not fit in the box

也可以将其呈现为省略号（...）：

This is some long text that will not fit in the box

CSS 代码如下：

### 实例

p.test1 {
 white-space: nowrap;
 width: 200px;
 border: 1px solid #000000;
 overflow: hidden;
 text-overflow: clip;
}

p.test2 {
 white-space: nowrap;
 width: 200px;
 border: 1px solid #000000;
 overflow: hidden;
 text-overflow: ellipsis;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-overflow)

下面的例子展示了将鼠标悬停在元素上时如何显示溢出的内容：

### 实例

div.test:hover {
 overflow: visible;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-overflow_hover)

------

------

## CSS3 字换行（Word Wrapping）

CSS word-wrap 属性使长文字能够被折断并换到下一行。

如果一个单词太长而无法容纳在一个区域内，它会向外扩展：

This paragraph contains a very long word: thisisaveryveryveryveryveryverylongword. The long word will break and wrap to the next line.

通过 word-wrap 属性，您可以强制对文本进行换行 - 即使这意味着在词中间将其拆分：

This paragraph contains a very long word: thisisaveryveryveryveryveryverylongword. The long word will break and wrap to the next line.

CSS 代码如下：

### 实例

允许长单词被打断并换行到下一行：

p {
 word-wrap: break-word;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_word-wrap)

------

## CSS3 换行规则

CSS word-break 属性指定换行规则。

本段包含一些文本。 此行将在连字符处中断。

本段包含一些文本。 换行会在任何字符处中断。

### CSS 代码如下：

### 实例

p.test1 {
 word-break: keep-all;
}

p.test2 {
 word-break: break-all;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_word-break)

------

## CSS3 书写模式

CSS writing-mode 属性规定文本行是水平放置还是垂直放置。

一些带有 span 元素的文本，其书写模式为 vertical-rl。

下面的例子展示了一些不同的书写模式：

### 实例

p.test1 {
 writing-mode: horizontal-tb;
}

span.test2 {
 writing-mode: vertical-rl;
}

p.test2 {
 writing-mode: vertical-rl;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_writing-mode)

------

## CSS3 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_text_effects1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_text_effects2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_text_effects3)

------

## CSS3 文本效果属性

下表列出了 CSS 文本效果属性：

| 属性                                                         | 描述                                   |
| :----------------------------------------------------------- | :------------------------------------- |
| [text-align-last](https://www.w3schools.cn/cssref/css3_pr_text-align-last.html) | 指定如何对齐文本的最后一行。           |
| [text-justify](https://www.w3schools.cn/cssref/css3_pr_text-justify.html) | 指定对齐的文本应如何对齐和间隔。       |
| [text-overflow](https://www.w3schools.cn/cssref/css3_pr_text-overflow.html) | 指定应如何向用户呈现未显示的溢出内容。 |
| [word-break](https://www.w3schools.cn/cssref/css3_pr_word-break.html) | 指定非 CJK 脚本的换行规则。            |
| [word-wrap](https://www.w3schools.cn/cssref/css3_pr_word-wrap.html) | 允许长单词被打断并换到下一行。         |
| [writing-mode](https://www.w3schools.cn/cssref/css3_pr_writing-mode.html) | 指定文本行是水平放置还是垂直放置。     |

# CSS3 Web 字体

[❮ 上一节](https://www.w3schools.cn/css/css3_text_effects.html)[下一节 ❯](https://www.w3schools.cn/css/css3_2dtransforms.html)

------

## CSS3 @font-face 规则

Web 字体允许 Web 设计人员使用用户计算机上未安装的字体。

当您找到/购买了想要使用的字体后，只需将字体文件包含在您的 Web 服务器上，它将在需要时自动下载给用户。

您的"自有"字体在 CSS @font-face 规则中进行定义。

------

## 不同的字体格式

### TrueType 字体 (TTF)

TrueType 是 1980 年代后期由 Apple 和 Microsoft 开发的字体标准。 TrueType 是 Mac OS 和 Microsoft Windows 操作系统最常用的字体格式。

### OpenType 字体 (OTF)

OpenType 是可缩放计算机字体的格式。它基于 TrueType 构建，并且是 Microsoft 的注册商标。今天，OpenType 字体在主要计算机平台上得到普遍使用。

### Web 开放字体格式 (WOFF)

WOFF 是用于网页的字体格式。它于 2009 年开发，现已成为 W3C 的推荐标准。 WOFF 本质上是具有压缩和其他元数据的 OpenType 或 TrueType。目标是支持在有带宽限制的网络上从服务器到客户端进行字体分发。

### Web 开放字体格式 (WOFF 2.0)

TrueType/OpenType 字体比 WOFF 1.0 提供更好的压缩。

### SVG 字体/形状

SVG 字体允许在显示文本时将 SVG 用作字形。 SVG 1.1 规范定义了一个字体模块，该模块允许在 SVG 文档中创建字体。您还可以将 CSS 应用于 SVG 文档，同时 @font-face 规则可以应用于 SVG 文档中的文本。

### 嵌入式 OpenType 字体 (EOT)

EOT 字体是 Microsoft 设计的 OpenType 字体的紧凑形式，用作网页上的嵌入式字体。

------

------

## 对字体格式的浏览器支持

表格中的数字注明了完全支持该字体格式的首个浏览器版本。

| Font format |               |               |               |               |               |
| :---------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| TTF/OTF     | 9.0*          | 4.0           | 3.5           | 3.1           | 10.0          |
| WOFF        | 9.0           | 5.0           | 3.6           | 5.1           | 11.1          |
| WOFF2       | 14.0          | 36.0          | 39.0          | 10.0          | 26.0          |
| SVG         | Not supported | Not supported | Not supported | 3.2           | Not supported |
| EOT         | 6.0           | Not supported | Not supported | Not supported | Not supported |

*IE：该字体格式仅在设置为 "installable" 时有效。

------

## 使用您需要的字体

在 `@font-face` 规则中：首先定义字体的名称（例如 myFirstFont），然后指向该字体文件。

**提示:** 字体 URL 始终使用小写字母。大写字母可能会在 IE 中产生意外结果。

如需将字体用于 HTML 元素，请通过 `font-family` 属性引用字体名称（myFirstFont）：

### 实例

@font-face {
 font-family: myFirstFont;
 src: url(sansation_light.woff);
}

div {
 font-family: myFirstFont;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_font-face_rule)

------

## 使用粗体文本

您必须添加另一条 `@font-face` 规则，其中包含粗体文本的描述符：

### 实例

@font-face {
 font-family: myFirstFont;
 src: url(sansation_bold.woff);
 font-weight: bold;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_font-face_rule_bold)

文件 "sansation_bold.woff" 是另一个字体文件，其中包含 Sansation 字体的粗体字符。

每当带有 "myFirstFont" 字体族的一段文本应呈现粗体时，浏览器都会使用它。

这样，您就可以为同一字体设置许多 @font-face 规则。

------

## CSS3 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_fonts1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_fonts2)

------

## CSS3 字体描述

下表列出了能够在 @font-face 规则内定义的所有字体描述符（font descriptor）：

| Descriptor    | Values                                                       | 描述                                                         |
| :------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| font-family   | *name*                                                       | 必需。定义字体名称。                                         |
| src           | *URL*                                                        | 必需。定义字体文件的 URL。                                   |
| font-stretch  | normal condensed ultra-condensed extra-condensed semi-condensed expanded semi-expanded extra-expanded ultra-expanded | 可选。定义应如何拉伸字体。默认值是 "normal"。                |
| font-style    | normal italic oblique                                        | 可选。定义字体的样式。默认值是 "normal"。                    |
| font-weight   | normal bold 100 200 300 400 500 600 700 800 900              | 可选。定义字体的粗细。默认值是 "normal"。                    |
| unicode-range | *unicode-range*                                              | 可选。定义字体支持的 UNICODE 字符范围。默认值是 "U+0-10FFFF"。 |

# CSS3 2D 转换

[❮ 上一节](https://www.w3schools.cn/css/css3_fonts.html)[下一节 ❯](https://www.w3schools.cn/css/css3_3dtransforms.html)

------

## CSS3 2D 转换

CSS 转换（transforms）允许您移动、旋转、缩放和倾斜元素。

把鼠标悬停在下面的元素上，可以查看 2D 转换：

2D rotate

在本章中，您将学习如下 CSS 属性：

- `transform`

------

## 浏览器支持

表中的数字表示支持该属性的第一个浏览器版本。

| 属性      |      |      |      |      |      |
| :-------- | ---- | ---- | ---- | ---- | ---- |
| transform | 36.0 | 10.0 | 16.0 | 9.0  | 23.0 |

------

## CSS3 2D 转换方法

通过使用 CSS transform 属性，您可以利用以下 2D 转换方法：

- `translate()`
- `rotate()`
- `scaleX()`
- `scaleY()`
- `scale()`
- `skewX()`
- `skewY()`
- `skew()`
- `matrix()`

**提示:** 您将在下一章中学习 3D 转换。

------

## translate() 方法

![Translate](https://www.w3schools.cn/css/transform_translate.gif)



translate() 方法从其当前位置移动元素（根据为 X 轴和 Y 轴指定的参数）。

下面的例子把 <div> 元素从其当前位置向右移动 50 个像素，并向下移动 100 个像素：

### 实例

div {
 transform: translate(50px, 100px);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_translate)

------

## rotate() 方法

![Rotate](https://www.w3schools.cn/css/transform_rotate.gif)

rotate() 方法根据给定的角度顺时针或逆时针旋转元素。

下面的例子把 <div> 元素顺时针旋转 20 度：

### 实例

div {
 transform: rotate(20deg);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_rotate)

使用负值将逆时针旋转元素。

下面的例子把 <div> 元素逆时针旋转 20 度：

### 实例

div {
 transform: rotate(-20deg);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_rotate2)

------

------

## scale() 方法

![Scale](https://www.w3schools.cn/css/transform_scale.gif)



scale() 方法增加或减少元素的大小（根据给定的宽度和高度参数）。

下面的例子把 <div> 元素增大为其原始宽度的两倍和其原始高度的三倍：

### 实例

div {
 transform: scale(2, 3);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_scale)

下面的例子把 <div> 元素减小为其原始宽度和高度的一半：

### 实例

div {
 transform: scale(0.5, 0.5);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_scale2)

------

## scaleX() 方法

scaleX() 方法增加或减少元素的宽度。

下面的例子把 <div> 元素增大为其原始宽度的两倍：

### 实例

div {
 transform: scaleX(2);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_scaleX)

以下例子把 <div> 元素缩减为其原始宽度的一半：

### 实例

div {
 transform: scaleX(0.5);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_scaleX2)

------

## scaleY() 方法

scaleY() 方法增加或减少元素的高度。

下面的例子把 <div> 元素增大到其原始高度的三倍：

### 实例

div {
 transform: scaleY(3);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_scaleY)

下面的例子把 <div> 元素缩减为其原始高度的一半：

### 实例

div {
 transform: scaleY(0.5);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_scaleY2)

------

## The skewX() Method

## skewX() 方法

skewX() 方法使元素沿 X 轴倾斜给定角度。

下例把 <div> 元素沿X轴倾斜 20 度：

### 实例

div {
 transform: skewX(20deg);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_skewx)

------

## skewY() 方法

skewY() 方法使元素沿 Y 轴倾斜给定角度。

下例把 <div> 元素沿 Y 轴倾斜 20 度：

### 实例

div {
 transform: skewY(20deg);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_skewy)

------

## skew() 方法

skew() 方法使元素沿 X 和 Y 轴倾斜给定角度。

下面的例子使 <div> 元素沿 X 轴倾斜 20 度，同时沿 Y 轴倾斜 10 度：

### 实例

div {
 transform: skew(20deg, 10deg);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_skew)

如果未指定第二个参数，则值为零。因此，下例使 <div> 元素沿 X 轴倾斜 20 度：

### 实例

div {
 transform: skew(20deg);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_skew2)

------

## matrix() 方法

![Rotate](https://www.w3schools.cn/css/transform_rotate.gif)

matrix() 方法把所有 2D 变换方法组合为一个。

matrix() 方法可接受六个参数，其中包括数学函数，这些参数使您可以旋转、缩放、移动（平移）和倾斜元素。

参数如下：matrix(scaleX(),skewY(),skewX(),scaleY(),translateX(),translateY())

### 实例

div {
 transform: matrix(1, -0.3, 0, 1, 0, 0);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_matrix1)

------

## CSS3 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_2dtransforms1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_2dtransforms2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_2dtransforms3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_2dtransforms4)

------

## CSS3 转换属性

下表列出了所有 2D 变换属性：

| 属性                                                         | 描述                         |
| :----------------------------------------------------------- | :--------------------------- |
| [transform](https://www.w3schools.cn/cssref/css3_pr_transform.html) | 向元素应用 2D 或 3D 转换。   |
| [transform-origin](https://www.w3schools.cn/cssref/css3_pr_transform-origin.html) | 允许你改变被转换元素的位置。 |

## CSS3 2D 转换方法

| 函数                            | 描述                                     |
| :------------------------------ | :--------------------------------------- |
| matrix(*n*,*n*,*n*,*n*,*n*,*n*) | 定义 2D 转换，使用六个值的矩阵。         |
| translate(*x*,*y*)              | 定义 2D 转换，沿着 X 和 Y 轴移动元素。   |
| translateX(*n*)                 | 定义 2D 转换，沿着 X 轴移动元素。        |
| translateY(*n*)                 | 定义 2D 转换，沿着 Y 轴移动元素。        |
| scale(*x*,*y*)                  | 定义 2D 缩放转换，改变元素的宽度和高度。 |
| scaleX(*n*)                     | 定义 2D 缩放转换，改变元素的宽度。       |
| scaleY(*n*)                     | 定义 2D 缩放转换，改变元素的高度。       |
| rotate(*angle*)                 | 定义 2D 旋转，在参数中规定角度。         |
| skew(*x-angle*,*y-angle*)       | 定义 2D 倾斜转换，沿着 X 和 Y 轴。       |
| skewX(*angle*)                  | 定义 2D 倾斜转换，沿着 X 轴。            |
| skewY(*angle*)                  | 定义 2D 倾斜转换，沿着 Y 轴。            |



[❮ 上一节](https://www.w3schools.cn/css/css3_fonts.html)[下一节 ❯](https://www.w3schools.cn/css/css3_3dtransforms.html)

# CSS3 3D 转换

[❮ 上一节](https://www.w3schools.cn/css/css3_2dtransforms.html)[下一节 ❯](https://www.w3schools.cn/css/css3_transitions.html)

------

## CSS3 3D 转换

CSS 还支持 3D 转换。

请将鼠标悬停在下面的元素上，即可查看 2D 和 3D 转换之间的区别：

2D rotate

3D rotate

在本章中，您将学习如下 CSS 属性：

- `transform`

------

## 浏览器支持

表中的数字表示支持该属性的第一个浏览器版本。

| 属性      |      |      |      |      |      |
| :-------- | ---- | ---- | ---- | ---- | ---- |
| transform | 36.0 | 10.0 | 16.0 | 9.0  | 23.0 |

------

## CSS3 3D 转换方法

通过 CSS transform 属性，您可以使用以下 3D 转换方法：

- `rotateX()`
- `rotateY()`
- `rotateZ()`

------

## rotateX() 方法

![Rotate X](https://www.w3schools.cn/css/transform_rotatex.gif)

rotateX() 方法使元素绕其 X 轴旋转给定角度：

### 实例

\#myDiv {
 transform: rotateX(150deg);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_rotateX)

------

## rotateY() 方法

![Rotate Y](https://www.w3schools.cn/css/transform_rotatey.gif)

rotateY() 方法使元素绕其 Y 轴旋转给定角度：

### 实例

\#myDiv {
 transform: rotateY(130deg);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_rotateY)

------

## rotateZ() 方法

rotateZ() 方法使元素绕其 Z 轴旋转给定角度：

### 实例

\#myDiv {
 transform: rotateZ(90deg);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_rotateZ)

------

## CSS3 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_3dtransforms1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_3dtransforms2)[Exercise 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_3dtransforms3)

------

## CSS3 转换属性

下表列出了所有 3D 变换属性：

| 属性                                                         | 描述                                 |
| :----------------------------------------------------------- | :----------------------------------- |
| [transform](https://www.w3schools.cn/cssref/css3_pr_transform.html) | 向元素应用 2D 或 3D 转换。           |
| [transform-origin](https://www.w3schools.cn/cssref/css3_pr_transform-origin.html) | 允许你改变被转换元素的位置。         |
| [transform-style](https://www.w3schools.cn/cssref/css3_pr_transform-style.html) | 规定被嵌套元素如何在 3D 空间中显示。 |
| [perspective](https://www.w3schools.cn/cssref/css3_pr_perspective.html) | 规定 3D 元素的透视效果。             |
| [perspective-origin](https://www.w3schools.cn/cssref/css3_pr_perspective-origin.html) | 规定 3D 元素的底部位置。             |
| [backface-visibility](https://www.w3schools.cn/cssref/css3_pr_backface-visibility.html) | 定义元素在不面对屏幕时是否可见。     |

## CSS3 3D 转换方法

| 函数                                                         | 描述                                      |
| :----------------------------------------------------------- | :---------------------------------------- |
| matrix3d(*n*,*n*,*n*,*n*,*n*,*n*, *n*,*n*,*n*,*n*,*n*,*n*,*n*,*n*,*n*,*n*) | 定义 3D 转换，使用 16 个值的 4x4 矩阵。   |
| translate3d(*x*,*y*,*z*)                                     | 定义 3D 转化。                            |
| translateX(*x*)                                              | 定义 3D 转化，仅使用用于 X 轴的值。       |
| translateY(*y*)                                              | 定义 3D 转化，仅使用用于 Y 轴的值。       |
| translateZ(*z*)                                              | 定义 3D 转化，仅使用用于 Z 轴的值。       |
| scale3d(*x*,*y*,*z*)                                         | 定义 3D 缩放转换。                        |
| scaleX(*x*)                                                  | 定义 3D 缩放转换，通过给定一个 X 轴的值。 |
| scaleY(*y*)                                                  | 定义 3D 缩放转换，通过给定一个 Y 轴的值。 |
| scaleZ(*z*)                                                  | 定义 3D 缩放转换，通过给定一个 Z 轴的值。 |
| rotate3d(*x*,*y*,*z*,*angle*)                                | 定义 3D 旋转。                            |
| rotateX(*angle*)                                             | 定义沿 X 轴的 3D 旋转。                   |
| rotateY(*angle*)                                             | 定义沿 Y 轴的 3D 旋转。                   |
| rotateZ(*angle*)                                             | 定义沿 Z 轴的 3D 旋转。                   |
| perspective(*n*)                                             | 定义 3D 转换元素的透视视图。              |



[❮ 上一节](https://www.w3schools.cn/css/css3_2dtransforms.html)[下一节 ❯](https://www.w3schools.cn/css/css3_transitions.html)

# CSS3 过渡

[❮ 上一节](https://www.w3schools.cn/css/css3_3dtransforms.html)[下一节 ❯](https://www.w3schools.cn/css/css3_animations.html)

------

## CSS3 过渡

CSS 过渡允许您在给定的时间内平滑地改变属性值。

请把鼠标移动到这个元素上，来查看 CSS 过渡效果：

CSS

在本章中，您将学习如下属性：

- `transition`
- `transition-delay`
- `transition-duration`
- `transition-property`
- `transition-timing-function`

------

## 对过渡的浏览器支持

表中的数字表示支持该属性的第一个浏览器版本。

| 属性                       |      |      |      |      |      |
| :------------------------- | ---- | ---- | ---- | ---- | ---- |
| transition                 | 26.0 | 10.0 | 16.0 | 6.1  | 12.1 |
| transition-delay           | 26.0 | 10.0 | 16.0 | 6.1  | 12.1 |
| transition-duration        | 26.0 | 10.0 | 16.0 | 6.1  | 12.1 |
| transition-property        | 26.0 | 10.0 | 16.0 | 6.1  | 12.1 |
| transition-timing-function | 26.0 | 10.0 | 16.0 | 6.1  | 12.1 |

------

## 如何使用 CSS 过渡？

如需创建过渡效果，必须明确两件事：

- 您要添加效果的 CSS 属性
- 效果的持续时间

**注释:** 如果未规定持续时间部分，则过渡不会有效果，因为默认值为 0。

下面的例子展示了 100px * 100px 的红色 <div> 元素。 <div> 元素还为 width 属性指定了过渡效果，持续时间为 2 秒：

### 实例

div {
 width: 100px;
 height: 100px;
 background: red;
 transition: width 2s;
}



当指定的 CSS 属性（width）值发生变化时，将开始过渡效果。

现在，让我们为 width 属性指定一个鼠标悬停在 <div> 元素上时的新值：

### 实例

div:hover {
 width: 300px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition1)

请注意，当光标从元素上移开时，它将逐渐变回其原始样式。

------

## 改变若干属性值

下面的例子为 width 和 height 属性都添加了过渡效果，width 是 2 秒，height 是 4 秒：

### 实例

div {
 transition: width 2s, height 4s;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition2)

------

------

## 指定过渡的速度曲线

transition-timing-function 属性规定过渡效果的速度曲线。

transition-timing-function 属性可接受以下值：

- ease - 规定过渡效果，先缓慢地开始，然后加速，然后缓慢地结束（默认）
- linear - 规定从开始到结束具有相同速度的过渡效果
- ease-in -规定缓慢开始的过渡效果
- ease-out - 规定缓慢结束的过渡效果
- ease-in-out - 规定开始和结束较慢的过渡效果
- cubic-bezier(n,n,n,n) - 允许您在三次贝塞尔函数中定义自己的值

下面的例子展示了可以使用的一些不同的速度曲线：

### 实例

\#div1 {transition-timing-function: linear;}
\#div2 {transition-timing-function: ease;}
\#div3 {transition-timing-function: ease-in;}
\#div4 {transition-timing-function: ease-out;}
\#div5 {transition-timing-function: ease-in-out;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition_speed)

------

## 延迟过渡效果

transition-delay 属性规定过渡效果的延迟（以秒计）。

下例在启动之前有 1 秒的延迟：

### 实例

div {
 transition-delay: 1s;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition_delay)

------

## 过渡 + 转换

下例为转换添加过渡效果：

### 实例

div {
 transition: width 2s, height 2s, transform 2s;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition_transform)

------

## 更多过渡实例

您可以可以一一指定 CSS 过渡属性，如下所示：

### 实例

div {
 transition-property: width;
 transition-duration: 2s;
 transition-timing-function: linear;
 transition-delay: 1s;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition4)

或使用简写的 transition 属性：

### 实例

div {
 transition: width 2s linear 1s;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition5)

------

## CSS3 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_transitions1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_transitions2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_transitions3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_transitions4)[测验 5 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_transitions5)

------

## CSS3 过渡属性

下表列出了所有 CSS 过渡属性：

| 属性                                                         | 描述                                         |
| :----------------------------------------------------------- | :------------------------------------------- |
| [transition](https://www.w3schools.cn/cssref/css3_pr_transition.html) | 简写属性，用于将四个过渡属性设置为单一属性。 |
| [transition-delay](https://www.w3schools.cn/cssref/css3_pr_transition-delay.html) | 规定过渡效果的延迟（以秒计）。               |
| [transition-duration](https://www.w3schools.cn/cssref/css3_pr_transition-duration.html) | 规定过渡效果要持续多少秒或毫秒。             |
| [transition-property](https://www.w3schools.cn/cssref/css3_pr_transition-property.html) | 规定过渡效果所针对的 CSS 属性的名称。        |
| [transition-timing-function](https://www.w3schools.cn/cssref/css3_pr_transition-timing-function.html) | 规定过渡效果的速度曲线。                     |





# CSS3 动画

[❮ 上一节](https://www.w3schools.cn/css/css3_transitions.html)[下一节 ❯](https://www.w3schools.cn/css/css_tooltip.html)

------

## CSS3 动画

CSS 可实现 HTML 元素的动画效果，而不使用 JavaScript 或 Flash！

CSS

在本章中，您将学习如下属性：

- `@keyframes`
- `animation-name`
- `animation-duration`
- `animation-delay`
- `animation-iteration-count`
- `animation-direction`
- `animation-timing-function`
- `animation-fill-mode`
- `animation`

------

## 对动画的浏览器支持

表中的数字表示支持该属性的第一个浏览器版本。

| 属性                      |      |      |      |      |      |
| :------------------------ | ---- | ---- | ---- | ---- | ---- |
| @keyframes                | 43.0 | 10.0 | 16.0 | 9.0  | 30.0 |
| animation-name            | 43.0 | 10.0 | 16.0 | 9.0  | 30.0 |
| animation-duration        | 43.0 | 10.0 | 16.0 | 9.0  | 30.0 |
| animation-delay           | 43.0 | 10.0 | 16.0 | 9.0  | 30.0 |
| animation-iteration-count | 43.0 | 10.0 | 16.0 | 9.0  | 30.0 |
| animation-direction       | 43.0 | 10.0 | 16.0 | 9.0  | 30.0 |
| animation-timing-function | 43.0 | 10.0 | 16.0 | 9.0  | 30.0 |
| animation-fill-mode       | 43.0 | 10.0 | 16.0 | 9.0  | 30.0 |
| animation                 | 43.0 | 10.0 | 16.0 | 9.0  | 30.0 |

------

## 什么是 CSS 动画？

动画使元素逐渐从一种样式变为另一种样式。

您可以随意更改任意数量的 CSS 属性。

如需使用 CSS 动画，您必须首先为动画指定一些关键帧。

关键帧包含元素在特定时间所拥有的样式。

------

## @keyframes 规则

如果您在 @keyframes 规则中指定了 CSS 样式，动画将在特定时间逐渐从当前样式更改为新样式。

要使动画生效，必须将动画绑定到某个元素。

下面的例子将 "example" 动画绑定到 <div> 元素。动画将持续 4 秒钟，同时将 <div> 元素的背景颜色从 "red" 逐渐改为 "yellow"：

### 实例

/* 动画代码 */
@keyframes example {
 from {background-color: red;}
 to {background-color: yellow;}
}

/* 将动画应用到的元素 */
div {
 width: 100px;
 height: 100px;
 background-color: red;
 animation-name: example;
 animation-duration: 4s;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation1)

**注释:** The `animation-duration` 属性定义需要多长时间才能完成动画。如果未指定 `animation-duration` 属性，则动画不会发生，因为默认值是 0s（0秒）。

在上面的例子中，通过使用关键字 "from" 和 "to"（代表 0％（开始）和 100％（完成）），我们设置了样式何时改变。

您也可以使用百分比值。通过使用百分比，您可以根据需要添加任意多个样式更改。

下面的例子将在动画完成 25％，完成 50％ 以及动画完成 100％ 时更改 <div> 元素的背景颜色：

### 实例

/* 动画代码 */
@keyframes example {
 0%  {background-color: red;}
 25% {background-color: yellow;}
 50% {background-color: blue;}
 100% {background-color: green;}
}

/* 将动画应用到的元素 */
div {
 width: 100px;
 height: 100px;
 background-color: red;
 animation-name: example;
 animation-duration: 4s;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation2)

下面的例子将在动画完成 25％，完成 50％ 以及动画完成 100％ 时更改背景颜色和 <div> 元素的位置：

### 实例

/* 动画代码 */
@keyframes example {
 0%  {background-color:red; left:0px; top:0px;}
 25% {background-color:yellow; left:200px; top:0px;}
 50% {background-color:blue; left:200px; top:200px;}
 75% {background-color:green; left:0px; top:200px;}
 100% {background-color:red; left:0px; top:0px;}
}

/* 将动画应用到的元素 */
div {
 width: 100px;
 height: 100px;
 position: relative;
 background-color: red;
 animation-name: example;
 animation-duration: 4s;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation3)

------

------

## 延迟动画

animation-delay 属性规定动画开始的延迟时间。

下面的例子在开始动画前有 2 秒的延迟：

### 实例

div {
 width: 100px;
 height: 100px;
 position: relative;
 background-color: red;
 animation-name: example;
 animation-duration: 4s;
 animation-delay: 2s;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_delay)

负值也是允许的。如果使用负值，则动画将开始播放，如同已播放 N 秒。

在下面的例子中，动画将开始播放，就好像它已经播放了 2 秒钟一样：

### 实例

div {
 width: 100px;
 height: 100px;
 position: relative;
 background-color: red;
 animation-name: example;
 animation-duration: 4s;
 animation-delay: -2s;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_delay2)

------

## 设置动画应运行多少次

animation-iteration-count 属性指定动画应运行的次数。

下面的例子在停止前把动画运行 3 次：

### 实例

div {
 width: 100px;
 height: 100px;
 position: relative;
 background-color: red;
 animation-name: example;
 animation-duration: 4s;
 animation-iteration-count: 3;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_count)

下面的例子使用值 "infinite" 使动画永远持续下去：

### 实例

div {
 width: 100px;
 height: 100px;
 position: relative;
 background-color: red;
 animation-name: example;
 animation-duration: 4s;
 animation-iteration-count: infinite;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_count2)

------

## 反向或交替运行动画

animation-direction 属性指定是向前播放、向后播放还是交替播放动画。

animation-direction 属性可接受以下值：

- normal - 动画正常播放（向前）。默认值
- reverse - 动画以反方向播放（向后）
- alternate - 动画先向前播放，然后向后
- alternate-reverse - 动画先向后播放，然后向前

下例将以相反的方向（向后）运行动画：

### 实例

div {
 width: 100px;
 height: 100px;
 position: relative;
 background-color: red;
 animation-name: example;
 animation-duration: 4s;
 animation-direction: reverse;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_direction)

下面的例子使用值 "alternate" 使动画先向前运行，然后向后运行：

### 实例

div {
 width: 100px;
 height: 100px;
 position: relative;
 background-color: red;
 animation-name: example;
 animation-duration: 4s;
 animation-iteration-count: 2;
 animation-direction: alternate;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_direction2)

下面的例子使用值 "alternate-reverse" 使动画先向后运行，然后向前运行：

### 实例

div {
 width: 100px;
 height: 100px;
 position: relative;
 background-color: red;
 animation-name: example;
 animation-duration: 4s;
 animation-iteration-count: 2;
 animation-direction: alternate-reverse;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_direction3)

------

## 指定动画的速度曲线

animation-timing-function 属性规定动画的速度曲线。

animation-timing-function 属性可接受以下值：

- ease - 指定从慢速开始，然后加快，然后缓慢结束的动画（默认）
- linear - 规定从开始到结束的速度相同的动画
- ease-in - 规定慢速开始的动画
- ease-out - 规定慢速结束的动画
- ease-in-out - 指定开始和结束较慢的动画
- cubic-bezier(n,n,n,n) - 运行您在三次贝塞尔函数中定义自己的值

下面这些例子展示了可以使用的一些不同速度曲线：

### 实例

\#div1 {animation-timing-function: linear;}
\#div2 {animation-timing-function: ease;}
\#div3 {animation-timing-function: ease-in;}
\#div4 {animation-timing-function: ease-out;}
\#div5 {animation-timing-function: ease-in-out;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_speed)

------

## 指定动画的填充模式

CSS 动画不会在第一个关键帧播放之前或在最后一个关键帧播放之后影响元素。animation-fill-mode 属性能够覆盖这种行为。

在不播放动画时（在开始之前，结束之后，或两者都结束时），animation-fill-mode 属性规定目标元素的样式。

animation-fill-mode 属性可接受以下值：

- none - 默认值。动画在执行之前或之后不会对元素应用任何样式。
- forwards - 元素将保留由最后一个关键帧设置的样式值（依赖 animation-direction 和 animation-iteration-count）。
- backwards - 元素将获取由第一个关键帧设置的样式值（取决于 animation-direction），并在动画延迟期间保留该值。
- both - 动画会同时遵循向前和向后的规则，从而在两个方向上扩展动画属性。

下面的例子让 <div> 元素在动画结束时保留来自最后一个关键帧的样式值：

### 实例

div {
 width: 100px;
 height: 100px;
 background: red;
 position: relative;
 animation-name: example;
 animation-duration: 3s;
 animation-fill-mode: forwards;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_fill-mode)

下面的例子在动画开始之前（在动画延迟期间）使 <div> 元素获得由第一个关键帧设置的样式值：

### 实例

div {
 width: 100px;
 height: 100px;
 background: red;
 position: relative;
 animation-name: example;
 animation-duration: 3s;
 animation-delay: 2s;
 animation-fill-mode: backwards;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_fill-mode2)

下面的例子在动画开始之前使 <div> 元素获得第一个关键帧设置的样式值，以及在动画结束时保留最后一个关键帧的样式值：

### 实例

div {
 width: 100px;
 height: 100px;
 background: red;
 position: relative;
 animation-name: example;
 animation-duration: 3s;
 animation-delay: 2s;
 animation-fill-mode: both;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_fill-mode3)

------

## 动画简写属性

下例使用六种动画属性：

### 实例

div {
 animation-name: example;
 animation-duration: 5s;
 animation-timing-function: linear;
 animation-delay: 2s;
 animation-iteration-count: infinite;
 animation-direction: alternate;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation4)

使用简写的 animation 属性也可以实现与上例相同的动画效果：

### 实例

div {
 animation: example 5s linear 2s infinite alternate;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation5)

------

## CSS3 习题和测验

[测验 1 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_animations1)[测验 2 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_animations2)[测验 3 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_animations3)[测验 4 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_animations4)[测验 5 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_animations5)[测验 6 »](https://www.w3schools.cn/css/exercise.asp?filename=exercise_css3_animations6)

------

## CSS3 动画属性

下表列出了 @keyframes 规则和所有 CSS 动画属性：

| 属性                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [@keyframes](https://www.w3schools.cn/cssref/css3_pr_animation-keyframes.html) | 规定动画模式。                                               |
| [animation](https://www.w3schools.cn/cssref/css3_pr_animation.html) | 设置所有动画属性的简写属性。                                 |
| [animation-delay](https://www.w3schools.cn/cssref/css3_pr_animation-delay.html) | 规定动画开始的延迟。                                         |
| [animation-direction](https://www.w3schools.cn/cssref/css3_pr_animation-direction.html) | 定动画是向前播放、向后播放还是交替播放。                     |
| [animation-duration](https://www.w3schools.cn/cssref/css3_pr_animation-duration.html) | 规定动画完成一个周期应花费的时间。                           |
| [animation-fill-mode](https://www.w3schools.cn/cssref/css3_pr_animation-fill-mode.html) | 规定元素在不播放动画时的样式（在开始前、结束后，或两者同时）。 |
| [animation-iteration-count](https://www.w3schools.cn/cssref/css3_pr_animation-iteration-count.html) | 规定动画应播放的次数。                                       |
| [animation-name](https://www.w3schools.cn/cssref/css3_pr_animation-name.html) | 规定 @keyframes 动画的名称。                                 |
| [animation-play-state](https://www.w3schools.cn/cssref/css3_pr_animation-play-state.html) | 规定动画是运行还是暂停。                                     |
| [animation-timing-function](https://www.w3schools.cn/cssref/css3_pr_animation-timing-function.html) | 规定动画的速度曲线。                                         |



[❮ 上一节](https://www.w3schools.cn/css/css3_transitions.html)[下一节 ❯](https://www.w3schools.cn/css/css_tooltip.html)

# CSS 提示框

[❮ 上一节](https://www.w3schools.cn/css/css3_animations.html)[下一节 ❯](https://www.w3schools.cn/css/css3_images.html)

------

通过 CSS 创建提示框（Tooltip）。

------

## 演示：提示框

当用户将鼠标指针移到元素上时，工具提示通常用于提供关于某内容的额外信息：

Top

Right

Bottom

Left



------

## 基础的工具提示

创建一个鼠标移到元素上时显示的工具提示：

### 实例

<style>/* 工具提示容器 */.tooltip {  position: relative;  display: inline-block;  border-bottom: 1px dotted black; /* 如果你想要悬停文本下的点 */}/* 工具提示文本 */.tooltip .tooltiptext {  visibility: hidden;  width: 120px;  background-color: black;  color: #fff;  text-align: center;  padding: 5px 0;  border-radius: 6px;   /* 定位工具提示文本 - 请参见下面的示例！ */  position: absolute;  z-index: 1;}/* 当您将鼠标悬停在工具提示容器上时显示工具提示文本 */.tooltip:hover .tooltiptext {  visibility: visible;}</style><div class="tooltip">Hover over me  <span class="tooltiptext">Tooltip text</span></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip)

### 实例解析

#### HTML：

使用容器元素（例如 <div>）并向其添加 "tooltip" 类。当用户将鼠标悬停在此 <div> 上时，会显示工具提示文本。

工具提示文本位于 class="tooltiptext" 的嵌入式元素（如 <span>）中。

#### CSS：

tooltip 类使用 position:relative，用于放置工具提示文本（position:absolute）。注意：有关如何放置工具提示，请参见下面的例子。

tooltiptext 类保存实际的工具提示文本。默认情况下它是隐藏的，并会在鼠标悬停时可见（请参阅下文）。我们还为其添加了一些基本样式：120 像素的宽度、黑色背景、白色文本、文本居中以及 5px 的上下内边距（padding）。

CSS border-radius 属性用于向工具提示文本添加圆角。

当用户将鼠标移到 class="tooltip" 的 <div> 上时，:hover 选择器用于显示工具提示文本。

------

------

## 定位工具提示

在本例中，工具提示位于"可悬停"文本（<div>）的右侧（left:105%）。另外请注意，top:-5px 用于将其放置在其容器元素的中间。我们使用数字 5 是因为工具提示文本的上下内边距均为 5px。如果增加其内边距，还请您同时增加 top 属性的值，以确保它停留在中间。如果要将工具提示放在左侧，也同样适用。

### Right Tooltip

.tooltip .tooltiptext {
 top: -5px;
 left: 105%;
}

结果:

Hover over me

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_right)

### 左侧工具提示

.tooltip .tooltiptext {
 top: -5px;
 right: 105%;
}

结果:

Hover over me

 [亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_left)

如果您希望工具提示位于上方或下方，请看下面的例子。请注意，我们使用了负 60 像素的左外边距属性（margin-left）。这是为了把工具提示与可悬停文本进行居中对齐。该值是工具提示宽度的一半（120/2 = 60）。

### 顶部工具提示

.tooltip .tooltiptext {
 width: 120px;
 bottom: 100%;
 left: 50%;
 margin-left: -60px; /* 使用宽度的一半 (120/2 = 60)，使工具提示居中 */
}

结果:

Hover over me

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_top)

### 底部工具提示

.tooltip .tooltiptext {
 width: 120px;
 top: 100%;
 left: 50%;
 margin-left: -60px; /* 使用宽度的一半 (120/2 = 60)，使工具提示居中 */
}

结果:

Hover over me

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_bottom)

------

## 工具提示箭头

如需创建在工具提示的指定侧面显示的箭头，请在工具提示后添加"空的"内容，并使用伪元素类 ::after 和 content 属性。箭头本身是使用边框创建的。这会使工具提示看起来像气泡。

本例演示如何在工具提示的底部添加箭头：

### 底部箭头

.tooltip .tooltiptext::after {
 content: " ";
 position: absolute;
 top: 100%; /* 在工具提示的底部 */
 left: 50%;
 margin-left: -5px;
 border-width: 5px;
 border-style: solid;
 border-color: black transparent transparent transparent;
}

结果:

Hover over me

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_arrow_bottom)

### 实例解析

将箭头定位在工具提示内：top: 100% 将箭头放置在工具提示的底部。left: 50% 将使箭头居中。

**注释:** `border-width` 属性指定箭头的大小。如果您更改此设置，也请将 `margin-left` 值更改为相同值。这将使箭头居中。

border-color 用于将内容转换为箭头。我们将上边框设置为黑色，其余设置为透明。如果所有面都是黑色，则最终将得到一个黑色的方形框。

本例演示了如何在工具提示的顶部添加箭头。请注意，这次我们设置了下边框的颜色：

### 顶部箭头

.tooltip .tooltiptext::after {
 content: " ";
 position: absolute;
 bottom: 100%; /* 在工具提示的顶部 */
 left: 50%;
 margin-left: -5px;
 border-width: 5px;
 border-style: solid;
 border-color: transparent transparent black transparent;
}

结果:

Hover over me

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_arrow_top)

本例演示如何在工具提示的左侧添加箭头：

### 左侧箭头

.tooltip .tooltiptext::after {
 content: " ";
 position: absolute;
 top: 50%;
 right: 100%; /* 在工具提示的左侧 */
 margin-top: -5px;
 border-width: 5px;
 border-style: solid;
 border-color: transparent black transparent transparent;
}

结果:

Hover over me

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_arrow_left)

本例演示如何在工具提示的右侧添加箭头：

### 右侧箭头

.tooltip .tooltiptext::after {
 content: " ";
 position: absolute;
 top: 50%;
 left: 100%; /* 在工具提示的右侧 */
 margin-top: -5px;
 border-width: 5px;
 border-style: solid;
 border-color: transparent transparent transparent black;
}

结果:

Hover over me

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_arrow_right)

------

## 淡入的工具提示（动画）

如果希望在即将显示的工具提示文本中淡入淡出，可以将 CSS transition 属性与 opacity 属性一同使用，并在指定的秒数（例子中是 1 秒）内从完全不可见变为 100％ 可见：

### 实例

.tooltip .tooltiptext {
 opacity: 0;
 transition: opacity 1s;
}

.tooltip:hover .tooltiptext {
 opacity: 1;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_transition)



# CSS3 样式图像

[❮ 上一节](https://www.w3schools.cn/css/css_tooltip.html)[下一节 ❯](https://www.w3schools.cn/css/css3_object-fit.html)

------

学习如何使用 CSS 设置图像样式。

------

## 圆角图像

使用 border-radius 属性创建圆形图像：

![Paris](https://www.w3schools.cn/css/paris.jpg)

### 实例

圆角图像:

img {
 border-radius: 8px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_round)

![Paris](https://www.w3schools.cn/css/paris.jpg)

### 实例

圆形图像：

img {
 border-radius: 50%;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_circle)

------

## 缩略图图像

使用 border 属性创建缩略图。

缩略图:

![Paris](https://www.w3schools.cn/css/paris.jpg)

### 实例

img {
 border: 1px solid #ddd;
 border-radius: 4px;
 padding: 5px;
 width: 150px;
}

<img src="paris.jpg" alt="Paris">

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_thumbnail)

作为链接的缩略图：

[![img](https://www.w3schools.cn/css/paris.jpg)](https://www.w3schools.cn/css/paris.jpg)

### 实例

img {
 border: 1px solid #ddd;
 border-radius: 4px;
 padding: 5px;
 width: 150px;
}

img:hover {
 box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5);
}

<a href="paris.jpg">
 <img src="paris.jpg" alt="Paris">
</a>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_thumbnail_link)

------

------

## 响应式图像

响应式图像会自动调整以适合屏幕尺寸。

![Cinque Terre](https://www.w3schools.cn/css/img_5terre_wide.jpg)

如果您希望根据需要缩小图像，但需要杜绝放大到大于原始尺寸，请添加如下代码：

### 实例

img {
 max-width: 100%;
 height: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_responsive)

**提示:** 在我们的 [CSS RWD 教程](https://www.w3schools.cn/css/css_rwd_intro.html) 中学习关于响应式 Web 设计的更多知识。

------

## 居中图像

如需使图像居中，请将左右外边距设置为 auto 并将其设置为块元素：

![Paris](https://www.w3schools.cn/css/paris.jpg)

### 实例

img {
 display: block;
 margin-left: auto;
 margin-right: auto;
 width: 50%;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_center)

------

## 宝丽来图片 / 卡片

![Cinque Terre](https://www.w3schools.cn/css/img_5terre.jpg)

Cinque Terre

![Norway](https://www.w3schools.cn/css/lights600x400.jpg)

Northern Lights

### 实例

div.polaroid {
 width: 80%;
 background-color: white;
 box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

img {width: 100%}

div.container {
 text-align: center;
 padding: 10px 20px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_card)

------

## 透明图像

opacity 属性的取值范围为 0.0 - 1.0。值越低，越透明：

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

## 图像文本

如何在图像中定位文本：

### 实例

![Cingue Terre](https://www.w3schools.cn/css/img_5terre_wide.jpg)

左下

左上

右上

右下

居中

在线实例:

[左上角 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_top_left) [右上 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_top_right) [左下角 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_bottom_left) [右下 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_bottom_right) [居中 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_center2)

------

## 图像滤镜

CSS filter 属性把视觉效果（如模糊和饱和度）添加到元素。

**注释:** Internet Explorer 或 Edge 12 不支持 filter 属性。

### 实例

把所有图像的颜色更改为黑白（100％ 灰色）：

img {
 filter: grayscale(100%);
}

<iframe src="https://www.w3schools.cn/css/trycss_ex_images_filters.htm" style="box-sizing: border-box; width: 837.984px; border: none; height: 600px;"></iframe>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_filters)

**提示:** 请访问我们的 [CSS 滤镜参考手册](https://www.w3schools.cn/cssref/css3_pr_filter.html)，了解有关 CSS 滤镜的更多信息。

------

## 图像悬停叠加

创建鼠标悬停时的叠加效果：

### 实例

淡入文本：

![Avatar](https://w3schools.cn/w3css/img_avatar3.png)

Hello World

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_css_image_overlay_fade)

### 实例

淡入框：

![Avatar](https://w3schools.cn/w3css/img_avatar3.png)

John

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_css_image_overlay_opacity)

### 实例

滑入（上）：

![Avatar](https://w3schools.cn/w3css/img_avatar3.png)

Hello World

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_css_image_overlay_slidetop)

### 实例

滑入（下）：

![Avatar](https://w3schools.cn/w3css/img_avatar3.png)

Hello World

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_css_image_overlay_slidebottom)

### 实例

滑入（左）：

![Avatar](https://w3schools.cn/w3css/img_avatar3.png)

Hello World

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_css_image_overlay_slideleft)

### 实例

滑入（右）：

![Avatar](https://w3schools.cn/w3css/img_avatar3.png)

Hello World

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_css_image_overlay_slideright)

------

## 翻转图像

请把鼠标移到图像上：

![Paris](https://www.w3schools.cn/css/paris.jpg)

------

### 实例

img:hover {
 transform: scaleX(-1);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_flip)

------

## 响应式图库

我们可以使用 CSS 创建自适应的图片库。

本例使用媒体查询来重新排列不同屏幕尺寸的图像。请调整浏览器窗口的大小以查看效果：

[![Cinque Terre](https://www.w3schools.cn/css/img_5terre.jpg)](https://www.w3schools.cn/css/img_5terre.jpg)

Add a description of the image here

[![Forest](https://www.w3schools.cn/css/img_forest.jpg)](https://www.w3schools.cn/css/img_forest.jpg)

Add a description of the image here

[![Northern Lights](https://www.w3schools.cn/css/img_lights.jpg)](https://www.w3schools.cn/css/img_lights.jpg)

Add a description of the image here

[![Mountains](https://www.w3schools.cn/css/img_mountains.jpg)](https://www.w3schools.cn/css/img_mountains.jpg)

Add a description of the image here

### 实例

.responsive {
 padding: 0 6px;
 float: left;
 width: 24.99999%;
}

@media only screen and (max-width: 700px){
 .responsive {
  width: 49.99999%;
  margin: 6px 0;
 }
}

@media only screen and (max-width: 500px){
 .responsive {
  width: 100%;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_gallery_responsive)

**提示:** 请在我们的 [CSS RWD 教程](https://www.w3schools.cn/css/css_rwd_intro.html) 中学习有关响应式 Web 设计的更多知识。

------

## 图像模态（Image Modal）

这是一个演示 CSS 和 JavaScript 如何协同工作的例子。

首先，请使用 CSS 创建模态窗口（对话框），并默认将其隐藏。

然后，当用户单击图像时，使用 JavaScript 显示模态窗口并在模态内部显示图像：

![Northern Lights, Norway](https://www.w3schools.cn/css/img_lights.jpg)

### 实例

// 获取模态
var modal = document.getElementById('myModal');

// 获取图像并将其插入模式中 - 使用它的“alt” 文字作为标题
var img = document.getElementById('myImg');
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
 modal.style.display = "block";
 modalImg.src = this.src;
 captionText.innerHTML = this.alt;
}

// 获取关闭 modal 的 <span> 元素
var span = document.getElementsByClassName("close")[0];

// 当用户点击 <span>(x) 时，关闭 modal
span.onclick = function() {
 modal.style.display = "none";
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_modal_js)



[❮ 上一节](https://www.w3schools.cn/css/css_tooltip.html)[下一节 ❯](https://www.w3schools.cn/css/css3_object-fit.html)



# CSS3 object-fit 属性

[❮ 上一节](https://www.w3schools.cn/css/css3_images.html)[下一节 ❯](https://www.w3schools.cn/css/css3_buttons.html)

------

CSS object-fit 属性用于规定应如何调整 <img> 或 <video> 的大小来适应其容器。

------

## 浏览器支持

表中的数字表示支持该属性的第一个浏览器版本。

| 属性       |      |      |      |      |      |
| :--------- | ---- | ---- | ---- | ---- | ---- |
| object-fit | 31.0 | 16.0 | 36.0 | 7.1  | 19.0 |

------

## CSS3 object-fit 属性

CSS object-fit 属性用于指定应如何调整 <img> 或 <video> 的大小以适合其容器。

这个属性告诉内容以不同的方式填充容器。比如"保留长宽比"或者"展开并占用尽可能多的空间"。

请看下面来自上海鲜花港的郁金香图片，它是 400x300 像素：

![Paris](https://www.w3schools.cn/css/paris.jpg)

但是，如果我们把上面的图像设置为 200x400 像素，则它会看起来像这样：

![Paris](https://www.w3schools.cn/css/paris.jpg)

### 实例

img {
 width: 200px;
 height: 400px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_object-fit_without)

我们看到图像被压缩以适合 200x400 像素的容器，并且原始宽高比被破坏了。

如果我们使用 object-fit: cover;，它会剪切图像的侧面，保留长宽比，并填充空间，如下所示：

![Paris](https://www.w3schools.cn/css/paris.jpg)

### 实例

img {
 width: 200px;
 height: 400px;
 object-fit: cover;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_object-fit)

------

------

## 另一个实例

在这里，我们有两幅图像，我们希望它们填充浏览器窗口的 50％ 的宽度和 100％ 的高度。

在下面的例子中，我们不使用 object-fit，因此，当我们调整浏览器窗口的大小时，图像的长宽比将被破坏：

### 实例

![Norway](https://www.w3schools.cn/css/rock600x400.jpg)![Paris](https://www.w3schools.cn/css/paris.jpg)



[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_object-fit2_without)

在下一个例子中，我们使用 object-fit: cover;，因此，当我们调整浏览器窗口的大小时，将保留图像的长宽比：

### 实例

![Norway](https://www.w3schools.cn/css/rock600x400.jpg)![Paris](https://www.w3schools.cn/css/paris.jpg)



[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_object-fit2)

------

## CSS3 object-fit 属性的所有值

object-fit 属性可接受如下值：

- fill - 默认值。调整替换后的内容大小，以填充元素的内容框。如有必要，将拉伸或挤压物体以适应该对象。
- contain - 缩放替换后的内容以保持其纵横比，同时将其放入元素的内容框。
- cover - 调整替换内容的大小，以在填充元素的整个内容框时保持其长宽比。该对象将被裁剪以适应。
- none - 不对替换的内容调整大小。
- scale-down - 调整内容大小就像没有指定内容或包含内容一样（将导致较小的具体对象尺寸）

下面的例子演示了 object-fit 属性的所有可能值：

### 实例

.fill {object-fit: fill;}
.contain {object-fit: contain;}
.cover {object-fit: cover;}
.scale-down {object-fit: scale-down;}
.none {object-fit: none;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_object-fit_all)

# CSS3 按钮

[❮ 上一节](https://www.w3schools.cn/css/css3_object-fit.html)[下一节 ❯](https://www.w3schools.cn/css/css3_pagination.html)

------

学习如何使用 CSS 设置按钮样式。

------

## 基本按钮样式

默认按钮 “CSS ”按钮

### 实例

.button {
 background-color: #4CAF50; /* Green */
 border: none;
 color: white;
 padding: 15px 32px;
 text-align: center;
 text-decoration: none;
 display: inline-block;
 font-size: 16px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_basic)

------

## 按钮颜色

绿 蓝 红 灰色 黑

请使用 background-color 属性更改按钮的背景色：

### 实例

.button1 {background-color: #4CAF50;} /* Green */
.button2 {background-color: #008CBA;} /* Blue */
.button3 {background-color: #f44336;} /* Red */
.button4 {background-color: #e7e7e7; color: black;} /* Gray */
.button5 {background-color: #555555;} /* Black */

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_color)

------

------

## 按钮尺寸

10像素 12像素 16像素 20像素 24像素

请使用 font-size 属性更改按钮的字体大小：

### 实例

.button1 {font-size: 10px;}
.button2 {font-size: 12px;}
.button3 {font-size: 16px;}
.button4 {font-size: 20px;}
.button5 {font-size: 24px;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_font)

请使用 padding 属性更改按钮的内边距：

10像素 24像素 12像素 28像素 14像素 40像素 32像素 16像素 16像素

### 实例

.button1 {padding: 10px 24px;}
.button2 {padding: 12px 28px;}
.button3 {padding: 14px 40px;}
.button4 {padding: 32px 16px;}
.button5 {padding: 16px;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_padding)

------

## 圆角按钮

2像素 4像素 8像素 12像素 50%

请使用 border-radius 属性为按钮添加圆角：

### 实例

.button1 {border-radius: 2px;}
.button2 {border-radius: 4px;}
.button3 {border-radius: 8px;}
.button4 {border-radius: 12px;}
.button5 {border-radius: 50%;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_round)

------

## 彩色的按钮边框

绿 蓝 红 灰色 黑

请使用 border 属性为按钮添加彩色边框：

### 实例

.button1 {
 background-color: white;
 color: black;
 border: 2px solid #4CAF50; /* Green */
}
...

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_border)

------

## 可悬停按钮

绿 蓝 红 灰色 黑
绿 蓝 红 灰色 黑

当鼠标移动到按钮上方时，使用 ：hover 选择器可更改按钮的样式。

**提示**： 请使用 transition-duration 属性来确定“悬停”效果的速度：

### 实例

.button {
 transition-duration: 0.4s;
}

.button:hover {
 background-color: #4CAF50; /* Green */
 color: white;
}
...

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_hover)

------

## 阴影按钮

阴影按钮 悬停时的阴影

请使用 box-shadow 属性为按钮添加阴影：

### 实例

.button1 {
 box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}

.button2:hover {
 box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_shadow)

------

## 禁用的按钮

“正常”按钮 禁用按钮

请使用 opacity 属性为按钮添加透明度（创建“禁用”外观）。

**提示：** 您还可以添加带有 “not-allowed” 值的 cursor 属性，当您将鼠标悬停在按钮上时，该属性会显示 “no parking sign”（禁停标志）：

### 实例

.disabled {
 opacity: 0.6;
 cursor: not-allowed;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_disabled)

------

## 按钮宽度

250像素
50% 100%

默认情况下，按钮的大小取决于其文本内容（与内容的宽度一样）。请使用 width 属性来更改按钮的宽度：

### 实例

.button1 {width: 250px;}
.button2 {width: 50%;}
.button3 {width: 100%;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_width)

------

## 按钮分组

按钮按钮按钮按钮


删除外边距并向每个按钮添加 float：left，来创建按钮组：

### 实例

.button {
 float: left;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_group)

------

## 带边框的按钮组

按钮按钮按钮按钮


使用 border 属性来创建带边框的按钮组：

### 实例

.button {
 float: left;
 border: 1px solid green;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_group_border)

------

## 垂直按钮组

按钮按钮按钮按钮


使用 display：block 取代 float：left 将按钮上下分组，而不是并排：

### 实例

.button {
 display: block;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_group_vertical)

------

## 图像上的按钮

![雪](https://www.w3schools.cn/css/img_lights.jpg)按钮

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_image)

------

## 动画按钮

### 实例

在鼠标悬停时添加箭头：

悬停

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_animate1)

### 实例

添加点击时的“pressed”效果：

点击

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_animate3)

### 实例

鼠标悬停时淡入：

淡入

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_fade)

### 实例

添加点击时的“ripple”效果：

点击

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_animate2)



[❮ 上一节](https://www.w3schools.cn/css/css3_object-fit.html)[下一节 ❯](https://www.w3schools.cn/css/css3_pagination.html)

# CSS3 分页实例

[❮ 上一节](https://www.w3schools.cn/css/css3_buttons.html)[下一节 ❯](https://www.w3schools.cn/css/css3_multiple_columns.html)

------

学习如何使用 CSS 创建响应式分页。

------

## 简单的分页

如果网站上有很多页面，那么您可能希望在每张页面上添加某种分页功能：

- [«](javascript:void(0))
- [1](javascript:void(0))
- [2](javascript:void(0))
- [3](javascript:void(0))
- [4](javascript:void(0))
- [5](javascript:void(0))
- [6](javascript:void(0))
- [»](javascript:void(0))

- [❮  ](javascript:void(0))
- [ ❯](javascript:void(0))

### 实例

.pagination {
 display: inline-block;
}

.pagination a {
 color: black;
 float: left;
 padding: 8px 16px;
 text-decoration: none;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination)

------

## 活动的可悬停分页

- [«](https://www.w3schools.cn/css/css3_pagination.html#)
- [1](https://www.w3schools.cn/css/css3_pagination.html#)
- [2](https://www.w3schools.cn/css/css3_pagination.html#)
- [3](https://www.w3schools.cn/css/css3_pagination.html#)
- [4](https://www.w3schools.cn/css/css3_pagination.html#)
- [5](https://www.w3schools.cn/css/css3_pagination.html#)
- [6](https://www.w3schools.cn/css/css3_pagination.html#)
- [7](https://www.w3schools.cn/css/css3_pagination.html#)
- [»](https://www.w3schools.cn/css/css3_pagination.html#)



用 .active 类突出显示当前页面，并在鼠标移到它们上方时使用 :hover 选择器更改每个页面链接的颜色：

### 实例

.pagination a.active {
 background-color: #4CAF50;
 color: white;
}

.pagination a:hover:not(.active) {background-color: #ddd;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_active)

### 圆角的活动可悬停分页

- [«](https://www.w3schools.cn/css/css3_pagination.html#)
- [1](https://www.w3schools.cn/css/css3_pagination.html#)
- [2](https://www.w3schools.cn/css/css3_pagination.html#)
- [3](https://www.w3schools.cn/css/css3_pagination.html#)
- [4](https://www.w3schools.cn/css/css3_pagination.html#)
- [5](https://www.w3schools.cn/css/css3_pagination.html#)
- [6](https://www.w3schools.cn/css/css3_pagination.html#)
- [7](https://www.w3schools.cn/css/css3_pagination.html#)
- [»](https://www.w3schools.cn/css/css3_pagination.html#)



如果您需要圆角的 "active" 和 "hover" 按钮，请添加 border-radius 属性：

### 实例

.pagination a {
 border-radius: 5px;
}

.pagination a.active {
 border-radius: 5px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_active_round)

### 可悬停的过渡效果

- [«](https://www.w3schools.cn/css/css3_pagination.html#)
- [1](https://www.w3schools.cn/css/css3_pagination.html#)
- [2](https://www.w3schools.cn/css/css3_pagination.html#)
- [3](https://www.w3schools.cn/css/css3_pagination.html#)
- [4](https://www.w3schools.cn/css/css3_pagination.html#)
- [5](https://www.w3schools.cn/css/css3_pagination.html#)
- [6](https://www.w3schools.cn/css/css3_pagination.html#)
- [7](https://www.w3schools.cn/css/css3_pagination.html#)
- [»](https://www.w3schools.cn/css/css3_pagination.html#)



请将 transition 属性添加到页面链接，创建鼠标悬停时的过渡效果：

### 实例

.pagination a {
 transition: background-color .3s;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_transition)

------

------

## 带边框的分页

- [«](https://www.w3schools.cn/css/css3_pagination.html#)
- [1](https://www.w3schools.cn/css/css3_pagination.html#)
- [2](https://www.w3schools.cn/css/css3_pagination.html#)
- [3](https://www.w3schools.cn/css/css3_pagination.html#)
- [4](https://www.w3schools.cn/css/css3_pagination.html#)
- [5](https://www.w3schools.cn/css/css3_pagination.html#)
- [6](https://www.w3schools.cn/css/css3_pagination.html#)
- [7](https://www.w3schools.cn/css/css3_pagination.html#)
- [»](https://www.w3schools.cn/css/css3_pagination.html#)



请使用 border 属性为分页添加边框：

### 实例

.pagination a {
 border: 1px solid #ddd; /* Gray */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_border)

### 圆角边框

**提示:** 在分页的第一个和最后一个链接中添加圆角边框：

- [«](https://www.w3schools.cn/css/css3_pagination.html#)
- [1](https://www.w3schools.cn/css/css3_pagination.html#)
- [2](https://www.w3schools.cn/css/css3_pagination.html#)
- [3](https://www.w3schools.cn/css/css3_pagination.html#)
- [4](https://www.w3schools.cn/css/css3_pagination.html#)
- [5](https://www.w3schools.cn/css/css3_pagination.html#)
- [6](https://www.w3schools.cn/css/css3_pagination.html#)
- [7](https://www.w3schools.cn/css/css3_pagination.html#)
- [»](https://www.w3schools.cn/css/css3_pagination.html#)



### 实例

.pagination a:first-child {
 border-top-left-radius: 5px;
 border-bottom-left-radius: 5px;
}

.pagination a:last-child {
 border-top-right-radius: 5px;
 border-bottom-right-radius: 5px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_border_round)

### 链接之间的空间

**提示:** 如果不想组合页面链接，请添加 margin 属性：

- [«](https://www.w3schools.cn/css/css3_pagination.html#)
- [1](https://www.w3schools.cn/css/css3_pagination.html#)
- [2](https://www.w3schools.cn/css/css3_pagination.html#)
- [3](https://www.w3schools.cn/css/css3_pagination.html#)
- [4](https://www.w3schools.cn/css/css3_pagination.html#)
- [5](https://www.w3schools.cn/css/css3_pagination.html#)
- [6](https://www.w3schools.cn/css/css3_pagination.html#)
- [7](https://www.w3schools.cn/css/css3_pagination.html#)
- [»](https://www.w3schools.cn/css/css3_pagination.html#)



### 实例

.pagination a {
 margin: 0 4px; /* 0 代表顶部和底部。 随意改变它 */
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_margin)

------

## 分页尺寸

- [«](https://www.w3schools.cn/css/css3_pagination.html#)
- [1](https://www.w3schools.cn/css/css3_pagination.html#)
- [2](https://www.w3schools.cn/css/css3_pagination.html#)
- [3](https://www.w3schools.cn/css/css3_pagination.html#)
- [4](https://www.w3schools.cn/css/css3_pagination.html#)
- [5](https://www.w3schools.cn/css/css3_pagination.html#)
- [6](https://www.w3schools.cn/css/css3_pagination.html#)
- [7](https://www.w3schools.cn/css/css3_pagination.html#)
- [»](https://www.w3schools.cn/css/css3_pagination.html#)



请使用 font-size 属性更改分页的大小：

### 实例

.pagination a {
 font-size: 22px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_size)

------

## 居中的分页

- [«](https://www.w3schools.cn/css/css3_pagination.html#)
- [1](https://www.w3schools.cn/css/css3_pagination.html#)
- [2](https://www.w3schools.cn/css/css3_pagination.html#)
- [3](https://www.w3schools.cn/css/css3_pagination.html#)
- [4](https://www.w3schools.cn/css/css3_pagination.html#)
- [5](https://www.w3schools.cn/css/css3_pagination.html#)
- [6](https://www.w3schools.cn/css/css3_pagination.html#)
- [7](https://www.w3schools.cn/css/css3_pagination.html#)
- [»](https://www.w3schools.cn/css/css3_pagination.html#)

如需居中分页，请使用设置了 text-align:center 的容器元素（如 <div>）包围它：

### 实例

.center {
 text-align: center;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_center)

------

## 更多实例

### 实例



[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_nav)

------

## 面包屑

- [Home](javascript:void(0))
-  

- [Pictures](javascript:void(0))
-  

- [Summer 15](javascript:void(0))
-  

- Italy

分页的另一种形式是所谓的"面包屑"（breadcrumbs）：

### 实例

ul.breadcrumb {
 padding: 8px 16px;
 list-style: none;
 background-color: #eee;
}

ul.breadcrumb li {display: inline;}

ul.breadcrumb li+li:before {
 padding: 8px;
 color: black;
 content: "/\00a0";
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_breadcrumbs)



# CSS3 多列

[❮ 上一节](https://www.w3schools.cn/css/css3_pagination.html)[下一节 ❯](https://www.w3schools.cn/css/css3_user_interface.html)

------

## CSS3 多列布局

CSS 多列布局允许我们轻松定义多列文本 - 就像报纸那样：

### Daily Ping

Lorem ipsum
dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum.

------

## CSS3 多列属性

在本章中，您将学到以下多列属性：

- `column-count`
- `column-gap`
- `column-rule-style`
- `column-rule-width`
- `column-rule-color`
- `column-rule`
- `column-span`
- `column-width`

------

## 浏览器支持

表中的数字表示支持该属性的第一个浏览器版本。

| 属性              |      |      |      |      |      |
| :---------------- | ---- | ---- | ---- | ---- | ---- |
| column-count      | 50.0 | 10.0 | 52.0 | 9.0  | 37.0 |
| column-gap        | 50.0 | 10.0 | 52.0 | 9.0  | 37.0 |
| column-rule       | 50.0 | 10.0 | 52.0 | 9.0  | 37.0 |
| column-rule-color | 50.0 | 10.0 | 52.0 | 9.0  | 37.0 |
| column-rule-style | 50.0 | 10.0 | 52.0 | 9.0  | 37.0 |
| column-rule-width | 50.0 | 10.0 | 52.0 | 9.0  | 37.0 |
| column-span       | 50.0 | 10.0 | 71.0 | 9.0  | 37.0 |
| column-width      | 50.0 | 10.0 | 52.0 | 9.0  | 37.0 |

------

------

## CSS3 创建多列

column-count 属性规定元素应被划分的列数。

下面的例子将 <div> 元素中的文本分为 3 列：

### 实例

div {
 column-count: 3;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-count)

------

## CSS3 指定列之间的间隙

column-gap 属性规定列之间的间隔。

下面的例子指定列之间的间距为 40 像素：

### 实例

div {
 column-gap: 40px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-gap)

------

## CSS3 列规则

column-rule-style 属性规定列之间的规则样式：

### 实例

div {
 column-rule-style: solid;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-rule-style)

column-rule-width 属性规定列之间的规则宽度：

### 实例

div {
 column-rule-width: 1px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-rule-width)

column-rule-color 属性规定列之间的规则的颜色：

### 实例

div {
 column-rule-color: lightblue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-rule-color)

`column-rule` 属性是用于设置上面所有 column-rule-* 属性的简写属性。

下例设置了列之间的规则的宽度、样式和颜色：

### 实例

div {
 column-rule: 1px solid lightblue;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-rule)

------

## 指定元素应该横跨多少列

column-span 属性规定元素应跨越多少列。

下例规定了<h2> 元素应跨所有列：

### 实例

h2 {
 column-span: all;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-span)

------

## 指定列宽度

column-width 属性为列指定建议的最佳宽度。

下例规定了列的建议最佳宽度应为 100px：

### 实例

div {
 column-width: 100px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-width)

------

## CSS3 多列属性

下表列出了所有的多列属性：

| 属性                                                         | 描述                                               |
| :----------------------------------------------------------- | :------------------------------------------------- |
| [column-count](https://www.w3schools.cn/cssref/css3_pr_column-count.html) | 规定元素应划分的列数。                             |
| [column-fill](https://www.w3schools.cn/cssref/css3_pr_column-fill.html) | 规定如何填充列。                                   |
| [column-gap](https://www.w3schools.cn/cssref/css3_pr_column-gap.html) | 指定列之间的间隙。                                 |
| [column-rule](https://www.w3schools.cn/cssref/css3_pr_column-rule.html) | 用于设置所有 column-rule-* 属性的简写属性。        |
| [column-rule-color](https://www.w3schools.cn/cssref/css3_pr_column-rule-color.html) | 规定列之间规则的颜色。                             |
| [column-rule-style](https://www.w3schools.cn/cssref/css3_pr_column-rule-style.html) | 规定列之间的规则样式。                             |
| [column-rule-width](https://www.w3schools.cn/cssref/css3_pr_column-rule-width.html) | 规定列之间的规则宽度。                             |
| [column-span](https://www.w3schools.cn/cssref/css3_pr_column-span.html) | 规定一个元素应该跨越多少列。                       |
| [column-width](https://www.w3schools.cn/cssref/css3_pr_column-width.html) | 为列指定建议的最佳宽度。                           |
| [columns](https://www.w3schools.cn/cssref/css3_pr_columns.html) | 用于设置 column-width 和 column-count 的简写属性。 |



[❮ 上一节](https://www.w3schools.cn/css/css3_pagination.html)[下一节 ❯](https://www.w3schools.cn/css/css3_user_interface.html)



# CSS3 用户界面

[❮ 上一节](https://www.w3schools.cn/css/css3_multiple_columns.html)[下一节 ❯](https://www.w3schools.cn/css/css3_variables.html)

------

## CSS3 用户界面

在本章中，您将学到以下 CSS 用户界面属性：

- resize
- outline-offset

------

## 浏览器支持

表中的数字表示支持该属性的第一个浏览器版本。

| 属性           |      |      |      |      |      |
| :------------- | ---- | ---- | ---- | ---- | ---- |
| resize         | 4.0  | 79.0 | 5.0  | 4.0  | 15.0 |
| outline-offset | 4.0  | 15.0 | 5.0  | 4.0  | 9.5  |

------

## CSS3 调整大小

resize 属性规定元素是否应（以及如何）被用户调整大小。

这个 div 元素可由用户调整大小！

调整大小：单击并拖动此 div 元素的右下角。

注意： Internet Explorer 不支持 resize 属性。

下例只允许用户调整 <div> 元素的宽度：

### 实例

div {
 resize: horizontal;
 overflow: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_resize_width)

下例只允许用户调整 <div> 元素的高度：

### 实例

div {
 resize: vertical;
 overflow: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_resize_height)

下例允许用户能够调整 <div> 元素的高度和宽度：

### 实例

div {
 resize: both;
 overflow: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_resize)

在许多浏览器中，<textarea> 默认可调整大小。在这里，我们使用了 resize 属性来禁用这种可缩放性：

### 实例

textarea {
 resize: none;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_resize_textarea)

------

------

## CSS3 轮廓偏移

outline-offset 属性在轮廓与元素的边缘边框之间添加空间。

这个 div 在边框边缘外有 15px 的轮廓。

**注释:** 轮廓与边框不同！与边框不同，轮廓线是在元素边框之外绘制的，并且可能与其他内容重叠。同时，轮廓也不是元素尺寸的一部分：元素的总宽度和高度不受轮廓线宽度的影响。

下面的例子使用 `outline-offset` 属性添加了边框和轮廓之间的空间：

### 实例

div.ex1 {
 margin: 20px;
 border: 1px solid black;
 outline: 4px solid red;
 outline-offset: 15px;
}

div.ex2 {
 margin: 10px;
 border: 1px solid black;
 outline: 5px dashed blue;
 outline-offset: 5px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_outline-offset)

------

## CSS3 用户界面属性

下表列出了所有用户界面属性：

| 属性                                                         | 描述                                 |
| :----------------------------------------------------------- | :----------------------------------- |
| [outline-offset](https://www.w3schools.cn/cssref/css3_pr_outline-offset.html) | 在轮廓和元素的边框边缘之间添加空间。 |
| [resize](https://www.w3schools.cn/cssref/css3_pr_resize.html) | 规定元素是否可由用户调整大小。       |

[

# CSS3 变量 - var() 函数

[❮ 上一节](https://www.w3schools.cn/css/css3_user_interface.html)[下一节 ❯](https://www.w3schools.cn/css/css3_variables_overriding.html)

------

## CSS3 变量

`var()` 函数用于插入 CSS 变量的值。

CSS 变量可以访问 DOM，这意味着您可以创建具有局部或全局范围的变量，使用 JavaScript 来修改变量，以及基于媒体查询来修改变量。

使用 CSS 变量的一种好方法涉及设计的颜色。您可以将它们放在变量中，而不必一遍又一遍地复制和粘贴相同的颜色。

------

## 传统方式

以下例子显示了在样式表中定义一些颜色的传统方式（通过为每个特定元素定义要使用的颜色）：

### 实例

body {
 background-color: #1e90ff;
}

h2 {
 border-bottom: 2px solid #1e90ff;
}

.container {
 color: #1e90ff;
 background-color: #ffffff;
 padding: 15px;
}

button {
 background-color: #ffffff;
 color: #1e90ff;
 border: 1px solid #1e90ff;
 padding: 5px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_var_old)

------

## var() 函数的语法

`var()` 函数用于插入 CSS 变量的值。

`var()` 函数的语法如下：

var(**name, value**)

| 值        | 描述                                 |
| :-------- | :----------------------------------- |
| **name**  | 必需。变量名（以两条破折号开头）。   |
| **value** | 可选。回退值（在未找到变量时使用）。 |

**注释:** 变量名称必须以两个破折号（--）开头，且区分大小写！

------

------

## var() 如何工作

首先：CSS 变量可以有全局或局部作用域。

全局变量可以在整个文档中进行访问/使用，而局部变量只能在声明它的选择器内部使用。

如需创建具有全局作用域的变量，请在 :root 选择器中声明它。 `:root` 选择器匹配文档的根元素。

如需创建具有局部作用域的变量，请在将要使用它的选择器中声明它。

下面的例子与上面的例子相同，但是在这里我们使用 `var()` 函数。

首先，我们声明两个全局变量（--blue 和 --white）。然后，我们使用 `var()` 函数稍后在样式表中插入变量的值：

### 实例

:root {
 --blue: #1e90ff;
 --white: #ffffff;
}

body {
 background-color: var(--blue);
}

h2 {
 border-bottom: 2px solid var(--blue);
}

.container {
 color: var(--blue);
 background-color: var(--white);
 padding: 15px;
}

button {
 background-color: var(--white);
 color: var(--blue);
 border: 1px solid var(--blue);
 padding: 5px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_var)

使用 var() 有如下优势：

- 使代码更易于阅读（更容易理解）
- 使修改颜色值更加容易

如需将蓝色和白色改为较柔和的蓝色和白色，您只需要修改两个变量值：

### 实例

:root {
 --blue: #6495ed;
 --white: #faf0e6;
}

body {
 background-color: var(--blue);
}

h2 {
 border-bottom: 2px solid var(--blue);
}

.container {
 color: var(--blue);
 background-color: var(--white);
 padding: 15px;
}

button {
 background-color: var(--white);
 color: var(--blue);
 border: 1px solid var(--blue);
 padding: 5px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_var2)

------

## 浏览器支持

表格中的数字注明了完全支持 `var()` 函数的首个浏览器版本。

| 函数  |      |      |      |      |      |
| :---- | ---- | ---- | ---- | ---- | ---- |
| var() | 49.0 | 15.0 | 31.0 | 9.1  | 36.0 |

------

## CSS3 var() 函数

| 属性                                                   | 描述                |
| :----------------------------------------------------- | :------------------ |
| [var()](https://www.w3schools.cn/cssref/func_var.html) | 插入 CSS 变量的值。 |



[❮ 上一节](https://www.w3schools.cn/css/css3_user_interface.html)[下一节 ❯](https://www.w3schools.cn/css/css3_variables_overriding.html)



# CSS3 覆盖变量

[❮ 上一节](https://www.w3schools.cn/css/css3_variables.html)[下一节 ❯](https://www.w3schools.cn/css/css3_variables_javascript.html)

------

## 用局部变量覆盖全局变量

从上一页我们了解到，可以在整个文档中访问/使用全局变量，而局部变量只能在声明它的选择器内使用。

请看上一页中的例子：

### 实例

:root {
 --blue: #1e90ff;
 --white: #ffffff;
}

body {
 background-color: var(--blue);
}

h2 {
 border-bottom: 2px solid var(--blue);
}

.container {
 color: var(--blue);
 background-color: var(--white);
 padding: 15px;
}

button {
 background-color: var(--white);
 color: var(--blue);
 border: 1px solid var(--blue);
 padding: 5px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_var)

有时，我们希望变量仅在页面的特定部分中进行更改。

假设我们想要按钮元素使用不同的蓝色。那么，我们可以在 button 选择器内重新声明 --blue 变量。当我们在这个选择器中使用 var(--blue) 时，它将使用此处声明的局部 --blue 变量值。

我们看到局部的 --blue 变量会覆盖 button 元素的全局 --blue 变量：

### 实例

:root {
 --blue: #1e90ff;
 --white: #ffffff;
}

body {
 background-color: var(--blue);
}

h2 {
 border-bottom: 2px solid var(--blue);
}

.container {
 color: var(--blue);
 background-color: var(--white);
 padding: 15px;
}

button {
 --blue: #0000ff;
 background-color: var(--white);
 color: var(--blue);
 border: 1px solid var(--blue);
 padding: 5px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_var_override)

------

------

## 添加一个新的局部变量

如果只在一个地方使用一个变量，我们也可以声明一个新的局部变量，就像这样：

### 实例

:root {
 --blue: #1e90ff;
 --white: #ffffff;
}

body {
 background-color: var(--blue);
}

h2 {
 border-bottom: 2px solid var(--blue);
}

.container {
 color: var(--blue);
 background-color: var(--white);
 padding: 15px;
}

button {
 --button-blue: #0000ff;
 background-color: var(--white);
 color: var(--button-blue);
 border: 1px solid var(--button-blue);
 padding: 5px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_var_local)

------

## 浏览器支持

表格中的数字注明了完全支持 `var()` 函数的首个浏览器版本。

| 函数  |      |      |      |      |      |
| :---- | ---- | ---- | ---- | ---- | ---- |
| var() | 49.0 | 15.0 | 31.0 | 9.1  | 36.0 |

------

## CSS3 var() 函数

| 属性                                                   | 描述                |
| :----------------------------------------------------- | :------------------ |
| [var()](https://www.w3schools.cn/cssref/func_var.html) | 插入 CSS 变量的值。 |



# CSS3 使用 JavaScript 更改变量

[❮ 上一节](https://www.w3schools.cn/css/css3_variables_overriding.html)[下一节 ❯](https://www.w3schools.cn/css/css3_box-sizing.html)

------

## CSS3 使用 JavaScript 更改变量

CSS 变量可以访问 DOM，这意味着您可以通过 JavaScript 更改它们。

这个例子说明了如何创建脚本来显示并更改上一页中使用的示例中的 --blue 变量。此刻，如果您不熟悉 JavaScript，不要担心。您可以在我们的 [JavaScript](https://www.w3schools.cn/js/default.html) 教程中学到有关 JavaScript 的更多知识：

### 实例

<script>// 获取根元素var r = document.querySelector(':root');// 创建一个获取变量值的函数function myFunction_get() {  // 获取根的样式（属性和值）  var rs = getComputedStyle(r);  // 提醒 --blue 变量的值  alert("The value of --blue is: " + rs.getPropertyValue('--blue'));}// 创建用于设置变量值的函数function myFunction_set() {  // 将变量 --blue 的值设置为另一个值（在本例中为“lightblue”）  r.style.setProperty('--blue', 'lightblue');}</script>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_var_js)

------

## 浏览器支持

表格中的数字注明了完全支持 `var()` 函数的首个浏览器版本。

| 函数  |      |      |      |      |      |
| :---- | ---- | ---- | ---- | ---- | ---- |
| var() | 49.0 | 15.0 | 31.0 | 9.1  | 36.0 |

------

## CSS3 var() Function

| 属性                                                   | 描述                |
| :----------------------------------------------------- | :------------------ |
| [var()](https://www.w3schools.cn/cssref/func_var.html) | 插入 CSS 变量的值。 |



[❮ 上一节](https://www.w3schools.cn/css/css3_variables_overriding.html)[下一节 ❯](https://www.w3schools.cn/css/css3_box-sizing.html)

# CSS3 Box Sizing

[❮ 上一节](https://www.w3schools.cn/css/css3_variables_javascript.html)[下一节 ❯](https://www.w3schools.cn/css/css3_mediaqueries.html)

------

## CSS3 Box Sizing

CSS box-sizing 属性允许我们在元素的总宽度和高度中包括内边距（填充）和边框。

------

## 假如不指定 CSS box-sizing 属性

默认情况下，元素的宽度和高度是这样计算的：

- width + padding + border = 元素的实际宽度
- height + padding + border = 元素的实际高度

这意味着：当您设置元素的宽度/高度时，该元素通常看起来比您设置的更大（因为元素的边框和内边距已被添加到元素的指定宽度/高度中）。

下图展示了两个有相同指定宽度和高度的 <div> 元素：

这个 div 较小
（宽度为 300px，高度为 100px）。



这个 div 更大
（宽度也为 300px，高度为 100px）。



上面的两个 <div> 元素在最终结果中呈现出不同的尺寸（因为 div2 指定了内边距）：

### 实例

.div1 {
 width: 300px;
 height: 100px;
 border: 1px solid blue;
}

.div2 {
 width: 300px;
 height: 100px;
 padding: 50px;
 border: 1px solid red;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-sizing_old)

`box-sizing` 属性解决了这个问题。

------

------

## 如果使用 CSS box-sizing 属性

box-sizing 属性允许我们在元素的总宽度和高度中包括内边距和边框。

如果在元素上设置了 box-sizing: border-box;，则宽度和高度会包括内边距和边框：

现在两个 div 的大小相同！



Hooray!



该例与上例相同，两个 <div> 元素都设置了 box-sizing: border-box;：

### 实例

.div1 {
 width: 300px;
 height: 100px;
 border: 1px solid blue;
 box-sizing: border-box;
}

.div2 {
 width: 300px;
 height: 100px;
 padding: 50px;
 border: 1px solid red;
 box-sizing: border-box;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-sizing_new)

由于使用 box-sizing: border-box; 的效果如此之好，许多开发人员希望页面上的所有元素都能够以这种方式工作。

下面的代码能够确保以这种更直观的方式调整所有元素的大小。许多浏览器已经在对许多表单元素使用 box-sizing: border-box;（但并非全部 - 这就是为什么 input 和 textarea 在 width: 100%; 时看起来不同）。

将其应用于所有元素是安全且明智的：

### 实例

\* {
 box-sizing: border-box;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-sizing_all)

------

## CSS3 Box Sizing 属性

| 属性                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [box-sizing](https://www.w3schools.cn/cssref/css3_pr_box-sizing.html) | 定义元素宽度和高度的计算方式：它们是否应包含内边距（padding）和边框。 |



[❮ 上一节](https://www.w3schools.cn/css/css3_variables_javascript.html)[下一节 ❯](https://www.w3schools.cn/css/css3_mediaqueries.html)



# CSS3 媒体查询

[❮ 上一节](https://www.w3schools.cn/css/css3_box-sizing.html)[下一节 ❯](https://www.w3schools.cn/css/css3_mediaqueries_ex.html)

------

## CSS2 引入了媒体类型

CSS2 中引入了 @media 规则，它让为不同媒体类型定义不同样式规则成为可能。

例如：您可能有一组用于计算机屏幕的样式规则、一组用于打印机、一组用于手持设备，甚至还有一组用于电视，等等。

不幸的是，除了打印媒体类型之外，这些媒体类型从未得到过设备的大规模支持。

------

## CSS3 引入了媒体查询

CSS3 中的媒体查询扩展了 CSS2 媒体类型的概念：它们并不查找设备类型，而是关注设备的能力。

媒体查询可用于检查许多事情，例如：

- 视口的宽度和高度
- 设备的宽度和高度
- 方向（平板电脑/手机处于横向还是纵向模式）
- 分辨率

使用媒体查询是一种流行的技术，可以向台式机、笔记本电脑、平板电脑和手机（例如 iPhone 和 Android 手机）提供定制的样式表。

------

## 浏览器支持

表格中的数字注明了完全支持 @media 规则的首个浏览器版本。

| 属性   |      |      |      |      |      |
| :----- | ---- | ---- | ---- | ---- | ---- |
| @media | 21.0 | 9.0  | 3.5  | 4.0  | 9.0  |

------

## 媒体查询语法

媒体查询由一种媒体类型组成，并可包含一个或多个表达式，这些表达式可以解析为 true 或 false。

@media not|only *mediatype* and (*expressions*) {*
 CSS-Code;
*}

如果指定的媒体类型与正在显示文档的设备类型匹配，并且媒体查询中的所有表达式均为 true，则查询结果为 true。当媒体查询为 true 时，将应用相应的样式表或样式规则，并遵循正常的级联规则。

除非您使用 not 或 only 运算符，否则媒体类型是可选的，且隐含 all 类型。

您还可以针对不同的媒体使用不同的样式表：

<link rel="stylesheet" media="**mediatype** and|not|only (**expressions**)" href="**print.css**">

------

------

## CSS3 媒体类型

| 值     | 描述                                     |
| :----- | :--------------------------------------- |
| all    | 用于所有媒体类型设备。                   |
| print  | 用于打印机。                             |
| screen | 用于计算机屏幕、平板电脑、智能手机等等。 |
| speech | 用于大声"读出"页面的屏幕阅读器。         |

------

## 媒体查询的简单实例

使用媒体查询的一种方法是在样式表内有一个备用的 CSS 部分。

下面的例子在视口宽度为 480 像素或更宽时将背景颜色更改为浅绿色（如果视口小于 480 像素，则背景颜色会是粉色）：

### 实例

@media screen and (min-width: 480px) {
 body {
  background-color: lightgreen;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_media_queries1)

下例显示了一个菜单，如果视口的宽度为 480 像素或更宽，则该菜单会浮动到页面的左侧（如果视口小于 480 像素，则该菜单将位于内容的顶部）：

### 实例

@media screen and (min-width: 480px) {
 \#leftsidebar {width: 200px; float: left;}
 \#main {margin-left: 216px;}
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_media_queries2)

## 更多媒体查询实例

如需更多媒体查询的实例，请访问下一页：[CSS MQ 实例](https://www.w3schools.cn/css/css3_mediaqueries_ex.html)。

------

## CSS3 @media 参考手册

有关所有媒体类型和特性/表达式的完整概述，请查看我们的 [CSS 参考中的 @media 规则](https://www.w3schools.cn/cssref/css3_pr_mediaquery.html)。

# CSS3 媒体查询 - 实例

[❮ 上一节](https://www.w3schools.cn/css/css3_mediaqueries.html)[下一节 ❯](https://www.w3schools.cn/css/css3_flexbox.html)

------

## CSS3 媒体查询 - 更多实例

让我们看看使用媒体查询的更多例子。

媒体查询是一种流行的技术，用于将定制的样式表传递给不同的设备。

下面演示一个简单的例子，让我们来更改不同设备的背景色：

![img](https://www.w3schools.cn/css/mqcap.JPG)

### 实例

/* 设置 body 的背景颜色为棕褐色 */
body {
 background-color: tan;
}

/* 在 992px 或更小的屏幕上，将背景颜色设置为蓝色 */
@media screen and (max-width: 992px) {
 body {
  background-color: blue;
 }
}

/* 在 600px 或更小的屏幕上，将背景颜色设置为橄榄色 */
@media screen and (max-width: 600px) {
 body {
  background-color: olive;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_ex1)

您想知道我们为什么要精确使用 992px 和 600px 吗？它们就是我们所称的设备的"典型断点"（typical breakpoints）。您可以在我们的 [响应式 Web 设计教程](https://www.w3schools.cn/css/css_rwd_intro.html) 中学习有关典型断点的更多知识。

------

## 菜单的媒体查询

在本例中，我们使用媒体查询来创建响应式导航菜单，该菜单在不同的屏幕尺寸上会有所不同。

### 大型屏幕：

[Home](javascript:void(0))[Link 1](javascript:void(0))[Link 2](javascript:void(0))[Link 3](javascript:void(0))

### 小型屏幕：

[Home](javascript:void(0))[Link 1](javascript:void(0))[Link 2](javascript:void(0))[Link 3](javascript:void(0))

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
 color: white;
 text-align: center;
 padding: 14px 16px;
 text-decoration: none;
}

/* 在 600 像素或更小的屏幕上，使菜单链接堆叠在一起而不是彼此相邻 */
@media screen and (max-width: 600px) {
 .topnav a {
  float: none;
  width: 100%;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_navbar)

------

------

## 列的媒体查询

媒体查询的常见用法是创建弹性布局。在本例中，我们创建了一个布局，该布局在四列、两列和全宽列之间变化，具体取决于不同的屏幕尺寸：

大型屏幕:

<iframe src="https://www.w3schools.cn/css/trycss_mq_ex_ifr4.htm" style="box-sizing: inherit; border: 0px; width: 240.656px; overflow: hidden; height: 110px;"></iframe>

中等屏幕:

<iframe src="https://www.w3schools.cn/css/trycss_mq_ex_ifr2.htm" style="box-sizing: inherit; border: 0px; width: 240.656px; overflow: hidden; height: 110px;"></iframe>

小型屏幕:

<iframe src="https://www.w3schools.cn/css/trycss_mq_ex_ifr.htm" style="box-sizing: inherit; border: 0px; width: 240.656px; overflow: hidden; height: 110px;"></iframe>

### 实例

/* 创建四个彼此相邻的相等列 */
.column {
 float: left;
 width: 25%;
}

/* 在 992 像素或以下宽的屏幕上，从四列变为两列 */
@media screen and (max-width: 992px) {
 .column {
  width: 50%;
 }
}

/* 在 600px 宽或更小的屏幕上，使列堆叠在一起而不是彼此相邻 */
@media screen and (max-width: 600px) {
 .column {
  width: 100%;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_ex2)

**提示:** 更现代的创建列布局方法是使用 CSS Flexbox（请参见下面的例子）。但是，Internet Explorer 10 以及更早版本不支持它。如果需要 IE6-10 的支持，请使用浮动（如上所示）。

如需学习有关弹性框布局模块的更多知识，请学习 [CSS Flexbox](https://www.w3schools.cn/css/css3_flexbox.html) 这一章。

如需学习有关响应式 Web 设计的更多知识，请学习我们的 [响应式 Web 设计教程](https://www.w3schools.cn/css/css_rwd_intro.html)。

### 实例

/* 弹性盒容器 */
.row {
 display: flex;
 flex-wrap: wrap;
}

/* 创建四个相等的列 */
.column {
 flex: 25%;
 padding: 20px;
}

/* 在 992 像素或以下宽的屏幕上，从四列变为两列 */
@media screen and (max-width: 992px) {
 .column {
  flex: 50%;
 }
}

/* 在 600px 宽或更小的屏幕上，使列堆叠在一起而不是彼此相邻 */
@media screen and (max-width: 600px) {
 .row {
  flex-direction: column;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_flex)

------

## 用媒体查询隐藏元素

媒体查询的另一种常见用法是在不同屏幕尺寸上隐藏元素：

在小屏幕上我会隐藏。

### 实例

/* If the screen size is 600px wide or less, hide the element */
@media screen and (max-width: 600px) {
 div.example {
  display: none;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_hide)

------

## 用媒体查询改变字体

您还可以使用媒体查询来更改不同屏幕尺寸上的元素的字体大小：

# 可变的字体大小。

### 实例

/* 如果屏幕尺寸超过 600px 宽，设置 <div> 的 font-size 为 80px */
@media screen and (min-width: 600px) {
 div.example {
  font-size: 80px;
 }
}

/* 如果屏幕尺寸为 600px 或更小，则设置的 font-size 到 30 像素 */
@media screen and (max-width: 600px) {
 div.example {
  font-size: 30px;
 }
}
[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_fontsize)

------

## 弹性图片库

在此例中，我们将媒体查询与 flexbox 一起使用来创建响应式图片库：

### 实例

<iframe src="https://www.w3schools.cn/howto/tryhow_css_image_grid_responsive.htm" style="box-sizing: inherit; background: white; border: none; width: 869.984px; height: 600px;"></iframe>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_img_gallery)

------

## 弹性网站

在本例中，我们将媒体查询与 flexbox 一起使用，以创建响应式网站，其中包含弹性导航栏和弹性内容。

### 实例

<iframe src="https://www.w3schools.cn/css/trycss3_flexbox_website_ifr.htm" style="box-sizing: inherit; border: 2px solid rgb(221, 221, 221); width: 869.984px; height: 625px;"></iframe>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_website)

------

## 方向：人像 / 风景

媒体查询还可以用于根据浏览器的方向更改页面的布局。

您可以设置一组 CSS 属性，这些属性仅在浏览器窗口的宽度大于其高度时才适用，即所谓的横屏：

### 实例

如果方向处于横向模式，请使用浅蓝色背景色:

@media only screen and (orientation: landscape) {
 body {
  background-color: lightblue;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_mediaquery_orientation)

------

## 最小宽度到最大宽度

您还可以使用 `max-width 和 min-width` 属性设置最小宽度和最大宽度。

例如，当浏览器的宽度在 600 到 900 像素之间时，更改 <div> 元素的外观：

### 实例

@media screen and (max-width: 900px) and (min-width: 600px) {
 div.example {
  font-size: 50px;
  padding: 50px;
  border: 8px solid black;
  background: yellow;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_minmax)

**使用附加值：**在下面的例子中，我们使用逗号（类似 OR 运算符）将附加的媒体查询添加到已有媒体查询中：

### 实例

/* 当宽度在 600px 和 900px 之间 **OR** 超过 1100px - 改变 <div> 的外观 */
@media screen and (max-width: 900px) and (min-width: 600px), (min-width: 1100px) {
 div.example {
  font-size: 50px;
  padding: 50px;
  border: 8px solid black;
  background: yellow;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_minmax2)

## CSS3 @media 参考手册

有关所有媒体类型和特性/表达式的完整概述，请查看 [CSS 参考中的 @media 规则](https://www.w3schools.cn/cssref/css3_pr_mediaquery.html)。

**提示：** 如需学习有关响应式 Web 设计（如何针对不同的设备和屏幕）的更多知识，以及使用媒体查询断点，请阅读我们的 [响应式 Web 设计教程](https://www.w3schools.cn/css/css_rwd_intro.html)。

# CSS3 Flexbox

[❮ 上一节](https://www.w3schools.cn/css/css3_mediaqueries_ex.html)[下一节 ❯](https://www.w3schools.cn/css/css3_flexbox_container.html)

------

# 1

# 2

# 3

# 4

# 5

# 6

# 7

# 8

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex-wrap_nowrap8)

------

## CSS3 Flexbox 布局模块

在 Flexbox 布局模块（问世）之前，可用的布局模式有以下四种：

- 块（Block），用于网页中的部分（节）
- 行内（Inline），用于文本
- 表，用于二维表数据
- 定位，用于元素的明确位置

弹性框布局模块，可以更轻松地设计灵活的响应式布局结构，而无需使用浮动或定位。

------

## 浏览器支持

所有现代浏览器均支持 flexbox 属性。

|      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- |
| 29.0 | 11.0 | 22.0 | 10   | 48   |

------

## Flexbox 元素

如需开始使用 Flexbox 模型，您需要首先定义 Flex 容器。

# 1

# 2

# 3

上面的元素表示一个带有三个 flex 项目的 flex 容器（蓝色区域）。

### 实例

含有三个 flex 项目的 flex 容器：

<div class="flex-container">  <div>1</div>  <div>2</div>  <div>3</div></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox)

在接下来的章节中，您将了解更多关于 flex 容器和 flex 项目的信息。

# CSS3 Flex 容器

[❮ 上一节](https://www.w3schools.cn/css/css3_flexbox.html)[下一节 ❯](https://www.w3schools.cn/css/css3_flexbox_items.html)

------

## 父元素（容器）

# 1

# 2

# 3

通过将 display 属性设置为 flex，flex 容器将可伸缩：

### 实例

.flex-container {
 display: flex;
}



[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox)

以下是 flex 容器属性：

- [flex-direction](https://www.w3schools.cn/css/css3_flexbox_container.html#flex-direction)
- [flex-wrap](https://www.w3schools.cn/css/css3_flexbox_container.html#flex-wrap)
- [flex-flow](https://www.w3schools.cn/css/css3_flexbox_container.html#flex-flow)
- [justify-content](https://www.w3schools.cn/css/css3_flexbox_container.html#justify-content)
- [align-items](https://www.w3schools.cn/css/css3_flexbox_container.html#align-items)
- [align-content](https://www.w3schools.cn/css/css3_flexbox_container.html#align-content)

------

## flex-direction 属性

flex-direction 属性定义容器要在哪个方向上堆叠 flex 项目。

# 1

# 2

# 3

### 实例

column 值设置垂直堆叠 flex 项目（从上到下）：

.flex-container {
 display: flex;
 flex-direction: column;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex-direction_column)

### 实例

column-reverse 值垂直堆叠 flex 项目（但从下到上）：

.flex-container {
 display: flex;
 flex-direction: column-reverse;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex-direction_column-reverse)

### 实例

row 值水平堆叠 flex 项目（从左到右）：

.flex-container {
 display: flex;
 flex-direction: row;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex-direction_row)

### 实例

row-reverse 值水平堆叠 flex 项目（但从右到左）：

.flex-container {
 display: flex;
 flex-direction: row-reverse;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex-direction_row-reverse)

------

## flex-wrap 属性

flex-wrap 属性规定是否应该对 flex 项目换行。

下面的例子包含 12 个 flex 项目，以便更好地演示 flex-wrap 属性。

# 1

# 2

# 3

# 4

# 5

# 6

# 7

# 8

# 9

# 10

# 11

# 12

### 实例

wrap 值规定 flex 项目将在必要时进行换行：

.flex-container {
 display: flex;
 flex-wrap: wrap;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex-wrap_wrap)

### 实例

nowrap 值规定将不对 flex 项目换行（默认）：

.flex-container {
 display: flex;
 flex-wrap: nowrap;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex-wrap_nowrap)

### 实例

wrap-reverse 值规定如有必要，弹性项目将以相反的顺序换行：

.flex-container {
 display: flex;
 flex-wrap: wrap-reverse;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex-wrap_wrap-reverse)

------

## flex-flow 属性

flex-flow 属性是用于同时设置 ` flex-direction` 和 `flex-wrap` 属性的简写属性。

### 实例

.flex-container {
 display: flex;
 flex-flow: row wrap;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex-flow_row_wrap)

------

## justify-content 属性

justify-content 属性用于对齐 flex 项目：

# 1

# 2

# 3

### 实例

`center` 值将 flex 项目在容器的中心对齐：

.flex-container {
 display: flex;
 justify-content: center;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_justify-content_center)

### 实例

flex-start 值将 flex 项目在容器的开头对齐（默认）：

.flex-container {
 display: flex;
 justify-content: flex-start;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_justify-content_flex-start)

### 实例

flex-end 值将 flex 项目在容器的末端对齐：

.flex-container {
 display: flex;
 justify-content: flex-end;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_justify-content_flex-end)

### 实例

space-around 值显示行之前、之间和之后带有空格的 flex 项目：

.flex-container {
 display: flex;
 justify-content: space-around;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_justify-content_space-around)

### 实例

space-between 值显示行之间有空格的 flex 项目：

.flex-container {
 display: flex;
 justify-content: space-between;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_justify-content_space-between)

------

## align-items 属性

align-items 属性用于垂直对齐 flex 项目。

# 1

# 2

# 3

在这些例子中，我们使用 200 像素高的容器，以便更好地演示 align-items 属性。

### 实例

center 值将 flex 项目在容器中间对齐：

.flex-container {
 display: flex;
 height: 200px;
 align-items: center;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-items_center)

### 实例

flex-start 值将 flex 项目在容器顶部对齐：

.flex-container {
 display: flex;
 height: 200px;
 align-items: flex-start;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-items_flex-start)

### 实例

flex-end 值将弹性项目在容器底部对齐：

.flex-container {
 display: flex;
 height: 200px;
 align-items: flex-end;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-items_flex-end)

### 实例

stretch 值拉伸 flex 项目以填充容器（默认）：

.flex-container {
 display: flex;
 height: 200px;
 align-items: stretch;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-items_stretch)

### 实例

baseline 值使 flex 项目基线对齐：

.flex-container {
 display: flex;
 height: 200px;
 align-items: baseline;
}

**注释:** 该例使用不同的 font-size 来演示项目已按文本基线对齐：

# 1

###### 2

### 3

4

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-items_baseline)

------

## align-content 属性

align-content 属性用于对齐弹性线。

# 1

# 2

# 3

# 4

# 5

# 6

# 7

# 8

# 9

# 10

# 11

# 12

在这些例子中，我们使用 600 像素高的容器，并将 flex-wrap 属性设置为 wrap，以便更好地演示 `align-content` 属性。

### 实例

space-between 值显示的弹性线之间有相等的间距：

.flex-container {
 display: flex;
 height: 600px;
 flex-wrap: wrap;
 align-content: space-between;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-content_space-between)

### 实例

space-around 值显示弹性线在其之前、之间和之后带有空格：

.flex-container {
 display: flex;
 height: 600px;
 flex-wrap: wrap;
 align-content: space-around;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-content_space-around)

### 实例

stretch 值拉伸弹性线以占据剩余空间（默认）：

.flex-container {
 display: flex;
 height: 600px;
 flex-wrap: wrap;
 align-content: stretch;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-content_stretch)

### 实例

center 值在容器中间显示弹性线：

.flex-container {
 display: flex;
 height: 600px;
 flex-wrap: wrap;
 align-content: center;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-content_center)

### 实例

flex-start 值在容器开头显示弹性线：

.flex-container {
 display: flex;
 height: 600px;
 flex-wrap: wrap;
 align-content: flex-start;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-content_flex-start)

### 实例

flex-end 值在容器的末尾显示弹性线：

.flex-container {
 display: flex;
 height: 600px;
 flex-wrap: wrap;
 align-content: flex-end;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-content_flex-end)

------

## 完美的居中

在下面的例子中，我们会解决一个非常常见的样式问题：完美居中。

解决方案：将 justify-content 和 align-items 属性设置为居中，然后 flex 项目将完美居中：

### 实例

.flex-container {
 display: flex;
 height: 300px;
 **justify-content: center;
 align-items: center;
**}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_perfect_center)



[❮ 上一节](https://www.w3schools.cn/css/css3_flexbox.html)[下一节 ❯](https://www.w3schools.cn/css/css3_flexbox_items.html)

# CSS3 Flex 项目

[❮ 上一节](https://www.w3schools.cn/css/css3_flexbox_container.html)[下一节 ❯](https://www.w3schools.cn/css/css3_flexbox_responsive.html)

------

## 子元素（项目）

flex 容器的直接子元素会自动成为弹性（flex）项目。

# 1

# 2

# 3

# 4

上面的元素代表一个灰色 flex 容器内的四个蓝色 flex 项目。

### 实例

<div class="flex-container">  <div>1</div>  <div>2</div>  <div>3</div>  <div>4</div></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_item)

用于弹性项目的属性有：

- [order](https://www.w3schools.cn/css/css3_flexbox_items.html#order)
- [flex-grow](https://www.w3schools.cn/css/css3_flexbox_items.html#flex-grow)
- [flex-shrink](https://www.w3schools.cn/css/css3_flexbox_items.html#flex-shrink)
- [flex-basis](https://www.w3schools.cn/css/css3_flexbox_items.html#flex-basis)
- [flex](https://www.w3schools.cn/css/css3_flexbox_items.html#flex)
- [align-self](https://www.w3schools.cn/css/css3_flexbox_items.html#align-self)

------

## order 属性

order 属性规定 flex 项目的顺序。

# 1

# 2

# 3

# 4

代码中的首个 flex 项目不必在布局中显示为第一项。

order 值必须是数字，默认值是 0。

### 实例

order 属性可以改变 flex 项目的顺序：

<div class="flex-container">  <div style="order: 3">1</div>  <div style="order: 2">2</div>  <div style="order: 4">3</div>  <div style="order: 1">4</div></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_order_2)

------

## flex-grow 属性

flex-grow 属性规定某个 flex 项目相对于其余 flex 项目将增长多少。

# 1

# 2

# 3

该值必须是数字，默认值是 0。

### 实例

使第三个弹性项目的增长速度比其他弹性项目快八倍：

<div class="flex-container">  <div style="flex-grow: 1">1</div>  <div style="flex-grow: 1">2</div>  <div style="flex-grow: 8">3</div></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex-grow)

------

## flex-shrink 属性

flex-shrink 属性规定某个 flex 项目相对于其余 flex 项目将收缩多少。

# 1

# 2

# 3

# 4

# 5

# 6

# 7

# 8

# 9

# 10

该值必须是数字，默认值是 0。

### 实例

不要让第三个弹性项目收缩得与其他弹性项目一样多：

<div class="flex-container">  <div>1</div>  <div>2</div>  <div style="flex-shrink: 0">3</div>  <div>4</div>  <div>5</div>  <div>6</div>  <div>7</div>  <div>8</div>  <div>9</div>  <div>10</div></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex-shrink)

------

## flex-basis 属性

flex-basis 属性规定 flex 项目的初始长度。

# 1

# 2

# 3

# 4

### 实例

将第三个弹性项目的初始长度设置为 200 像素：

<div class="flex-container">  <div>1</div>  <div>2</div>  <div style="flex-basis: 200px">3</div>  <div>4</div></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex-basis)

------

## flex 属性

flex 属性是 `flex-grow`、`flex-shrink` 和 `flex-basis` 属性的简写属性。

### 实例

使第三个弹性项目不可增长（0），不可收缩（0），且初始长度为 200 像素：

<div class="flex-container">  <div>1</div>  <div>2</div>  <div style="flex: 0 0 200px">3</div>  <div>4</div></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex)

------

## align-self 属性

align-self 属性规定弹性容器内所选项目的对齐方式。

align-self 属性将覆盖容器的 `align-items` 属性所设置的默认对齐方式。

# 1

# 2

# 3

# 4

在这些例子中，我们使用 200 像素高的容器，以便更好地演示 `align-self` 属性：

### 实例

把第三个弹性项目对齐到容器的中间：

<div class="flex-container">  <div>1</div>  <div>2</div>  <div style="align-self: center">3</div>  <div>4</div></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-self_center)

### 实例

将第二个弹性项目在容器顶部对齐，将第三个弹性项目在容器底部对齐：

<div class="flex-container">  <div>1</div>  <div style="align-self: flex-start">2</div>  <div style="align-self: flex-end">3</div>  <div>4</div></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-self_flex)



[❮ 上一节](https://www.w3schools.cn/css/css3_flexbox_container.html)[下一节 ❯](https://www.w3schools.cn/css/css3_flexbox_responsive.html)

# CSS3 Flex 响应式

[❮ 上一节](https://www.w3schools.cn/css/css3_flexbox_items.html)[下一节 ❯](https://www.w3schools.cn/css/css_rwd_intro.html)

------

## 响应式 Flexbox

您从 [媒体查询](https://www.w3schools.cn/css/css3_mediaqueries.html) 一章中了解到，可以使用媒体查询为不同屏幕大小的设备创建不同的布局。

笔记本电脑和台式电脑:

1

2

3

手机和平板电脑:

1

2

3



例如，如果要为大多数屏幕尺寸创建两列布局，为小屏幕尺寸（如手机和平板电脑）创建一列布局，可以在特定断点（以下示例中为800px）将 `flex-direction` 从 `row` 更改为 `column`:

### 实例

.flex-container {
 display: flex;
 flex-direction: row;
}

/*响应式布局 - 制作一列布局而不是两列布局 */
@media (max-width: 800px) {
 .flex-container {
  flex-direction: column;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_responsive)

另一种方法是更改 flex 项的 `flex` 属性的百分比， 以便为不同的屏幕大小创建不同的布局。请注意，我们还必须在 flex 容器中包含 `flex-wrap: wrap;` ，以使本例生效:

### 实例

.flex-container {
 display: flex;
 flex-wrap: wrap;
}

.flex-item-left {
 flex: 50%;
}

.flex-item-right {
 flex: 50%;
}

/* 响应式布局 - 制作一列布局而不是两列布局 */
@media (max-width: 800px) {
 .flex-item-right, .flex-item-left {
  flex: 100%;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_responsive2)

------

## 使用 Flexbox 的响应式图库

使用 flexbox 创建响应式图像库，该图像库根据屏幕大小在四幅、两幅或全宽图像之间变化：

<iframe src="https://www.w3schools.cn/howto/tryhow_css_image_grid_responsive.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 6px solid rgb(241, 241, 241); width: 869.984px; height: 600px;"></iframe>

 [亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_image_gallery)

------

## 使用 Flexbox 的响应式网站

使用 flexbox 创建响应式网站，其中包含弹性导航栏和弹性内容：

<iframe src="https://www.w3schools.cn/css/trycss3_flexbox_website_ifr.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 6px solid rgb(238, 238, 238); width: 869.984px; height: 630px;"></iframe>

 [亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_website2)

------

## CSS3 Flexbox 属性

下表列出了与 flexbox 一起使用的 CSS 属性：

| 属性                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [display](https://www.w3schools.cn/cssref/pr_class_display.html) | 规定用于 HTML 元素的盒类型。                                 |
| [flex-direction](https://www.w3schools.cn/cssref/css3_pr_flex-direction.html) | 规定弹性容器内的弹性项目的方向。                             |
| [justify-content](https://www.w3schools.cn/cssref/css3_pr_justify-content.html) | 当弹性项目没有用到主轴上的所有可用空间时，水平对齐这些项目。 |
| [align-items](https://www.w3schools.cn/cssref/css3_pr_align-items.html) | 当弹性项目没有用到主轴上的所有可用空间时，垂直对齐这些项。   |
| [flex-wrap](https://www.w3schools.cn/cssref/css3_pr_flex-wrap.html) | 规定弹性项目是否应该换行，若一条 flex 线上没有足够的空间容纳它们。 |
| [align-content](https://www.w3schools.cn/cssref/css3_pr_align-content.html) | 修改 flex-wrap 属性的行为。与 align-items 相似，但它不对齐弹性项目，而是对齐 flex 线。 |
| [flex-flow](https://www.w3schools.cn/cssref/css3_pr_flex-flow.html) | flex-direction 和 flex-wrap 的简写属性。                     |
| [order](https://www.w3schools.cn/cssref/css3_pr_order.html)  | 规定弹性项目相对于同一容器内其余弹性项目的顺序。             |
| [align-self](https://www.w3schools.cn/cssref/css3_pr_align-self.html) | 用于弹性项目。覆盖容器的 align-items 属性。                  |
| [flex](https://www.w3schools.cn/cssref/css3_pr_flex.html)    | flex-grow、flex-shrink 以及 flex-basis 属性的简写属性。      |



[❮ 上一节](https://www.w3schools.cn/css/css3_flexbox_items.html)[下一节 ❯](https://www.w3schools.cn/css/css_rwd_intro.html)

# 响应式网页设计 - 简介

[❮ 上一节](https://www.w3schools.cn/css/css3_flexbox_responsive.html)[下一节 ❯](https://www.w3schools.cn/css/css_rwd_viewport.html)

------

## 什么是响应式网页设计？

响应式 web 设计会让您的网页在所有设备上看起来都不错。

响应式 web 设计仅使用 HTML 和 CSS。

响应式 web 设计并不是程序或 JavaScript。

------

## 为所有用户获得最佳体验的设计

可以使用许多不同的设备来查看网页：台式机、平板电脑和手机。无论使用哪种设备，您的网页都应该看起来美观且易用。

网页不应舍弃信息来适合较小的设备，而应使其内容适合任何设备：



![img](https://www.w3schools.cn/css/rwd_desktop.png)
桌面电脑

![img](https://www.w3schools.cn/css/rwd_tablet.png)
平板电脑

![img](https://www.w3schools.cn/css/rwd_phone.png)
手机

如果您使用 CSS 和 HTML 调整大小、隐藏、缩小、放大或移动内容，以使其在任何屏幕上看起来都很好，则称为响应式 Web 设计。

如果您不理解下面的例子，请不要担心，我们将在下一章中一步一步地分解代码：

<iframe src="https://www.w3schools.cn/css/tryresponsive_col-s.htm" style="box-sizing: inherit; color: rgb(0, 0, 0); font-family: Verdana, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 6px solid rgb(238, 238, 238); width: 869.984px; height: 585px; margin-bottom: -6px;"></iframe>



[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_col-s)

------

# 响应式网页设计 - 视口

[❮ 上一节](https://www.w3schools.cn/css/css_rwd_intro.html)[下一节 ❯](https://www.w3schools.cn/css/css_rwd_grid.html)

------

## 什么是视口？

视口（viewport）是用户在网页上的可见区域。

视口随设备而异，在移动电话上会比在计算机屏幕上更小。

在平板电脑和手机之前，网页仅设计为用于计算机屏幕，并且网页拥有静态设计和固定大小是很常见的。

然后，当我们开始使用平板电脑和手机上网时，固定大小的网页太大了，无法适应视口。为了解决这个问题，这些设备上的浏览器会按比例缩小整个网页以适合屏幕大小。

这并不是完美的！勉强是一种快速的修正。

------

## 设置视口

HTML5 引入了一种方法，使 Web 设计者可以通过 <meta> 标签来控制视口。

您应该在所有网页中包含以下 <meta> 视口元素：

<meta name="viewport" content="width=device-width, initial-scale=1.0">

它为浏览器提供了关于如何控制页面尺寸和缩放比例的指令。

width=device-width 部分将页面的宽度设置为跟随设备的屏幕宽度（视设备而定）。

当浏览器首次加载页面时，initial-scale=1.0 部分设置初始缩放级别。

下面分别是不带视口 meta 标签的网页、以及带视口 meta 标签的网页的例子：

**提示:** 如果您使用手机或平板电脑浏览这张页面，则可以单击下面的两个链接以查看不同之处。



[![img](https://www.w3schools.cn/css/img_viewport1.png)

**没有 viewport meta 标签**](https://www.w3schools.cn/css/example_withoutviewport.htm)



[![img](https://www.w3schools.cn/css/img_viewport2.png)

**使用 viewport meta 标签**](https://www.w3schools.cn/css/example_withviewport.htm)



------

## 把内容调整到视口的大小

用户习惯在台式机和移动设备上垂直滚动网站，而不是水平滚动！

因此，如果迫使用户水平滚动或缩小以查看整个网页，则会导致不佳的用户体验。

还需要遵循的一些附加规则：

**1. 请勿使用较大的固定宽度元素** - 例如，如果图像的宽度大于视口的宽度，则可能导致视口水平滚动。请务必调整此内容以适合视口的宽度。

**2. 不要让内容依赖于特定的视口宽度来呈现好的效果** - 由于以 CSS 像素计的屏幕尺寸和宽度在设备之间变化很大，因此内容不应依赖于特定的视口宽度来呈现良好的效果。

**3. 使用 CSS 媒体查询为小屏幕和大屏幕应用不同的样式** - 为页面元素设置较大的 CSS 绝对宽度将导致该元素对于较小设备上的视口太宽。而是应该考虑使用相对宽度值，例如 width: 100%。另外，要小心使用较大的绝对定位值，这可能会导致元素滑落到小型设备的视口之外。

# 响应式网页设计 - 网格

[❮ 上一节](https://www.w3schools.cn/css/css_rwd_viewport.html)[下一节 ❯](https://www.w3schools.cn/css/css_rwd_mediaqueries.html)

------

## 什么是网格视图？

许多网页都基于网格视图（grid-view），这意味着页面被分割为几列：



在设计网页时，使用网格视图非常有帮助。这样可以更轻松地在页面上放置元素。



响应式网格视图通常有 12 列，总宽度为 100％，并且在调整浏览器窗口大小时会收缩和伸展。

[Example: Responsive Grid View](https://www.w3schools.cn/css/tryresponsive_grid.htm)

------

------

## 构建响应式网格视图

让我们开始构建响应式网格视图。

首先，确保所有 HTML 元素的 box-sizing 属性设置为 border-box。这样可以确保元素的总宽度和高度中包括内边距（填充）和边框。

请在 CSS 中添加如下代码：

\* {
 box-sizing: border-box;
}

请在我们的 [CSS Box Sizing](https://www.w3schools.cn/css/css3_box-sizing.html) 一章中阅读有关 box-sizing 属性的更多内容。

下面的例子展示了一张简单的响应式网页，其中包含两列：

25%

75%

### 实例

.menu {
 width: 25%;
 float: left;
}
.main {
 width: 75%;
 float: left;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_webpage)

若网页只包含两列，则上面的例子还不错。

但是，我们希望使用拥有 12 列的响应式网格视图，来更好地控制网页。

首先，我们必须计算一列的百分比：100% / 12 列 = 8.33%。

然后，我们为 12 列中的每一列创建一个类，即 class="col-" 和一个数字，该数字定义此节应跨越的列数：

### CSS:

.col-1 {width: 8.33%;}
.col-2 {width: 16.66%;}
.col-3 {width: 25%;}
.col-4 {width: 33.33%;}
.col-5 {width: 41.66%;}
.col-6 {width: 50%;}
.col-7 {width: 58.33%;}
.col-8 {width: 66.66%;}
.col-9 {width: 75%;}
.col-10 {width: 83.33%;}
.col-11 {width: 91.66%;}
.col-12 {width: 100%;}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_cols)

所有这些列应向左浮动，并带有 15px 的内边距：

### CSS:

[class*="col-"] {
 float: left;
 padding: 15px;
 border: 1px solid red;
}

每行都应被包围在 <div> 中。行内的列数总应总计为 12：

### HTML:

<div class="row">  <div class="col-3">...</div> <!-- 25% -->  <div class="col-9">...</div> <!-- 75% --></div>

行内的所有列全部都向左浮动，因此会从页面流中移出，并将放置其他元素，就好像这些列不存在一样。为了防止这种情况，我们会添加清除流的样式：

### CSS:

.row::after {
 content: "";
 clear: both;
 display: table;
}

我们还想添加一些样式和颜色，使其看起来更美观：

### 实例

html {
 font-family: "Lucida Sans", sans-serif;
}

.header {
 background-color: #9933cc;
 color: #ffffff;
 padding: 15px;
}

.menu ul {
 list-style-type: none;
 margin: 0;
 padding: 0;
}

.menu li {
 padding: 8px;
 margin-bottom: 7px;
 background-color :#33b5e5;
 color: #ffffff;
 box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}

.menu li:hover {
 background-color: #0099cc;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_styles)

**请注意:** 当您将浏览器窗口调整为非常小的宽度时，例中的网页看起来并不理想。在下一章中，您将学习如何解决这个问题。

# 响应式网页设计 - 媒体查询

[❮ 上一节](https://www.w3schools.cn/css/css_rwd_grid.html)[下一节 ❯](https://www.w3schools.cn/css/css_rwd_images.html)

------

## 什么是媒体查询？

媒体查询是 CSS3 中引入的一种 CSS 技术。

仅在满足特定条件时，它才会使用 @media 规则来引用 CSS 属性块。

### 实例

如果浏览器窗口是 600px 或更小，则背景颜色为浅蓝色：

@media only screen and (max-width: 600px) {
 body {
  background-color: lightblue;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_mediaquery)

------

## 添加断点

在本教程中稍早前，我们制作了一张包含行和列的网页，但是这张响应式网页在小屏幕上看起来效果并不好。

媒体查询可以帮助您。我们可以添加一个断点，其中设计的某些部分在断点的每一侧会表现得有所不同。

![img](https://www.w3schools.cn/css/rwd_desktop.png)
桌面电脑

![img](https://www.w3schools.cn/css/rwd_phone.png)
手机



使用媒体查询在 768px 处添加断点：

### 实例

当屏幕（浏览器窗口）小于 768px 时，每列的宽度应为 100％：

/* For desktop: */
.col-1 {width: 8.33%;}
.col-2 {width: 16.66%;}
.col-3 {width: 25%;}
.col-4 {width: 33.33%;}
.col-5 {width: 41.66%;}
.col-6 {width: 50%;}
.col-7 {width: 58.33%;}
.col-8 {width: 66.66%;}
.col-9 {width: 75%;}
.col-10 {width: 83.33%;}
.col-11 {width: 91.66%;}
.col-12 {width: 100%;}

@media only screen and (max-width: 768px) {
 /* For mobile phones: */
 [class*="col-"] {
  width: 100%;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_breakpoints)

------

------

## 始终移动优先设计

移动优先（Mobile First）指的是在对台式机或任何其他设备进行设计之前，优先针对移动设备进行设计（这将使页面在较小的设备上显示得更快）。

这意味着我们必须在 CSS 中做一些改进。

当宽度小于 768px 时，我们应该修改设计，而不是更改宽度。我们就这样进行了"移动优先"的设计：

### 实例

/* 手机: */
[class*="col-"] {
 width: 100%;
}

@media only screen and (min-width: 768px) {
 /* 台式机: */
 .col-1 {width: 8.33%;}
 .col-2 {width: 16.66%;}
 .col-3 {width: 25%;}
 .col-4 {width: 33.33%;}
 .col-5 {width: 41.66%;}
 .col-6 {width: 50%;}
 .col-7 {width: 58.33%;}
 .col-8 {width: 66.66%;}
 .col-9 {width: 75%;}
 .col-10 {width: 83.33%;}
 .col-11 {width: 91.66%;}
 .col-12 {width: 100%;}
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_mobilefirst)

------

## 另一个断点

您可以添加任意多个断点。

我们还会在平板电脑和手机之间插入一个断点。

![img](https://www.w3schools.cn/css/rwd_desktop.png)
桌面电脑

![img](https://www.w3schools.cn/css/rwd_tablet.png)
平板电脑

![img](https://www.w3schools.cn/css/rwd_phone.png)
手机



为此，我们添加了一个媒体查询（在 600 像素），并为大于 600 像素（但小于 768 像素）的设备添加了一组新类：

### 实例

请注意，两组类几乎相同，唯一的区别是名称(`col-` 和 `col-s-`):

/* 手机: */
[class*="col-"] {
 width: 100%;
}

@media only screen and (min-width: 600px) {
 /* 平板电脑: */
 .col-s-1 {width: 8.33%;}
 .col-s-2 {width: 16.66%;}
 .col-s-3 {width: 25%;}
 .col-s-4 {width: 33.33%;}
 .col-s-5 {width: 41.66%;}
 .col-s-6 {width: 50%;}
 .col-s-7 {width: 58.33%;}
 .col-s-8 {width: 66.66%;}
 .col-s-9 {width: 75%;}
 .col-s-10 {width: 83.33%;}
 .col-s-11 {width: 91.66%;}
 .col-s-12 {width: 100%;}
}

@media only screen and (min-width: 768px) {
 /* 台式机: */
 .col-1 {width: 8.33%;}
 .col-2 {width: 16.66%;}
 .col-3 {width: 25%;}
 .col-4 {width: 33.33%;}
 .col-5 {width: 41.66%;}
 .col-6 {width: 50%;}
 .col-7 {width: 58.33%;}
 .col-8 {width: 66.66%;}
 .col-9 {width: 75%;}
 .col-10 {width: 83.33%;}
 .col-11 {width: 91.66%;}
 .col-12 {width: 100%;}
}

有两组相同的类似乎很奇怪，但是它给了我们机会用 HTML 来决定在每个断点处的列会发生什么：

### HTML 实例

#### 对于台式机：

第一和第三部分都会跨越 3 列。中间部分将跨越 6 列。

#### 对于平板电脑：

第一部分将跨越 3 列，第二部分将跨越 9 列，第三部分将显示在前两部分的下方，并将跨越 12 列：

<div class="row">  <div class="col-3 col-s-3">...</div>  <div class="col-6 col-s-9">...</div>  <div class="col-3 col-s-12">...</div></div>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_col-s)

------

## 典型的设备断点

高度和宽度不同的屏幕和设备不计其数，因此很难为每个设备创建精确的断点。为了简单起见，您可以瞄准这五组：

### 实例

/* 超小设备（手机，600px 及以下）*/
@media only screen and (max-width: 600px) {...}

/* 小型设备（纵向平板电脑和大型手机，600 像素及以上）*/
@media only screen and (min-width: 600px) {...}

/* 中型设备（横向平板电脑，768 像素及以上）*/
@media only screen and (min-width: 768px) {...}

/* 大型设备（笔记本电脑/台式机，992 像素及以上）*/
@media only screen and (min-width: 992px) {...}

/* 超大型设备（大型笔记本电脑和台式机，1200 像素及以上）*/
@media only screen and (min-width: 1200px) {...}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_mediaquery_breakpoints)

------

## 方向：人像 / 风景

媒体查询还可用于根据浏览器的方向来更改页面的布局。

您可以设置一组 CSS 属性，这些属性仅在浏览器窗口的宽度大于其高度时才适用，即所谓的"横屏"方向：

### 实例

如果方向为横向模式（landscape mode），则网页背景为浅蓝色：

@media only screen and (orientation: landscape) {
 body {
  background-color: lightblue;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_mediaquery_orientation)

------

## 用媒体查询隐藏元素

媒体查询的另一种常见用法是在不同屏幕尺寸上对元素进行隐藏：

我将隐藏在小屏幕上。

### 实例

/* 如果屏幕尺寸为 600px 或以下，隐藏元素 */
@media only screen and (max-width: 600px) {
 div.example {
  display: none;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_hide)

------

## 用媒体查询修改字体

您还可以使用媒体查询来更改不同屏幕尺寸上的元素的字体大小：

# 可变字体大小。

### 实例

/* 如果屏幕尺寸为 601px 或更大，将 <div> 的 font-size 设置为 80px */
@media only screen and (min-width: 601px) {
 div.example {
  font-size: 80px;
 }
}

/* 如果屏幕尺寸为 600px 或更小，设置 <div> 的 font-size 为 30px */
@media only screen and (max-width: 600px) {
 div.example {
  font-size: 30px;
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_fontsize)

------

## CSS @media 参考手册

有关所有媒体类型和特性/表达式的完整概述，请在 [CSS 参考手册中参阅 @media 规则](https://www.w3schools.cn/cssref/css3_pr_mediaquery.html)。



[❮ 上一节](https://www.w3schools.cn/css/css_rwd_grid.html)[下一节 ❯](https://www.w3schools.cn/css/css_rwd_images.html)

# 响应式网页设计 - 图像

[❮ 上一节](https://www.w3schools.cn/css/css_rwd_mediaqueries.html)[下一节 ❯](https://www.w3schools.cn/css/css_rwd_videos.html)

------

![img](https://www.w3schools.cn/css/img_chania.jpg)

Resize the browser window to see how the image scales to fit the page.

------

## 使用 width 属性

如果 width 属性设置为百分比，且高度设置为 "auto"，则图像将进行响应来放大或缩小：

### 实例

img {
 width: 100%;
 height: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_image2)

请注意，在上面的例子中，图像可以放大到大于其原始大小。在多数情况下，更好的解决方案是改为使用 max-width 属性。

------

## 使用 max-width 属性

如果将 max-width 属性设置为 100％，则图像将按需缩小，但绝不会放大到大于其原始大小：

### 实例

img {
 max-width: 100%;
 height: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_image)

------

## 向实例网页添加图像

### 实例

img {
 width: 100%;
 height: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_image3)

------

------

## 背景图像

背景图像也可以响应调整大小和缩放比例。

这是我们展示的三种不同方法：

\1. 如果将 background-size 属性设置为 "contain"，则背景图像将缩放，并尝试匹配内容区域。不过图像将保持其长宽比（图像宽度与高度之间的比例关系）：



这是 CSS 代码：

### 实例

div {
 width: 100%;
 height: 400px;
 background-image: url('img_flowers.jpg');
 background-repeat: no-repeat;
 background-size: contain;
 border: 1px solid red;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_image_background1)

------

\2. 如果将 background-size 属性设置为 "100% 100%"，则背景图像将拉伸以覆盖整个内容区域：



这是 CSS 代码：

### 实例

div {
 width: 100%;
 height: 400px;
 background-image: url('img_flowers.jpg');
 background-size: 100% 100%;
 border: 1px solid red;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_image_background2)

------

\3. 如果 background-size 属性设置为 "cover"，则背景图像将缩放以覆盖整个内容区域。请注意，"cover" 值保持长宽比，且可能会裁剪背景图像的某部分：



这是 CSS 代码：

### 实例

div {
 width: 100%;
 height: 400px;
 background-image: url('img_flowers.jpg');
 background-size: cover;
 border: 1px solid red;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_image_background3)

------

## 为不同设备准备不同图像

大幅的图像在大型计算机屏幕上可以完美显示，但在小型设备上就没用了。为什么在不得不缩小图像时又加载大图像呢？为了减少负载或出于任何其他原因，您可以使用媒体查询在不同的设备上显示不同的图像。

这是一幅大图像和一幅小图像，会在不同的设备上显示：

![img](https://www.w3schools.cn/css/img_flowers.jpg)

![img](https://www.w3schools.cn/css/img_smallflower.jpg)

### 实例

/* 对于小于 400px 的宽度：*/
body {
 background-image: url('img_smallflower.jpg');
}

/* 宽度为 400 像素及更大：*/
@media only screen and (min-width: 400px) {
 body {
  background-image: url('img_flowers.jpg');
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_image_mediaq)

您可以使用媒体查询 min-device-width 而不是 min-width 来检查设备宽度，而不是浏览器宽度。然后，当您调整浏览器窗口的大小时，图像将不会变化：

### 实例

/* 对于小于 400px 的设备：*/
body {
 background-image: url('img_smallflower.jpg');
}

/* 对于 400 像素及更大的设备：*/
@media only screen and (min-device-width: 400px) {
 body {
  background-image: url('img_flowers.jpg');
 }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_image_mediaq2)

------

## HTML5 <picture> 元素

HTML5 引入了 <picture> 元素，该元素使您可以定义多幅图像。

### 浏览器支持

| 元素      |      |      |      |      |      |
| :-------- | ---- | ---- | ---- | ---- | ---- |
| <picture> | 13   | 38.0 | 38.0 | 9.1  | 25.0 |



<picture> 元素的作用类似于 <video> 和 <audio> 元素。我们设置了不同的来源，而匹配优先权的第一个来源是正在使用的来源：

### 实例

<picture>
 <source srcset="img_smallflower.jpg" media="(max-width: 400px)">
 <source srcset="img_flowers.jpg">
 <img src="img_flowers.jpg" alt="Flowers">
</picture>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_image_picture)

srcset 属性是必需的，它定义图像的来源。

media 属性是可选的，它接受可在 [CSS @media 规则](https://www.w3schools.cn/cssref/css3_pr_mediaquery.html) 中找到的媒体查询。

您还应该为不支持 <picture> 元素的浏览器定义 <img> 元素。

# 响应式网页设计 - 视频

[❮ 上一节](https://www.w3schools.cn/css/css_rwd_images.html)[下一节 ❯](https://www.w3schools.cn/css/css_rwd_frameworks.html)

------

## 使用 width 属性

如果 width 属性设置为100％，则视频播放器将响应并放大和缩小：

### 实例

video {
 width: 100%;
 height: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_video2)

请注意，在上面的例子中，视频播放器可以放大到大于其原始尺寸。在许多情况下，更好的解决方案是改用 `max-width` 属性。

------

## 使用 max-width 属性

如果将 max-width 属性设置为 100％，则视频播放器将按比例缩小，但绝不会放大到大于其原始尺寸：

### 实例

video {
 max-width: 100%;
 height: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_video)

------

## 在实例网页中添加视频

我们希望在实例网页中添加视频。视频将被调整大小以便始终占据所有可用空间：

### 实例

video {
 width: 100%;
 height: auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_video3)

# 响应式网页设计 - 框架

[❮ 上一节](https://www.w3schools.cn/css/css_rwd_videos.html)[下一节 ❯](https://www.w3schools.cn/css/css_rwd_templates.html)

------

现在有许多的 CSS 框架提供响应性设计。

它们是免费的，易于使用。

------

## 启动

当前流行的框架是 Bootstrap，它使用 HTML、CSS 和 jQuery 来创建响应式网页。

### 实例

<!DOCTYPE html><html lang="en"><head><title>Bootstrap Example</title><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.5.1/jquery.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script></head><body><div class="container">  <div class="jumbotron">    <h1>我的第一个 Bootstrap 页面</h1>  </div>  <div class="row">    <div class="col-sm-4">      ...    </div>    <div class="col-sm-4">      ...    </div>    <div class="col-sm-4">    ...    </div>  </div></div></body></html>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_bootstrap)

要了解有关 Bootstrap 的更多信息，请转到我们的 [Bootstrap 教程](https://www.w3schools.cn/bootstrap/bootstrap_ver.html)。



[❮ 上一节](https://www.w3schools.cn/css/css_rwd_videos.html)[下一节 ❯](https://www.w3schools.cn/css/css_rwd_templates.html)

# CSS 响应式网页设计 - 模板

[❮ 上一节](https://www.w3schools.cn/css/css_rwd_frameworks.html)[下一节 ❯](https://www.w3schools.cn/css/css_grid.html)

------

## W3.CSS 网站模板

我们已经用 [W3.CSS 框架](https://www.w3schools.cn/w3css/default.html)创建了一些响应式模板。

您可以在所有项目中自由修改、保存、共享和使用它们。

------

### Band Template

[![Start Page Template](https://www.w3schools.cn/css/img_temp_band.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_band.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_band.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_band&stacked=h)

### Art Template

[![Streert Art Template](https://w3schools.cn/w3css/img_temp_art.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_streetart.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_streetart.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_streetart&stacked=h)

### Architect Template

[![Architect Template](https://w3schools.cn/w3css/img_temp_architect.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_architect.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_architect.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_architect&stacked=h)

### Coming Soon Template

[![Coming Soon Template](https://w3schools.cn/w3css/img_temp_comingsoon.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_coming_soon.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_coming_soon.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_coming_soon&stacked=h)

------

------

### Blog Template

[![Blog Template](https://www.w3schools.cn/css/img_temp_blog.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_blog.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_blog.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_blog&stacked=h)

### Food Blog Template

[![Food Blog Template](https://w3schools.cn/w3css/img_temp_food_blog.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_food_blog.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_food_blog.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_food_blog&stacked=h)

### Fashion Blog Template

[![Fashion Blog Template](https://w3schools.cn/w3css/img_temp_fashion_blog.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_fashion_blog.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_fashion_blog.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_fashion_blog&stacked=h)

### Gourmet Catering Template

[![Gourmet Catering Template](https://w3schools.cn/w3css/img_temp_gourmet_catering.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_gourmet_catering.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_gourmet_catering.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_gourmet_catering&stacked=h)

### CV Template

[![CV Template](https://w3schools.cn/w3css/img_temp_cv.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_cv.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_cv.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_cv&stacked=h)

### Wedding Invitation Template

[![Wedding Invitation Template](https://w3schools.cn/w3css/img_temp_wedding.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_wedding.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_wedding.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_wedding&stacked=h)

### Photo Template

[![Photo Template](https://www.w3schools.cn/css/img_temp_photo.JPG)](https://www.w3schools.cn/w3css/tryw3css_templates_photo.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_photo.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_photo&stacked=h)

### Black & White Photo Template

[![Black and White Photo Template](https://w3schools.cn/w3css/img_temp_photo2.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_photo2.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_photo2.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_photo2&stacked=h)

### Photo III Template

[![Photo Template](https://w3schools.cn/w3css/img_temp_photo3.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_photo3.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_photo3.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_photo3&stacked=h)

### Nature Portfolio Template

[![Nature Portfolio Template](https://w3schools.cn/w3css/img_temp_portfolio.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_portfolio.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_portfolio.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_portfolio&stacked=h)

### People Portfolio Template

[![People Portfolio Template](https://w3schools.cn/w3css/img_temp_portfolio2.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_portfolio2.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_portfolio2.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_portfolio2&stacked=h)

### People Portfolio II Template

[![People Portfolio II Template](https://w3schools.cn/w3css/img_temp_portfolio3.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_portfolio3.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_portfolio3.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_portfolio3&stacked=h)

### Dark Portfolio Template

[![Dark Icon Bar Template](https://w3schools.cn/w3css/img_temp_dark_icon.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_dark_portfolio.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_dark_portfolio.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_dark_portfolio&stacked=h)

### Black & White Portfolio Template

[![Black and White Portfolio Template](https://w3schools.cn/w3css/img_temp_bw_port.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_bw_portfolio.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_bw_portfolio.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_bw_portfolio&stacked=h)

### Parallax Template

[![Portfolio Template](https://www.w3schools.cn/css/img_temp_parallax.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_parallax.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_parallax.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_parallax&stacked=h)

### Clothing Store Template

[![Clothing/Fashion StoreTemplate](https://w3schools.cn/w3css/img_temp_clothing_store.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_clothing_store.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_clothing_store.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_clothing_store&stacked=h)

### Interior Design Template

[![Interior Design Template](https://w3schools.cn/w3css/img_temp_interior_design.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_interior_design.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_interior_design.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_interior_design&stacked=h)

### Cafe Template

[![Cafe Template](https://w3schools.cn/w3css/img_temp_cafe.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_cafe.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_cafe.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_cafe)

### Pizza Restaurant Template

[![Pizza Restaurant Template](https://w3schools.cn/w3css/img_temp_pizza.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_pizza.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_pizza.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_pizza)

### Modal Restaurant Template

[![Modal Restaurant Template](https://w3schools.cn/w3css/img_temp_modal_restaurant.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_restaurant_modal.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_restaurant_modal.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_restaurant_modal)

### Start Page Template

[![Start Page Template](https://www.w3schools.cn/css/img_temp_startpage.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_start_page.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_start_page.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_start_page&stacked=h)

### Startup Template

[![Startup Template](https://w3schools.cn/w3css/img_temp_startup.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_startup.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_startup.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_startup)

### App Launch Template

[![App Launch Template](https://w3schools.cn/w3css/img_temp_app_launch.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_app_launch.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_app_launch.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_app_launch&stacked=h)

### Marketing Template

[![Marketing Template](https://www.w3schools.cn/css/img_temp_marketing.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_marketing.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_marketing.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_marketing&stacked=h)

### Marketing / Website Template

[![Web Page Template](https://www.w3schools.cn/css/img_temp_website.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_website.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_website.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_website&stacked=h)

### Web Page Template

[![Web Page Template](https://www.w3schools.cn/css/img_temp_webpage.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_webpage.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_webpage.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_webpage&stacked=h)

### Social Media Template

[![Social Media Template](https://www.w3schools.cn/css/img_temp_social.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_social.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_social.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_social&stacked=h)

### Analytics Template

[![Analytics Template](https://www.w3schools.cn/css/img_temp_analytics.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_analytics.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_analytics.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_analytics&stacked=h)

### Apartment Rental Template

[![Apartment Rental Template](https://w3schools.cn/w3css/img_temp_apartment_rental.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_apartment_rental.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_apartment_rental.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_apartment_rental&stacked=h)

### Hotel Template

[![Hotel Template](https://w3schools.cn/w3css/img_temp_hotel.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_hotel.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_hotel.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_hotel&stacked=h)

### Travel Template

[![Travel Template](https://w3schools.cn/w3css/img_temp_travel2.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_travel2.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_travel2.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_travel2&stacked=h)

### Travel Agency Template

[![Start Page Template](https://www.w3schools.cn/css/img_temp_travel.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_travel.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_travel.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_travel&stacked=h)

### House Design Template

[![Start Page Template](https://www.w3schools.cn/css/img_temp_design.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_design.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_design.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_design&stacked=h)

### Screen 50/50 Template

[![Start Page Template](https://www.w3schools.cn/css/img_temp_fifty.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_fifty.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_fifty.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_fifty&stacked=h)

### Mail Template

[![Start Page Template](https://w3schools.cn/w3css/img_temp_mail.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_mail.htm)

[演示](https://www.w3schools.cn/w3css/tryw3css_templates_mail.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_mail&stacked=h)

### Kitchen Sink/Demo Template

[![Demo Template](https://www.w3schools.cn/css/img_temp_demosite.jpg)](https://www.w3schools.cn/w3css/tryw3css_templates_black.htm)



[Black](https://www.w3schools.cn/w3css/tryw3css_templates_black.htm)

[Red](https://www.w3schools.cn/w3css/tryw3css_templates_red.htm)

[Teal](https://www.w3schools.cn/w3css/tryw3css_templates_teal.htm)

[亲自试一试](https://www.w3schools.cn/w3css/tryit.asp?filename=tryw3css_templates_black&stacked=h)

# CSS 网格布局

[❮ 上一节](https://www.w3schools.cn/css/css_rwd_templates.html)[下一节 ❯](https://www.w3schools.cn/css/css_grid_container.html)

------

### Header

### Menu

### Main

### Right

### Footer

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_layout_named)

------

## 网格布局

CSS 网格布局模块（CSS Grid Layout Module）提供了带有行和列的基于网格的布局系统，它使网页设计变得更加容易，而无需使用浮动和定位。

------

## 浏览器支持

所有现代浏览器均支持网格属性。

|      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- |
| 57.0 | 16.0 | 52.0 | 10   | 44   |

------

## 网格元素

网格布局由一个父元素以及一个或多个子元素组成。

### 实例

<div class="grid-container">  <div class="grid-item">1</div>  <div class="grid-item">2</div>  <div class="grid-item">3</div>  <div class="grid-item">4</div>  <div class="grid-item">5</div>  <div class="grid-item">6</div>  <div class="grid-item">7</div>  <div class="grid-item">8</div>  <div class="grid-item">9</div></div>

# 1

# 2

# 3

# 4

# 5

# 6

# 7

# 8

# 9

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid)

------

## Display 属性

当 HTML 元素的 display 属性设置为 `grid` 或 `inline-grid` 时，它就会成为网格容器。

### 实例

.grid-container {
 display: grid;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_display_grid)

### 实例

.grid-container {
 display: inline-grid;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_display_inline-grid)

**网格容器的所有直接子元素将自动成为网格项目。**

------

## 网格列（Grid Columns）

网格项的垂直线被称为列。

![img](https://www.w3schools.cn/css/grid_columns.png)

------

## 网隔行（Grid Rows）

网格项的水平线被称为行。

![img](https://www.w3schools.cn/css/grid_rows.png)

------

## 网格间隙（Grid Gaps）

每列/行之间的间隔称为间隙。

![img](https://www.w3schools.cn/css/grid_gaps.png)

您可以通过使用以下属性之一来调整间隙大小：

```
grid-column-gap`
`grid-row-gap`
`grid-gap
```

### 实例

grid-column-gap 属性设置列之间的间隙：

.grid-container {
 display: grid;
 **grid-column-gap: 50px;**
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-column-gap)

### 实例

grid-row-gap 属性设置行之间的间隙：

.grid-container {
 display: grid;
 **grid-row-gap: 50px;
**}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-row-gap)

### 实例

grid-gap 属性是 grid-row-gap 和 grid-column-gap 属性的简写属性：

.grid-container {
 display: grid;
 **grid-gap: 50px 100px;
**}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-gap2)

### 实例

grid-gap 属性还可用于将行间隙和列间隙设置为一个值：

.grid-container {
 display: grid;
 **grid-gap: 50px;
**}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-gap)

------

## 网格行（Grid Lines）

列之间的线称为列线（column lines）。

行之间的线称为行线（row lines）。

![img](https://www.w3schools.cn/css/grid_lines.png)

当把网格项目放在网格容器中时，请引用行号：

### 实例

把网格项目放在列线 1，并在列线 3 结束它：

.item1 {
 grid-column-start: 1;
 grid-column-end: 3;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_lines)

### 实例

把网格项目放在行线 1，并在行线 3 结束它：

.item1 {
 grid-row-start: 1;
 grid-row-end: 3;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_lines2)

# CSS 网格容器

[❮ 上一节](https://www.w3schools.cn/css/css_grid.html)[下一节 ❯](https://www.w3schools.cn/css/css_grid_item.html)

------

# 1

# 2

# 3

# 4

# 5

# 6

# 7

# 8

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_container)

------

## 网格容器

如需使 HTML 元素充当网格容器，您必须把 display 属性设置为 grid 或 inline-grid。

网格容器由放置在列和行内的网格项目组成。

------

## grid-template-columns 属性

grid-template-columns 属性定义网格布局中的列数，并可定义每列的宽度。

该值是以空格分隔的列表，其中每个值定义相应列的长度。

如果您希望网格布局包含 4 列，请指定这 4 列的宽度；如果所有列都应当有相同的宽度，则设置为 "auto"。

### 实例

生成包含四列的网格：

.grid-container {
 display: grid;
 grid-template-columns: auto auto auto auto;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-template-columns1)

**注释:** 如果在 4 列网格中有 4 个以上的项目，则网格会自动添加新行并将这些项目放入其中。

grid-template-columns 属性还可以用于指定列的尺寸（宽度）。

### 实例

为 4 列设置大小：

.grid-container {
 display: grid;
 grid-template-columns: 80px 200px auto 40px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-template-columns2)

------

## grid-template-rows 属性

grid-template-rows 属性定义每列的高度。

# 1

# 2

# 3

# 4

# 5

# 6

# 7

# 8

它的值是以空格分隔的列表，其中每个值定义相应行的高度：

### 实例

.grid-container {
 display: grid;
 grid-template-rows: 80px 200px;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-template-rows)

------

## justify-content 属性

justify-content 属性用于在容器内对齐整个网格。

# 1

# 2

# 3

# 4

# 5

# 6

**注释:** 网格的总宽度必须小于容器的宽度，这样 justify-content 属性才能生效。

### 实例

.grid-container {
 display: grid;
 justify-content: space-evenly;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_justify-content_space-evenly)

### 实例

.grid-container {
 display: grid;
 justify-content: space-around;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_justify-content_space-around)

### 实例

.grid-container {
 display: grid;
 justify-content: space-between;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_justify-content_space-between)

### 实例

.grid-container {
 display: grid;
 justify-content: center;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_justify-content_center)

### 实例

.grid-container {
 display: grid;
 justify-content: start;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_justify-content_start)

### 实例

.grid-container {
 display: grid;
 justify-content: end;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_justify-content_end)

------

## align-content 属性

align-content 属性用于垂直对齐容器内的整个网格。

# 1

# 2

# 3

# 4

# 5

# 6

**注释:** 网格的总高度必须小于容器的高度，这样 align-content 属性才能生效。

### 实例

.grid-container {
 display: grid;
 height: 400px;
 align-content: center;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_align-content_center)

### 实例

.grid-container {
 display: grid;
 height: 400px;
 align-content: space-evenly;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_align-content_space-evenly)

### 实例

.grid-container {
 display: grid;
 height: 400px;
 align-content: space-around;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_align-content_space-around)

### 实例

.grid-container {
 display: grid;
 height: 400px;
 align-content: space-between;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_align-content_space-between)

### 实例

.grid-container {
 display: grid;
 height: 400px;
 align-content: start;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_align-content_start)

### 实例

.grid-container {
 display: grid;
 height: 400px;
 align-content: end;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_align-content_end)

# CSS 网格项目

[❮ 上一节](https://www.w3schools.cn/css/css_grid_container.html)[下一节 ❯](https://www.w3schools.cn/css/css_templates.html)

------

# 1

# 2

# 3

# 4

# 5

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_item)

------

## 子元素（项目）

网格容器包含网格项目。

默认情况下，容器在每一行的每一列都有一个网格项目，但是您可以设置网格项目的样式，让它们跨越多个列和/或行。

------

## grid-column 属性：

grid-column 属性定义将项目放置在哪一列上。

您可以定义项目的开始位置以及结束位置。

# 1

# 2

# 3

# 4

# 5

# 6

# 7

# 8

# 9

# 10

# 11

# 12

# 13

# 14

# 15

**注释:** grid-column 属性是 grid-column-start 和 grid-column-end 属性的简写属性。

如需放置某个项目，您可以引用行号（line numbers），或使用关键字 "span" 来定义该项目将跨越多少列。

### 实例

使 "item1" 从第 1 列开始并在第 5 列之前结束：

.item1 {
 grid-column: 1 / 5;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-column_line)

### 实例

使 "item1" 从第 1 列开始，并跨越 3 列：

.item1 {
 grid-column: 1 / span 3;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-column)

### 实例

使 "item2" 从第 2 列开始，并跨越 3 列：

.item2 {
 grid-column: 2 / span 3;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-column2)

------

## grid-row 属性：

grid-row 属性定义了将项目放置在哪一行。

您可以定义项目的开始位置以及结束位置。

# 1

# 2

# 3

# 4

# 5

# 6

# 7

# 8

# 9

# 10

# 11

# 12

# 13

# 14

# 15

# 16

**注释:** `grid-row` 属性是 grid-row-start 和 grid-row-end 属性的简写属性。

如需放置项目，您可以引用行号，或使用关键字 "span" 定义该项目将跨越多少行：

### 实例

使 "item1" 在 row-line 1 开始，在 row-line 4 结束：

.item1 {
 grid-row: 1 / 4;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-row1)

### 实例

使 "item1" 从第 1 行开始并跨越 2 行：

.item1 {
 grid-row: 1 / span 2;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-row2)

------

## grid-area 属性

grid-area 属性可以用作 grid-row-start、grid-column-start、grid-row-end 和 grid-column-end 属性的简写属性。

# 1

# 2

# 3

# 4

# 5

# 6

# 7

# 8

# 9

# 10

# 11

# 12

# 13

# 14

# 15

### 实例

使 "item8" 从 row-line 1 和 column-line 2 开始，在 row-line 5 和 column line 6 结束：

.item8 {
 grid-area: 1 / 2 / 5 / 6;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-area1)

### 实例

使 "item8" 从 row-line 2 和 column-line 1 开始，并跨越 2 行和 3 列：

.item8 {
 grid-area: 2 / 1 / span 2 / span 3;
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-area2)

## 命名网格项

grid-area 属性也可以用于为网格项目分配名称。

### Header

### Menu

### Main

### Right

### Footer

可以通过网格容器的 grid-template-areas 属性来引用命名的网格项目。

### 实例

item1 的名称是 "myArea"，并跨越五列网格布局中的所有五列：

.item1 {
 grid-area: myArea;
}
.grid-container {
 grid-template-areas: 'myArea myArea myArea myArea myArea';
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-area_named)

每行由撇号（' '）定义。

每行中的列都在撇号内定义，并以空格分隔。

**注释:** 句号表示没有名称的网格项目。

### 实例

让 "myArea" 跨越五列网格布局中的两列（句号代表没有名称的项目）：

.item1 {
 grid-area: myArea;
}
.grid-container {
 grid-template-areas: 'myArea myArea . . .';
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-area_named1)

如需定义两行，请在另一组撇号内定义第二行的列：

### 实例

使 "item1" 跨越两列和两行：

.grid-container {
 grid-template-areas: 'myArea myArea . . .' 'myArea myArea . . .';
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-area_named2)

### 实例

命名所有项目，并制作一张随时可用的网页模板：

.item1 { grid-area: header; }
.item2 { grid-area: menu; }
.item3 { grid-area: main; }
.item4 { grid-area: right; }
.item5 { grid-area: footer; }

.grid-container {
 grid-template-areas:
  'header header header header header header'
  'menu main main main right right'
  'menu footer footer footer footer footer';
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-area_named3)

------

## 项目的顺序

网格布局允许我们将项目放置在我们喜欢的任意位置。

HTML 代码中的第一项不必显示为网格中的第一项。

# 1

# 2

# 3

# 4

# 5

# 6

### 实例

.item1 { grid-area: 1 / 3 / 2 / 4; }
.item2 { grid-area: 2 / 3 / 3 / 4; }
.item3 { grid-area: 1 / 1 / 2 / 2; }
.item4 { grid-area: 1 / 2 / 2 / 3; }
.item5 { grid-area: 2 / 1 / 3 / 2; }
.item6 { grid-area: 2 / 2 / 3 / 3; }

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_flexible_order)

您可以通过使用媒体查询来重新排列某些屏幕尺寸的顺序：

### 实例

@media only screen and (max-width: 500px) {
 .item1 { grid-area: 1 / span 3 / 2 / 4; }
 .item2 { grid-area: 3 / 3 / 4 / 4; }
 .item3 { grid-area: 2 / 1 / 3 / 2; }
 .item4 { grid-area: 2 / 2 / span 2 / 3; }
 .item5 { grid-area: 3 / 1 / 4 / 2; }
 .item6 { grid-area: 2 / 3 / 3 / 4; }
}

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_flexible_order2)

# CSS 布局模板

[❮ 上一节](https://www.w3schools.cn/css/css_grid_item.html)[下一节 ❯](https://www.w3schools.cn/css/css_examples.html)

------

## CSS 布局模板

我们用 CSS 创建了一些快速响应的入门模板。

您可以在所有项目中自由修改、保存、共享和使用它们。

页眉、等宽列和页脚:

<iframe src="https://www.w3schools.cn/css/trycss_template_ifr.htm" style="box-sizing: inherit; border: 0px; width: 833.984px; overflow: hidden; height: 280px;"></iframe>

[Try it (using float) »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_template1_float)[Try it (using flexbox) »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_template1_flexbox)[Try it (using grid) »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_template1_grid)

页眉、不等宽列和页脚:

<iframe src="https://www.w3schools.cn/css/trycss_template_ifr3.htm" style="box-sizing: inherit; border: 0px; width: 833.984px; overflow: hidden; height: 280px;"></iframe>

[Try it (using float) »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_template2_float)[Try it (using flexbox) »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_template2_flexbox)[Try it (using grid) »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_template2_grid)

顶部导航、内容和页脚:

<iframe src="https://www.w3schools.cn/css/trycss_template_ifr2.htm" style="box-sizing: inherit; border: 0px; width: 833.984px; overflow: hidden; height: 280px;"></iframe>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_template3)

侧边导航和内容:

<iframe src="https://www.w3schools.cn/css/trycss_template_ifr4.htm" style="box-sizing: inherit; border: 0px; width: 833.984px; overflow: hidden; height: 280px;"></iframe>

[亲自试一试 »](https://www.w3schools.cn/css/tryit.asp?filename=trycss_template4)

# CSS 实例

[❮ 上一节](https://www.w3schools.cn/css/css_templates.html)[下一节 ❯](https://www.w3schools.cn/css/css_quiz.html)

------

### CSS 语法

[CSS 语法](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax1)

[实例解析：CSS 语法](https://www.w3schools.cn/css/css_syntax.html)

------

### CSS 选择器

[元素选择器](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax_element)[元素选择器](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax_id)[类选择器（针对所有元素）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax_class)[类选择器（只针对  元素）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax_element_class)[引用两个类的 HTML 元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax_element_class2)[通用选择器](https://www.w3schools.cn/css/tryit.asp?filename=trycss_syntax_universal)[分组选择器](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grouping)

[实例解析：CSS 选择器](https://www.w3schools.cn/css/css_selectors.html)

------

### CSS 使用

[外部 CSS](https://www.w3schools.cn/css/tryit.asp?filename=trycss_howto_external)[内部 CSS](https://www.w3schools.cn/css/tryit.asp?filename=trycss_howto_internal)[行内 CSS](https://www.w3schools.cn/css/tryit.asp?filename=trycss_howto_inline)[多个样式表](https://www.w3schools.cn/css/tryit.asp?filename=trycss_howto_multiple)[层叠顺序](https://www.w3schools.cn/css/tryit.asp?filename=trycss_howto_cascade)

[实例解析：如何添加 CSS](https://www.w3schools.cn/css/css_howto.html)

------

### CSS 注释

[单行注释](https://www.w3schools.cn/css/tryit.asp?filename=trycss_comments)[多行注释](https://www.w3schools.cn/css/tryit.asp?filename=trycss_comments3)

[实例解析：CSS 注释](https://www.w3schools.cn/css/css_comments.html)

------

### CSS 颜色

[设置颜色的背景色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_background)[设置文本颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_text)[设置边框颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_border)[设置不同的颜色值](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_values)[设置 RGB 值](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_rgb2)[设置 HEX 值](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_hex_gray)[设置 HSL 值](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color_hsl2)

[实例解析：CSS 颜色](https://www.w3schools.cn/css/css_colors.html)

------

### CSS 背景

[设置页面的背景色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-color_body)[设置不同元素的背景色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-color_elements)[把图像设置为页面背景](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image)[如何只在水平方向重复背景图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_gradient2)[如何定位背景图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_position)[固定的背景图像（该图像不会随着页面的其余部分滚动）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background-image_attachment)[所有背景属性在一条声明中](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background_shorthand)[高级背景实例](https://www.w3schools.cn/css/tryit.asp?filename=trycss_background_shorthand2)

[实例解析：CSS 背景](https://www.w3schools.cn/css/css_background.html)

------

### CSS 边框

[设置四条边框的宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-width)[设置上边框的宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-top-width)[设置下边框的宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-bottom-width)[设置左边框的宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-left-width)[设置右边框的宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-right-width)[设置四条边框的样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-style)[设置上边框的样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-top-style)[设置下边框的样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-bottom-style)[设置左边框的样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-left-style)[设置右边框的样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-right-style)[设置四条边框的颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-color)[设置上边框的颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-top-color)[设置下边框的颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-bottom-color)[设置左边框的颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-left-color)[设置右边框的颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-right-color)[所有边框属性在一条声明中](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border)[为元素添加圆角](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border_round)[为每个边设置不同的边框](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-style2)[所有上边框属性在一条声明中](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-top)[所有下边框属性在一条声明中](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-bottom)[所有左边框属性在一条声明中](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-left)[所有右边框属性在一条声明中](https://www.w3schools.cn/css/tryit.asp?filename=trycss_border-right)

[实例解析：CSS 边框](https://www.w3schools.cn/css/css_border.html)

------

### CSS 外边距

[为元素的各边规定不同的外边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_sides)[使用带有四个值的简写 margin 属性](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_shorthand_4val)[使用带有三个值的简写 margin 属性](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_shorthand_3val)[使用带有两个值的简写 margin 属性](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_shorthand_2val)[使用带有一个值的简写 margin 属性](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_shorthand_1val)[把外边距设置 auto，来居中其容器内的元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_auto)[让左外边距继承父元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin-left_inherit)[外边距合并](https://www.w3schools.cn/css/tryit.asp?filename=trycss_margin_collapse)

[实例解析：CSS 外边距](https://www.w3schools.cn/css/css_margin.html)

------

------

### CSS 内边距

[为元素的各边规定不同的内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_sides)[使用带有四个值的简写内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_shorthand_4val)[使用带有三个值的简写内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_shorthand_3val)[使用带有两个值的简写内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_shorthand_2val)[使用带有一个值的简写内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_shorthand_1val)[内边距和元素宽度（不设置 box-sizing）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_width)[内边距和元素宽度（设置 box-sizing）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding_width2)[设置元素的左内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding-left)[设置元素的右内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding-right)[设置元素的上内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding-top)[设置元素的下内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_padding-bottom)

[实例解析：CSS 内边距](https://www.w3schools.cn/css/css_padding.html)

------

### CSS 高度/宽度

[设置元素的高度和宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_height_width)[设置元素的最大宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_max_width)[设置不同元素的高度和宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_height)[使用百分百来设置图像的高度和宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_height_percent)[设置元素的最小宽度和最大宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_max-width)[设置元素的最小高度和最大高度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dim_max-height)

[实例解析：CSS 高度/宽度](https://www.w3schools.cn/css/css_dimension.html)

------

### CSS 盒模型

[演示盒模型](https://www.w3schools.cn/css/tryit.asp?filename=trycss_boxmodel)[规定总宽度为 250 像素的元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_boxmodel_width)

[实例解析：CSS 盒模型](https://www.w3schools.cn/css/css_boxmodel.html)

------

### CSS 轮廓

[绘制围绕元素的线条（轮廓）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline_intro)[设置轮廓的样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-style)[设置轮廓的颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-color)[使用 outline-color：翻转轮廓](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-color_invert)[设置轮廓的宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-width)[使用简写的轮廓属性](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline)[在元素的轮廓与边框之间添加空间](https://www.w3schools.cn/css/tryit.asp?filename=trycss_outline-offset)

[实例解析：CSS 轮廓属性](https://www.w3schools.cn/css/css_outline.html)

------

### CSS 文本

[设置不同元素的文本色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_color)[对齐文本](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text-align)[删除链接下面的线](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text-decoration_link)[修饰文本](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text-decoration)[控制文本中的字母大小写](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text-transform)[缩进文本](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text-indent)[规定字符间距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_letter-spacing)[规定行间距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_line-height)[设置元素的文本方向](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text_direction)[增加字间距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text_word-spacing)[规定元素的文本阴影](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text-shadow)[在元素内禁用文本换行](https://www.w3schools.cn/css/tryit.asp?filename=trycss_text_white-space)[垂直对齐文本内的图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss_vertical-align)

[实例解析：CSS 文本属性](https://www.w3schools.cn/css/css_text.html)

------

### CSS 字体

[设置文本的字体](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-family)[设置字体的大小](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-size)[以 px 为单位设置字体大小](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-size_px)[以 em 为单位设置字体大小](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-size_em)[以百分百和 em 为单位设置字体大小](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-size_percent_em)[设置字体的样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-style)[设置字体的变体](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-variant)[设置字体的粗细](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font-weight)[所有字体属性在一条声明中](https://www.w3schools.cn/css/tryit.asp?filename=trycss_font)

[实例解析：CSS 字体属性](https://www.w3schools.cn/css/css_font.html)

------

### CSS 图标

[Font Awesome 图标](https://www.w3schools.cn/css/tryit.asp?filename=trycss_icons_fa)[Bootstrap 图标](https://www.w3schools.cn/css/tryit.asp?filename=trycss_icons_bs)[Google 图标](https://www.w3schools.cn/css/tryit.asp?filename=trycss_icons_google)

[实例解析：CSS 图标](https://www.w3schools.cn/css/css_icons.html)

------

### CSS 链接

[为已访问/未访问链接添加不同的颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link)[在链接上使用 text-decoration](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link_decoration)[在链接上使用 text-decoration](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link_background)[为超链接添加其他样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link2)[不同类型的指针](https://www.w3schools.cn/css/tryit.asp?filename=trycss_cursor)[高级 - 创建链接框](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link_advanced)[高级 - 创建带边框的链接框](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link_advanced2)

[实例解析：CSS 链接属性](https://www.w3schools.cn/css/css_link.html)

------

### CSS 列表

[列表中的所有不同的列表项标记](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style-type_all)[把图像设置为列表项标记](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style-image)[定位列表项标记](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style-position)[删除默认列表设置](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style_none)[所有列表属性在一条声明中](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style)[用颜色设置列表样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style_colors)[全宽带边框的列表](https://www.w3schools.cn/css/tryit.asp?filename=trycss_list-style-border)

[实例解析：CSS 列表属性](https://www.w3schools.cn/css/css_list.html)

------

### CSS 表格

[规定 table、th 以及 td 元素的黑色边框](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_border)[使用 border-collapse](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_border-collapse)[围绕表格的单一边框](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_border2)[规定表格的宽度和高度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_width)[设置内容的水平对齐（text-align）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_align)[设置内容的垂直对齐（vertical-align）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_vertical-align)[规定 th 和 td 元素的内边距](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_padding)[水平分隔符](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_border_divider)[可悬停的表格](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_hover)[条状表格](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_striped)[规定表格边框的颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_color)[设置表格标题的位置](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_caption-side)[响应式表格](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_responsive)[创建美观的表格](https://www.w3schools.cn/css/tryit.asp?filename=trycss_table_fancy)

[实例解析：CSS 表格属性](https://www.w3schools.cn/css/css_table.html)

------

### CSS 显示

[如何隐藏元素（visibility:hidden）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_visibility_hidden)[如何不显示元素（display:none）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_display_none)[如何把块级元素显示为行内元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_display_inline)[如何把行内元素显示为块级元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_display_block)[如何将 CSS 与 JavaScript 一起使用来显示隐藏内容](https://www.w3schools.cn/css/tryit.asp?filename=trycss_display_js)

[实例解析：CSS Display 属性](https://www.w3schools.cn/css/css_display_visibility.html)

------

### CSS 定位

[相对于浏览器窗口来放置元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_fixed)[相对于元素正常位置来放置元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_relative)[用绝对值定位元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_absolute)[粘性定位](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_sticky)[重叠元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_zindex)[设置元素的形状](https://www.w3schools.cn/css/tryit.asp?filename=trycss_clip)[使用像素值设置图像的上边缘](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_top)[使用像素值设置图像的下边缘](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_bottom)[使用像素值设置图像的左边缘](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_left)[使用像素值设置图像的右边缘](https://www.w3schools.cn/css/tryit.asp?filename=trycss_position_right)[定位图像文本（左上角）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_top_left)[定位图像文本（右上角）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_top_right)[定位图像文本（左下角）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_bottom_left)[定位图像文本（右下角）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_bottom_right)[定位图像文本（居中）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_center)

[实例解析：CSS 定位属性](https://www.w3schools.cn/css/css_positioning.html)

------

### CSS 溢出

[使用 overflow: visible - 溢出没有被裁剪。它在元素框之外渲染。](https://www.w3schools.cn/css/tryit.asp?filename=trycss_overflow_visible)[使用 overflow: hidden - 溢出被裁剪，其余内容被隐藏。](https://www.w3schools.cn/css/tryit.asp?filename=trycss_overflow_hidden)[使用 overflow: scroll - 溢出被裁剪，但是添加了滚动条以查看其余内容。](https://www.w3schools.cn/css/tryit.asp?filename=trycss_overflow_scroll)[使用 overflow: auto - 如果裁剪了溢出，则应添加滚动条以查看其余内容。](https://www.w3schools.cn/css/tryit.asp?filename=trycss_overflow_auto)[使用 overflow-x 和 overflow-y](https://www.w3schools.cn/css/tryit.asp?filename=trycss_overflow_xy)

[实例解析：CSS 溢出属性](https://www.w3schools.cn/css/css_overflow.html)

------

### CSS 浮动

[float 属性的简单使用](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float)[带有边框和外边距的图像浮动到段落的右侧](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float2)[带标题的图像向右浮动](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float3)[让段落的第一个字母向左浮动](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float4)[关闭浮动（使用 clear 属性）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float_clear)[关闭浮动（使用 clearfix hack）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_layout_clearfix2)[创建浮动框](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float_boxes)[创建并排图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float_images_side)[创建等高框（通过 flexbox）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float_boxes_flex)[创建水平菜单](https://www.w3schools.cn/css/tryit.asp?filename=trycss_float5)[创建 web 布局实例](https://www.w3schools.cn/css/tryit.asp?filename=trycss_layout_cols)

[实例解析：CSS 浮动属性](https://www.w3schools.cn/css/css_float.html)

------

### CSS Inline-block

[展示行内、行内块、块级元素的区别](https://www.w3schools.cn/css/tryit.asp?filename=trycss_inline-block_span1)[使用 inline-block 来创建导航链接](https://www.w3schools.cn/css/tryit.asp?filename=trycss_inline-block_nav)

[实例解析：CSS Inline-block](https://www.w3schools.cn/css/css_inline-block.html)

------

### CSS 对齐元素

[通过外边距进行居中对齐](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_container)[居中对齐文本](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_text)[居中对齐图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_image)[通过 position 实现左对齐/右对齐](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_pos)[通过 position 实现左对齐/右对齐 - 跨浏览器方案](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_pos_crossbrowser)[通过 float 实现左对齐/右对齐](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_float)[通过 float 实现左对齐/右对齐 - 跨浏览器方案](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_float_crossbrowser)[通过 padding 垂直居中](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_padding)[垂直和水平居中](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_padding2)[通过 line-height 垂直居中](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_line-height)[通过 position 实现垂直和水平居中](https://www.w3schools.cn/css/tryit.asp?filename=trycss_align_transform)

[实例解析：CSS 对齐属性](https://www.w3schools.cn/css/css_align.html)

------

### CSS 组合器

[后代选择器](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_element_element)[子选择器](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_element_gt)[相邻同胞选择器](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_element_pluss)[通用同胞选择器](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_element_tilde)

[实例解析：CSS 组合器选择器](https://www.w3schools.cn/css/css_combinators.html)

------

### CSS 伪类

[给链接添加不同的颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link)[为链接添加其他样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link2)[使用 :focus](https://www.w3schools.cn/css/tryit.asp?filename=trycss_link_focus)[:first-child - 匹配首个 p 元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_first-child1)[:first-child - 匹配所有 p 元素内的首个 i 元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_first-child2)[:first-child - 匹配所有第一个子 p 元素中的所有 i 元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_first-child3)[使用 :lang](https://www.w3schools.cn/css/tryit.asp?filename=trycss_lang)

[实例解析：CSS 伪类](https://www.w3schools.cn/css/css_pseudo_classes.html)

------

### CSS 伪元素

[制作文本中特别的首字母](https://www.w3schools.cn/css/tryit.asp?filename=trycss_firstletter)[制作文本中特别的首行](https://www.w3schools.cn/css/tryit.asp?filename=trycss_firstline)[制作特别的首字母和首行](https://www.w3schools.cn/css/tryit.asp?filename=trycss_firstline_letter)[使用 :before 在元素之前插入内容](https://www.w3schools.cn/css/tryit.asp?filename=trycss_before)[使用 :after 在元素之后插入内容](https://www.w3schools.cn/css/tryit.asp?filename=trycss_after)

[实例解析：CSS 伪元素](https://www.w3schools.cn/css/css_pseudo_elements.html)

------

### CSS 内容生成

[在每个带有 content 属性的链接之后的括号中插入 URL](https://www.w3schools.cn/css/tryit.asp?filename=trycss_gen_content)[用 "Section 1", "1.1", "1.2" 等为节和子节编号](https://www.w3schools.cn/css/tryit.asp?filename=trycss_gen_counter-reset)[用 quotes 属性指定引号](https://www.w3schools.cn/css/tryit.asp?filename=trycss_gen_quotes)

[实例解析：CSS 计数器](https://www.w3schools.cn/css/css_counters.html)

------

### CSS 不透明度

[创建透明图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_opacity)[创建透明图像 - mouseover 效果](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_transparency)[透明图像的反转的 mouseover 效果](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_transparency2)[透明框（div）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_opacity_box)[用了 RGBA 值的透明框](https://www.w3schools.cn/css/tryit.asp?filename=trycss_opacity_box2)[创建一个文本位于背景图像上的透明框](https://www.w3schools.cn/css/tryit.asp?filename=trycss_transparency)

[实例解析：CSS 图像不透明度](https://www.w3schools.cn/css/css_image_transparency.html)

------

### CSS 导航栏

[拥有完整样式的垂直导航栏](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_vertical_active)[拥有完整样式的水平导航栏](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_float_advanced)[全高的固定垂直导航栏](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_vertical_fixed)[固定的水平导航栏](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_black_fixed)[固定的水平导航栏](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_sticky)[响应式的顶部导航栏](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_horizontal_responsive)[响应式的侧边导航栏](https://www.w3schools.cn/css/tryit.asp?filename=trycss_navbar_vertical_responsive)

[实例解析：CSS 导航栏](https://www.w3schools.cn/css/css_navbar.html)

------

### CSS 下拉列表

[下拉文本](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dropdown_text)[下拉菜单](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dropdown_button)[下拉菜单](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dropdown_right)[下拉图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dropdown_image)[下拉导航栏](https://www.w3schools.cn/css/tryit.asp?filename=trycss_dropdown_navbar)

[实例解析：CSS 下拉菜单](https://www.w3schools.cn/css/css_dropdowns.html)

------

### CSS 图片库

[图片库](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_gallery)[响应式图片库](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_gallery_responsive)

[实例解析：CSS 图片库](https://www.w3schools.cn/css/css_image_gallery.html)

------

### CSS 图像精灵

[图像精灵](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sprites_img)[图像精灵 - 导航列表](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sprites_nav)[有悬停效果的图像精灵](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sprites_hover_nav)

[实例解析：CSS 图像精灵](https://www.w3schools.cn/css/css_image_sprites.html)

------

### CSS 属性选择器

[选取带有 target 属性的所有  元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute)[选取带有 target="_blank" 属性的所有  元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute_value)[选取所有带有 title 属性的元素，其中 title 属性包含以空格分隔的单词列表，单词之一是 "flower"](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute_value2)[选取所有带有以 "top" 开头的 class 属性值的元素（必须是整个单词）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute_hyphen)[选取所有带有以 "top" 开头的 class 属性值的元素（一定不能是整个单词）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute_start)[选取所有带有以 "test" 结尾的 class 属性值的元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute_end)[选择带有包含 "te" 的 class 属性值的所有元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_sel_attribute_contain)

[实例解析：CSS 属性选择器](https://www.w3schools.cn/css/css_attribute_selectors.html)

------

### CSS 表单

[全宽的输入字段](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_width)[填充的输入字段](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_padding)[填充的输入字段](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_border)[带下边框的输入字段](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_border2)[带颜色的输入字段](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_color)[获得焦点的输入字段](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_focus)[获得焦点的输入字段](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_focus2)[带图标的输入字段](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_icon)[有动画效果的搜索框](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_search_anim)[设置文本框的样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_textarea)[设置选择菜单的样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_select)[设置按钮的样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_button)[响应式表单](https://www.w3schools.cn/css/tryit.asp?filename=trycss_form_responsive)

[实例解析：CSS 表单](https://www.w3schools.cn/css/css_form.html)

------

### CSS 计数器

[创建计数器](https://www.w3schools.cn/css/tryit.asp?filename=trycss_counters1)[嵌套计数器 1](https://www.w3schools.cn/css/tryit.asp?filename=trycss_counters2)[嵌套计数器 2](https://www.w3schools.cn/css/tryit.asp?filename=trycss_counters3)

[实例解析：CSS 计数器](https://www.w3schools.cn/css/css_counters.html)

------

### CSS 网站布局

[简单的响应式网站布局](https://www.w3schools.cn/css/tryit.asp?filename=trycss_website_layout_footer)[简单的响应式网站布局](https://www.w3schools.cn/css/tryit.asp?filename=trycss_website_layout_blog)

[实例解析：CSS 网站布局](https://www.w3schools.cn/css/css_website_layout.html)

------

### CSS 圆角

[为元素添加圆角](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_border-radius)[单独设置每个圆角](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_border-radius2)[创建椭圆角](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_border-radius3)

[实例解析：CSS 圆角边框](https://www.w3schools.cn/css/css3_borders.html)

------

### CSS 边框图像

[创建椭圆角](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_border-image)[创建围绕元素的图像边框，使用 stretch 关键字](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_border-image2)[图像边框 - 不同的 slice 边框](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_border-image3)

[实例解析：CSS 边框图像](https://www.w3schools.cn/css/css3_border_images.html)

------

### CSS 背景

[图像边框 - 不同的 slice 边框](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background_multiple)[规定背景图像的大小](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background-size)[使用 "contain" 和 "cover" 缩放背景图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background-size_contain)[使用 "contain" 和 "cover" 缩放背景图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background_multiple3)[全尺寸的背景图像（完全覆盖内容区域）](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background_full)[使用 background-origin 来规定放置背景图像的位置](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background-origin)[使用 background-clip 来规定背景的绘制区域](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_background-clip)

[实例解析：CSS 背景](https://www.w3schools.cn/css/css3_backgrounds.html)

------

### CSS 渐变

[线性渐变 - 从上到下](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear)[线性渐变 - 从左到右](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_ltr)[线性渐变 - 从左到右](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_diagonal)[线性渐变 - 特定角度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_angles)[线性渐变 - 多个色标](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_cs)[线性渐变 - 彩虹色 + 文本](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_rainbow)[线性渐变 - 透明度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_trans)[线性渐变 - 重复的线性渐变](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-linear_repeating)[线性渐变 - 重复的线性渐变](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-radial)[径向渐变 - 间距不同的色标](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-radial2)[径向渐变 - 设置形状](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-radial_shape)[径向渐变 - 不同的尺寸关键字](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-radial_size)[径向渐变 - 重复的径向渐变](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_gradient-radial_repeating)

[实例解析：CSS 渐变](https://www.w3schools.cn/css/css3_gradients.html)

------

### CSS 阴影效果

[简单的阴影效果](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow1)[向阴影添加颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow2)[向阴影添加模糊效果](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow3)[带黑色阴影的白色文本](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow4)[红色霓虹灯发光阴影](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow5)[红色和蓝色霓虹灯发光阴影](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow6)[黑色、蓝色和深蓝色阴影的白色文本](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-shadow7)[向元素添加简单的 box-shadow](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-shadow)[向 box-shadow 添加颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-shadow2)[向 box-shadow 添加颜色和模糊效果](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-shadow3)[创建类似纸质卡片（文本）](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-shadow4)[创建类似纸质卡片（宝丽来图像）](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-shadow5)

[实例解析：CSS 阴影效果](https://www.w3schools.cn/css/css3_shadows.html)

------

### CSS 文本效果

[指定应如何向用户呈现未显示的溢出内容](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-overflow)[将鼠标悬停在元素上时如何显示溢出的内容](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_text-overflow_hover)[允许长文字能够被折断并换到下一行](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_word-wrap)[规定换行规则](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_word-break)

[实例解析：CSS 文本效果](https://www.w3schools.cn/css/css3_text_effects.html)

------

### CSS Web 字体

[在 @font-face 规则中使用您自己的字体](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_font-face_rule)[在 @font-face 规则中使用您自己的字体（粗体）](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_font-face_rule_bold)

[实例解析：CSS 网络字体](https://www.w3schools.cn/css/css3_fonts.html)

------

### CSS 2D 转换

[translate() - 从当前位置删除元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_translate)[rotate() - 顺时针旋转元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_rotate)[rotate() - 逆时针旋转元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_rotate2)[scale() - 增加元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_scale)[scale() - 减少元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_scale2)[skewX() - 沿 X 轴倾斜元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_skewx)[skewY() - 沿 Y 轴倾斜元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_skewy)[skew() - 沿 X 和 Y 轴倾斜元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_skew)[matrix() - 旋转、缩放、移动和倾斜元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_matrix1)

[实例解析：CSS 2D 转换](https://www.w3schools.cn/css/css3_2dtransforms.html)

------

### CSS 3D 转换

[rotateX() - 将元素绕其 X 轴旋转给定角度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_rotatex)[rotateY() - 将元素绕其 Y 轴旋转给定角度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_rotatey)[rotateZ() - 将元素绕其 Z 轴旋转给定角度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transform_rotatez)

[实例解析：CSS 3D 转换](https://www.w3schools.cn/css/css3_3dtransforms.html)

------

### CSS 过渡

[过渡 - 更改元素的宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition1)[过渡 - 更改元素的宽度和高度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition2)[为过渡规定不同的速度曲线](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition_speed)[为过渡效果规定延迟](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition_delay)[向过渡效果添加变换](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition_transform)[在一条简写属性中规定所有过渡属性](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_transition5)

[实例解析：CSS 过渡](https://www.w3schools.cn/css/css3_transitions.html)

------

### CSS 动画

[把动画绑定到一个元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation1)[动画 - 改变一个元素的背景色](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation2)[动画 - 改变一个元素的背景色和位置](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation3)[延迟动画](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_delay)[在动画停止前运行三次](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_count)[永远运行动画](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_count2)[从反方向运行动画](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_direction)[交替运行动画](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_direction2)[动画的速度曲线](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation_speed)[动画的简写属性](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_animation5)

[实例解析：CSS 动画](https://www.w3schools.cn/css/css3_animations.html)

------

### CSS 工具提示

[右侧工具提示](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_right)[左侧工具提示](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_left)[顶部工具提示](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_top)[底部工具提示](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_bottom)[底部工具提示](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_arrow_bottom)[底部工具提示](https://www.w3schools.cn/css/tryit.asp?filename=trycss_tooltip_transition)

[实例解析：CSS 工具提示](https://www.w3schools.cn/css/css_tooltip.html)

------

### CSS 样式图像

[圆角图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_round)[圆形图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_circle)[缩略图](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_thumbnail)[作为链接的缩略图](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_thumbnail_link)[响应式图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_responsive)[图像文本（左上角）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_top_left)[图像文本（右上角）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_top_right)[图像文本（左下角）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_bottom_left)[图像文本（右上角）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_bottom_right)[图像文本（居中）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_text_center)[宝丽来图像](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_images_card)[灰度图像滤镜](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_filter_grayscale)[高级 - 通过 CSS 和 JavaScript 实现的图像模态](https://www.w3schools.cn/css/tryit.asp?filename=trycss_image_modal_js)

[实例解析：CSS 图像](https://www.w3schools.cn/css/css3_images.html)

------

### CSS Object-fit

[剪裁图像的两边，保留长宽比，然后填充空间](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_object-fit2)[所有 object-fit 属性值的例子](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_object-fit_all)

[实例解析：CSS Object-fit](https://www.w3schools.cn/css/css3_object-fit.html)

------

### CSS 按钮

[基础的 CSS 按钮](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_basic)[按钮颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_color)[按钮尺寸](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_font)[圆角按钮](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_round)[圆角按钮](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_border)[可悬停的按钮](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_hover)[带阴影的按钮](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_shadow)[被禁用的按钮](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_disabled)[按钮宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_width)[按钮分组](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_group)[带边框的按钮分组](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_group_border)[带动画的按钮（悬停效果）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_animate1)[带动画的按钮（按键效果）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_animate2)[带动画的按钮（涟漪效果）](https://www.w3schools.cn/css/tryit.asp?filename=trycss_buttons_animate3)

[实例解析：CSS 按钮](https://www.w3schools.cn/css/css3_buttons.html)

------

### CSS 分页

[简单的分页](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination)[活动的、可悬停的分页](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_active)[活动的、可悬停的分页](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_active_round)[可悬停的过渡效果](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_transition)[带边框的分页](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_border)[带边框的分页](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_border_round)[链接之间隔着空白的分页](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_margin)[分页的大小](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_size)[居中的分页](https://www.w3schools.cn/css/tryit.asp?filename=trycss_ex_pagination_center)[面包屑](https://www.w3schools.cn/css/tryit.asp?filename=trycss_breadcrumbs)

[实例解析：CSS 分页](https://www.w3schools.cn/css/css3_pagination.html)

------

### CSS 多列

[创建多列](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-count)[规定列之间的间隙](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-gap)[规定列之间的规则样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-rule-style)[规定列之间的规则样式](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-rule-width)[规定列之间的规则颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-rule-color)[规定列之间的规则的宽度、样式和颜色](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-rule)[规定元素应该横跨多少列](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-span)[为列规定建议的最佳宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_column-width)

[实例解析：CSS 多列](https://www.w3schools.cn/css/css3_multiple_columns.html)

------

### CSS 用户界面

[允许用户调整元素的宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_resize_width)[允许用户调整元素的高度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_resize_height)[允许用户同时调整元素的宽度和高度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_resize)[在元素轮廓与边框之间添加空间](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_outline-offset)

[实例解析：CSS 用户界面](https://www.w3schools.cn/css/css3_user_interface.html)

------

### CSS 变量

[使用 var() 函数](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_var)[使用 var() 函数来插入若干自定义的属性值](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_var2)

[实例解析：CSS 变量](https://www.w3schools.cn/css/css3_variables.html)

------

### CSS Box Sizing

[不设置 box-sizing 的元素宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-sizing_old)[设置 box-sizing 的元素宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-sizing_new)[表单元素 + box-sizing](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_box-sizing_all)

[实例解析：CSS Box Sizing](https://www.w3schools.cn/css/css3_box-sizing.html)

------

### CSS 弹性盒

[带有三个弹性项目的弹性盒](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flexline)[带有三个弹性项目的弹性盒 - rtl 方向](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flexline_rtl)[flex-direction - row-reverse](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_direction_row-reverse)[flex-direction - column](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_direction_column)[flex-direction - column-reverse](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_direction_column-reverse)[justify-content - flex-end](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_justify_flex-end)[justify-content - center](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_justify_center)[justify-content - space-between](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_justify_space-between)[justify-content - space-around](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_justify_space-around)[align-items - stretch](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align_stretch)[align-items - flex-start](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align_flex-start)[align-items - flex-end](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align_flex-end)[align-items - center](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align_center)[align-items - baseline](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align_baseline)[flex-wrap - nowrap](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_nowrap)[flex-wrap - wrap](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_wrap)[flex-wrap - wrap-reverse](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_wrap-reverse)[align-content - center](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-content)[弹性项目排序](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_order)[Margin-right:auto;](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_margin)[Margin:auto; = 完美的居中](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_margin2)[在弹性项目上设置 align-self](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_align-self)[规定弹性项目的长度，相对于弹性项目的其余部分](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_flex_number)[规定弹性项目的长度，相对于弹性项目的其余部分](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_image_gallery)[用弹性盒创建响应式网站](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_flexbox_website2)

[实例解析：CSS flexbox](https://www.w3schools.cn/css/css3_flexbox.html)

------

### CSS 媒体查询

[如果视口宽度为 480 像素或更宽，则将背景色改为浅绿色](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_media_queries1)[如果视口宽度为 480 像素或更宽，显示一个浮动到页面左侧的菜单](https://www.w3schools.cn/css/tryit.asp?filename=trycss3_media_queries2)

[实例解析：CSS 媒体查询](https://www.w3schools.cn/css/css3_mediaqueries.html)

------

### CSS 媒体查询 - 更多实例

[如果视口宽度为 480 像素或更宽，显示一个浮动到页面左侧的菜单](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_ex1)[响应式的导航菜单](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_navbar)[使用浮动的响应式列](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_ex2)[使用弹性盒的响应式列](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_flex)[通过媒体查询隐藏元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_hide)[响应式字体大小](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_fontsize)[响应式图片库](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_img_gallery)[响应式网站](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_website)[根据浏览器方向改变页面布局](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_mediaquery_orientation)[最小宽度到最大宽度](https://www.w3schools.cn/css/tryit.asp?filename=trycss_mediaqueries_minmax)

[实例解析：CSS 媒体查询实例](https://www.w3schools.cn/css/css3_mediaqueries_ex.html)

------

### CSS 响应式 Web 设计

[响应式网格视图](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_styles)[为台式机、笔电和手机添加断点](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_col-s)[典型的断点](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_mediaquery_breakpoints)[响应式图像](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_image)[响应式视频](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_video)[响应式框架：W3.CSS](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_w3css)[响应式框架：Bootstrap](https://www.w3schools.cn/css/tryit.asp?filename=tryresponsive_bootstrap)

[实例解析：CSS 响应式 Web 设计](https://www.w3schools.cn/css/css_rwd_intro.html)

------

### CSS 网格

[网格布局](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_layout_named)[网格元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid)[网格元素](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_grid-column-gap)[网格行](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_lines)[网格容器](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_container)[网格项目](https://www.w3schools.cn/css/tryit.asp?filename=trycss_grid_item)

[实例解析：CSS 网格](https://www.w3schools.cn/css/css_grid.html)



[❮ 上一节](https://www.w3schools.cn/css/css_templates.html)[下一节 ❯](https://www.w3schools.cn/css/css_quiz.html)

# CSS 参考手册

[❮ 首页](https://www.w3schools.cn/default.html)[下一节 ❯](https://www.w3schools.cn/cssref/css3_browsersupport.html)

------

## CSS 属性



## A

| [align-content](https://www.w3schools.cn/cssref/css3_pr_align-content.html) | 规定弹性容器内的行之间的对齐方式，当项目不使用所有可用空间时。 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [align-items](https://www.w3schools.cn/cssref/css3_pr_align-items.html) | 规定弹性容器内项目的对齐方式。                               |
| [align-self](https://www.w3schools.cn/cssref/css3_pr_align-self.html) | 规定弹性容器内所选项目的对齐方式。                           |
| [all](https://www.w3schools.cn/cssref/css3_pr_all.html)      | 重置所有属性（除了 unicode-bidi 和 direction）。             |
| [animation](https://www.w3schools.cn/cssref/css3_pr_animation.html) | 所有 animation-* 属性的简写属性。                            |
| [animation-delay](https://www.w3schools.cn/cssref/css3_pr_animation-delay.html) | 规定开始动画的延迟。                                         |
| [animation-direction](https://www.w3schools.cn/cssref/css3_pr_animation-direction.html) | 规定动画是向前播放、向后播放还是交替播放。                   |
| [animation-duration](https://www.w3schools.cn/cssref/css3_pr_animation-duration.html) | 规定动画完成一个周期应花费的时间。                           |
| [animation-fill-mode](https://www.w3schools.cn/cssref/css3_pr_animation-fill-mode.html) | 规定元素在不播放动画时（在开始之前、结束之后、或同时）的样式。 |
| [animation-iteration-count](https://www.w3schools.cn/cssref/css3_pr_animation-iteration-count.html) | 规定动画的播放次数。                                         |
| [animation-name](https://www.w3schools.cn/cssref/css3_pr_animation-name.html) | 规定 @keyframes 动画的名称。                                 |
| [animation-play-state](https://www.w3schools.cn/cssref/css3_pr_animation-play-state.html) | 规定动画是播放还是暂停。                                     |
| [animation-timing-function](https://www.w3schools.cn/cssref/css3_pr_animation-timing-function.html) | 规定动画的速度曲线。                                         |

## B

| [backface-visibility](https://www.w3schools.cn/cssref/css3_pr_backface-visibility.html) | 定义当面对用户时元素的背面是否应可见。                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [background](https://www.w3schools.cn/cssref/css3_pr_background.html) | 所有 background-* 属性的简写属性。                           |
| [background-attachment](https://www.w3schools.cn/cssref/pr_background-attachment.html) | 设置背景图像是与页面的其余部分一起滚动还是固定的。           |
| [background-blend-mode](https://www.w3schools.cn/cssref/pr_background-blend-mode.html) | 规定每个背景图层（颜色/图像）的混合模式。                    |
| [background-clip](https://www.w3schools.cn/cssref/css3_pr_background-clip.html) | 定义背景（颜色或图像）应在元素内延伸的距离。                 |
| [background-color](https://www.w3schools.cn/cssref/pr_background-color.html) | 规定元素的背景色。                                           |
| [background-image](https://www.w3schools.cn/cssref/pr_background-image.html) | 规定元素的一幅或多幅背景图像。                               |
| [background-origin](https://www.w3schools.cn/cssref/css3_pr_background-origin.html) | 规定背景图像的初始位置。                                     |
| [background-position](https://www.w3schools.cn/cssref/pr_background-position.html) | 规定背景图像的位置。                                         |
| [background-repeat](https://www.w3schools.cn/cssref/pr_background-repeat.html) | 设置是否以及如何重复背景图像。                               |
| [background-size](https://www.w3schools.cn/cssref/css3_pr_background-size.html) | 规定背景图像的尺寸。                                         |
| [border](https://www.w3schools.cn/cssref/pr_border.html)     | border-width、border-style 以及 border-color 的简写属性。    |
| [border-bottom](https://www.w3schools.cn/cssref/pr_border-bottom.html) | border-bottom-width、border-bottom-style 以及 border-bottom-color 的简写属性。 |
| [border-bottom-color](https://www.w3schools.cn/cssref/pr_border-bottom_color.html) | 设置下边框的颜色。                                           |
| [border-bottom-left-radius](https://www.w3schools.cn/cssref/css3_pr_border-bottom-left-radius.html) | 定义左下角的边框圆角。                                       |
| [border-bottom-right-radius](https://www.w3schools.cn/cssref/css3_pr_border-bottom-right-radius.html) | 定义右下角的边框圆角。                                       |
| [border-bottom-style](https://www.w3schools.cn/cssref/pr_border-bottom_style.html) | 设置下边框的样式。                                           |
| [border-bottom-width](https://www.w3schools.cn/cssref/pr_border-bottom_width.html) | 设置下边框的宽度。                                           |
| [border-collapse](https://www.w3schools.cn/cssref/pr_border-collapse.html) | 设置表格边框是折叠为单一边框还是分开的。                     |
| [border-color](https://www.w3schools.cn/cssref/pr_border-color.html) | 设置四条边框的颜色。                                         |
| [border-image](https://www.w3schools.cn/cssref/css3_pr_border-image.html) | border-image-* 属性的简写属性。                              |
| [border-image-outset](https://www.w3schools.cn/cssref/css3_pr_border-image-outset.html) | 规定边框图像区域超出边框的量。                               |
| [border-image-repeat](https://www.w3schools.cn/cssref/css3_pr_border-image-repeat.html) | 规定边框图像应重复、圆角、还是拉伸。                         |
| [border-image-slice](https://www.w3schools.cn/cssref/css3_pr_border-image-slice.html) | 规定如何裁切边框图像。                                       |
| [border-image-source](https://www.w3schools.cn/cssref/css3_pr_border-image-source.html) | 规定用作边框的图像的路径。                                   |
| [border-image-width](https://www.w3schools.cn/cssref/css3_pr_border-image-width.html) | 规定边框图像的宽度。                                         |
| [border-left](https://www.w3schools.cn/cssref/pr_border-left.html) | 所有 border-left-* 属性的简写属性。                          |
| [border-left-color](https://www.w3schools.cn/cssref/pr_border-left_color.html) | 设置左边框的颜色。                                           |
| [border-left-style](https://www.w3schools.cn/cssref/pr_border-left_style.html) | 设置左边框的样式。                                           |
| [border-left-width](https://www.w3schools.cn/cssref/pr_border-left_width.html) | 设置左边框的宽度。                                           |
| [border-radius](https://www.w3schools.cn/cssref/css3_pr_border-radius.html) | 四个 border-*-radius 属性的简写属性。                        |
| [border-right](https://www.w3schools.cn/cssref/pr_border-right.html) | 所有 border-right-* 属性的简写属性。                         |
| [border-right-color](https://www.w3schools.cn/cssref/pr_border-right_color.html) | 设置右边框的颜色。                                           |
| [border-right-style](https://www.w3schools.cn/cssref/pr_border-right_style.html) | 设置右边框的样式。                                           |
| [border-right-width](https://www.w3schools.cn/cssref/pr_border-right_width.html) | 设置右边框的宽度。                                           |
| [border-spacing](https://www.w3schools.cn/cssref/pr_border-spacing.html) | 设置相邻单元格边框之间的距离。                               |
| [border-style](https://www.w3schools.cn/cssref/pr_border-style.html) | 设置四条边框的样式。                                         |
| [border-top](https://www.w3schools.cn/cssref/pr_border-top.html) | border-top-width、border-top-style 以及 border-top-color 的简写属性。 |
| [border-top-color](https://www.w3schools.cn/cssref/pr_border-top_color.html) | 设置上边框的颜色。                                           |
| [border-top-left-radius](https://www.w3schools.cn/cssref/css3_pr_border-top-left-radius.html) | 定义左上角的边框圆角。                                       |
| [border-top-right-radius](https://www.w3schools.cn/cssref/css3_pr_border-top-right-radius.html) | 定义右上角的边框圆角。                                       |
| [border-top-style](https://www.w3schools.cn/cssref/pr_border-top_style.html) | 设置上边框的样式。                                           |
| [border-top-width](https://www.w3schools.cn/cssref/pr_border-top_width.html) | 设置上边框的宽度。                                           |
| [border-width](https://www.w3schools.cn/cssref/pr_border-width.html) | 设置四条边框的宽度。                                         |
| [bottom](https://www.w3schools.cn/cssref/pr_pos_bottom.html) | 设置元素相对于其父元素底部的位置。                           |
| [box-decoration-break](https://www.w3schools.cn/cssref/css3_pr_box-decoration-break.html) | 设置元素在分页符处的背景和边框的行为，或对于行内元素在换行符处的行为。 |
| [box-shadow](https://www.w3schools.cn/cssref/css3_pr_box-shadow.html) | 将一个或多个阴影附加到元素。                                 |
| [box-sizing](https://www.w3schools.cn/cssref/css3_pr_box-sizing.html) | 定义元素的宽度和高度的计算方式：它们是否应包含内边距和边框。 |
| [break-after](https://www.w3schools.cn/cssref/pr_break-after.html) | 规定指定元素之后是否应出现 page-、column- 或 region-break。  |
| [break-before](https://www.w3schools.cn/cssref/pr_break-before.html) | 规定指定元素之前是否应出现 page-、column- 或 region-break。  |
| [break-inside](https://www.w3schools.cn/cssref/pr_break-inside.html) | 规定指定元素内部是否应出现 page-、column- 或 region-break。  |

## C

| [caption-side](https://www.w3schools.cn/cssref/pr_tab_caption-side.html) | 规定表格标题的放置方式。                                |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| [caret-color](https://www.w3schools.cn/cssref/css3_pr_caret-color.html) | 规定光标在 input、textarea 或任何可编辑元素中的颜色。   |
| [@charset](https://www.w3schools.cn/cssref/pr_charset_rule.html) | 规定样式表中使用的字符编码。                            |
| [clear](https://www.w3schools.cn/cssref/pr_class_clear.html) | 规定不允许在元素的哪一侧浮动元素                        |
| [clip](https://www.w3schools.cn/cssref/pr_pos_clip.html)     | 剪裁绝对定位的元素。                                    |
| [color](https://www.w3schools.cn/cssref/pr_text_color.html)  | 设置文本的颜色。                                        |
| [column-count](https://www.w3schools.cn/cssref/css3_pr_column-count.html) | 规定元素应分为的列数。                                  |
| [column-fill](https://www.w3schools.cn/cssref/css3_pr_column-fill.html) | 指定如何填充列（是否 balanced）。                       |
| [column-gap](https://www.w3schools.cn/cssref/css3_pr_column-gap.html) | 规定列间隙。                                            |
| [column-rule](https://www.w3schools.cn/cssref/css3_pr_column-rule.html) | 所有 column-rule-* 属性的简写属性。                     |
| [column-rule-color](https://www.w3schools.cn/cssref/css3_pr_column-rule-color.html) | 规定列之间规则的颜色。                                  |
| [column-rule-style](https://www.w3schools.cn/cssref/css3_pr_column-rule-style.html) | 规定列之间的规则样式。                                  |
| [column-rule-width](https://www.w3schools.cn/cssref/css3_pr_column-rule-width.html) | 规定列之间的规则宽度。                                  |
| [column-span](https://www.w3schools.cn/cssref/css3_pr_column-span.html) | 规定元素应该跨越多少列。                                |
| [column-width](https://www.w3schools.cn/cssref/css3_pr_column-width.html) | 规定列宽度。                                            |
| [columns](https://www.w3schools.cn/cssref/css3_pr_columns.html) | column-width 和 column-count 的简写属性。               |
| [content](https://www.w3schools.cn/cssref/pr_gen_content.html) | 与 :before 和 :after 伪元素一起使用，来插入生成的内容。 |
| [counter-increment](https://www.w3schools.cn/cssref/pr_gen_counter-increment.html) | 增加或减少一个或多个 CSS 计数器的值。                   |
| [counter-reset](https://www.w3schools.cn/cssref/pr_gen_counter-reset.html) | 创建或重置一个或多个 CSS 计数器。                       |
| [cursor](https://www.w3schools.cn/cssref/pr_class_cursor.html) | 规定当指向元素时要显示的鼠标光标。                      |

## D

| [direction](https://www.w3schools.cn/cssref/pr_text_direction.html) | 规定文本方向/书写方向。      |
| ------------------------------------------------------------ | ---------------------------- |
| [display](https://www.w3schools.cn/cssref/pr_class_display.html) | 规定如何显示某个 HTML 元素。 |

## E

| [empty-cells](https://www.w3schools.cn/cssref/pr_tab_empty-cells.html) | 规定是否在表格中的空白单元格上显示边框和背景。 |
| ------------------------------------------------------------ | ---------------------------------------------- |
|                                                              |                                                |

## F

| [filter](https://www.w3schools.cn/cssref/css3_pr_filter.html) | 定义元素显示之前的效果（例如，模糊或颜色偏移）。             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [flex](https://www.w3schools.cn/cssref/css3_pr_flex.html)    | flex-grow、flex-shrink 以及 flex-basis 的简写属性。          |
| [flex-basis](https://www.w3schools.cn/cssref/css3_pr_flex-basis.html) | 规定弹性项目的初始长度。                                     |
| [flex-direction](https://www.w3schools.cn/cssref/css3_pr_flex-direction.html) | 规定弹性项目的方向。                                         |
| [flex-flow](https://www.w3schools.cn/cssref/css3_pr_flex-flow.html) | flex-direction 和 flex-wrap 的简写属性。                     |
| [flex-grow](https://www.w3schools.cn/cssref/css3_pr_flex-grow.html) | 规定项目相对于其余项目的增量。                               |
| [flex-shrink](https://www.w3schools.cn/cssref/css3_pr_flex-shrink.html) | 规定项目相对于其余项目的减量。                               |
| [flex-wrap](https://www.w3schools.cn/cssref/css3_pr_flex-wrap.html) | 规定弹性项目是否应该换行。                                   |
| [float](https://www.w3schools.cn/cssref/pr_class_float.html) | 规定弹性项目是否应该换行。                                   |
| [font](https://www.w3schools.cn/cssref/pr_font_font.html)    | font-style、font-variant、font-weight、font-size/line-height 以及 font-family 的简写属性。 |
| [@font-face](https://www.w3schools.cn/cssref/css3_pr_font-face_rule.html) | 允许网站下载和使用 "web-safe" 字体以外的其他字体的规则。     |
| [font-family](https://www.w3schools.cn/cssref/pr_font_font-family.html) | 规定文本的字体族（字体系列）。                               |
| [font-feature-settings](https://www.w3schools.cn/cssref/css3_pr_font-feature-settings.html) | 允许控制 OpenType 字体中的高级印刷特性。                     |
| @font-feature-values                                         | 允许创作者使用 font-variant-alternate 中的通用名来实现在 OpenType 中以不同方式激活的特性。 |
| [font-kerning](https://www.w3schools.cn/cssref/css3_pr_font-kerning.html) | 控制字距调整信息的使用（字母间距）。                         |
| font-language-override                                       | 控制特定语言的字形在字体的使用。                             |
| [font-size](https://www.w3schools.cn/cssref/pr_font_font-size.html) | 规定文本的字体大小。                                         |
| [font-size-adjust](https://www.w3schools.cn/cssref/css3_pr_font-size-adjust.html) | 保持发生字体回退时的可读性。                                 |
| [font-stretch](https://www.w3schools.cn/cssref/css3_pr_font-stretch.html) | 从字体系列中选择一个普通的、压缩的或扩展的字体。             |
| [font-style](https://www.w3schools.cn/cssref/pr_font_font-style.html) | 规定文本的字体样式。                                         |
| font-synthesis                                               | 控制哪些缺失的字体（粗体或斜体）可以由浏览器合成。           |
| [font-variant](https://www.w3schools.cn/cssref/pr_font_font-variant.html) | 规定是否应该以小型大写字体显示文本。                         |
| font-variant-alternates                                      | 控制与 @font-feature-values 中定义的备用名称关联的备用字形的使用。 |
| [font-variant-caps](https://www.w3schools.cn/cssref/css3_pr_font-variant-caps.html) | 控制大写字母的备用字形的使用。                               |
| font-variant-east-asian                                      | 控制东亚文字（例如中文和日语）的备用字形的使用。             |
| font-variant-ligatures                                       | 控制在适用于元素的文本内容中使用哪些连字和上下文形式。       |
| font-variant-numeric                                         | 控制数字、分数和序号标记的备用字形的使用。                   |
| font-variant-position                                        | 控制较小字体的替代字形的使用，这些字形相对于字体基线定位为上标或下标。 |
| [font-weight](https://www.w3schools.cn/cssref/pr_font_weight.html) | 规定字体的粗细。                                             |

## G

| [grid](https://www.w3schools.cn/cssref/pr_grid.html)         | grid-template-rows、grid-template-columns、grid-template-areas、grid-auto-rows、grid-auto-columns 以及 grid-auto-flow 属性的简写属性。 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [grid-area](https://www.w3schools.cn/cssref/pr_grid-area.html) | 即可规定网格项的名称，也可以是 grid-row-start、grid-column-start、grid-row-end 以及 grid-column-end 属性的简写属性。 |
| [grid-auto-columns](https://www.w3schools.cn/cssref/pr_grid-auto-columns.html) | 规定默认的列尺寸。                                           |
| [grid-auto-flow](https://www.w3schools.cn/cssref/pr_grid-auto-flow.html) | 规定如何在网格中插入自动放置的项目。                         |
| [grid-auto-rows](https://www.w3schools.cn/cssref/pr_grid-auto-rows.html) | 规定默认的行尺寸。                                           |
| [grid-column](https://www.w3schools.cn/cssref/pr_grid-column.html) | grid-column-start 和 grid-column-end 属性的简写属性。        |
| [grid-column-end](https://www.w3schools.cn/cssref/pr_grid-column-end.html) | 规定如何结束网格项目。                                       |
| [grid-column-gap](https://www.w3schools.cn/cssref/pr_grid-column-gap.html) | 规定列间隙的尺寸。                                           |
| [grid-column-start](https://www.w3schools.cn/cssref/pr_grid-column-start.html) | 规定网格项目从何处开始。                                     |
| [grid-gap](https://www.w3schools.cn/cssref/pr_grid-gap.html) | grid-row-gap 和 grid-column-gap 的简写属性。                 |
| [grid-row](https://www.w3schools.cn/cssref/pr_grid-row.html) | grid-row-start 和 grid-row-end 属性的简写属性。              |
| [grid-row-end](https://www.w3schools.cn/cssref/pr_grid-row-end.html) | 规定网格项目在何处结束。                                     |
| [grid-row-gap](https://www.w3schools.cn/cssref/pr_grid-row-gap.html) | 规定列间隙的尺寸。                                           |
| [grid-row-start](https://www.w3schools.cn/cssref/pr_grid-row-start.html) | 规定网格项目从何处开始。                                     |
| [grid-template](https://www.w3schools.cn/cssref/pr_grid-template.html) | grid-template-rows、grid-template-columns 以及 grid-areas 属性的简写属性。 |
| [grid-template-areas](https://www.w3schools.cn/cssref/pr_grid-template-areas.html) | 规定如何使用命名的网格项显示列和行。                         |
| [grid-template-columns](https://www.w3schools.cn/cssref/pr_grid-template-columns.html) | 指定列的尺寸以及网格布局中的列数。                           |
| [grid-template-rows](https://www.w3schools.cn/cssref/pr_grid-template-rows.html) | 指定网格布局中的行的尺寸。                                   |

## H

| [hanging-punctuation](https://www.w3schools.cn/cssref/css3_pr_hanging-punctuation.html) | 规定是否可以在行框外放置标点符号。 |
| ------------------------------------------------------------ | ---------------------------------- |
| [height](https://www.w3schools.cn/cssref/pr_dim_height.html) | 设置元素的高度。                   |
| [hyphens](https://www.w3schools.cn/cssref/css3_pr_hyphens.html) | 设置如何分割单词以改善段落的布局。 |

## I

| image-rendering                                              | 当图像被缩放时，向浏览器提供关于保留图像的哪些最重要的方面的信息。 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [@import](https://www.w3schools.cn/cssref/pr_import_rule.html) | 允许您将样式表导入另一张样式表。                             |
| [isolation](https://www.w3schools.cn/cssref/css3_pr_isolation.html) | 定义元素是否必须创建新的堆叠内容。                           |

## J

| [justify-content](https://www.w3schools.cn/cssref/css3_pr_justify-content.html) | 规定项目在弹性容器内的对齐方式，当项目未用到所有可用空间时。 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

## K

| [@keyframes](https://www.w3schools.cn/cssref/css3_pr_animation-keyframes.html) | 规定动画代码。 |
| ------------------------------------------------------------ | -------------- |
|                                                              |                |

## L

| [left](https://www.w3schools.cn/cssref/pr_pos_left.html)     | 规定定位元素的左侧位置。       |
| ------------------------------------------------------------ | ------------------------------ |
| [letter-spacing](https://www.w3schools.cn/cssref/pr_text_letter-spacing.html) | 增加或减少文本中的字符间距。   |
| line-break                                                   | 如何如何/是否换行。            |
| [line-height](https://www.w3schools.cn/cssref/pr_dim_line-height.html) | 设置行高。                     |
| [list-style](https://www.w3schools.cn/cssref/pr_list-style.html) | 在一条声明中设置所有列表属性。 |
| [list-style-image](https://www.w3schools.cn/cssref/pr_list-style-image.html) | 把图像指定为列表项标记。       |
| [list-style-position](https://www.w3schools.cn/cssref/pr_list-style-position.html) | 规定列表项标记的位置。         |
| [list-style-type](https://www.w3schools.cn/cssref/pr_list-style-type.html) | 规定列表项标记的类型。         |

## M

| [margin](https://www.w3schools.cn/cssref/pr_margin.html)     | 在一条声明中设置所有外边距属性。           |
| ------------------------------------------------------------ | ------------------------------------------ |
| [margin-bottom](https://www.w3schools.cn/cssref/pr_margin-bottom.html) | 设置元素的下外边距。                       |
| [margin-left](https://www.w3schools.cn/cssref/pr_margin-left.html) | 设置元素的左外边距。                       |
| [margin-right](https://www.w3schools.cn/cssref/pr_margin-right.html) | 设置元素的右外边距。                       |
| [margin-top](https://www.w3schools.cn/cssref/pr_margin-top.html) | 设置元素的上外边距。                       |
| mask                                                         | 通过在特定位置遮罩或剪切图像来隐藏元素。   |
| mask-type                                                    | 规定将遮罩元素用作亮度或 Alpha 遮罩。      |
| [max-height](https://www.w3schools.cn/cssref/pr_dim_max-height.html) | 设置元素的最大高度。                       |
| [max-width](https://www.w3schools.cn/cssref/pr_dim_max-width.html) | 设置元素的最大宽度。                       |
| [@media](https://www.w3schools.cn/cssref/css3_pr_mediaquery.html) | 为不同的媒体类型、设备、尺寸设置样式规则。 |
| [min-height](https://www.w3schools.cn/cssref/pr_dim_min-height.html) | 设置元素的最小高度。                       |
| [min-width](https://www.w3schools.cn/cssref/pr_dim_min-width.html) | 设置元素的最小宽度。                       |
| [mix-blend-mode](https://www.w3schools.cn/cssref/pr_mix-blend-mode.html) | 规定元素内容应如何与其直接父的背景相混合。 |

## O

| [object-fit](https://www.w3schools.cn/cssref/css3_pr_object-fit.html) | 规定替换元素的内容应如何适合其所用高度和宽度建立的框。       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [object-position](https://www.w3schools.cn/cssref/css3_pr_object-position.html) | 指定替换元素在其框内的对齐方式。                             |
| [opacity](https://www.w3schools.cn/cssref/css3_pr_opacity.html) | 设置元素的不透明等级。                                       |
| [order](https://www.w3schools.cn/cssref/css3_pr_order.html)  | 设置弹性项目相对于其余项目的顺序。                           |
| orphans                                                      | 设置在元素内发生分页时必须保留在页面底部的最小行数。         |
| [outline](https://www.w3schools.cn/cssref/pr_outline.html)   | outline-width、outline-style 以及 outline-color 属性的简写属性。 |
| [outline-color](https://www.w3schools.cn/cssref/pr_outline-color.html) | 设置轮廓的颜色。                                             |
| [outline-offset](https://www.w3schools.cn/cssref/css3_pr_outline-offset.html) | 对轮廓进行偏移，并将其绘制到边框边缘之外。                   |
| [outline-style](https://www.w3schools.cn/cssref/pr_outline-style.html) | 设置轮廓的样式。                                             |
| [outline-width](https://www.w3schools.cn/cssref/pr_outline-width.html) | 设置轮廓的宽度。                                             |
| [overflow](https://www.w3schools.cn/cssref/pr_pos_overflow.html) | 规定如果内容溢出元素框会发生什么情况。                       |
| overflow-wrap                                                | 规定浏览器是否可能为了防止溢出而在单词内折行（当字符串太长而无法适应其包含框时）。 |
| [overflow-x](https://www.w3schools.cn/cssref/css3_pr_overflow-x.html) | 规定是否剪裁内容的左右边缘，如果它溢出了元素的内容区域。     |
| [overflow-y](https://www.w3schools.cn/cssref/css3_pr_overflow-y.html) | 规定是否剪裁内容的上下边缘，如果它溢出了元素的内容区域。     |

## P

| [padding](https://www.w3schools.cn/cssref/pr_padding.html)   | 所有 padding-* 属性的简写属性。                          |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| [padding-bottom](https://www.w3schools.cn/cssref/pr_padding-bottom.html) | 设置元素的下内边距。                                     |
| [padding-left](https://www.w3schools.cn/cssref/pr_padding-left.html) | 设置元素的左内边距。                                     |
| [padding-right](https://www.w3schools.cn/cssref/pr_padding-right.html) | 设置元素的右内边距。                                     |
| [padding-top](https://www.w3schools.cn/cssref/pr_padding-top.html) | 设置元素的上内边距。                                     |
| [page-break-after](https://www.w3schools.cn/cssref/pr_print_pageba.html) | 设置元素之后的分页（page-break）行为。                   |
| [page-break-before](https://www.w3schools.cn/cssref/pr_print_pagebb.html) | 设置元素之前的分页（page-break）行为。                   |
| [page-break-inside](https://www.w3schools.cn/cssref/pr_print_pagebi.html) | 设置元素内的分页（page-break）行为。                     |
| [perspective](https://www.w3schools.cn/cssref/css3_pr_perspective.html) | 为 3D 定位元素提供透视。                                 |
| [perspective-origin](https://www.w3schools.cn/cssref/css3_pr_perspective-origin.html) | 定义用户观看 3D 定位元素的位置。                         |
| [pointer-events](https://www.w3schools.cn/cssref/css3_pr_pointer-events.html) | 定义元素是否对指针事件做出反应。                         |
| [position](https://www.w3schools.cn/cssref/pr_class_position.html) | 规定用于元素的定位方法的类型（静态、相对、绝对或固定）。 |

## Q

| [quotes](https://www.w3schools.cn/cssref/pr_gen_quotes.html) | 设置引号类型。 |
| ------------------------------------------------------------ | -------------- |
|                                                              |                |

## R

| [resize](https://www.w3schools.cn/cssref/css3_pr_resize.html) | 定义用户是否以及如何调整元素的尺寸。 |
| ------------------------------------------------------------ | ------------------------------------ |
| [right](https://www.w3schools.cn/cssref/pr_pos_right.html)   | 规定定位元素的左侧位置。             |

## S

| [scroll-behavior](https://www.w3schools.cn/cssref/pr_scroll-behavior.html) | 规定可滚动框中是否平滑地滚动，而不是直接跳跃。 |
| ------------------------------------------------------------ | ---------------------------------------------- |
|                                                              |                                                |

## T

| [tab-size](https://www.w3schools.cn/cssref/css3_pr_tab-size.html) | 规定制表符的宽度。                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [table-layout](https://www.w3schools.cn/cssref/pr_tab_table-layout.html) | 定义用于对单元格、行和列进行布局的算法。                     |
| [text-align](https://www.w3schools.cn/cssref/pr_text_text-align.html) | 规定文本的水平对齐方式。                                     |
| [text-align-last](https://www.w3schools.cn/cssref/css3_pr_text-align-last.html) | 描述当 text-align 为 "justify" 时，如何在强制换行之前对齐块或行的最后一行。 |
| text-combine-upright                                         | 将多个字符组合到到单个字符的空间中。                         |
| [text-decoration](https://www.w3schools.cn/cssref/pr_text_text-decoration.html) | 规定文本装饰。                                               |
| [text-decoration-color](https://www.w3schools.cn/cssref/css3_pr_text-decoration-color.html) | 规定文本装饰（text-decoration）的颜色。                      |
| [text-decoration-line](https://www.w3schools.cn/cssref/css3_pr_text-decoration-line.html) | 规定文本装饰（text-decoration）中的的行类型。                |
| [text-decoration-style](https://www.w3schools.cn/cssref/css3_pr_text-decoration-style.html) | 规定文本装饰（text-decoration）中的行样式。                  |
| [text-indent](https://www.w3schools.cn/cssref/pr_text_text-indent.html) | 规定文本块（text-block）中的的首行缩进。                     |
| [text-justify](https://www.w3schools.cn/cssref/css3_pr_text-justify.html) | 规定当 text-align 为 "justify" 时使用的对齐方法。            |
| text-orientation                                             | 定义行中的文本方向。                                         |
| [text-overflow](https://www.w3schools.cn/cssref/css3_pr_text-overflow.html) | 规定当文本溢出包含元素时应该发生的情况。                     |
| [text-shadow](https://www.w3schools.cn/cssref/css3_pr_text-shadow.html) | 添加文本阴影。                                               |
| [text-transform](https://www.w3schools.cn/cssref/pr_text_text-transform.html) | 控制文本的大写。                                             |
| text-underline-position                                      | 规定使用 text-decoration 属性设置的下划线的位置。            |
| [top](https://www.w3schools.cn/cssref/pr_pos_top.html)       | 规定定位元素的顶端位置。                                     |
| [transform](https://www.w3schools.cn/cssref/css3_pr_transform.html) | 向元素应用 2D 或 3D 转换。                                   |
| [transform-origin](https://www.w3schools.cn/cssref/css3_pr_transform-origin.html) | 允许您更改转换元素的位置。                                   |
| [transform-style](https://www.w3schools.cn/cssref/css3_pr_transform-style.html) | 规定如何在 3D 空间中渲染嵌套的元素。                         |
| [transition](https://www.w3schools.cn/cssref/css3_pr_transition.html) | 所有 transition-* 属性的简写属性。                           |
| [transition-delay](https://www.w3schools.cn/cssref/css3_pr_transition-delay.html) | 规定合适开始过渡效果。                                       |
| [transition-duration](https://www.w3schools.cn/cssref/css3_pr_transition-duration.html) | 规定完成过渡效果所需的秒或毫秒数。                           |
| [transition-property](https://www.w3schools.cn/cssref/css3_pr_transition-property.html) | 规定过渡效果对应的 CSS 属性的名称。                          |
| [transition-timing-function](https://www.w3schools.cn/cssref/css3_pr_transition-timing-function.html) | 规定过渡效果的速度曲线。                                     |

## U

| [unicode-bidi](https://www.w3schools.cn/cssref/pr_text_unicode-bidi.html) | 与 [direction](https://www.w3schools.cn/cssref/pr_text_direction.html) 属性一起使用，设置或返回是否应覆写文本来支持同一文档中的多种语言。 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [user-select](https://www.w3schools.cn/cssref/css3_pr_user-select.html) | 规定是否能选取元素的文本。                                   |

## V

| [vertical-align](https://www.w3schools.cn/cssref/pr_pos_vertical-align.html) | 设置元素的垂直对齐方式。 |
| ------------------------------------------------------------ | ------------------------ |
| [visibility](https://www.w3schools.cn/cssref/pr_class_visibility.html) | 规定元素是否可见。       |

## W

| [white-space](https://www.w3schools.cn/cssref/pr_text_white-space.html) | 规定如何处理元素内的空白字符。                         |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| widows                                                       | 设置如果元素内发生分页，必须在页面顶部保留的最小行数。 |
| [width](https://www.w3schools.cn/cssref/pr_dim_width.html)   | 设置元素的宽度。                                       |
| [word-break](https://www.w3schools.cn/cssref/css3_pr_word-break.html) | 规定单词到达行末后如何换行。                           |
| [word-spacing](https://www.w3schools.cn/cssref/pr_text_word-spacing.html) | 增加或减少文本中的单词间距。                           |
| [word-wrap](https://www.w3schools.cn/cssref/css3_pr_word-wrap.html) | 允许长的、不能折行的单词换到下一行。                   |
| [writing-mode](https://www.w3schools.cn/cssref/css3_pr_writing-mode.html) | 规定文本行是水平还是垂直布局。                         |

## Z

| [z-index](https://www.w3schools.cn/cssref/pr_pos_z-index.html) | 设置定位元素的堆叠顺序。 |
| ------------------------------------------------------------ | ------------------------ |
|                                                              |                          |

# CSS 选择器参考手册

[❮ 上一节](https://www.w3schools.cn/cssref/css3_browsersupport.html)[下一节 ❯](https://www.w3schools.cn/cssref/css_functions.html)

------

## CSS 选择器

在 CSS 中，选择器是选取需设置样式的元素的模式。

请使用我们的 [CSS 选择器测试工具](https://www.w3schools.cn/cssref/trysel.html)，它可为您演示不同的选择器。

| 选择器                                                       | 实例                  | 实例描述                                                   |
| :----------------------------------------------------------- | :-------------------- | :--------------------------------------------------------- |
| [.*class*](https://www.w3schools.cn/cssref/sel_class.html)   | .intro                | 选择 class="intro" 的所有元素。                            |
| *.class1.class2*                                             | .name1.name2          | 选择 class 属性中同时有 name1 和 name2 的所有元素。        |
| *.class1 .class2*                                            | .name1 .name2         | 选择作为类名 name1 元素后代的所有类名 name2 元素。         |
| [#*id*](https://www.w3schools.cn/cssref/sel_id.html)         | #firstname            | 选择 id="firstname" 的元素。                               |
| [*](https://www.w3schools.cn/cssref/sel_all.html)            | *                     | 选择所有元素。                                             |
| *[element](https://www.w3schools.cn/cssref/sel_element.html)* | p                     | 选择所有 <p> 元素。                                        |
| *[element.class](https://www.w3schools.cn/cssref/sel_element_class.html)* | p.intro               | 选择 class="intro" 的所有 <p> 元素。                       |
| *[element,element](https://www.w3schools.cn/cssref/sel_element_comma.html)* | div, p                | 选择所有 <div> 元素和所有 <p> 元素。                       |
| [*element* *element*](https://www.w3schools.cn/cssref/sel_element_element.html) | div p                 | 选择 <div> 元素内的所有 <p> 元素。                         |
| [*element*>*element*](https://www.w3schools.cn/cssref/sel_element_gt.html) | div > p               | 选择父元素是 <div> 的所有 <p> 元素。                       |
| [*element*+*element*](https://www.w3schools.cn/cssref/sel_element_pluss.html) | div + p               | 选择紧跟 <div> 元素的首个 <p> 元素。                       |
| [*element1*~*element2*](https://www.w3schools.cn/cssref/sel_gen_sibling.html) | p ~ ul                | 选择前面有 <p> 元素的每个 <ul> 元素。                      |
| [[*attribute*\]](https://www.w3schools.cn/cssref/sel_attribute.html) | [target]              | 选择带有 target 属性的所有元素。                           |
| [[*attribute*=*value*\]](https://www.w3schools.cn/cssref/sel_attribute_value.html) | [target=_blank]       | 选择带有 target="_blank" 属性的所有元素。                  |
| [[*attribute*~=*value*\]](https://www.w3schools.cn/cssref/sel_attribute_value_contains.html) | [title~=flower]       | 选择 title 属性包含单词 "flower" 的所有元素。              |
| [[*attribute*\|=*value*\]](https://www.w3schools.cn/cssref/sel_attribute_value_lang.html) | [lang\|=en]           | 选择 lang 属性值以 "en" 开头的所有元素。                   |
| [[*attribute*^=*value*\]](https://www.w3schools.cn/cssref/sel_attr_begin.html) | a[href^="https"]      | 选择其 src 属性值以 "https" 开头的每个 <a> 元素。          |
| [[*attribute*$=*value*\]](https://www.w3schools.cn/cssref/sel_attr_end.html) | a[href$=".pdf"]       | 选择其 src 属性以 ".pdf" 结尾的所有 <a> 元素。             |
| [[*attribute**=*value*\]](https://www.w3schools.cn/cssref/sel_attr_contain.html) | a[href*="w3schools"]  | 选择其 href 属性值中包含 "w3schools" 子串的每个 <a> 元素。 |
| [:active](https://www.w3schools.cn/cssref/sel_active.html)   | a:active              | 选择活动链接。                                             |
| [::after](https://www.w3schools.cn/cssref/sel_after.html)    | p::after              | 在每个 <p> 的内容之后插入内容。                            |
| [::before](https://www.w3schools.cn/cssref/sel_before.html)  | p::before             | 在每个 <p> 的内容之前插入内容。                            |
| [:checked](https://www.w3schools.cn/cssref/sel_checked.html) | input:checked         | 选择每个被选中的 <input> 元素。                            |
| [:default](https://www.w3schools.cn/cssref/sel_default.html) | input:default         | 选择默认的 <input> 元素。                                  |
| [:disabled](https://www.w3schools.cn/cssref/sel_disabled.html) | input:disabled        | 选择每个被禁用的 <input> 元素。                            |
| [:empty](https://www.w3schools.cn/cssref/sel_empty.html)     | p:empty               | 选择没有子元素的每个 <p> 元素（包括文本节点）。            |
| [:enabled](https://www.w3schools.cn/cssref/sel_enabled.html) | input:enabled         | 选择每个启用的 <input> 元素。                              |
| [:first-child](https://www.w3schools.cn/cssref/sel_firstchild.html) | p:first-child         | 选择属于父元素的第一个子元素的每个 <p> 元素。              |
| [::first-letter](https://www.w3schools.cn/cssref/sel_firstletter.html) | p::first-letter       | 选择每个 <p> 元素的首字母。                                |
| [::first-line](https://www.w3schools.cn/cssref/sel_firstline.html) | p::first-line         | 选择每个 <p> 元素的首行。                                  |
| [:first-of-type](https://www.w3schools.cn/cssref/sel_first-of-type.html) | p:first-of-type       | 选择属于其父元素的首个 <p> 元素的每个 <p> 元素。           |
| [:focus](https://www.w3schools.cn/cssref/sel_focus.html)     | input:focus           | 选择获得焦点的 input 元素。                                |
| [:hover](https://www.w3schools.cn/cssref/sel_hover.html)     | a:hover               | 选择鼠标指针位于其上的链接。                               |
| [:in-range](https://www.w3schools.cn/cssref/sel_in-range.html) | input:in-range        | 选择其值在指定范围内的 input 元素。                        |
| [:indeterminate](https://www.w3schools.cn/cssref/sel_indeterminate.html) | input:indeterminate   | 选择处于不确定状态的 input 元素。                          |
| [:invalid](https://www.w3schools.cn/cssref/sel_invalid.html) | input:invalid         | 选择具有无效值的所有 input 元素。                          |
| [:lang(*language*)](https://www.w3schools.cn/cssref/sel_lang.html) | p:lang(it)            | 选择 lang 属性等于 "it"（意大利）的每个 <p> 元素。         |
| [:last-child](https://www.w3schools.cn/cssref/sel_last-child.html) | p:last-child          | 选择属于其父元素最后一个子元素每个 <p> 元素。              |
| [:last-of-type](https://www.w3schools.cn/cssref/sel_last-of-type.html) | p:last-of-type        | 选择属于其父元素的最后 <p> 元素的每个 <p> 元素。           |
| [:link](https://www.w3schools.cn/cssref/sel_link.html)       | a:link                | 选择所有未访问过的链接。                                   |
| [:not(*selector*)](https://www.w3schools.cn/cssref/sel_not.html) | :not(p)               | 选择非 <p> 元素的每个元素。                                |
| [:nth-child(*n*)](https://www.w3schools.cn/cssref/sel_nth-child.html) | p:nth-child(2)        | 选择属于其父元素的第二个子元素的每个 <p> 元素。            |
| [:nth-last-child(*n*)](https://www.w3schools.cn/cssref/sel_nth-last-child.html) | p:nth-last-child(2)   | 同上，从最后一个子元素开始计数。                           |
| [:nth-last-of-type(*n*)](https://www.w3schools.cn/cssref/sel_nth-last-of-type.html) | p:nth-last-of-type(2) | 选择属于其父元素第二个 <p> 元素的每个 <p> 元素。           |
| [:nth-of-type(*n*)](https://www.w3schools.cn/cssref/sel_nth-of-type.html) | p:nth-of-type(2)      | 同上，但是从最后一个子元素开始计数。                       |
| [:only-of-type](https://www.w3schools.cn/cssref/sel_only-of-type.html) | p:only-of-type        | 选择属于其父元素唯一的 <p> 元素的每个 <p> 元素。           |
| [:only-child](https://www.w3schools.cn/cssref/sel_only-child.html) | p:only-child          | 选择属于其父元素的唯一子元素的每个 <p> 元素。              |
| [:optional](https://www.w3schools.cn/cssref/sel_optional.html) | input:optional        | 选择不带 "required" 属性的 input 元素。                    |
| [:out-of-range](https://www.w3schools.cn/cssref/sel_out-of-range.html) | input:out-of-range    | 选择值超出指定范围的 input 元素。                          |
| [::placeholder](https://www.w3schools.cn/cssref/sel_placeholder.html) | input::placeholder    | 选择已规定 "placeholder" 属性的 input 元素。               |
| [:read-only](https://www.w3schools.cn/cssref/sel_read-only.html) | input:read-only       | 选择已规定 "readonly" 属性的 input 元素。                  |
| [:read-write](https://www.w3schools.cn/cssref/sel_read-write.html) | input:read-write      | 选择未规定 "readonly" 属性的 input 元素。                  |
| [:required](https://www.w3schools.cn/cssref/sel_required.html) | input:required        | 选择已规定 "required" 属性的 input 元素。                  |
| [:root](https://www.w3schools.cn/cssref/sel_root.html)       | :root                 | 选择文档的根元素。                                         |
| [::selection](https://www.w3schools.cn/cssref/sel_selection.html) | ::selection           | 选择用户已选取的元素部分。                                 |
| [:target](https://www.w3schools.cn/cssref/sel_target.html)   | #news:target          | 选择当前活动的 #news 元素。                                |
| [:valid](https://www.w3schools.cn/cssref/sel_valid.html)     | input:valid           | 选择带有有效值的所有 input 元素。                          |
| [:visited](https://www.w3schools.cn/cssref/sel_visited.html) | a:visited             | 选择所有已访问的链接。                                     |



[❮ 上一节](https://www.w3schools.cn/cssref/css3_browsersupport.html)[下一节 ❯](https://www.w3schools.cn/cssref/css_functions.html)

# CSS 函数参考手册

[❮ 上一节](https://www.w3schools.cn/cssref/css_selectors.html)[下一节 ❯](https://www.w3schools.cn/cssref/css_ref_aural.html)

------

## CSS 函数

CSS 函数用作各种CSS属性的值。

| 函数                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [attr()](https://www.w3schools.cn/cssref/func_attr.html)     | 返回所选元素的属性值。                                       |
| [calc()](https://www.w3schools.cn/cssref/func_calc.html)     | 允许您执行计算来确定 CSS 属性值。                            |
| [cubic-bezier()](https://www.w3schools.cn/cssref/func_cubic-bezier.html) | 定义三次贝塞尔曲线。                                         |
| [hsl()](https://www.w3schools.cn/cssref/func_hsl.html)       | 使用色相-饱和度-亮度模型（HSL）定义颜色。                    |
| [hsla()](https://www.w3schools.cn/cssref/func_hsla.html)     | 使用色相-饱和度-亮度-阿尔法模型（HSLA）定义颜色。            |
| [linear-gradient()](https://www.w3schools.cn/cssref/func_linear-gradient.html) | 将线性渐变设置为背景图像。定义至少两种颜色（从上到下）。     |
| [radial-gradient()](https://www.w3schools.cn/cssref/func_radial-gradient.html) | 将径向渐变设置为背景图像。定义至少两种颜色（从中心到边缘）。 |
| [repeating-linear-gradient()](https://www.w3schools.cn/cssref/func_repeating-linear-gradient.html) | 重复线性渐变。                                               |
| [repeating-radial-gradient()](https://www.w3schools.cn/cssref/func_repeating-radial-gradient.html) | 重复径向渐变。                                               |
| [rgb()](https://www.w3schools.cn/cssref/func_rgb.html)       | 使用红-绿-蓝模型（RGB）定义颜色。                            |
| [rgba()](https://www.w3schools.cn/cssref/func_rgba.html)     | 使用红-绿-蓝-阿尔法模型（RGB）定义颜色。                     |
| [var()](https://www.w3schools.cn/cssref/func_var.html)       | 插入自定义属性的值。                                         |



[❮ 上一节](https://www.w3schools.cn/cssref/css_selectors.html)[下一节 ❯](https://www.w3schools.cn/cssref/css_ref_aural.html)

# CSS 听觉参考手册

[❮ 上一节](https://www.w3schools.cn/cssref/css_functions.html)[下一节 ❯](https://www.w3schools.cn/cssref/css_websafe_fonts.html)

------

## 听觉样式表

听觉样式表使用了语音合成和声音效果的结合，让用户收听信息，而不是读取信息。

有声显示可用于：

- 失明人士
- 帮助用户学习阅读
- 帮助具有阅读问题的用户
- 家庭娱乐
- 在车上

听觉呈现通常会把文档转化为纯文本，然后传给屏幕阅读器（可读出屏幕上所有字符的一种程序）。

听觉样式表的一个例子：

h1, h2, h3, h4 {
 voice-family: male;
 richness: 80;
 cue-before: url("beep.au")
}

上面的例子用语音合成器播放声音，开头有一个男性的声音说话。

------

------

## CSS 听觉参考手册

"CSS" 列指示该属性在哪个 CSS 版本中定义（CSS1 或 CSS2）。

| 属性              | 描述                                                         | 值                                                           | CSS  |
| :---------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :--- |
| azimuth           | 设置声音应该来自哪里                                         | *angle* left-side far-left left center-left center center-right right far-right right-side behind leftwards rightwards | 2    |
| cue               | 在一个声明中设置cue属性                                      | *cue-before cue-after*                                       | 2    |
| cue-after         | 指定要播放的声音在一个元素的内容后面                         | none *url*                                                   | 2    |
| cue-before        | 指定要播放的声音在一个元素的内容前面                         | none *url*                                                   | 2    |
| elevation         | 设置声音应该来自哪里                                         | angle below level above higher lower                         | 2    |
| pause             | 在一个声明中设置pause属性                                    | *pause-before pause-after*                                   | 2    |
| pause-after       | 在一个元素的内容之后，指定暂停                               | *time %*                                                     | 2    |
| pause-before      | 在一个元素的内容之前，指定暂停                               | *time %*                                                     | 2    |
| pitch             | 指定讲话声音                                                 | *frequency* x-low low medium high x-high                     | 2    |
| pitch-range       | 指定讲话声音的变化。（单调的声音或动态的声音？）             | *number*                                                     | 2    |
| play-during       | 指定在读一个元素的内容时要播放的声音                         | auto none *url* mix repeat                                   | 2    |
| richness          | 指定丰富的讲话声音。（浑厚的声音或细的声音？）               | *number*                                                     | 2    |
| speak             | 指定内容是否会提供听觉方式                                   | normal none spell-out                                        | 2    |
| speak-header      | 此属性设置或检索表格标题是在所有的单元格之前发声，还是到一个不与之关联的单元格就结束发声。 | always once                                                  | 2    |
| speak-numeral     | 设置或检索数字如何发音。                                     | digits continuous                                            | 2    |
| speak-punctuation | 设置或检索标点字符如何发音                                   | none code                                                    | 2    |
| speech-rate       | 指定发言速度                                                 | *number* x-slow slow medium fast x-fast faster slower        | 2    |
| stress            | 讲话声音在指定的地方"重音"                                   | *number*                                                     | 2    |
| voice-family      | 设置或检索当前声音类型                                       | *specific-voice generic-voice*                               | 2    |
| volume            | 指定发言的音量                                               | *number **% *silent x-soft soft medium loud x-loud           | 2    |



[❮ 上一节](https://www.w3schools.cn/cssref/css_functions.html)[下一节 ❯](https://www.w3schools.cn/cssref/css_websafe_fonts.html)

# CSS 网络安全字体

[❮ 上一节](https://www.w3schools.cn/cssref/css_ref_aural.html)[下一节 ❯](https://www.w3schools.cn/cssref/css_animatable.html)

------

## 常用的字体组合

font-family属性是多种字体的名称，作为一个"应变"制度，以确保浏览器/操作系统之间的最大兼容性。如果浏览器不支持的第一个字体，它尝试下一个的字体。

你想要的字体类型如果浏览器找不到，它会从通用的字体类型中找到与你相似的:

### 实例

p {
 font-family: "Times New Roman", Times, serif;
}

[亲自试一试 »](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_font-family)

下面是一些常用的字体组合，通用的字体系列。

------

## Serif 字体

| 字体                                                 | 文本示例                             |
| :--------------------------------------------------- | :----------------------------------- |
| Georgia, serif                                       | This is a headingThis is a paragraph |
| "Palatino Linotype", "Book Antiqua", Palatino, serif | This is a headingThis is a paragraph |
| "Times New Roman", Times, serif                      | This is a headingThis is a paragraph |

------

------

## Sans-Serif 字体

| 字体                                               | 文本示例                             |
| :------------------------------------------------- | :----------------------------------- |
| Arial, Helvetica, sans-serif                       | This is a headingThis is a paragraph |
| "Arial Black", Gadget, sans-serif                  | This is a headingThis is a paragraph |
| "Comic Sans MS", cursive, sans-serif               | This is a headingThis is a paragraph |
| Impact, Charcoal, sans-serif                       | This is a headingThis is a paragraph |
| "Lucida Sans Unicode", "Lucida Grande", sans-serif | This is a headingThis is a paragraph |
| Tahoma, Geneva, sans-serif                         | This is a headingThis is a paragraph |
| "Trebuchet MS", Helvetica, sans-serif              | This is a headingThis is a paragraph |
| Verdana, Geneva, sans-serif                        | This is a headingThis is a paragraph |

## Monospace 字体

| 字体                                | 文本示例                             |
| :---------------------------------- | :----------------------------------- |
| "Courier New", Courier, monospace   | This is a headingThis is a paragraph |
| "Lucida Console", Monaco, monospace | This is a headingThis is a paragraph |

**提示:** 还可以查看所有可用的 [谷歌字体](https://www.w3schools.cn/howto/howto_google_fonts.html) 以及如何使用它们。



[❮ 上一节](https://www.w3schools.cn/cssref/css_ref_aural.html)[下一节 ❯](https://www.w3schools.cn/cssref/css_animatable.html)

# CSS 动画相关属性

[❮ 上一节](https://www.w3schools.cn/cssref/css_websafe_fonts.html)[下一节 ❯](https://www.w3schools.cn/cssref/css_units.html)

------

## 定义和用法

一些 CSS 属性可用于动画制作，这意味着它们可用于过渡等效果中。

可设置动画的属性可以从一个值逐渐更改为另一个值，例如尺寸、数字、百分比和颜色。

------

## 浏览器支持

表格中的数字注明了完全支持 CSS 动画的首个浏览器版本。

-webkit-、-moz- 或 -o- 后面的数字注明了使用前缀的第一个版本。

|                   |      |                |                  |                             |
| ----------------- | ---- | -------------- | ---------------- | --------------------------- |
| 43.0 4.0 -webkit- | 10.0 | 16.0 5.0 -moz- | 9.0 4.0 -webkit- | 30.0 15.0 -webkit- 12.0 -o- |



### 实例

设置背景颜色从红色到蓝色的动画：

@keyframes mymove {
 from {background-color: red;}
 to {background-color: blue;}
}

[亲自试一试 »](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_animatable)

------

------

## 动画相关属性

下面的表格中列出了 CSS 中的动画相关属性：

| 属性                                                         |
| :----------------------------------------------------------- |
| [background](https://www.w3schools.cn/cssref/css3_pr_background.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_background) |
| [background-color](https://www.w3schools.cn/cssref/pr_background-color.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_background-color) |
| [background-position](https://www.w3schools.cn/cssref/pr_background-position.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_background-position) |
| [background-size](https://www.w3schools.cn/cssref/css3_pr_background-size.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_background-size) |
| [border](https://www.w3schools.cn/cssref/pr_border.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border) |
| [border-bottom](https://www.w3schools.cn/cssref/pr_border-bottom.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-bottom) |
| [border-bottom-color](https://www.w3schools.cn/cssref/pr_border-bottom_color.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-bottom-color) |
| [border-bottom-left-radius](https://www.w3schools.cn/cssref/css3_pr_border-bottom-left-radius.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-bottom-left-radius) |
| [border-bottom-right-radius](https://www.w3schools.cn/cssref/css3_pr_border-bottom-right-radius.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-bottom-right-radius) |
| [border-bottom-width](https://www.w3schools.cn/cssref/pr_border-bottom_width.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-bottom-width) |
| [border-color](https://www.w3schools.cn/cssref/pr_border-color.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-color) |
| [border-left](https://www.w3schools.cn/cssref/pr_border-left.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-left) |
| [border-left-color](https://www.w3schools.cn/cssref/pr_border-left_color.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-left-color) |
| [border-left-width](https://www.w3schools.cn/cssref/pr_border-left_width.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-left-width) |
| [border-right](https://www.w3schools.cn/cssref/pr_border-right.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-right) |
| [border-right-color](https://www.w3schools.cn/cssref/pr_border-right_color.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-right-color) |
| [border-right-width](https://www.w3schools.cn/cssref/pr_border-right_width.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-right-width) |
| [border-spacing](https://www.w3schools.cn/cssref/pr_border-spacing.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-spacing) |
| [border-top](https://www.w3schools.cn/cssref/pr_border-top.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-top) |
| [border-top-color](https://www.w3schools.cn/cssref/pr_border-top_color.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-top-color) |
| [border-top-left-radius](https://www.w3schools.cn/cssref/css3_pr_border-top-left-radius.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-top-left-radius) |
| [border-top-right-radius](https://www.w3schools.cn/cssref/css3_pr_border-top-right-radius.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-top-right-radius) |
| [border-top-width](https://www.w3schools.cn/cssref/pr_border-top_width.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_border-top-width) |
| [bottom](https://www.w3schools.cn/cssref/pr_pos_bottom.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_bottom) |
| [box-shadow](https://www.w3schools.cn/cssref/css3_pr_box-shadow.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_box-shadow) |
| [clip](https://www.w3schools.cn/cssref/pr_pos_clip.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_clip) |
| [color](https://www.w3schools.cn/cssref/pr_text_color.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_color) |
| [column-count](https://www.w3schools.cn/cssref/css3_pr_column-count.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_column-count) |
| [column-gap](https://www.w3schools.cn/cssref/css3_pr_column-gap.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_column-gap) |
| [column-rule](https://www.w3schools.cn/cssref/css3_pr_column-rule.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_column-rule) |
| [column-rule-color](https://www.w3schools.cn/cssref/css3_pr_column-rule-color.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_column-rule-color) |
| [column-rule-width](https://www.w3schools.cn/cssref/css3_pr_column-rule-width.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_column-rule-width) |
| [column-width](https://www.w3schools.cn/cssref/css3_pr_column-width.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_column-width) |
| [columns](https://www.w3schools.cn/cssref/css3_pr_columns.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_columns) |
| [filter](https://www.w3schools.cn/cssref/css3_pr_filter.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_filter) |
| [flex](https://www.w3schools.cn/cssref/css3_pr_flex.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_flex) |
| [flex-basis](https://www.w3schools.cn/cssref/css3_pr_flex-basis.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_flex-basis) |
| [flex-grow](https://www.w3schools.cn/cssref/css3_pr_flex-grow.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_flex-grow) |
| [flex-shrink](https://www.w3schools.cn/cssref/css3_pr_flex-shrink.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_flex-shrink) |
| [font](https://www.w3schools.cn/cssref/pr_font_font.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_font) |
| [font-size](https://www.w3schools.cn/cssref/pr_font_font-size.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_font-size) |
| [font-size-adjust](https://www.w3schools.cn/cssref/css3_pr_font-size-adjust.html) |
| [font-stretch](https://www.w3schools.cn/cssref/css3_pr_font-stretch.html) |
| [font-weight](https://www.w3schools.cn/cssref/pr_font_weight.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_font-weight) |
| [grid](https://www.w3schools.cn/cssref/pr_grid.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid) |
| [grid-area](https://www.w3schools.cn/cssref/pr_grid-area.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-area) |
| [grid-auto-columns](https://www.w3schools.cn/cssref/pr_grid-auto-columns.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-auto-columns) |
| [grid-auto-flow](https://www.w3schools.cn/cssref/pr_grid-auto-flow.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-auto-flow) |
| [grid-auto-rows](https://www.w3schools.cn/cssref/pr_grid-auto-rows.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-auto-rows) |
| [grid-column](https://www.w3schools.cn/cssref/pr_grid-column.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-column) |
| [grid-column-end](https://www.w3schools.cn/cssref/pr_grid-column-end.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-column-end) |
| [grid-column-gap](https://www.w3schools.cn/cssref/pr_grid-column-gap.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-column-gap) |
| [grid-column-start](https://www.w3schools.cn/cssref/pr_grid-column-start.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-column-start) |
| [grid-gap](https://www.w3schools.cn/cssref/pr_grid-gap.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-gap) |
| [grid-row](https://www.w3schools.cn/cssref/pr_grid-row.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-row) |
| [grid-row-end](https://www.w3schools.cn/cssref/pr_grid-row-end.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-row-end) |
| [grid-row-gap](https://www.w3schools.cn/cssref/pr_grid-row-gap.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-row-gap) |
| [grid-row-start](https://www.w3schools.cn/cssref/pr_grid-row-start.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-row-start) |
| [grid-template](https://www.w3schools.cn/cssref/pr_grid-template.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-template) |
| [grid-template-areas](https://www.w3schools.cn/cssref/pr_grid-template-areas.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-template-areas) |
| [grid-template-columns](https://www.w3schools.cn/cssref/pr_grid-template-columns.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-template-columns) |
| [grid-template-rows](https://www.w3schools.cn/cssref/pr_grid-template-rows.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_grid-template-rows) |
| [height](https://www.w3schools.cn/cssref/pr_dim_height.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_height) |
| [left](https://www.w3schools.cn/cssref/pr_pos_left.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_left) |
| [letter-spacing](https://www.w3schools.cn/cssref/pr_text_letter-spacing.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_letter-spacing) |
| [line-height](https://www.w3schools.cn/cssref/pr_dim_line-height.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_line-height) |
| [margin](https://www.w3schools.cn/cssref/pr_margin.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_margin) |
| [margin-bottom](https://www.w3schools.cn/cssref/pr_margin-bottom.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_margin-bottom) |
| [margin-left](https://www.w3schools.cn/cssref/pr_margin-left.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_margin-left) |
| [margin-right](https://www.w3schools.cn/cssref/pr_margin-right.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_margin-right) |
| [margin-top](https://www.w3schools.cn/cssref/pr_margin-top.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_margin-top) |
| [max-height](https://www.w3schools.cn/cssref/pr_dim_max-height.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_max-height) |
| [max-width](https://www.w3schools.cn/cssref/pr_dim_max-width.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_max-width) |
| [min-height](https://www.w3schools.cn/cssref/pr_dim_min-height.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_min-height) |
| [min-width](https://www.w3schools.cn/cssref/pr_dim_min-width.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_min-width) |
| [object-position](https://www.w3schools.cn/cssref/css3_pr_object-position.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_object-position) |
| [opacity](https://www.w3schools.cn/cssref/css3_pr_opacity.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_opacity) |
| [order](https://www.w3schools.cn/cssref/css3_pr_order.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_order) |
| [outline](https://www.w3schools.cn/cssref/pr_outline.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_outline) |
| [outline-color](https://www.w3schools.cn/cssref/pr_outline-color.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_outline-color) |
| [outline-offset](https://www.w3schools.cn/cssref/css3_pr_outline-offset.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_outline-offset) |
| [outline-width](https://www.w3schools.cn/cssref/pr_outline-width.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_outline-width) |
| [padding](https://www.w3schools.cn/cssref/pr_padding.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_padding) |
| [padding-bottom](https://www.w3schools.cn/cssref/pr_padding-bottom.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_padding-bottom) |
| [padding-left](https://www.w3schools.cn/cssref/pr_padding-left.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_padding-left) |
| [padding-right](https://www.w3schools.cn/cssref/pr_padding-right.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_padding-right) |
| [padding-top](https://www.w3schools.cn/cssref/pr_padding-top.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_padding-top) |
| [perspective](https://www.w3schools.cn/cssref/css3_pr_perspective.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_perspective) |
| [perspective-origin](https://www.w3schools.cn/cssref/css3_pr_perspective-origin.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_perspective-origin) |
| [right](https://www.w3schools.cn/cssref/pr_pos_right.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_right) |
| [text-decoration-color](https://www.w3schools.cn/cssref/css3_pr_text-decoration-color.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_text-decoration-color) |
| [text-indent](https://www.w3schools.cn/cssref/pr_text_text-indent.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_text-indent) |
| [text-shadow](https://www.w3schools.cn/cssref/css3_pr_text-shadow.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_text-shadow) |
| [top](https://www.w3schools.cn/cssref/pr_pos_top.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_top) |
| [transform](https://www.w3schools.cn/cssref/css3_pr_transform.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_transform) |
| [transform-origin](https://www.w3schools.cn/cssref/css3_pr_transform-origin.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_transform-origin) |
| [vertical-align](https://www.w3schools.cn/cssref/pr_pos_vertical-align.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_vertical-align) |
| [visibility](https://www.w3schools.cn/cssref/pr_class_visibility.html) |
| [width](https://www.w3schools.cn/cssref/pr_dim_width.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_width) |
| [word-spacing](https://www.w3schools.cn/cssref/pr_text_word-spacing.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_word-spacing) |
| [z-index](https://www.w3schools.cn/cssref/pr_pos_z-index.html)[测试一下](https://www.w3schools.cn/cssref/tryit.asp?filename=trycss_anim_z-index) |





[❮ 上一节](https://www.w3schools.cn/cssref/css_websafe_fonts.html)[下一节 ❯](https://www.w3schools.cn/cssref/css_units.html)

# CSS 单位

[❮ 上一节](https://www.w3schools.cn/cssref/css_animatable.html)[下一节 ❯](https://www.w3schools.cn/cssref/css_pxtoemconversion.html)

------

## CSS 单位

CSS 有几种表示长度的不同单位。

许多 CSS 属性接受"长度"值，诸如 width、margin、padding、font-size 等。

长度是一个后面跟着长度单位的数字，诸如 `10px`、`2em` 等。

数字和单位之间不能出现空格。但是，如果值为 0，则可以省略单位。

对于某些 CSS 属性，允许使用负的长度。

长度单位有两种类型：*绝对单位*和*相对单位*。

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
视口（Viewport）= 浏览器窗口的尺寸。如果视口宽 50 里面，则 1vw = 0.5cm。

------

------

## 浏览器支持

表格中的数字注明了完全支持该长度单位的首个浏览器版本。

| Length Unit                       |      |      |      |      |      |
| :-------------------------------- | ---- | ---- | ---- | ---- | ---- |
| em, ex, %, px, cm, mm, in, pt, pc | 1.0  | 3.0  | 1.0  | 1.0  | 3.5  |
| ch                                | 27.0 | 9.0  | 1.0  | 7.0  | 20.0 |
| rem                               | 4.0  | 9.0  | 3.6  | 4.1  | 11.6 |
| vh, vw                            | 20.0 | 9.0  | 19.0 | 6.0  | 20.0 |
| vmin                              | 20.0 | 12.0 | 19.0 | 6.0  | 20.0 |
| vmax                              | 26.0 | 16.0 | 19.0 | 7.0  | 20.0 |

------

[❮ 上一节](https://www.w3schools.cn/cssref/css_animatable.html)[下一节 ❯](https://www.w3schools.cn/cssref/css_pxtoemconversion.html)





