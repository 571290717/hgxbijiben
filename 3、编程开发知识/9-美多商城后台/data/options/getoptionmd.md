## 查询获取规格选项表列表数据

### 接口分析

**请求方式**： GET   `/meiduo_admin/specs/options/`

**请求参数**： 通过请求头传递jwt token数据。

**返回数据**：  JSON

```json
  [
        {
            "id": "选项id",
            "value": "选项名称",
            "spec": "规格名称",
            "spec_id": "规格id"
        },
        ...
    ]
```

| 返回值  | 类型 | 是否必须 | 说明     |
| ------- | ---- | -------- | -------- |
| id      | int  | 是       | 选项id   |
| value   | 数组 | 是       | 选项名称 |
| spec    | str  | 是       | 规格名称 |
| spec_id | int  | 是       | 规格id   |



### 后端实现

``` python
class OptionsView(ModelViewSet):
  	"""
  			规格选项表的增删改查
  	"""
    serializer_class = OptionSerialzier
    queryset = SpecificationOption.objects.all()
    pagination_class = PageNum
```



序列化器的定义

```python
class OptionSerialzier(serializers.ModelSerializer):
  	# 嵌套返回规格名称
    spec=serializers.StringRelatedField(read_only=True)
    # 返回规格id
    spec_id=serializers.IntegerField()
    class Meta:
        model = SpecificationOption  # 规格选项表中的spec字段关联了规格表
        fields="__all__"
```

