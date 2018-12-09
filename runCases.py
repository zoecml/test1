import unittest
import HTMLTestRunner
from mytestcases import trybaidu
from mytestcases import tryTestfan

mysuite = unittest.TestSuite()
mysuite.addTest(unittest.makeSuite(trybaidu.BaiduTest))
mysuite.addTest(unittest.makeSuite(tryTestfan.Testfan))

res_file = "Result1.html"
fp = open(res_file, "wb")

runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title = "百度搜索测试报告", description='用例执行情况')
runner.run(mysuite)