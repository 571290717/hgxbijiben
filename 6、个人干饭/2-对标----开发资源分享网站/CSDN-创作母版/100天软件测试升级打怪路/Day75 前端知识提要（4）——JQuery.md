# Day75 前端知识提要（4）——JQuery



# jQuery的介绍

**学习目标**

- 能够知道jQuery的作用及优点

------

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



# jQuery的用法

**学习目标**

- 能够知道jQuery的引入方式
- 能够说出两种jQuery入口函数的写法

------

### 1. jQuery的引入

```js
<script src="js/jquery-1.12.4.min.js"></script>
```

### 2. jQuery的入口函数

我们知道使用js获取标签元素，需要页面加载完成以后再获取，我们通过给onload事件属性设置了一个函数来获取标签元素，而jquery提供了**ready函数**来解决这个问题，保证获取标签元素没有问题，**它的速度比原生的 window.onload 更快**。

**入口函数示例代码:**

```js
<script src="js/jquery-1.12.4.min.js"></script>
<script>
    window.onload = function(){
        var oDiv = document.getElementById('div01');
        alert('原生就是获取的div：' + oDiv);
    };
    $(document).ready(function(){
        var $div = $('#div01');
        alert('jquery获取的div：' + $div);
    });
</script>

<div id="div01">这是一个div</div>
```

**入口函数的简写示例代码:**

```js
<script src="js/jquery-1.12.4.min.js"></script>
<script>
    window.onload = function(){
        var oDiv = document.getElementById('div01');
        alert('原生就是获取的div：' + oDiv);
    };

    /*
    $(document).ready(function(){
        var $div = $('#div01');
        alert('jquery获取的div：' + $div);
    });
    */

    // 上面ready的写法可以简写成下面的形式：
    $(function(){
        var $div = $('#div01');
        alert('jquery获取的div：' + $div);
    }); 
</script>

<div id="div01">这是一个div</div>
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



# jQuery选择器

**学习目标**

- 能够使用jQuery选择器获取标签元素

------

### 1. jQuery选择器的介绍

jquery选择器就是快速选择标签元素，获取标签的，选择规则和css样式一样。

### 2. jQuery选择器的种类

1. 标签选择器
2. 类选择器
3. id选择器
4. 层级选择器
5. 属性选择器

**示例代码:**

```js
$('#myId') //选择id为myId的标签
$('.myClass') // 选择class为myClass的标签
$('li') //选择所有的li标签
$('#ul1 li span') //选择id为ul1标签下的所有li标签下的span标签
$('input[name=first]') // 选择name属性等于first的input标签
```

**说明:**
可以使用length属性来判断标签是否选择成功, 如果length大于0表示选择成功，否则选择失败。

```js
$(function(){
    result = $("div").length;
    alert(result);
});
```

### 3. 小结

- jQuery选择器就是选择标签的
- 标签选择器是**根据标签名来选择标签**
- 类选择器是**根据类名来选择标签**
- id选择器是**根据id来选择标签**
- 层级选择器是**根据层级关系来选择标签**
- 属性选择器是**根据属性名来选择标签**



# 选择集过滤

**学习目标**

- 能够使用选择器进行标签过滤

------

### 1. 选择集过滤的介绍

选择集过滤就是在选择标签的集合里面过滤自己需要的标签

### 2. 选择集过滤的操作

- has(选择器名称)方法，表示选取包含指定选择器的标签
- eq(索引)方法，表示选取指定索引的标签

**has方法的示例代码:**

```js
<script>
    $(function(){
        //  has方法的使用
        var $div = $("div").has("#mytext");
        //  设置样式
        $div.css({"background":"red"});
    });
</script>

<div>
    这是第一个div
    <input type="text" id="mytext">
</div>

<div>
    这是第二个div
    <input type="text">
    <input type="button">
</div>
```

**eq方法的示例代码:**

```js
<script>
    $(function(){
        //  has方法的使用
        var $div = $("div").has("#mytext");
        //  设置样式
        $div.css({"background":"red"});

        //  eq方法的使用
        var $div = $("div").eq(1);
        //  设置样式
        $div.css({"background":"yellow"});
    });
</script>

<div>
    这是第一个div
    <input type="text" id="mytext">
</div>

<div>
    这是第二个div
    <input type="text">
    <input type="button">
</div>
```

### 3. 小结

- 选择集过滤可以使用has方法和eq方法来完成
- jquery给标签设置样式使用css方法

# 选择集转移

**学习目标**

- 能够说出2种选择集转移方法

------

### 1. 选择集转移介绍

选择集转移就是以选择的标签为参照，然后获取转移后的标签

### 2. 选择集转移操作

- $('#box').prev(); 表示选择id是box元素的上一个的同级元素
- $('#box').prevAll(); 表示选择id是box元素的上面所有的同级元素
- $('#box').next(); 表示选择id是box元素的下一个的同级元素
- $('#box').nextAll(); 表示选择id是box元素的下面所有的同级元素
- $('#box').parent(); 表示选择id是box元素的父元素
- $('#box').children(); 表示选择id是box元素的所有子元素
- $('#box').siblings(); 表示选择id是box元素的其它同级元素
- $('#box').find('.myClass'); 表示选择id是box元素的class等于myClass的元素

**选择集转移的示例代码:**

```js
<script>
    $(function(){
        var $div = $('#div01');

        $div.prev().css({'color':'red'});
        $div.prevAll().css({'text-indent':50});
        $div.next().css({'color':'blue'});
        $div.nextAll().css({'text-indent':80});
        $div.siblings().css({'text-decoration':'underline'})
        $div.parent().css({'background':'gray'});
        $div.children().css({'color':'red'});
        $div.find('.sp02').css({'font-size':30});
    });  
</script>

<div>
    <h2>这是第一个h2标签</h2>
    <p>这是第一个段落</p>
    <div id="div01">这是一个<span>div</span><span class="sp02">第二个span</span></div>
    <h2>这是第二个h2标签</h2>
    <p>这是第二个段落</p>
</div>
```

### 3. 小结

- prev() 表示获取上一个同级元素
- prevAll() 表示获取上面所有同级元素
- next() 表示获取下一个同级元素
- nextAll() 表示获取下面所有同级元素
- parent() 表示获取父元素
- children() 表示获取所有的子元素
- siblings() 表示获取其它同级元素
- find("选择器名称") 表示获取指定选择器的元素

# 获取和设置元素内容

**学习目标**

- 能够知道获取和设置元素内容的操作

------

### 1. html方法的使用

jquery中的html方法可以获取和设置标签的html内容

**示例代码:**

```js
<script>
    $(function(){

        var $div = $("#div1");
        //  获取标签的html内容
        var result = $div.html();
        alert(result);
        //  设置标签的html内容，之前的内容会清除
        $div.html("<span style='color:red'>你好</span>");
        //  追加html内容
        $div.append("<span style='color:red'>你好</span>");

    });
</script>

<div id="div1">
    <p>hello</p>
</div>
```

**说明:**

给指定标签追加html内容使用**append方法**

### 2. 小结

- 获取和设置元素的内容使用: html方法
- 给指定元素追加html内容使用: append方法

# 获取和设置元素属性

**学习目标**

- 能够知道获取和设置元素属性的操作

------

### 1. prop方法的使用

之前使用css方法可以给标签设置样式属性，那么设置标签的其它属性可以使用prop方法了。

**示例代码:**

```js
<style>
    .a01{
        color:red;
    }
</style>

<script>
    $(function(){
        var $a = $("#link01");
        var $input = $('#input01')

        // 获取元素属性
        var sId = $a.prop("id");
        alert(sId);

        // 设置元素属性
        $a.prop({"href":"http://www.baidu.com","title":'这是去到百度的链接',"class":"a01"});

        //  获取value属性
        // var sValue = $input.prop("value");
        // alert(sValue);

        // 获取value属性使用val()方法的简写方式
        var sValue = $input.val();
        alert(sValue);
        // 设置value值
        $input.val("222222");
    })
</script>

<a id="link01">这是一个链接</a>
<input type="text" id="input01" value="111111">
```

**说明:** 获取value属性和设置value属性还可以通过**val方法**来完成。

### 2. 小结

- 获取和设置元素属性的操作可以通过prop方法来完成
- 获取和设置元素的value属性可以通过val方法来完成，更加简单和方便

# jQuery事件

**学习目标**

- 能够说出两个常用的jQuery事件

------

### 1. 常用事件

- click() 鼠标单击
- blur() 元素失去焦点
- focus() 元素获得焦点
- mouseover() 鼠标进入（进入子元素也触发）
- mouseout() 鼠标离开（离开子元素也触发）
- ready() DOM加载完成

**示例代码:**

```js
<script>
    $(function(){
        var $li = $('.list li');
        var $button = $('#button1')
        var $text = $("#text1");
        var $div = $("#div1")

        //  鼠标点击
        $li.click(function(){             
            // this指的是当前发生事件的对象，但是它是一个原生js对象
            // this.style.background = 'red';

            // $(this) 指的是当前发生事件的jquery对象
            $(this).css({'background':'gold'});
            // 获取jquery对象的索引值,通过index() 方法
            alert($(this).index());
        });

        //  一般和按钮配合使用
        $button.click(function(){
            alert($text.val());
        });

        //  获取焦点
        $text.focus(function(){
            $(this).css({'background':'red'});

        });

        //  失去焦点
        $text.blur(function(){
            $(this).css({'background':'white'});

        });

        //  鼠标进入
        $div.mouseover(function(){
            $(this).css({'background':'gold'});

        });

        //  鼠标离开
        $div.mouseout(function() {
            $(this).css({'background':'white'});
        });
    });
</script>

<div id="div1">
    <ul class="list">
        <li>列表文字</li>
        <li>列表文字</li>
        <li>列表文字</li>
    </ul>

    <input type="text" id="text1">
    <input type="button" id="button1" value="点击">
</div>
```

**说明:**

- this指的是当前发生事件的对象，但是它是一个原生js对象
- $(this) 指的是当前发生事件的jquery对象

### 2. 小结

jQuery常用事件:

- click() 鼠标单击
- blur() 元素失去焦点
- focus() 元素获得焦点
- mouseover() 鼠标进入（进入子元素也触发）
- mouseout() 鼠标离开（离开子元素也触发）
- ready() DOM加载完成

# 事件代理

**学习目标**

- 能够知道事件代理的使用方式

------

### 1. 事件代理介绍

事件代理就是利用事件冒泡的原理(事件冒泡就是事件会向它的父级一级一级传递),把事件加到父级上，通过判断事件来源，执行相应的子元素的操作，**事件代理首先可以极大减少事件绑定次数，提高性能；其次可以让新加入的子元素也可以拥有相同的操作**。

**事件冒泡代码:**

```js
 <script>
    $(function(){

        var $div1 = $('#div1');
        var $div2 = $('#div2');

        $div1.click(function(){
            alert($(this).html());
        }); 

        $div2.click(function(){
            alert($(this).html());
        }); 
    });
</script>

 <div id="div1" style="width:200px; height:200px; background: red;">
    <div id="div2" style="width:100px; height:100px;background: yellow;">
        哈哈
    </div>
</div>
```

**说明:**

当点击子元素div，它的点击事件会向它父元素传递，也会触发了父元素的点击事件，这就是事件冒泡。

### 2. 事件代理的使用

**一般绑定事件的写法:**

```js
$(function(){
    $ali = $('#list li');
    $ali.click(function() {
        $(this).css({background:'red'});
    });
})

<ul id="list">
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <li>4</li>
    <li>5</li>
</ul>
```

**事件代理的写法**

```js
$(function(){
    $list = $('#list');
    // 父元素ul 来代理 子元素li的点击事件
    $list.delegate('li', 'click', function() {
        // $(this)表示当前点击的子元素对象
        $(this).css({background:'red'});
    });
})

<ul id="list">
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <li>4</li>
    <li>5</li>
</ul>
```

**delegate方法参数说明:**

delegate(childSelector,event,function)

- childSelector: 子元素的选择器
- event: 事件名称，比如: 'click'
- function: 当事件触发执行的函数

### 3. 小结

- 事件代理就是使用父元素来代理子元素的事件，好处是减少事件的绑定次数，提高性能。
- 使用场景当多个相同的子元素绑定同一个事件，可以使用事件代理。
- 事件代理使用是使用delegate方法来完成



# JavaScript对象

**学习目标**

- 能够知道JavaScript对象有两种创建方式

------

### 1. JavaScript对象的介绍

JavaScript 中的所有事物都是对象：字符串、数值、数组、函数等都可以认为是对象，此外，JavaScript 允许自定义对象，对象可以拥有属性和方法。

### 2. JavaScript创建对象操作

创建自定义javascript对象有两种方式:

- 通过顶级Object类型来实例化一个对象
- 通过对象字面量创建一个对象

**Object类创建对象的示例代码:**

```js
<script>
    var person = new Object();

    // 添加属性：
    person.name = 'tom';
    person.age = '25';

    // 添加方法：
    person.sayName = function(){
        alert(this.name);
    }

    // 调用属性和方法：
    alert(person.age);
    person.sayName();
</script>
```

**对象字面量创建对象的示例代码:**

```js
<script>
    var person2 = {
        name:'Rose',
        age: 18,
        sayName:function(){
            alert('My name is' + this.name);
        }
    }

    // 调用属性和方法：
    alert(person2.age);
    person2.sayName();
</script>
```

**说明:**

调用属性和方法的操作都是通过点语法的方式来完成，对象的创建推荐使用字面量方式，因为更加简单。

### 3. 小结

创建自定义javascript对象有两种方式:

- Object
- 字面量



# json

**学习目标**

- 能够知道json的格式

------

### 1. json的介绍

json是 JavaScript Object Notation 的首字母缩写，翻译过来就是javascript对象表示法，这里说的json就是**类似于javascript对象的字符串**，它同时是一种**数据格式**，目前这种数据格式比较流行，逐渐替换掉了传统的xml数据格式。

### 2. json的格式

json有两种格式：

1. 对象格式
2. 数组格式

**对象格式:**

对象格式的json数据，使用一对大括号({})，大括号里面放入key:value形式的键值对，多个键值对使用逗号分隔。

**对象格式的json数据:**

```json
{
    "name":"tom",
    "age":18
}
```

**格式说明:**

json中的(key)属性名称和字符串值需要用**双引号**引起来，用单引号或者不用引号会导致读取数据错误。

**数组格式:**

数组格式的json数据，使用一对中括号([])，中括号里面的数据使用逗号分隔。

**数组格式的json数据:**

```json
["tom",18,"programmer"]
```

**实际开发的json格式比较复杂,例如:**

```json
{
    "name":"jack",
    "age":29,
    "hobby":["reading","travel","photography"]
    "school":{
        "name":"Merrimack College",
        "location":"North Andover, MA"
    }
}
```

### 3. json数据转换成JavaScript对象

**json本质上是字符串**，如果在js中操作json数据，可以将json字符串转化为JavaScript对象。

**示例代码:**

```json
var sJson = '{"name":"tom","age":18}';
var oPerson = JSON.parse(sJson);

// 操作属性
alert(oPerson.name);
alert(oPerson.age);
```

### 4. 小结

- json就是一个javascript对象表示法，json本质上是一个字符串。
- json有两种格式：1. 对象格式, 2. 数组格式

# ajax

**学习目标**

- 能够知道ajax的作用

------

### 1. ajax的介绍

ajax 是 Asynchronous JavaScript and XML的简写，ajax一个前后台配合的技术，它可以**让 javascript 发送异步的 http 请求，与后台通信进行数据的获取**，ajax 最大的优点是**实现局部刷新**，ajax可以发送http请求，当获取到后台数据的时候更新页面显示数据实现局部刷新，在这里大家只需要记住，**当前端页面想和后台服务器进行数据交互就可以使用ajax了。**

这里提示一下大家, **在html页面使用ajax需要在web服务器环境下运行, 一般向自己的web服务器发送ajax请求。**

### 2. ajax的使用

jquery将它封装成了一个方法$.ajax()，我们可以直接用这个方法来执行ajax请求。

**示例代码:**

```js
<script>
    $.ajax({
    // 1.url 请求地址
    url:'http://t.weather.sojson.com/api/weather/city/101010100',
    // 2.type 请求方式，默认是'GET'，常用的还有'POST'
    type:'GET',
    // 3.dataType 设置返回的数据格式，常用的是'json'格式
    dataType:'JSON',
    // 4.data 设置发送给服务器的数据, 没有参数不需要设置

    // 5.success 设置请求成功后的回调函数
    success:function (response) {
        console.log(response);    
    },
    // 6.error 设置请求失败后的回调函数
    error:function () {
        alert("请求失败,请稍后再试!");
    },
    // 7.async 设置是否异步，默认值是'true'，表示异步，一般不用写
    async:true
});
</script>
```

**ajax方法的参数说明:**

1. url 请求地址
2. type 请求方式，默认是'GET'，常用的还有'POST'
3. dataType 设置返回的数据格式，常用的是'json'格式
4. data 设置发送给服务器的数据，没有参数不需要设置
5. success 设置请求成功后的回调函数
6. error 设置请求失败后的回调函数
7. async 设置是否异步，默认值是'true'，表示异步，一般不用写
8. 同步和异步说明
   - 同步是一个ajax请求完成另外一个才可以请求，需要等待上一个ajax请求完成，好比线程同步。
   - 异步是多个ajax同时请求，不需要等待其它ajax请求完成， 好比线程异步。

**ajax的简写方式:**

$.ajax按照请求方式可以简写成$.get或者$.post方式

**ajax简写方式的示例代码:**

```js
 <script>
    $(function(){
        /*
         1. url 请求地址
         2. data 设置发送给服务器的数据, 没有参数不需要设置
         3. success 设置请求成功后的回调函数
         4. dataType 设置返回的数据格式，常用的是'json'格式, 默认智能判断数据格式
        */ 
        $.get("http://t.weather.sojson.com/api/weather/city/101010100", function(dat,status){
            console.log(dat);
            console.log(status);
            alert(dat);
        }).error(function(){
            alert("网络异常");
        });

        /*
         1. url 请求地址
         2. data 设置发送给服务器的数据, 没有参数不需要设置
         3. success 设置请求成功后的回调函数
         4. dataType 设置返回的数据格式，常用的是'json'格式, 默认智能判断数据格式
        */ 
        $.post("test.php", {"func": "getNameAndTime"}, function(data){
            alert(data.name); 
            console.log(data.time); 
        }, "json").error(function(){
            alert("网络异常");
        }); 
    });


</script>
```

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























