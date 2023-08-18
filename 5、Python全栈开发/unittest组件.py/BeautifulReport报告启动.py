import unittest
from BeautifulReport import BeautifulReport


# 收集测试用例
suite = unittest.defaultTestLoader.discover(r"webstudy\a_a_unittest")

# #创建一个测试套件
# suite = unittest.TestSuite()

# #创建一个用例加载器
# loader = unittest.TestLoader()

# #三、通过用例文件所在路径进行加载路径
# suite.addTest(loader.discover(r'C:\Users\180927\Desktop\hgxs\hgx自动化测试\webstudy\a_a_unittest'))

#获取套件中的用例数量
print('数量:',suite.countTestCases())


# #四、用例运行
# with open(r"webstudy\a_a_unittest\result.txt",'w',encoding='utf-8') as f :
#     runner = unittest.TextTestRunner(stream=f,verbosity=2)
#     runner.run(suite)


runner = BeautifulReport(suites=suite)
runner.report(description="11111",filename='666',report_dir=r"webstudy\a_a_unittest")