# 调整列表页展示 {#调整列表页展示}

#### 1 页大小 {#1--页大小}

每页中显示多少条数据，默认为每页显示100条数据，属性如下：

```
list_per_page=100
```

1）打开booktest/admin.py文件，修改AreaAdmin类如下：

```
class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 2
```

2）在浏览器中查看区域信息的列表页面，效果如下图：

![](/assets/admin_list_per_page.png)

#### 2 "操作选项"的位置 {#2--操作选项的位置}

顶部显示的属性，设置为True在顶部显示，设置为False不在顶部显示，默认为True。

```
actions_on_top=True
```

底部显示的属性，设置为True在底部显示，设置为False不在底部显示，默认为False。

```
actions_on_bottom=False
```

1）打开booktest/admin.py文件，修改BookInfoAdmin类如下：

```
class BookInfoAdmin(admin.ModelAdmin):
    ...
    actions_on_top = True
    actions_on_bottom = True
```

2）在浏览器中刷新效果如下图：

![](/assets/admin_action.png)

#### 3 列表中的列 {#3--列表中的列}

属性如下：

```
list_display=[模型字段1,模型字段2,...]
```

1）打开book/admin.py文件，修改BookInfoAdmin类如下：

```
class BookInfoAdmin(admin.ModelAdmin):
    ...
    list_display = ['id','name']
```

2）在浏览器中刷新效果如下图：

![](/assets/list_display.png)

**点击列头可以进行升序或降序排列。**

#### 4 将方法作为列 {#4--将方法作为列}

列可以是模型字段，还可以是模型方法，要求方法有返回值。

**通过设置short\_description属性，可以设置在admin站点中显示的列名。**

1）打开book/models.py文件，修改BookInfo类如下：

```
class BookInfo (models.Model):

    ...

def bookname(self):
        return '<<' + self.name + '>>'

    bookname.short_description = '书名'  # 设置方法字段在admin中显示的标题
```

2）打开book/admin.py文件，修改BookInfoAdmin类如下：

```
class BookInfoAdmin (admin.ModelAdmin) :

    ...
   list_display = ['id','name','bookname']
```

3）在浏览器中刷新效果如下图：

![](/assets/custom.png)

方法列是不能排序的，如果需要排序需要为方法指定排序依据。

```
admin_order_field=模型类字段
```

1）打开book/models.py文件，修改BookInfo类如下：

```
class BookInfo(models.Model):

    ...

def bookname(self):
        return '<<' + self.name + '>>'

    bookname.short_description = '书名'  # 设置方法字段在admin中显示的标题
    bookname.admin_order_field = 'name'
```

2）在浏览器中刷新效果如下图：

![](/assets/order_field.png)

#### 5 关联对象 {#5--关联对象}

无法直接访问关联对象的属性或方法，可以在模型类中封装方法，访问关联对象的成员。

1）打开book/models.py文件，修改PeopleInfo类如下：

```
class PeopleInfo(models.Model):

    ...

    def readcount(self):
        return self.book.readcount
    readcount.short_description = '图书阅读量'
```

2）打开book/admin.py文件，修改PeopleInfoAdmin类如下：

```
@admin.register(PeopleInfo)
class PeopleInfoAdmin(admin.ModelAdmin):

    list_display = ['id','name','book','readcount']
```

3）在浏览器中刷新效果如下图：

![](/assets/associate.png)

#### 6 右侧栏过滤器 {#6--右侧栏过滤器}

属性如下，只能接收字段，会将对应字段的值列出来，用于快速过滤。一般用于有重复值的字段。

```
list_filter=[]
```

1）打开book/admin.py文件，修改PeopleInfoAdmin类如下：

```
@admin.register(PeopleInfo)
class PeopleInfoAdmin(admin.ModelAdmin):

    list_display = ['id','name','book','readcount']

    list_filter = ['book','gender']
```

2）在浏览器中刷新效果如下图：

![](/assets/filter.png)

#### 7 搜索框 {#7--搜索框}

属性如下，用于对指定字段的值进行搜索，支持模糊查询。列表类型，表示在这些字段上进行搜索。

```
search_fields=[]
```

1）打开book/admin.py文件，修改PeopleInfoAdmin类如下：

```
@admin.register(PeopleInfo)
class PeopleInfoAdmin(admin.ModelAdmin):

    list_display = ['id','name','book','readcount']

    list_filter = ['book','gender']

    search_fields = ['name']
```

2）在浏览器中刷新效果如下图：

![](/assets/search.png)

