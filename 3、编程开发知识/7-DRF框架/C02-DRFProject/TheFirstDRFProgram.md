# 见识DRF的魅力

我们仍以在学习Django框架时使用的图书英雄为案例，使用Django REST framework快速实现图书的REST API。

## 1.  创建序列化器

在booktest应用中新建serializers.py用于保存该应用的序列化器。

创建一个BookInfoSerializer用于序列化与反序列化。

```python
class BookInfoSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""
    class Meta:
        model = BookInfo
        fields = '__all__'
```

* **model** 指明该序列化器处理的数据字段从模型类BookInfo参考生成
* **fields** 指明该序列化器包含模型类中的哪些字段，'\_\_all\_\_'指明包含所有字段

## 2.  编写视图

在booktest应用的views.py中创建视图BookInfoViewSet，这是一个视图集合。

```python
from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer
from .models import BookInfo

class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
```

* **queryset** 指明该视图集在查询数据时使用的查询集
* **serializer_class** 指明该视图在进行序列化或反序列化时使用的序列化器

## 3.  定义路由

在booktest应用的urls.py中定义路由信息。

```python
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    ...
]

router = DefaultRouter()  # 可以处理视图的路由器
router.register(r'books', views.BookInfoViewSet)  # 向路由器中注册视图集

urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
```

## 4.   运行测试

运行当前程序（与运行Django一样）

```shell
python manage.py runserver
```

在浏览器中输入网址127.0.0.1:8000，可以看到DRF提供的API Web浏览页面：

![图书接口Web浏览页面](/images/图书接口Web浏览页面.png)

1）点击链接127.0.0.1:8000/books/ 可以访问**获取所有数据的接口**，呈现如下页面：

![查询所有图书信息1](/images/查询所有图书信息1.png)

![查询所有图书信息2](/images/查询所有图书页面2.png)

2）在页面底下表单部分填写图书信息，可以访问**添加新图书的接口**，保存新书：

![保存新图书](/images/保存新图书信息.png)

点击POST后，返回如下页面信息：

![保存图书返回信息](/images/保存图书返回信息.png)

3）在浏览器中输入网址127.0.0.1:8000/books/1/，可以访问**获取单一图书信息的接口**（id为1的图书），呈现如下页面：

![获取单一图书信息](/images/获取单一图书信息.png)

4）在页面底部表单中填写图书信息，可以访问**修改图书的接口**：

![修改图书信息](/images/修改图书信息.png)

点击PUT，返回如下页面信息：

![修改图书返回信息](/images/修改图书返回信息.png)

5）点击DELETE按钮，可以访问**删除图书的接口**：

![删除图书](/images/删除图书.png)

返回，如下页面：

![删除图书返回信息](/images/删除返回信息.png)

至此，是不是发现Django REST framework很好用！