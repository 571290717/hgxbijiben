# Day90  部署项目——项目搬迁，快捷导出环境依赖包到requirements.txt

项目搬迁的时候，需要把当前的环境依赖包导出，然后到部署项目的服务器上安装依赖。 我们可以通过下面的命令执行，把依赖包导出到requirements.txt文件里。 生成requirements.txt

```
pip freeze > requirements.txt
```

安装requirements.txt依赖

```
pip install -r requirements.txt
```





```
ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
```