import unittest,os,sys
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from function_page.register import register_page
from function_page.login import login_page

class RegisterPageTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost/startbbs/index.php")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
    
    def setUp(self):
        pass

    def tearDown(self):
        # 删除本站点的cookies
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def testcase_01_normal_register(self):
        """正常注册"""
        self.normal_register = register_page(self.driver)
        self.normal_register.New_User_Registration("test04", "test04@163.com", "123456", "123456")
        sleep(5)
    # 预期结果的校验：有【用户信息】的图标    
        try:
            user_information = self.driver.find_element_by_xpath("//a[@class='dropdown-toggle']")
            self.login_page = login_page(self.driver)
            self.login_page.user_loginout()
            self.assertTrue(True)
        except NoSuchElementException as identifier:
            self.assertTrue(False)

    def testcase_02_username_duplicate(self):
        self.abnormal_register1 = register_page(self.driver)
        self.abnormal_register1.New_User_Registration("test1", "test0001@163.com", "123456", "123456")
        sleep(3)
        span_occupation_name = self.driver.find_element_by_xpath("//p[contains(text(),'该用户名已被使用')]")
        occupation_name = span_occupation_name.text
        self.assertEqual(occupation_name, "该用户名已被使用")

    def testcase_03_email_duplicate(self):
        self.abnormal_register2 = register_page(self.driver)
        self.abnormal_register2.New_User_Registration("test9999", "test1@163.com", "123456", "123456")
        sleep(3)
        span_occupation_emial = self.driver.find_element_by_xpath("//p[contains(text(),'该邮箱已被使用')]")
        occupation_emial = span_occupation_emial.text
        self.assertEqual(occupation_emial, "该邮箱已被使用")

    def testcase_04_email_format(self):
        self.abnormal_register3 = register_page(self.driver)
        self.abnormal_register3.New_User_Registration("test9999", "test1@163", "123456", "123456")
        sleep(3)
        span_occupation_emial_format = self.driver.find_element_by_xpath("//p[contains(text(),'邮箱无效的email')]")
        occupation_emial_format = span_occupation_emial_format.text
        self.assertEqual(occupation_emial_format, "邮箱无效的email")

    def testcase_05_passwd_length(self):
        self.abnormal_register4 = register_page(self.driver)
        self.abnormal_register4.New_User_Registration("test9999", "test999@163.com", "123", "123")
        sleep(3)
        span_invalid_passwd_length = self.driver.find_element_by_xpath("//p[contains(text(),'密码至少需要6个字')]")
        invalid_passwd_length = span_invalid_passwd_length.text
        self.assertEqual(invalid_passwd_length, "密码至少需要6个字")

    def testcase_06_passwd_inconsistent(self):
        self.abnormal_register5 = register_page(self.driver)
        self.abnormal_register5.New_User_Registration("test9999", "test999@163.com", "123456", "123789")
        sleep(3)
        span_invalid_passwd_inconsistent = self.driver.find_element_by_xpath("//p[contains(text(),'重复密码和密码不一致')]")
        invalid_passwd_inconsistent = span_invalid_passwd_inconsistent.text
        self.assertEqual(invalid_passwd_inconsistent, "重复密码和密码不一致")

    def testcase_07_name_empty(self):
        self.abnormal_register6 = register_page(self.driver)
        self.abnormal_register6.New_User_Registration("", "test999@163.com", "123456", "123456")
        sleep(3)
        span_name_empty = self.driver.find_element_by_xpath("//p[contains(text(),'请输入用户名')]")
        name_empty = span_name_empty.text
        self.assertEqual(name_empty, "请输入用户名")

    def testcase_08_passwd_empty(self):
        self.abnormal_register7 = register_page(self.driver)
        self.abnormal_register7.New_User_Registration("test9999", "test999@163.com", "", "123789")
        sleep(3)
        span_passwd_empty = self.driver.find_element_by_xpath("//p[contains(text(),'请输入密码')]")
        passwd_empty = span_passwd_empty.text
        self.assertEqual(passwd_empty, "请输入密码")

    def testcase_09_emial_empty(self):
        self.abnormal_register8 = register_page(self.driver)
        self.abnormal_register8.New_User_Registration("test9999", "", "123456", "123456")
        sleep(3)
        span_emial_empty = self.driver.find_element_by_xpath("//p[contains(text(),'请输入邮箱')]")
        emial_empty = span_emial_empty.text
        self.assertEqual(emial_empty, "请输入邮箱")

    def testcase_10_surepasswd_empty(self):
        self.abnormal_register9 = register_page(self.driver)
        self.abnormal_register9.New_User_Registration("test9999", "test999@163.com", "123456", "")
        sleep(3)
        span_surepasswd_empty = self.driver.find_element_by_xpath("//p[contains(text(),'请输入重复密码')]")
        surepasswd_empty = span_surepasswd_empty.text
        self.assertEqual(surepasswd_empty, "请输入重复密码")

    def testcase_11_name_special(self):
        self.abnormal_register10 = register_page(self.driver)
        self.abnormal_register10.New_User_Registration("#$%test999", "test9999@163.com", "123456", "123456")
        sleep(3)
        span_name_special = self.driver.find_element_by_xpath("//p[contains(text(),'用户名 只能含有汉字、数字、字母、下划线（不能开头或结尾)')]")
        name_special = span_name_special.text
        self.assertEqual(name_special, "用户名 只能含有汉字、数字、字母、下划线（不能开头或结尾)")

    def testcase_12_name_length(self):
        self.abnormal_register11 = register_page(self.driver)
        self.abnormal_register11.New_User_Registration("test1test1test1test1", "test999@163.com", "123456", "123456")
        sleep(3)
        span_name_length = self.driver.find_element_by_xpath("//p[contains(text(),'用户名不超过15个字')]")
        name_length = span_name_length.text
        self.assertEqual(name_length, "用户名不超过15个字")


if __name__ == "__main__":
    unittest.main()
