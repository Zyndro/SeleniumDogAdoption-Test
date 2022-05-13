from selenium.webdriver.common.by import By


class OverwievPage():
    xp_confirm = "/html/body/div[1]/div[1]/div[3]/div[2]/div/form/input[1]"
    xp_back = "/html/body/div[1]/div[1]/div[3]/a"

    def clickConfirm(self):
        self.driver.find_element(by=By.XPATH, value=OverwievPage.xp_confirm).click()

    def clickBack(self):
        self.driver.find_element(by=By.XPATH, value=OverwievPage.xp_back).click()
