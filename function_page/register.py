from selenium import webdriver
from time import sleep

class register_page:

    def __init__(self,driver):
        self.driver = driver
        
    def New_User_Registration(self, name, E_Mail, passwd, Confirm_Password):
        '''新用户注册功能'''
        element_register = self.driver.find_element_by_link_text("注册")
        element_register.click()
        sleep(2)
        element_name = self.driver.find_element_by_xpath("//input[@id='user_nickname']")
        element_name.clear()
        element_name.send_keys(name)
        element_mail = self.driver.find_element_by_xpath("//input[@id='user_email']")
        element_mail.clear()
        element_mail.send_keys(E_Mail)
        element_passwd = self.driver.find_element_by_xpath("//input[@id='user_password']")
        element_passwd.clear()
        element_passwd.send_keys(passwd)
        element_Confirm_Password = self.driver.find_element_by_xpath("//input[@id='user_password_confirmation']")
        element_Confirm_Password.clear()
        element_Confirm_Password.send_keys(Confirm_Password)
        element_Confirm_register = self.driver.find_element_by_xpath("//button[@name='commit']")
        element_Confirm_register.click()
