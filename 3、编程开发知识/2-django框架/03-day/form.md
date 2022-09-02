# 表单 {#表单}

Django提供对表单处理的支持，可以简化并自动化大部分的表单处理工作。

## 1 定义表单类 {#1--定义表单类}

表单系统的核心部分是Django 的Form类。 Django 的数据库模型描述一个对象的逻辑结构、行为以及展现给我们的方式，与此类似，Form类描述一个表单并决定它如何工作和展现。

假如我们想在网页中创建一个表单，用来获取用户想保存的图书信息，可能类似的html 表单如下：

```
<form action="" method="post">
    <input type="text" name="title">
    <input type="date" name="pub_date">
    <input type="submit">
</form>
```

我们可以据此来创建一个Form类来描述这个表单。

新建一个**forms.py**文件，编写Form类。

```
from django import forms

class BookForm(forms.Form):
    title = forms.CharField(label="书名", required=True, max_length=50)
    pub_date = forms.DateField(label='出版日期', required=True)
```

注：[表单字段类型参考资料连接](https://yiyibooks.cn/xx/Django_1.11.6/ref/forms/fields.html)

## 2 视图中使用表单类 {#2--视图中使用表单类}

```
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .forms import BookForm

class BookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'book.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():  # 验证表单数据
            print(form.cleaned_data)  # 获取验证后的表单数据
            return HttpResponse("OK")
        else:
            return render(request, 'book.html', {'form': form})
```

* form.is\_valid\(\) 验证表单数据的合法性
* form.cleaned\_data 验证通过的表单数据

## 3 模板中使用表单类 {#3-模板中使用表单类}

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>书籍</title>
</head>
<body>
    <form action="" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit">
    </form>
</body>
</html>
```

* csrf\_token 用于添加CSRF防护的字段
* form 快速渲染表单字段的方法

## 4 模型类表单 {#4--模型类表单}

如果表单中的数据与模型类对应，可以通过继承**forms.ModelForm**更快速的创建表单。

```
class BookForm(forms.ModelForm):
    class Meta:
        model = BookInfo
        fields = ('name', 'pub_date')
```

* model 指明从属于哪个模型类
* fields 指明向表单中添加模型类的哪个字段



