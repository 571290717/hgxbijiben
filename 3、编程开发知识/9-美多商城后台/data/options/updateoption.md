## 更新规格选项表数据

### 1、 获取要修改的规格选项的详情信息

点就修改按钮时，我们需要先获取要修改的规格选项的详情信息

#### 接口分析

**请求方式**： GET ` /meiduo_admin/specs/options/(?P<pk>\d+)/`

**请求参数**： 通过请求头传递jwt token数据。

在头部中携带要获取的规格选项ID

**返回数据**：  JSON

``` json
 {
        "id": "选项id",
        "value": "选项名称",
        "spec": "规格名称",
        "spec_id": "规格id"
    }
```

| 参数    | 类型 | 是否必须 | 说明     |
| ------- | ---- | -------- | -------- |
| id      | Int  | 是       | 规格id   |
| name    | Str  | 是       | 规格名称 |
| spec    | str  | 是       | 规格名称 |
| spec_id | Int  | 是       | 规格id   |

后端实现

``` python

# OptionsView继承的是ModelViewSet 所以获取规格选项详情的逻辑还是使用同一个类视图
class OptionsView(ModelViewSet):

    serializer_class =OptionSerialzier
    queryset = SpecificationOption.objects.all()
    pagination_class = PageNum
```



### 2、更新规格选项表数据

#### 接口分析

**请求方式**： PUT   `/meiduo_admin/specs/options/(?P<pk>\d+)/`

**请求参数**： 通过请求头传递jwt token数据。

| 参数    | 类型 | 是否必须 | 说明     |
| ------- | ---- | -------- | -------- |
| value   | str  | 是       | 选项名称 |
| spec_id | int  | 是       | 规格id   |

**返回数据**：  JSON

```json
  {
        "id": "选项id",
        "value": "选项名称",
        "spec": "规格名称",
        "spec_id": "规格id"
    }
```

| 参数    | 类型 | 是否必须 | 说明     |
| ------- | ---- | -------- | -------- |
| id      | Int  | 是       | 规格id   |
| name    | Str  | 是       | 规格名称 |
| spec    | str  | 是       | 规格名称 |
| spec_id | Int  | 是       | 规格id   |



后端实现

```python

# OptionsView继承的是ModelViewSet 所以修改逻辑还是使用同一个类视图
class OptionsView(ModelViewSet):

    serializer_class =OptionSerialzier
    queryset = SpecificationOption.objects.all()
    pagination_class = PageNum
```

