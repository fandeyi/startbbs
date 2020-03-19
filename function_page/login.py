from selenium import webdriver
from time import sleep

class login_page:

    def __init__(self,driver):
        self.driver = driver
    
    def user_login(self, name, password):
        """用户登录模块"""
        element_login = self.driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right']//a[contains(text(),'登入')]")
        element_login.click()
        sleep(3)
        element_login_name = self.driver.find_element_by_xpath("//input[@id='user_nickname']")
        element_login_name.clear()
        element_login_name.send_keys(name)
        element_login_password = self.driver.find_element_by_xpath("//input[@id='user_password']")
        element_login_password.clear()
        element_login_password.send_keys(password)
        element_login_commit = self.driver.find_element_by_xpath("//button[@name='commit']")
        element_login_commit.click()
    def user_loginout(self):
        """用户退出功能"""
        element_loginout = self.driver.find_element_by_xpath("//a[@class='dropdown-toggle']")
        element_loginout.click()
        sleep(3)
        element_loginout_sure = self.driver.find_element_by_xpath("//a[contains(text(),'退出')]")
        element_loginout_sure.click()