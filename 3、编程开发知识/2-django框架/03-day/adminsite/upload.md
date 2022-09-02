# 上传图片 {#上传图片}

Django有提供文件系统支持，在Admin站点中可以轻松上传图片。

使用Admin站点保存图片，需要安装Python的图片操作包

```
pip install Pillow
```

## 1 配置 {#1--配置}

默认情况下，Django会将上传的图片保存在本地服务器上，需要配置保存的路径。

我们可以将上传的文件保存在静态文件目录中，如我们之前设置的static目录中在settings.py 文件中添加如下上传保存目录信息

```
MEDIA_ROOT=os.path.join(BASE_DIR,"static/media")
```

![](/assets/static_media.png)

## 2 为模型类添加ImageField字段 {#2--为模型类添加imagefield字段}

我们为之前的BookInfo模型类添加一个ImageFiled

```
class BookInfo(models.Model):

    ...
    image = models.ImageField(upload_to='book', verbose_name='图片', null=True)
```

* upload\_to 选项指明该字段的图片保存在MEDIA\_ROOT目录中的哪个子目录

进行数据库迁移操作

```
python manage.py makemigrations
python manage.py migrate
```

## 3 使用Admin站点上传图片 {#3--使用admin站点上传图片}

进入Admin站点的图书管理页面，选择一个图书，能发现多出来一个上传图片的字段

![](/assets/admin_image.png)

选择一张图片并保存后，图片会被保存在**static/media/book/**目录下。

在数据库中，我们能看到image字段被设置为图片的路径

![](/assets/image_upload.png)

