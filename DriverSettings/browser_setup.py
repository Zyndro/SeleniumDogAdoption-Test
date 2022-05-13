from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class BrowserSetup():
    def browser_startup(self):
        # Change the desired browser by changing this function argument to either "Chrome" or "Firefox"
        BrowserSetup.load_browser(self, "Chrome")

    def load_browser(self, browser):
        if browser == "Chrome":
            self.deca = DesiredCapabilities().CHROME
            self.deca["pageLoadStrategy"] = "normal"
            self.driver = webdriver.Chrome(executable_path=r'./Drivers/chromedriver.exe', desired_capabilities=self.deca)
        if browser == "Firefox":
            self.deca = DesiredCapabilities().FIREFOX
            self.deca["pageLoadStrategy"] = "normal"
            self.driver = webdriver.Firefox(executable_path=r'./Drivers/geckodriver.exe',desired_capabilities=self.deca)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


