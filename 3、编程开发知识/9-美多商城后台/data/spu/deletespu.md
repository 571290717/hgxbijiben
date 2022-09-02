## 删除SPU表数据

#### 接口分析

**请求方式**： Delte   `meiduo_admin/goods/(?P<pk>\d+)/`

**请求参数**： 通过请求头传递jwt token数据。

在路径中携带删除的sku的id值

**返回数据**：  JSON

返回空

后端实现

```python
# SPUGoodsView继承的是ModelViewSet 所以删除逻辑还是使用同一个类视图
class SPUGoodsView(ModelViewSet):
    """
        SPU表
    """
    serializer_class = SPUGoodsSerialzier
    queryset = SPU.objects.all()
    pagination_class = PageNum

```

