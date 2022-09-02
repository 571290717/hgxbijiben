## 查询获取SPU表列表数据

在获取sku数据时，我们在请求中包含了查询关键keyword，这时我么就需要对keyword进行判断，来返回不同的查询数据

### 接口分析

**请求方式**： GET   `/meiduo_admin/goods/?keyword=<名称|副标题>&page=<页码>&page_size=<页容量>`

**请求参数**： 通过请求头传递jwt token数据。

**返回数据**：  JSON

```json
{
        "counts": "商品SPU总数量",
        "lists": [
            {
                "id": "商品SPU ID",
                "name": "SPU名称",
                "brand": "品牌名称",
                "brand_id": "品牌id",
                "category1_id": "一级分类id",
                "category2_id": "二级分类id",
                "category3_id": "三级分类id",
                "sales": "SPU商品销量",
                "comments": "SPU商品评论量",
                "desc_detail": "商品详情",
                "desc_pack": "商品包装",
                "desc_service": "售后服务"
            },
            ...
       ],
       "page": "页码",
       "pages": "总页数",
       "pagesize": "页容量"
  }
```

| 返回值   | 类型 | 是否必须 | 说明        |
| -------- | ---- | -------- | ----------- |
| count    | int  | 是       | SPU商品总量 |
| lists    | 数组 | 是       | SPU信息     |
| page     | int  | 是       | 页码        |
| pages    | int  | 是       | 总页数      |
| pagesize | int  | 是       | 页容量      |



### 后端实现

``` python
class SPUGoodsView(ModelViewSet):
    """
        SPU表的增删改查
    """
    # 指定序列化器
    serializer_class = SPUGoodsSerialzier
    # 指定查询及
    queryset = SPU.objects.all()
    # 指定分页
    pagination_class = PageNum
```



序列化器的定义

```python
class SPUGoodsSerialzier(serializers.ModelSerializer):
    """
        SPU表序列化器
    """
    # 一级分类id
    category1_id=serializers.IntegerField()
    # 二级分类id
    category2_id=serializers.IntegerField()
    # 三级级分类id
    category3_id=serializers.IntegerField()
    # 关联的品牌id
    brand_id=serializers.IntegerField()
    # 关联的品牌，名称
    brand=serializers.StringRelatedField(read_only=True)

    class Meta:
        model=SPU
        exclude=('category1','category2','category3') 
```

