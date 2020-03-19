import unittest,os,sys
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from function_page.login import login_page

class LoginPageTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost/startbbs/index.php")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
    
    def setUp(self):
        self.login_page = login_page(self.driver)

    def tearDown(self):
        # 删除本站点的cookies
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def testcase_01_normal_login(self):
        """用户正常登陆"""
        self.login_page.user_login("test1", "123456")
        sleep(5)
        try:
            user1_information = self.driver.find_element_by_xpath("//a[@class='dropdown-toggle']")
            self.login_page.user_loginout()
            self.assertTrue(True)
        except NoSuchElementException as identifier:
            self.assertTrue(False)
    
    def testcase_02_name_notexist(self):
        self.login_page.user_login("testfy", "123456")
        sleep(5)
        try:
            span_name_notexist = self.driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right']//a[contains(text(),'登入')]")
            self.assertTrue(True)
        except NoSuchElementException as identifier:
            self.assertTrue(False)
            self.login_page.user_loginout()

    def testcase_03_passwd_notexist(self):
        self.login_page.user_login("test1", "123789")
        sleep(5)
        try:
            span_passwd_notexist = self.driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right']//a[contains(text(),'登入')]")
            self.assertTrue(True)
        except NoSuchElementException as identifier:
            self.assertTrue(False)
            self.login_page.user_loginout()

    def testcase_04_name_Empt(self):
        self.login_page.user_login("", "123456")
        sleep(3)
        span_name_Empt = self.driver.find_element_by_xpath("//p[contains(text(),'请输入用户名')]")
        name_Empt = span_name_Empt.text
        self.assertEqual(name_Empt, "请输入用户名")

    def testcase_05_passwd_Empt(self):
        self.login_page.user_login("test1", "")
        sleep(3)
        span_passwd_Empt = self.driver.find_element_by_xpath("//p[contains(text(),'请输入密码')]")
        passwd_Empt = span_passwd_Empt.text
        self.assertEqual(passwd_Empt, "请输入密码")

    def testcase_05_name_Length(self):
        self.login_page.user_login("test1test1test1test1", "123456")
        sleep(3)
        span_name_Length = self.driver.find_element_by_xpath("//p[contains(text(),'用户名不超过15个字')]")
        name_Length = span_name_Length.text
        self.assertEqual(name_Length, "用户名不超过15个字")

if __name__ == "__main__":
    unittest.main()
        