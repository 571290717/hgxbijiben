# Django 迁移   +++报错





## 2 迁移

将模型类同步到数据库中。

**1）生成迁移文件**

```
python manage.py makemigrations
```

**2）同步到数据库中**

```
python manage.py migrate
```





已安装情况下仍然报错
报错内容为找不到mysqlclient
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module. Did you install mysqlclient?

通常解决办法

**项目（settings.py同级)目录中init.py中添加**
import pymysql
pymysql.install_as_MySQLdb()
1
2
强制重装一下
pip install mysqlclient‑1.4.6‑cp38‑cp38‑win32.whl --force-reinstall