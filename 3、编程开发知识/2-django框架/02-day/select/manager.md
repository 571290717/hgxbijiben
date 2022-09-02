# 管理器Manager {#管理器manager}

管理器是Django的模型进行数据库操作的接口，Django应用的每个模型类都拥有至少一个管理器。

我们在通过模型类的**objects**属性提供的方法操作数据库时，即是在使用一个管理器对象objects。当没有为模型类定义管理器时，Django会为每一个模型类生成一个名为objects的管理器，它是**models.Manager**类的对象。

### 自定义管理器 {#自定义管理器}

我们可以自定义管理器，并应用到我们的模型类上。

**注意：一旦为模型类指明自定义的过滤器后，Django不再生成默认管理对象objects。**

自定义管理器类主要用于两种情况：

* 准备工作：把`bookinfo`表中的一条记录`is_delete`字段修改成`True`

  ![](/assets/update_recode.png)

* 问题：逻辑删除字段为`True`的那条记录依然会被查询出来

**1. 修改原始查询集，重写all\(\)方法。**

a）打开book/models.py文件，定义类BookInfoManager

```
class BookInfoManager(models.Manager):

    def all(self):
        #默认查询未删除的图书信息
        #调用父类的成员语法为：super().方法名
        return super().filter(is_delete=False)
```

b）在模型类BookInfo中定义管理器

```
class BookInfo(models.Model):
    ...
    books = BookInfoManager()
```

c）使用方法

```
>>> books = BookInfo.books.all()
>>> books
<QuerySet [<BookInfo: 天龙八部>, <BookInfo: 笑傲江湖>, <BookInfo: 雪山飞狐>, <BookInfo: python入门>]>
```

d）视图方法

```
# 书籍列表信息视图
  def bookList(request):
    # 查询数据库书籍列表数据
    # books = BookInfo.objects.all()
    books = BookInfo.books.all()
    # 构造上下文
    context = {'books':books}
    # 数据交给模板处理，处理完成后通过视图响应给客户端
    return render(request, 'Book/booklist.html', context)
```

**2. 在管理器类中补充定义新的方法**

a）打开book/models.py文件，定义方法create。

```
class BookInfoManager(models.Manager):

    def create_book(self,name,pub_date):
        # 创建模型类对象self.model可以获得模型类
        book = self.model()
        book.name = name
        book.pub_date = pub_date
        book.save()
        return book
```

b）为模型类BookInfo定义管理器books语法如下

```
class BookInfo(models.Model):
      ...
    books = BookInfoManager()
```

c）调用语法如下：

```
>>> from book.models import BookInfo
>>> book = BookInfo.books.create_book('python高级','2010-1-1')
>>> book
<BookInfo: python高级>
```



