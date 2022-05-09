from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from page_object.home_page import PuppyPage


class browser():
    def browserSettings(self):
        self.deca = DesiredCapabilities().FIREFOX
        self.deca["pageLoadStrategy"] = "normal"
        self.driver = webdriver.Firefox(desired_capabilities=self.deca)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        PuppyPage.openPage(self)
