from selenium import webdriver
from time import sleep

class post_page:

    def __init__(self,driver):
        self.driver = driver
    
    def user_post(self, title, content):
        """用户发表帖子模块"""
        element_post = self.driver.find_element_by_xpath("//a[contains(text(),'发表')]")
        element_post.click()
        sleep(3)
        element_title = self.driver.find_element_by_xpath("//input[@id='topic_title']")
        element_title.clear()
        element_title.send_keys(title)
        element_node = self.driver.find_element_by_xpath("//select[@id='node_id']")
        element_node.click()
        sleep(3)
        element_option = self.driver.find_element_by_xpath("//option[contains(text(),'c++')]")
        element_option.click()
        element_content = self.driver.find_element_by_xpath("//textarea[@id='post_content']")
        element_content.send_keys(content)
        element_submit = self.driver.find_element_by_xpath("//button[@class='btn btn-primary']")
        element_submit.click()

