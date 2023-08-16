# Day94 python+requests+pytest 接口自动化的实现

主要思路：
①对 requests 进行二次封装，做到定制化效果
②使用 excel 存放接口请求数据，作为数据驱动
③里面有一些功能模仿了 jmeter，比如用户参数定义、jsonpath 提取
④用 pytest 进行测试用例管理

**一、环境**

python==3.8.0
requests==2.31.0
pytest==7.4
还有一些其他第三方库例如 allure 报告、jsonpath 等
这块不过多介绍，安装 python 配置环境变量，pip install 命令安装所需插件即可

**二、项目目录结构**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/xAXvHmia17JrR5UtkKEtjWH7icpEx7XtvOEdvUDp134Fyug5IOGm4RsoW2Vv5MYB5Labt0MR0BPiakgyvLRkwRk0Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

1、config：用来存放项目配置文件，包括接口基础配置，数据库信息等，使用的是 configparser 进行读取

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/xAXvHmia17JrR5UtkKEtjWH7icpEx7XtvORROpwKBSMlMtANVQ4PluIsKGNniaTxBTibqBNgDJcAvxoJc12GyE4nibw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

2、Outputs 层存放了日志和测试报告，这里报告用的是 allure

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/xAXvHmia17JrR5UtkKEtjWH7icpEx7XtvOfE2cdRlV8m5MNicY9pUpLMzx6W17OWeNbciceDGF0d3vwcIjia6Ndloug/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/xAXvHmia17JrR5UtkKEtjWH7icpEx7XtvOORzpxh9dfQw8ZrhoIq1eJ3wcfWX3OQUQYliaVCibDHaD6zibibY0eTJanQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

3、resources 存放的是测试数据 (这里用的 excel 作为接口数据驱动) 以及其他的一些测试文件等

4、Testcases 存放测试类

5、utils：工具类，包含了读取配置、记录日志、http 请求、接口数据处理等功能

**三、重点功能介绍**

**1、读取 excel**

实现代码如下：

```
from openpyxl import load_workbookclass DoExcel:

    def __init__(self, file_name):  
        # 打开文件        self.filepath = os.path.join(resources,'case_datas', f'{file_name}.xlsx')
        # 获取工作表        self.wb = load_workbook(self.filepath)
        # 获取当前sheet        self.ws = self.wb.active

    def get_data_from_excel(self):
        '''从excel获取测试数据'''
        datas = []
        for row in range(1, self.ws.max_row + 1):
            row_data = {}
            if row > 1:
                # 将行数据转为字典数据格式                for column in range(1, self.ws.max_column + 1):
                    row_data[f"{self.ws.cell(1, column).value}"] = self.ws.cell(row, column).value

                # 将json_path转字典                if row_data["json_path"]:
                    row_data["json_path"] = {k: v for item in row_data["json_path"].split("&") for k, v in[item.split("=")]}

                datas.append(row_data)
        self.wb.close()
        return datas

    def close(self):
        # 关闭文件流        self.wb.close()
```

数据文档格式：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/xAXvHmia17JrR5UtkKEtjWH7icpEx7XtvO8CfZVdAZkhqnSBGQ5NcBiaYqRs1Vxcm4ob9EaorYDIwjAwZsibd5ks0Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

（这里目前只支持单 sheet 页读取，后续将扩展成 sheet 名称传参获取方式）

**2、requests 请求部分**

```
import requestsclass HttpRequest:

    def __init__(self):
        self.session = requests.sessions.session()
        self.global_headers = {"X-Request-Sign": "xxxxxxxxx"}

    def set_headers(self, path, content_type, headers):
        # 判断接口是登录时，将Authorization请求头删除        if path in ["oauth/oauth/userlogin", "/oauth/oauth/login"] and "Authorization" in self.global_headers.keys():
            self.global_headers.pop("Authorization")

        # 判断content_type为json时，添加请求头content_type        if content_type == "json":
            self.global_headers["Content-Type"] = "application/json;charset=UTF-8"
        # 判断content_type不为json时,删除请求头content_type        elif content_type != "json" and "Content-Type" in self.global_headers.keys():
            self.global_headers.pop("Content-Type")

        # 将接口信息中的请求头更新到global_headers中        if headers:
            self.global_headers.update(headers)

    def set_token(self, path, res_code, res_json):
        # 请求接口为登录并且返回成功时，将token附加到headers里        if path == "/oauth/oauth/login" and res_code == 200:
            token = json_path(res_json, "$.data.access_token")
            self.global_headers["Authorization"] = f"Bearer {token}"

    def clear_headers(self, headers):
        # 清除无用的请求头        if headers:
            for i in headers.keys():
                if i in self.global_headers.keys():
                    self.global_headers.pop(i)

    def http_request(self, datas, file=None):
        log_info.log_info('--------------------')
        log_info.log_info('↓↓↓↓↓接口请求开始↓↓↓↓↓')

        # 拼接url  base从配置文件获取+参数传递接口路径        urls = config.get_strValue('api', 'base_url') + datas["path"]

        self.set_headers(path=datas["path"], content_type=datas["content_type"], headers=datas["headers"])

        log_info.log_info(f'接口名称:{datas["desc"]}')
        log_info.log_info(f"请求地址:{urls}")
        log_info.log_info(f"请求头:{self.global_headers}")
        log_info.log_info(f'请求参数:{datas["params"]}')
        print((f"请求地址:{urls}"))
        res = None
        # 请求封装，这里用的session会话保持，https请求需要将verify设置为False        try:
            if datas["method"].lower() == 'get':
                res = self.session.request(datas["method"], urls, params=datas["params"], headers=self.global_headers,
                                           verify=False)
            elif datas["method"].lower() == 'post':
                if datas["content_type"] in ["form", "upload"]:
                    res = self.session.request(datas["method"], urls, data=datas["params"], headers=self.global_headers,
                                               files=file,verify=False)
                elif datas["content_type"] == "json":
                    res = self.session.request(datas["method"], urls, json=datas["params"], headers=self.global_headers,
                                               verify=False)

            log_info.log_info(f"响应信息:{res.text}")
        except Exception as e:
            log_info.log_info(e)
            raise e

        self.set_token(path=datas["path"], res_code=res.status_code, res_json=res.json())
        self.clear_headers(headers=datas["headers"])

        log_info.log_info('↑↑↑↑↑接口请求结束↑↑↑↑↑')
        log_info.log_info('--------------------')
        return res

    def close(self):
        self.session.close()
```

在这里我根据项目情况，进行了请求头的特殊处理；
①实例化对象的时候添加了全局请求头
②根据不同类型的请求和传参格式对 content-type 做了相应处理
③token 的处理
④最后请求后把当前无用请求头部分做了清理

**3、接口数据处理**

```
class DataHandle:

    def datas_init(self,datas,params_list):
        self.datas = datas
        self.params_list = params_list

    def headers_handle(self):
        # 将请求头进行参数化        if self.datas["headers"]:
            self.datas["headers"] = re_replace(self.datas["headers"], self.params_list)
        # 请求头转字典格式        if self.datas["headers"]:
            self.datas["headers"] = {k: v for item in self.datas["headers"].split("&") for k, v in [item.split("=", 1)]}
        return self.datas["headers"]

    def params_handle(self):
        # 将请求参数进行参数化        if self.datas["params"]:
            self.datas["params"] = re_replace(self.datas["params"], self.params_list)

        # 这里把请求参数格式化，转成不同方法需要的参数格式        # 将form表单格式的参数转化成字典        if self.datas["content_type"] in ["form","upload"] and self.datas["params"]:
            self.datas["params"] = {k: v for item in self.datas["params"].split("&") for k, v in [item.split("=")]}
        # 将json字符串解包为字典        elif self.datas["content_type"] == "json":
            self.datas["params"] = eval(self.datas["params"])

        return self.datas["params"]

    def user_var_handle(self,res):
        # 获取响应信息中下文接口用到的参数        if self.datas["json_path"]:
            for i in self.datas["json_path"].keys():
                self.params_list[i] = json_path(res.json(), self.datas["json_path"][i])

        return self.params_list

    def assert_handle(self,res):
        # 将预期结果处理        if self.datas["except"]:
            # 参数化替换            self.datas["except"] = re_replace(self.datas["except"], self.params_list)
            # 转成字符串列表            self.datas["except"] = self.datas["except"].split("&")

        # 断言        for i in self.datas["except"]:
            print(f"断言:{i}")
            assert i in res.text

    def send_request(self,datas,file=None):
        res = http_request.http_request(datas,file)
        return res
```

这里主要做了几点处理：
①将请求头部分做了参数化替换并进行了数据格式转换，转为字典格式
②请求 body 进行参数化，并根据请求方式和 content-type 做了相应处理
③用户参数处理，用 jsonpath 获取响应信息字段值存放到测试类属性中
④预期结果断言处理（这里统一用的自带的 assert 方法，还没进行二次封装）
⑤将更新后的 data 发送请求

**4、测试类，测试方法**

```
class TestDemo(DataHandle):
    params_list = {'custName': unique_string(), "custCertiNo": random_string(),
                   "custLegalPersonCertiNo": random_string(18), "custBankAccount": random_string(18),
                   "managerStamp":{"file": ("testpicture.png", open(upload_file + "\\" + "testpicture.png", "rb"), "image/png")}
                   }

    @ pytest.mark.usefixtures("login_guanliren")
    @ pytest.mark.parametrize("datas", DoExcel("demo").get_data_from_excel())
    def test_case(self, datas):
        # 数据初始化        self.datas_init(datas, self.params_list)
        # 请求头处理        datas["headers"] = self.headers_handle()
        # 请求参数处理        datas["params"] = self.params_handle()
        # 获取文件名        filename = datas["filename"]
        # 发送接口请求        res = self.send_request(datas=datas,file=self.params_list[filename] if datas["content_type"] == "upload" else None)
        # 参数列表处理        self.params_list = self.user_var_handle(res)
        # 预期结果及断言        self.assert_handle(res)
```

这里测试类继承了上面的 DataHandle 类，测试方法中可以调用父类方法进行测试数据的处理
params_list 是用字典存放的参数化的数据，我这里是通过正则替换把请求参数里面的需要被替换的部分找到 params_list 里的 key，将 value 进行替换

**5、runner 执行测试用例**

```
import pytestfrom project.utils.base_dir import *if __name__ == '__main__':
    pytest.main(['-vs', f'{test_class}', f'--alluredir={allure_dir} ', '--clean-alluredir'])
    os.system(f"allure generate {allure_dir} -o {allure_html} --clean")
```

调用 pytest 的 main 方法进行命令行参数执行，添加了 allure 生成测试报告

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/xAXvHmia17JrR5UtkKEtjWH7icpEx7XtvOdCibrml3ibsspOopPOfRVTnLibroNOWxY2zhkeWVtL4jBjhETuenpwdAA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**6、测试报告展示**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/xAXvHmia17JrR5UtkKEtjWH7icpEx7XtvObhv7duxdCNGTBzS6NR8CErdSzcHYjALQ7vzUkEzs12h6GGUWONU0AQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/xAXvHmia17JrR5UtkKEtjWH7icpEx7XtvOibOHGOnW48GDbfABULx1SNEs91k4U4shGT2oloria1ibAosNicMpJxSY0A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**7、未完成功能**

①excel 读取：现在只支持当前 sheet 页读取，后续扩展成传 sheet 名称指定获取
②数据库断言：excel 添加一列存放 sql 语句，发送接口请求后查询数据库，将这部分加进断言里
③http_requests 目前只有 get 和 post 方法，后续将其他方法也封装进去
④断言方式：目前没有对断言封装，用的自带的 assert 函数，后面可以进行二次封装或用第三方库实现

**最后希望可以给一些想要入手自动化的同学们一些参考吧，也希望各路大神留言提提意见。**

------

附上百度网盘链接，有需要的可以拿走，谢谢支持！
链接：https://pan.baidu.com/s/1IhDP2PwNGEkJycqgopDmjg
提取码：ztje