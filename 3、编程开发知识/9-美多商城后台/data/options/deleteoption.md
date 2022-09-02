## 删除规格选项表数据

#### 接口分析

**请求方式**： Delte   `/meiduo_admin/specs/options/(?P<pk>\d+)/`

**请求参数**： 通过请求头传递jwt token数据。

在路径中携带删除的规格选项的id值

**返回数据**：  JSON

返回空

后端实现

```python
# OptionsView继承的是ModelViewSet 所以删除逻辑还是使用同一个类视图
class OptionsView(ModelViewSet):
		"""
			规格选项表数据处理
		"""
    serializer_class =OptionSerialzier
    queryset = SpecificationOption.objects.all()
    pagination_class = PageNum


```

