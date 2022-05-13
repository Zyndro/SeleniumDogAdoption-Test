from selenium.webdriver.common.by import By


class OverviewPage():
    xp_confirm = "/html/body/div[1]/div[1]/div[3]/div[2]/div/form/input[1]"
    xp_back = "/html/body/div[1]/div[1]/div[3]/a"

    def click_confirm(self):
        self.driver.find_element(by=By.XPATH, value=OverviewPage.xp_confirm).click()

    def click_back(self):
        self.driver.find_element(by=By.XPATH, value=OverviewPage.xp_back).click()
