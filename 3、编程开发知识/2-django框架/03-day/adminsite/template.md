# 调整站点信息 {#调整站点信息}

Admin站点的名称信息也是可以自定义的。

未调整前如下图：

![](/assets/admin_before.png)

* **admin.site.site\_header**设置网站页头
* **admin.site.site\_title**设置页面标题
* **admin.site.index\_title**设置首页标语

在book/admin.py文件中添加一下信息

```
from django.contrib import admin

admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用传智书城MIS'
```

刷新网站，效果如下

![](/assets/admin_after.png)



