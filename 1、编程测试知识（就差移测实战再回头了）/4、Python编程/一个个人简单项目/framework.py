"""web框架的职责专门负责处理动态资源请求"""
import time
import pymysql
import json
import logging


# 路由列表, 列表里面的每一条记录都是一个路由
route_list = [
    # ("/index.html", index),
    # ("/center.html", center),
]


# 定义带有参数的装饰器
def route(path):
    # 装饰器
    def decorator(func):
        # 当执行装饰器的时候就需要把路由添加到路由列表里面,
        # 当装饰函数的时候只添加一次路由即可
        route_list.append((path, func))

        def inner():

            result = func()
            return result

        return inner
    # 返回一个装饰器
    return decorator


# 获取首页数据
@route("/index.html")  # => @decorator => index = decorator(index)
def index():
    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [("Server", "PWS/1.1")]
    # 1. 打开指定模板文件，读取模板文件中的数据
    with open("template/index.html", "r") as file:
        file_data = file.read()
    # 2. 查询数据库，模板里面的模板变量( {%content%}) 替换成以后从数据库里面查询的数据
    # 创建连接对象
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="mysql",
                           database="stock_db",
                           charset="utf8")

    # 获取游标
    cursor = conn.cursor()
    # 准备sql
    sql = "select * from info;"
    # 执行sql
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()
    print(result)
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    # 遍历每一条数据，完成数据的tr标签的封装
    data = ""
    for row in result:
        data += """<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
               </tr>""" % row

    response_body = file_data.replace("{%content%}", data)

    # 这里返回的是元组
    return status, response_header, response_body


# 个人中心数据接口
@route("/center_data.html")
def center_data():
    # 从数据库把数据查询出来，然后把查询处理的数据转成json数据
    # 创建连接对象
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="mysql",
                           database="stock_db",
                           charset="utf8")
    # 获取游标
    cursor = conn.cursor()
    # 准备sql
    sql = '''select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info 
             from info i inner join focus f 
             on i.id = f.info_id;
          '''
    # 执行sql
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()
    print(result)
    # 把元组转成列表字典
    center_data_list = [{
                            "code": row[0],
                            "short": row[1],
                            "chg": row[2],
                            "turnover": row[3],
                            "price": str(row[4]),
                            "highs": str(row[5]),
                            "note_info": row[6]
                         } for row in result]
    print(center_data_list)
    # 把列表转成json字符串数据
    # ensure_ascii=False 表示在控制台能够显示中文
    json_str = json.dumps(center_data_list, ensure_ascii=False)
    print(json_str)
    print(type(json_str))
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [
        ("Server", "PWS/1.1"),
        # 指定编码格式，因为没有模板文件，可以通过响应头指定编码格式
        ("Content-Type", "text/html;charset=utf-8")
    ]
    return status, response_header, json_str


# 获取个人中心数据
@route("/center.html")
def center():
    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [("Server", "PWS/1.1")]
    # 1. 打开指定模板文件，读取模板文件中的数据
    with open("template/center.html", "r") as file:
        file_data = file.read()
    # 2. 查询数据库，模板里面的模板变量( {%content%}) 替换成以后从数据库里面查询的数据

    response_body = file_data.replace("{%content%}", "")

    # 这里返回的是元组
    return status, response_header, response_body


# 处理没有找到的动态资源
def not_found():
    # 状态信息
    status = "404 Not Found"
    # 响应头信息
    response_header = [("Server", "PWS/1.1")]
    # web框架处理后的数据
    data = "not found"

    # 这里返回的是元组
    return status, response_header, data


# 处理动态资源请求
def handle_request(env):
    # 获取动态的请求资源路径
    request_path = env["request_path"]
    print("动态资源请求的地址:", request_path)

    # 遍历路由列表，匹配请求的url
    for path, func in route_list:
        if request_path == path:
            # 找到了指定路由，执行对应的处理函数
            result = func()
            return result
    else:
        # 没有动态资源数据, 返回404状态信息
        result = not_found()
        logging.error("没有设置相关的路由信息:" + request_path)
        # 把处理后的结果返回给web服务器使用，让web服务器拼接响应报文时使用
        return result


    # # 判断请求的动态资源路径，选择指定的函数处理对应的动态资源请求
    # if request_path == "/index.html":
    #     # 获取首页数据
    #     result = index()
    #     # 把处理后的结果返回给web服务器使用，让web服务器拼接响应报文时使用
    #     return result
    # elif request_path == "/center.html":
    #     # 获取个人中心数据
    #     result = center()
    #     return result
    # else:
    #     # 没有动态资源数据, 返回404状态信息
    #     result = not_found()
    #     # 把处理后的结果返回给web服务器使用，让web服务器拼接响应报文时使用
    #     return result

if __name__ == '__main__':
    center_data()
