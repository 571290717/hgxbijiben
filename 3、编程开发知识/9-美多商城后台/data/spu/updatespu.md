## 更新SPU表数据

### 1、 获取修改商品的详情信息

点就修改按钮时，我们需要先获取要修改的商品详情信息

#### 接口分析

**请求方式**： GET ` /meiduo_admin/goods/(?P<pk>\d+)/`

**请求参数**： 通过请求头传递jwt token数据。

在头部中携带要获取的sku商品ID

**返回数据**：  JSON

``` json
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
   }
```

| 参数         | 类型  | 是否必须 | 说明          |
| ------------ | ----- | -------- | ------------- |
| id           | int   | 是       | 商品SPU ID    |
| name         | str   | 是       | SPU名称       |
| brand        | str   | 是       | 品牌名称      |
| brand_id     | int   | 是       | 品牌id        |
| category1_id | int   | 是       | 一级分类id    |
| category2_id | int   | 是       | 二级分类id    |
| category3_id | int   | 是       | 三级分类id    |
| comments     | int   | 是       | SPU商品评论量 |
| desc_detail  | boole | 是       | 商品详情      |
| desc_pack    | str   | 是       | 商品包装      |
| desc_service | str   | 是       | 售后服务      |

后端实现

``` python

# SKUGoodsView继承的是ModelViewSet 所以保存逻辑还是使用同一个类视图
class SKUGoodsView(ModelViewSet):

    serializer_class =SKUGoodsSerializer
    pagination_class = PageNum

    def get_queryset(self):
        keyword=self.request.query_params.get('keyword')
        if keyword == '' or keyword is None:
            return SKU.objects.all()

        else:
            return SKU.objects.filter(name=keyword)
```







#### 接口分析

**请求方式**： PUT   `/meiduo_admin/goods/(?P<pk>\d+)/`

**请求参数**： 通过请求头传递jwt token数据。

| 参数         | 类型 | 是否必须 | 说明       |
| ------------ | ---- | -------- | ---------- |
| name         | str  | 是       | SPU名称    |
| brand_id     | int  | 是       | 商品SPU ID |
| category1_id | str  | 是       | 商品副标题 |
| category2_id | int  | 是       | 三级分类ID |
| category3_id | int  | 是       | 价格       |
| desc_detail  | str  | 是       | 进价       |
| desc_pack    | str  | 是       | 市场价     |
| desc_service | str  | 是       | 库存       |



**返回数据**：  JSON

```json
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
   }
```

| 参数         | 类型 | 是否必须 | 说明          |
| ------------ | ---- | -------- | ------------- |
| id           | Int  | 是       | 商品SPU ID    |
| name         | Str  | 是       | 商品SPU 名称  |
| brand        | str  | 是       | 品牌名称      |
| brand_id     | int  | 是       | 品牌id        |
| category1_id | int  | 是       | 一级分类id    |
| category2_id | int  | 是       | 二级分类id    |
| category3_id | int  | 是       | 三级分类id    |
| sales        | int  | 是       | SPU商品销量   |
| comments     | int  | 是       | SPU商品评论量 |
| desc_detail  | str  | 是       | 商品详情      |
| desc_pack    | str  | 是       | 商品包装      |
| desc_service | str  | 是       | 售后服务      |

后端实现

```python
class SPUGoodsView(ModelViewSet):
    """
        SPU表
    """
    serializer_class = SPUGoodsSerialzier
    queryset = SPU.objects.all()
    pagination_class = PageNum
```

