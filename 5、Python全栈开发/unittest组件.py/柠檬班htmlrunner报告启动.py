from unittestreport import TestRunner
import unittest


# 第一步收集测试用例
suite = unittest.defaultTestLoader.discover(r"webstudy\.a_a_unittest")



#第二步：运行用例生产测试报告
runner = TestRunner(suite,
                filename="report.html",
                report_dir=r"webstudy\.a_a_unittest\reports",
                title='测试报告',
                tester='hgx测试员',
                desc="hgx项目测试生成的报告",
                templates=5)



runner.run()