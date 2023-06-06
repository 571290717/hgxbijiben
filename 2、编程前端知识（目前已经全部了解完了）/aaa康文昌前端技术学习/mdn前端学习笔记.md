# mdn前端学习笔记

*设计网站外观？* 在为网站编写代码之前必须进行规划和设计工作，包括“网站提供什么信息？”、“想要什么字体和颜色？”、“网站是做什么的？”

## [第一步：计划](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/What_will_your_website_look_like#第一步：计划)

1. **网站的主题是什么？** 你喜欢狗、上海、还是吃豆人？
2. **基于所选主题要展示哪些信息？** 写下标题和几段文字，构思一个用于展示的图像。
3. **网站采用怎样的外观？** 用高阶术语来说，背景颜色是什么？使用哪种字体比较合适：正式的、卡通的、粗体、瘦体？

## [绘制草图](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/What_will_your_website_look_like#绘制草图)

![img](image/website-drawing-scan.png)





后面就是写内容

写文本标题

主题颜色

图像

字体



[网站应该使用什么结构？](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/Dealing_with_files#网站应该使用什么结构？)

1. **`index.html`**：这个文件一般会包含主页内容，也就是人们第一次进入网站时看到的文字和图片。使用文本编辑器，创建一个名为`index.html`的新文件，并将其保存在`test-site`文件夹内。
2. **`images` 文件夹**：这个文件夹包含网站上使用的所有图片。在 `test-site` 文件夹内创建一个名为 `images` 的文件夹。
3. **`styles` 文件夹**：这个文件夹包含用于设置内容样式的 CSS 代码（例如，设置文本和背景颜色）。在你的 `test-site` 文件夹内创建一个名为 `styles` 的文件夹。
4. **`scripts` 文件夹**：这个文件夹包含所有用于向网站添加交互功能的 JavaScript 代码（例如，点击时加载数据的按钮）。在 `test-site` 文件夹内创建一个名为 `scripts` 的文件夹。

```
 <img src="" alt="My test image">
 
 
```

[HTML 元素详解](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/HTML_basics#html_元素详解)

1. **开始标签**（Opening tag）：包含元素的名称（本例为 p），被大于号、小于号所包围。表示元素从这里开始或者开始起作用 —— 在本例中即段落由此开始。
2. **结束标签**（Closing tag）：与开始标签相似，只是其在元素名之前包含了一个斜杠。这表示着元素的结尾 —— 在本例中即段落在此结束。初学者常常会犯忘记包含结束标签的错误，这可能会产生一些奇怪的结果。
3. **内容**（Content）：元素的内容，本例中就是所输入的文本本身。
4. **元素**（Element）：开始标签、结束标签与内容相结合，便是一个完整的元素。





### [嵌套元素](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/HTML_basics#嵌套元素)



```
<p>My cat is <strong>very</strong> grumpy.</p>
```



必须保证元素嵌套次序正确



### [空元素](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/HTML_basics#空元素)

不包含任何内容的元素称为空元素。比如 [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img) 元素：

```
<img src="images/firefox-icon.png" alt="My test image" />
```







- `<!DOCTYPE html>` — 文档类型。混沌初分，HTML 尚在襁褓（大约是 1991/92 年）之时，`DOCTYPE` 用来链接一些 HTML 编写守则，比如自动查错之类。`DOCTYPE` 在当今作用有限，仅用于保证文档正常读取。现在知道这些就足够了。
- `<html></html>` — [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/html) 元素。该元素包含整个页面的内容，也称作根元素。
- `<head></head>` — [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/head) 元素。该元素的内容对用户不可见，其中包含例如面向搜索引擎的搜索关键字（[keywords](https://developer.mozilla.org/zh-CN/docs/Glossary/Keyword)）、页面描述、CSS 样式表和字符编码声明等。
- `<meta charset="utf-8">` — 该元素指定文档使用 UTF-8 字符编码，UTF-8 包括绝大多数人类已知语言的字符。基本上 UTF-8 可以处理任何文本内容，还可以避免以后出现某些问题，没有理由再选用其他编码。
- `<title></title>` — [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/title) 元素。该元素设置页面的标题，显示在浏览器标签页上，也作为收藏网页的描述文字。
- `<body></body>` — [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/body) 元素。该元素包含期望让用户在访问页面时看到的内容，包括文本、图像、视频、游戏、可播放的音轨或其他内容。



## [图像](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/HTML_basics#图像)

重温一下 [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img) 元素：

```
<img src="images/firefox-icon.png" alt="My test image" />
```





### [标题（Heading）](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/HTML_basics#标题（heading）)

标题元素可用于指定内容的标题和子标题。就像一本书的书名、每章的大标题、小标题，等。HTML 文档也是一样。HTML 包括六个级别的标题， [`` (en-US)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements)–[`` (en-US)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) ，一般最多用到 3-4 级标题。

```
<h1>主标题</h1>
<h2>顶层标题</h2>
<h3>子标题</h3>
<h4>次子标题</h4>
```



### [列表（List）](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/HTML_basics#列表（list）)

Web 上的许多内容都是列表，HTML 有一些特别的列表元素。标记列表通常包括至少两个元素。最常用的列表类型为：

1. **无序列表**（Unordered List）中项目的顺序并不重要，就像购物列表。用一个 [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/ul) 元素包围。
2. **有序列表**（Ordered List）中项目的顺序很重要，就像烹调指南。用一个 [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/ol) 元素包围。



```
<p>At Mozilla, we're a global community of</p>

<ul>
  <li>technologists</li>
  <li>thinkers</li>
  <li>builders</li>
</ul>

<p>working together… </p>
```



## [链接](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/HTML_basics#链接)

链接非常重要 — 它们赋予 Web 网络属性。要植入一个链接，我们需要使用一个简单的元素 — [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a) — a 是 "anchor" （锚）的缩写。要将一些文本添加到链接中，只需如下几步：

1. 选择一些文本。比如“Mozilla Manifesto”。

2. 将文本包含在

    

   `<a>`

    

   元素内，就像这样：

   ```
   <a>Mozilla Manifesto</a>
   ```

   Copy to Clipboard

3. 为此

    

   `<a>`

    

   元素添加一个

    

   ```
   href
   ```

    

   属性，就像这样：

   ```
   <a href="">Mozilla Manifesto</a>
   ```

   Copy to Clipboard

4. 把属性的值设置为所需网址：

   ```
   <a href="https://www.mozilla.org/zh-CN/about/manifesto/">Mozilla Manifesto</a>
   ```



# CSS 基础



```
p {
  color: red;
}
```

打开 `index.html` 文件，然后将下面一行粘贴到文档头部（也就是 [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/head) 和 `</head>` 标签之间）。

```
<link href="styles/style.css" rel="stylesheet" />
```

| 选择器名称                           | 选择的内容                                                   | 示例                                                         |
| :----------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 元素选择器（也称作标签或类型选择器） | 所有指定类型的 HTML 元素                                     | `p` 选择 `<p>`                                               |
| ID 选择器                            | 具有特定 ID 的元素。单一 HTML 页面中，每个 ID 只对应一个元素，一个元素只对应一个 ID | `#my-id` 选择 `<p id="my-id">` 或 `<a id="my-id">`           |
| 类选择器                             | 具有特定类的元素。单一页面中，一个类可以有多个实例           | `.my-class` 选择 `<p class="my-class">` 和 `<a class="my-class">` |
| 属性选择器                           | 拥有特定属性的元素                                           | `img[src]` 选择 `<img src="myimage.png">` 但不是 `<img>`     |
| 伪类选择器                           | 特定状态下的特定元素（比如鼠标指针悬停于链接之上）           | `a:hover` 选择仅在鼠标指针悬停在链接上时的 `<a>` 元素        |

```
<link
  href="https://fonts.googleapis.com/css?family=Open+Sans"
  rel="stylesheet" />
```

Copy to Clipboard

这段代码将你的页面链接到一个样式表，该样式表将 Open Sans 字体家族与你的网页一起加载。

```
html {
  font-size: 10px; /* px 表示“像素（pixel）”: 基础字号为 10 像素 */
  font-family: "Open Sans", sans-serif; /* 这应该是你从 Google Fonts 得到的其余输出。 */
}
```

- `width`：元素的宽度
- `background-color`：元素内容和内边距底下的颜色
- `color`：元素内容（通常是文本）的颜色
- `text-shadow`：为元素内的文本设置阴影
- `display`：设置元素的显示模式（继续阅读文章以了解更多细节）

### [文档体样式](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/CSS_basics#文档体样式)

```
body {
  width: 600px;
  margin: 0 auto;
  background-color: #ff9500;
  padding: 0 20px 20px 20px;
  border: 5px solid black;
}
```



这里有对于 [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/body) 元素的几条声明，我们来逐条查看：

- `width: 600px;` 强制页面永远保持 600 像素宽。
- `margin: 0 auto;` 当你在 `margin` 或 `padding` 这样的属性上设置两个值时，第一个值影响元素的*上下*方向（在这个例子中设置为 `0`）；第二个值影响*左右*方向。(这里，`auto` 是一个特殊的值，它将可用的水平空间平均分配给左和右）。如 [Margin 语法](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin#语法)中所记载的那样，你也可以使用一个、两个、三个或四个值。
- `background-color: #FF9500;` 如前文所述，指定元素的背景颜色。我们给 body 用了一种略微偏红的橘色以与深蓝色的 [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/html) 元素形成反差，你也可以尝试其他颜色。
- `padding: 0 20px 20px 20px;` 我们给内边距设置了四个值来让内容四周产生一点空间。这一次我们不设置上方的内边距，设置右边，下方，左边的内边距为 20 像素。值以上、右、下、左的顺序排列。与 `margin` 一样，你也可以像 [Padding 语法](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding#语法)中所记载的那样，使用一个、两个、三个或四个值。
- `border: 5px solid black;` 这是为边框的宽度、样式和颜色设置的值。在本例中，它是一个在主体的所有侧面的 5 像素宽的纯黑色边框。

### [定位页面主标题并添加样式](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/CSS_basics#定位页面主标题并添加样式)



```
h1 {
  margin: 0;
  padding: 20px 0;
  color: #00539f;
  text-shadow: 3px 3px 1px black;
}
```

### [图像居中](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/CSS_basics#图像居中)

```
img {
  display: block;
  margin: 0 auto;
}
```

# JavaScript 基础

交互

下一步，在 `index.html` 文件</body> 标签前的新行添加以下代码。

```
<script src="scripts/main.js" defer></script>
```

现在将以下代码添加到 `main.js` 文件中：

```
let myHeading = document.querySelector('h1');
myHeading.textContent = 'Hello world!';
```

### [变量（Variable）](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/JavaScript_basics#变量（variable）)

```
let myVariable;
```

变量定义后可以进行赋值：

```
myVariable = '李雷';
```

Copy to Clipboard

也可以将定义、赋值操作写在同一行：

```
let myVariable = '李雷';
```

Copy to Clipboard

可以直接通过变量名取得变量的值：

```
myVariable;
```

Copy to Clipboard

变量在赋值后是可以更改的：

```
let myVariable = '李雷';
myVariable = '韩梅梅';
```

注意变量可以有不同的 [数据类型](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Data_structures) ：

| 变量                                                         | 解释                                                         | 示例                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| [String](https://developer.mozilla.org/zh-CN/docs/Glossary/String) | 字符串（一串文本）：字符串的值必须用引号（单双均可，必须成对）括起来。 | `let myVariable = '李雷';`                                   |
| [Number](https://developer.mozilla.org/zh-CN/docs/Glossary/Number) | 数字：无需引号。                                             | `let myVariable = 10;`                                       |
| [Boolean](https://developer.mozilla.org/zh-CN/docs/Glossary/Boolean) | 布尔值（真 / 假）： `true`/`false` 是 JS 里的特殊关键字，无需引号。 | `let myVariable = true;`                                     |
| [Array](https://developer.mozilla.org/zh-CN/docs/Glossary/Array) | 数组：用于在单一引用中存储多个值的结构。                     | `let myVariable = [1, '李雷', '韩梅梅', 10];` 元素引用方法：`myVariable[0]`, `myVariable[1]` …… |
| [Object](https://developer.mozilla.org/zh-CN/docs/Glossary/Object) | 对象：JavaScript 里一切皆对象，一切皆可储存在变量里。这一点要牢记于心。 | `let myVariable = document.querySelector('h1');` 以及上面所有示例都是对象。 |

| 运算符     | 解释                                                         | 符号          | 示例                                                         |
| :--------- | :----------------------------------------------------------- | :------------ | :----------------------------------------------------------- |
| 加         | 将两个数字相加，或拼接两个字符串。                           | `+`           | `6 + 9;"Hello " + "world!";`                                 |
| 减、乘、除 | 这些运算符操作与基础算术一致。只是乘法写作星号，除法写作斜杠。 | `-`, `*`, `/` | `9 - 3;8 * 2; //乘法在 JS 中是一个星号9 / 3;`                |
| 赋值运算符 | 为变量赋值（你之前已经见过这个符号了）                       | `=`           | `let myVariable = '李雷';`                                   |
| 等于       | 测试两个值是否相等，并返回一个 `true`/`false` （布尔）值。   | `===`         | `let myVariable = 3;myVariable === 4; // false`              |
| 不等于     | 和等于运算符相反，测试两个值是否不相等，并返回一个 `true`/`false` （布尔）值。 | `!==`         | `let myVariable = 3;myVariable !== 3; // false`              |
| 取非       | 返回逻辑相反的值，比如当前值为真，则返回 `false`。           | `!`           | 原式为真，但经取非后值为 `false`： `let myVariable = 3;!(myVariable === 3); // false` |

运算符种类远不止这些，不过目前上表已经够用了。完整列表请参阅 [表达式和运算符](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators)。

**备注：** 不同类型数据之间的计算可能出现奇怪的结果，因此必须正确引用变量，才能得出预期结果。比如在控制台输入 `"35" + "25"`，为什么不能得到 `60`？因为引号将数字转换成了字符串，所以结果是连接两个字符串而不是把两个数字相加。输入 `35 + 25` 才能得到正确结果。

### [条件语句](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/JavaScript_basics#条件语句)

条件语句是一种代码结构，用来测试表达式的真假，并根据测试结果运行不同的代码。一个常用的条件语句是 `if ... else`。下面是一个示例：

```
let iceCream = 'chocolate';
if (iceCream === 'chocolate') {
  alert('我最喜欢巧克力冰激淋了。');
} else {
  alert('但是巧克力才是我的最爱呀……');
}
```



### [函数（Function）](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/JavaScript_basics#函数（function）)

[函数](https://developer.mozilla.org/zh-CN/docs/Glossary/Function) 用来封装可复用的功能。如果没有函数，一段特定的操作过程用几次就要重复写几次，而使用函数则只需写下函数名和一些简短的信息。之前已经涉及过一些函数，比如：

```
let myVariable = document.querySelector('h1');
```

Copy to Clipboard

```
alert('hello!');
```



```
function multiply(num1, num2) {
  let result = num1 * num2;
  return result;
}
```

Copy to Clipboard

尝试在控制台运行这个函数，不妨多试几组参数，比如：

```
multiply(4, 7);
multiply(20, 20);
multiply(0.5, 3);
```



### [事件](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/JavaScript_basics#事件)

事件能为网页添加真实的交互能力。它可以捕捉浏览器操作并运行一些代码做为响应。最简单的事件是[点击事件](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/click_event)，鼠标的点击操作会触发该事件。可尝试将下面的代码输入到控制台，然后点击页面的任意位置：

```
document.querySelector("html").addEventListener("click", function () {
  alert("别戳我，我怕疼。");
});
```

### [事件](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/JavaScript_basics#事件)

事件能为网页添加真实的交互能力。它可以捕捉浏览器操作并运行一些代码做为响应。最简单的事件是[点击事件](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/click_event)，鼠标的点击操作会触发该事件。可尝试将下面的代码输入到控制台，然后点击页面的任意位置：

```
document.querySelector("html").addEventListener("click", function () {
  alert("别戳我，我怕疼。");
});
```



```
document.querySelector('html').addEventListener('click', () => {
  alert('别戳我，我怕疼。');
});
```



打开 `main.js` 文件，输入下面的 JavaScript 代码 ( 请删除刚才的 "hello world" 脚本)：

```
let myImage = document.querySelector('img');

myImage.onclick = function() {
    let mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/firefox-icon.png') {
      myImage.setAttribute('src', 'images/firefox2.png');
    } else {
      myImage.setAttribute('src', 'images/firefox-icon.png');
    }
}
```





### [添加个性化欢迎信息](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/JavaScript_basics#添加个性化欢迎信息)

下面来添加另一段代码，在用户初次进入站点时将网页的标题改成一段个性化欢迎信息（即在标题中添加用户的名字）。名字信息会由 [Web Storage API](https://developer.mozilla.org/zh-CN/docs/Web/API/Web_Storage_API) 保存下来，即使用户关闭页面之后再重新打开，仍可得到之前的信息。还会添加一个选项，可以根据需要改变用户名字以更新欢迎信息。

1. 打开

    

   ```
   index.html
   ```

   ，在

    

   `<script>`

    

   标签

   前

   添加以下代码，将在页面底部显示一个“切换用户”字样的按钮：

   ```
   <button>切换用户</button>
   ```

   Copy to Clipboard

2. 将以下 JavaScript 代码原封不动添加到

    

   ```
   main.js
   ```

    

   文件底部，将获取新按钮和标题的引用，并保存至变量中：

   ```
   let myButton = document.querySelector('button');
   let myHeading = document.querySelector('h1');
   ```

   Copy to Clipboard

3. 然后添加以下函数来设置个性化欢迎信息。（函数需要在调用后生效，下文中提供了两种对该函数的调用方式）

   ```
   function setUserName() {
     let myName = prompt('请输入你的名字。');
     localStorage.setItem('name', myName);
     myHeading.textContent = 'Mozilla 酷毙了，' + myName;
   }
   ```

   Copy to Clipboard

   该函数首先调用了

    

   `prompt()`

    

   函数，与

    

   ```
   alert()
   ```

    

   类似会弹出一个对话框。但是这里需要用户输入数据，并在确定后将数据存储在

    

   ```
   myName
   ```

    

   变量里。接下来将调用

    

   `localStorage`

    

   API，它可以将数据存储在浏览器中供后续获取。这里用

    

   ```
   localStorage
   ```

    

   的

    

   ```
   setItem()
   ```

    

   函数来创建一个

   ```
   'name'
   ```

    

   数据项，并把

    

   ```
   myName
   ```

    

   变量复制给它。最后将

    

   ```
   textContent
   ```

    

   属性设置为一个欢迎字符串加上这个新设置的名字。

4. 接下来，添加以下的

    

   ```
   if ... else
   ```

    

   块。我们可以称之为初始化代码，因为它在页面初次读取时进行构造工作：

   ```
   if(!localStorage.getItem('name')) {
     setUserName();
   } else {
     let storedName = localStorage.getItem('name');
     myHeading.textContent = 'Mozilla 酷毙了，' + storedName;
   }
   ```

   Copy to Clipboard

   这里首次使用了取非运算符（逻辑非，用

    

   ```
   !
   ```

    

   表示）来检测

    

   ```
   'name'
   ```

    

   数据是否存在。若不存在，调用

    

   ```
   setUserName()
   ```

    

   创建。若存在（即用户上次访问时设置过），调用

    

   ```
   getItem()
   ```

    

   获取保存的名字，像上文的

    

   ```
   setUserName()
   ```

    

   那样设置

    

   ```
   textContent
   ```

   。

5. 最后，为按钮设置 onclick 事件处理器。按钮按下时运行 setUserName() 函数。这样用户就可以通过按这个按钮来自由设置新名字了：

   ```
   myButton.onclick = function() {
      setUserName();
   }
   ```

   Copy to Clipboard

第一次访问网页时，页面将询问用户名并发出一段个性化的信息。可随时点击按钮来改变用户名。告诉你一个额外的福利，因为用户名是保存在 `localStorage` 里的，网页关闭后也不会丢失，所以重新打开浏览器时所设置的名字信息将依然存在:)



## [客户端和服务器](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/How_the_Web_works#客户端和服务器)

连接到互联网的计算机被称作客户端和服务器。下面是一个简单描述它们如何交互的图表：

![Two circles representing client and server. An arrow labelled request is going from client to server, and an arrow labelled responses is going from server to client](image/simple-client-server.png)

- 客户端是典型的 Web 用户入网设备（比如，你连接了 Wi-Fi 的电脑，或接入移动网络的手机）和设备上可联网的软件（通常使用像 Firefox 和 Chrome 的浏览器）。
- 服务器是存储网页，站点和应用的计算机。当一个客户端设备想要获取一个网页时，一份网页的拷贝将从服务器上下载到客户端机器上来在用户浏览器上显示。









https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/How_the_Web_works



















