import unittest,os,sys
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from function_page.login import login_page
from function_page.post import post_page

class PostPageTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost/startbbs/index.php")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def setUp(self):
        self.login_page = login_page(self.driver)
        self.post_page = post_page(self.driver)

    def tearDown(self):
        # 删除本站点的cookies
        self.driver.delete_all_cookies()
        self.login_page.user_loginout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()    
    
    def testcase_01_normal_post(self):
        self.login_page.user_login("test1", "123456")
        sleep(5)
        title = "test01"
        content = "每個人都會累，沒人能為你承擔所有悲傷，人總有一段時間要學會自己長大。"
        self.post_page.user_post(title, content)
        sleep(5)
        actual_post = self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/h2[1]")
        actual_title = actual_post.text
        self.assertEqual(actual_title, title)
    
    def testcase_02_duplicate_post(self):
        self.login_page.user_login("test1", "123456")
        sleep(5)
        title = ""
        content = "每個人都會累，沒人能為你承擔所有悲傷，人總有一段時間要學會自己長大。"
        self.post_page.user_post(title, content)
        sleep(5)
        actual_new = self.driver.find_element_by_xpath("//p[contains(text(),'请输入标题')]")
        actual_t = actual_new.text
        self.assertEqual(actual_t, "请输入标题")

    def testcase_03_duplicate_post(self):
        self.login_page.user_login("test1", "123456")
        sleep(5)
        title = "teststart"
        content = ""
        self.post_page.user_post(title, content)
        sleep(5)
        actual_content = self.driver.find_element_by_xpath("//p[contains(text(),'请输入内容')]")
        actual_ti = actual_content.text
        self.assertEqual(actual_ti, "请输入内容")

    def testcase_04_duplicate_post(self):
        self.login_page.user_login("test1", "123456")
        sleep(5)
        title = "te"
        content = "每個人都會累，沒人能為你承擔所有悲傷，人總有一段時間要學會自己長大。"
        self.post_page.user_post(title, content)
        sleep(5)
        actual_post_empt = self.driver.find_element_by_xpath("//p[contains(text(),'标题至少需要4个字')]")
        actual_title_empt = actual_post_empt.text
        self.assertEqual(actual_title_empt, "标题至少需要4个字")

    def testcase_05_duplicate_post(self):
        self.login_page.user_login("test1", "123456")
        sleep(5)
        title = "teststart"
        content = "te"
        self.post_page.user_post(title, content)
        sleep(5)
        actual_post_new = self.driver.find_element_by_xpath("//p[contains(text(),'内容至少需要8个字')]")
        actual_title_new = actual_post_new.text
        self.assertEqual(actual_title_new, "内容至少需要8个字")

if __name__ == "__main__":
    unittest.main()
