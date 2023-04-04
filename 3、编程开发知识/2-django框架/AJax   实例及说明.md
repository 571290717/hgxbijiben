# AJax   实例及说明





```html
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Ajax实战--城市级联操作</title>
        <script type="text/javascript" src="/static/jquery-1.8.2.min.js"></script>
        <script type="text/javascript">
            //编写js代码
            //jquery入口程序
            $(function(){
                //alert("ok");
                //使用jquery的Ajax请求加载城市信息
                 $.ajax({//这个就是发送一起请求 --固定形式以下
                    type : 'get',//请求方式
                    url : '{% url "district" 0 %}',//请求地址
                    dataType : 'json',//响应数据格式
                    async:false,//异步请求
                    success:function(res){//请求成功后返回（响应）的回调函数
                        //alert(res);
                        alert(res['data'][0]['name']);
                        //alert(res);
                    }

                 });
            });

        </script>
    </head>
    <body>
        <h2>Ajax实战--城市级联操作</h2>
        <script src="" async defer></script>
    </body>
</html>
```

