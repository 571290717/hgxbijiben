
import time
import HTMLTestRunner
import unittest


# 加载当前目录
test_dir='webstudy\.a_a_unittest'


# 加载当前目录下test开头的.py文件
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")


if __name__ == '__main__':
    # 定义报告目录
    file_dir="webstudy\.a_a_unittest"
    # 定义报告名称格式
    nowtime=time.strftime("%Y-%m-%d %H_%M_%S")
    # 报告完整路径和名称
    file_name=file_dir+nowtime+"Report11.html"
    with open(file_name,"wb")as f:
        # 实例化HTMLTestRunenr对象，传入报告文件流f
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="iweb_shop项目Web自动化测试报告",description="测试用例共计2条")
        runner.run(discover)