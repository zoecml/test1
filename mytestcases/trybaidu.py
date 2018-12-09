from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest


class BaiduTest(unittest.TestCase):
    url = ""

    def setUp(self):
        self.url = "https://www.baidu.com"
        self.dr = webdriver.Firefox()
        self.dr.get(self.url)

    def test_search(self):
        # self.dr.get(self.url)
        self.dr.find_element_by_id("kw").clear()
        self.dr.find_element_by_id("kw").send_keys("selenium")
        self.dr.find_element_by_id("su").click()
        sleep(2)

    def test_setting(self):
        hover = self.dr.find_element_by_link_text("设置")
        ActionChains(self.dr).move_to_element(hover).perform()

        self.dr.find_element_by_link_text("搜索设置").click()

        sleep(2)

        self.dr.find_element_by_id("SL_1").click()
        options = self.dr.find_elements_by_xpath("//*[@id=\"nr\"]/option")
        for option in options:
            # if option.text == "每页显示20条":
            #     option.click()
            if option.get_attribute("value") == "20":
                option.click()
            # print(option.get_attribute("value"))

        self.dr.find_element_by_link_text("保存设置").click()
        sleep(2)
        self.dr.switch_to.alert.accept()
        # sleep(2)

    def tearDown(self):
        self.url = None
        self.dr.quit()


def mysuite():
    suite = unittest.TestSuite()
    suite.addTest(BaiduTest("test_search"))
    # suite.addTest(MyFirstUnit("test_case_list"))
    suite.addTest(BaiduTest("test_setting"))
    return suite


if __name__ == "__main__":
    # unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(mysuite())



