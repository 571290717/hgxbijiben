# Vue3 教程

## 阅读本教程前，您需要了解的知识：

- HTML

- CSS

- JavaScript

  

# Vue3 安装

## 1、独立版本

我们可以在 Vue.js 的官网上直接下载最新版本, 并用 **<script>** 标签引入。

- [下载 Vue.js](https://unpkg.com/vue@next)

以下推荐国外比较稳定的两个 CDN，国内还没发现哪一家比较好，目前还是建议下载到本地。

- **Staticfile CDN（国内）** : https://cdn.staticfile.org/vue/3.0.5/vue.global.js
- **unpkg**：https://unpkg.com/vue@next, 会保持和 npm 发布的最新的版本一致。
- **cdnjs** : https://cdnjs.cloudflare.com/ajax/libs/vue/3.0.5/vue.global.js

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Vue 测试实例 - 菜鸟教程(runoob.com)</title>
<script src="https://cdn.staticfile.org/vue/3.0.5/vue.global.js"></script>
</head>
<body>
<div id="hello-vue" class="demo">
  {{ message }}
</div>

<script>
const HelloVueApp = {
  data() {
    return {
      message: 'Hello Vue!!'
    }
  }
}

Vue.createApp(HelloVueApp).mount('#hello-vue')
</script>
</body>
</html>
```



## vue create 命令 创建项目

vue create 命令创建项目语法格式如下：

```
vue create [options] <app-name>
```

创建一个由 vue-cli-service 提供支持的新项目：

options 选项可以是：

- **-p, --preset <presetName>**： 忽略提示符并使用已保存的或远程的预设选项
- **-d, --default**： 忽略提示符并使用默认预设选项
- **-i, --inlinePreset <json>**： 忽略提示符并使用内联的 JSON 字符串预设选项
- **-m, --packageManager <command>**： 在安装依赖时使用指定的 npm 客户端
- **-r, --registry <url>**： 在安装依赖时使用指定的 npm registry
- **-g, --git [message]**： 强制 / 跳过 git 初始化，并可选的指定初始化提交信息
- **-n, --no-git**： 跳过 git 初始化
- **-f, --force**： 覆写目标目录可能存在的配置
- **-c, --clone**： 使用 git clone 获取远程预设选项
- **-x, --proxy**： 使用指定的代理创建项目
- **-b, --bare**： 创建项目时省略默认组件中的新手指导信息
- **-h, --help**： 输出使用帮助信息

接下来我们创建 runoob-vue3-app 项目：

```
vue create runoob-vue3-app
```

执行以上命令会出现安装选项界面：

```
Vue CLI v4.4.6
? Please pick a preset: (Use arrow keys)
❯ default (babel, eslint)
  Manually select features
```

按下回车键后就会进入安装，等候片刻即可完成安装。

安装完成后，我们进入项目目录：

cd runoob-vue3-app2

启动应用：

```
npm run serve
```

然后打开 **http://localhost:8080/**，就可以看到应用界面了：

![img](images/53627B96-0166-4FE1-B055-F8A3C3817B95.jpg)



## Vite创建项目

Vite 是一个 web 开发构建工具，由于其原生 ES 模块导入方式，可以实现闪电般的冷服务器启动。

通过在终端中运行以下命令，可以使用 Vite 快速构建 Vue 项目，语法格式如下：

```
npm init vite-app <project-name>
```

创建项目 runoob-vue3-test2：

```
$  npm init vite-app runoob-vue3-test2
```

运行项目:

```
$ cd runoob-vue3-test2
$ cnpm install
$ cnpm run dev
> runoob-vue3-test2@0.0.0 dev /Users/tianqixin/runoob-test/vue3/runoob-vue3-test2
> vite

[vite] Optimizable dependencies detected:
vue

  Dev server running at:
  > Local:    http://localhost:3000/
```

打开 **http://localhost:3000/**，显示如下：

![img](https://www.runoob.com/wp-content/uploads/2021/02/62FB6F27-456F-46CF-8892-93D6A3E6F341.jpg)



Vue3 项目打包

```
cnpm run build
```

# Vue3 目录结构





**命令行工具 vue-cli（runoob-vue3-test）：**

![img](images/7C26D06C-4B1B-4E80-BBE1-E407C3E945B3.jpg)



**Vite（runoob-vue3-test2）**

![img](images/7C797674-06CF-4E87-B344-63990EF519B6.jpg)



### 目录解析

| 目录/文件    | 说明                                                         |
| :----------- | :----------------------------------------------------------- |
| build        | 项目构建(webpack)相关代码                                    |
| config       | 配置目录，包括端口号等。我们初学可以使用默认的。             |
| node_modules | npm 加载的项目依赖模块                                       |
| src          | 这里是我们要开发的目录，基本上要做的事情都在这个目录里。里面包含了几个目录及文件：assets: 放置一些图片，如logo等。components: 目录里面放了一个组件文件，可以不用。App.vue: 项目入口文件，我们也可以直接将组件写这里，而不使用 components 目录。main.js: 项目的核心文件。index.css: 样式文件。 |
| static       | 静态资源目录，如图片、字体等。                               |
| public       | 公共资源目录。                                               |
| test         | 初始测试目录，可删除                                         |
| .xxxx文件    | 这些是一些配置文件，包括语法配置，git配置等。                |
| index.html   | 首页入口文件，你可以添加一些 meta 信息或统计代码啥的。       |
| package.json | 项目配置文件。                                               |
| README.md    | 项目的说明文档，markdown 格式                                |
| dist         | 使用 **npm run build** 命令打包后会生成该目录。              |





# Vue3 起步

> 起步两步
>
> 创建应用，并写东西，挂载
>
> Vue.createApp({ xxxx}).mount('#xxxid')
>
> ```
> 其他写法：
> const project_name1 = Vue.createApp({ xxxx}).mount('#xxxid')
> 
> 
> const HelloVueApp = Vue.createApp({
>   data() {
>     return {
>       message: 'Hello Vue!!'
>     }
>   }
> }).mount('#hello-vue')
> 
> 
> 
> 2\
> const app = Vue.createApp({ /* 选项 */ })
> app.mount('#xxxid')
> 
> 
> ```
>
> 



Vue3 中的应用是通过使用 createApp 函数来创建的，语法格式如下：

```
const app = Vue.createApp({ /* 选项 */ })
```

传递给 createApp 的选项用于配置根组件。在使用 **mount()** 挂载应用时，该组件被用作渲染的起点。



一个简单的实例：

```
Vue.createApp(xxxxxx根组件).mount('#hello-vue')
```

createApp 的参数是根组件（HelloVueApp），在挂载应用时，该组件是渲染的起点。



```html
<div id="hello-vue" class="demo">
  {{ message }}
</div>
​
<script>
const HelloVueApp = {
  data() {
    return {
      message: 'Hello Vue!!'
    }
  }
}
​
Vue.createApp(HelloVueApp).mount('#hello-vue')
</script>
```



### data 选项

**data 选项**是一个函数。Vue 在创建新组件实例的过程中调用此函数。它应该返回一个对象，然后 Vue 会通过响应性系统将其包裹起来，并以 $data 的形式存储在组件实例中。



```html
const app = Vue.createApp({
  data() {
    return { count: 4 }
  }
})

const vm = app.mount('#app')

document.write(vm.$data.count) // => 4
document.write("<br>")
document.write(vm.count)       // => 4
document.write("<br>")
// 修改 vm.count 的值也会更新 $data.count
vm.count = 5
document.write(vm.$data.count) // => 5
document.write("<br>")
// 反之亦然
vm.$data.count = 6
document.write(vm.count) // => 6
```

## 方法

 **methods** 选项

```vue
const app = Vue.createApp({
  data() {
    return { count: 4 }
  },
  methods: {
    increment() {
      // `this` 指向该组件实例
      this.count++
    }
  }
})

const vm = app.mount('#app')

document.write(vm.count) // => 4
document.write("<br>")
vm.increment()

document.write(vm.count) // => 5
```





# Vue3 指令

核心功能

以 v- 开头的特殊属性形式使用

响应式数据绑定到 DOM 元素上或在 DOM 元素上进行一些操作

文档对象模型。 *DOM*是Javascript看到其包含页面数据的方式。它是一个对象，包括HTML / XHTML / XML的格式，以及浏览器状态。 *DOM元素*类似于页面上的DIV，HTML

 Vue 创建响应式页面要容易得多，并且需要的代码更少

| 指令      | 描述                                                         |
| :-------- | :----------------------------------------------------------- |
| `v-bind`  | 用于将 Vue 实例的数据绑定到 HTML 元素的属性上。              |
| `v-if`    | 用于根据表达式的值来条件性地渲染元素或组件。                 |
| `v-show`  | v-show 是 Vue.js 提供的一种指令，用于根据表达式的值来条件性地显示或隐藏元素。 |
| `v-for`   | 用于根据数组或对象的属性值来循环渲染元素或组件。             |
| `v-on`    | 用于在 HTML 元素上绑定事件监听器，使其能够触发 Vue 实例中的方法或函数。 |
| `v-model` | 用于在表单控件和 Vue 实例的数据之间创建双向数据绑定。        |



```html
<div id="hello-vue" class="demo">
    <button v-on:click="showMessage = !showMessage">显示/隐藏</button>
    <p v-show="showMessage">Hello Vue!</p>
</div>

<script>
const HelloVueApp = {
  data() {
    return {
      showMessage: true
    }
  }
}

Vue.createApp(HelloVueApp).mount('#hello-vue')
</script>
```



# Vue3 创建单文件组件(SFC)

Vue 的单文件组件 (即 *.vue 文件，英文 Single-File Component，简称 SFC) 

是一种特殊的文件格式，使我们能够将一个 Vue 组件的模板、逻辑与样式封装在单个文件中。

## App.vue 文件：

<script></script>

<template></template>

<style></style>



同时我们可以先清空 **src** 目录中的文件夹 **assets** 和 **components**，里面的文件我们可以后期自己添加补充 。

main.js 文件代码修改为如下代码：



## main.js 文件代码：

```vue
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')


现在我们就创建了一个简单的项目，在 App.vue 文件写入以下代码：

App.vue 文件代码：
<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello, RUNOOB!'
    }
  }
}
</script>

<style>
h1 {
  color: blue;
}
</style>




```

![img](images/bd73268cae09ec3209e42c9509f1da74.png)

```vue
使用组件
当我们定义好了一个组件之后，我们可以在其他组件中使用这个组件。

使用组件，我们需要先创建组件，比如以下实例在 ./src/components/ 目录下创建 HelloRunoob.vue 组件文件，代码如下：

./src/components/HelloRunoob.vue 文件代码：
<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello, Runoob!'
    }
  }
}
</script>

<style>
h1 {
  color: red;
}
</style>



然后我们在 ./src/main.js 文件中引入并定义该组件：

./src/main.js 文件代码：
import { createApp } from 'vue'

import App from './App.vue'
import HelloRunoob from './components/HelloRunoob.vue'

const app = createApp(App)
app.component('hello-runoob', HelloRunoob) // 自定义标签
app.mount('#app')



在父组件的模板中，我们可以使用自定义标签的方式来引入子组件，就像以下 App.vue 文件代码：


App.vue 文件代码


<template>
  <div>
    <hello-runoob></hello-runoob>
  </div>
</template>
访问 http://localhost:5173/，以上代码执行结果为：


```

![img](images/0ed91fd15ff9df3cfcd1a198d4c2b92f.png)Vue3 模板语法

# Vue3 模板语法

Vue 使用了基于 HTML 的模板语法，允许开发者声明式地将 DOM 绑定至底层 Vue 实例的数据。

Vue 的核心是一个允许你采用简洁的模板语法来声明式的将数据渲染进 DOM 的系统。



 **v-once** 指令执行一次性地插值，当数据改变时，插值处的内容不会更新。

```
<span v-once>这个将不会改变: {{ message }}</span>
```

**使用 v-html 指令用于输出 html 代码：**

   <p>使用 v-html 指令: <span v-html="rawHtml"></span></p>

```
 <p>使用 v-html 指令: <span v-html="rawHtml"></span></p>
 
 
 <script>
const RenderHtmlApp = {
  data() {
    return {
      rawHtml: '<span style="color: red">这里会显示红色！</span>'
    }
  }
}
 
Vue.createApp(RenderHtmlApp).mount('#example1')
</script>
```



**HTML 属性中的值应使用 v-bind 指令。**



Vue.js 都提供了完全的 JavaScript 表达式支持。

```
<div id="app">
    {{5+5}}<br>
    {{ ok ? 'YES' : 'NO' }}<br>
    {{ message.split('').reverse().join('') }}
    <div v-bind:id="'list-' + id">菜鸟教程</div>
</div>
    
<script>
const app = {
  data() {
    return {
      ok: true,
      message: 'RUNOOB!!',
      id: 1
    }
  }
}
 
Vue.createApp(app).mount('#app')
</script>


<!--  这是语句，不是表达式：-->
{{ var a = 1 }}

<!-- 流控制也不会生效，请使用三元表达式 -->
{{ if (ok) { return message } }}
```





## 缩写

### v-bind 缩写

Vue.js 为两个最为常用的指令提供了特别的缩写：

```
<!-- 完整语法 -->
<a v-bind:href="url"></a>
<!-- 缩写 -->
<a :href="url"></a>
```

### v-on 缩写

```
<!-- 完整语法 -->
<a v-on:click="doSomething"></a>
<!-- 缩写 -->
<a @click="doSomething"></a>
```

[返回顶](javascript:scroll(0,0))

**v-if**

**v-show**

**v-else-if**

**v-else**

```vue
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Vue 测试实例 - 菜鸟教程(runoob.com)</title>
<script src="https://unpkg.com/vue@next"></script>
</head>
<body>
<div id="app">
   <select @change="changeVal($event)" v-model="selOption">
      <template v-for="(site,index) in sites" :site="site" :index="index" :key="site.id">
         <!-- 索引为 1 的设为默认值，索引值从0 开始-->
         <option v-if = "index == 1" :value="site.name" selected>{{site.name}}</option>
         <option v-else :value="site.name">{{site.name}}</option>
      </template>
   </select>
   <div>您选中了:{{selOption}}</div>
</div>
 
<script>
const app = {
    data() {
        return {
            selOption: "Runoob",
            sites: [
                  {id:1,name:"Google"},
                  {id:2,name:"Runoob"},
                  {id:3,name:"Taobao"},
            ]
         }
        
    },
    methods:{
        changeVal:function(event){
            this.selOption = event.target.value;
            alert("你选中了"+this.selOption);
        }
    }
}
 
Vue.createApp(app).mount('#app')
</script>
</body>
</html>
```







# Vue3 计算属性

计算属性关键词: computed。

计算属性在处理一些复杂逻辑时是很有用的。



```
<div id="app">
  {{ message.split('').reverse().join('') }}
</div>
```

```vue
实例 2
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Vue 测试实例 - 菜鸟教程(runoob.com)</title>
<script src="https://cdn.staticfile.org/vue/3.0.5/vue.global.js"></script>
</head>
<body>
<div id="app">
  <p>原始字符串: {{ message }}</p>
  <p>计算后反转字符串: {{ reversedMessage }}</p>
</div>
    
<script>
const app = {
  data() {
    return {
      message: 'RUNOOB!!'
    }
  },
  computed: {
    // 计算属性的 getter
    reversedMessage: function () {
      // `this` 指向 vm 实例
      return this.message.split('').reverse().join('')
    }
  }
}
 
Vue.createApp(app).mount('#app')
</script>
</body>
</html>





```

vm.reversedMessage 依赖于 vm.message，在 vm.message 发生改变时，

我们可以使用 methods 来替代 computed，效果上两个都是一样的，但是 computed 是基于它的依赖缓存，只有相关依赖发生改变时才会重新取值。而使用 methods ，在重新渲染的时候，函数总会重新调用执行。

（换人话就是computed在message变的时候才调用执行一般是缓存着的，而methods每次刷新都会执行一次）



可以说使用 computed 性能会更好，但是如果你不希望缓存，你可以使用 methods 属性



https://m.runoob.com/vue3/vu3-computed.html



































