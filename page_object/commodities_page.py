from selenium.webdriver.common.by import By


class CommodityPage():
    id_collar = "collar"
    id_toy = "toy"
    id_carrier = "carrier"
    id_vet = "vet"
    xp_complete = "/html/body/div[1]/div[1]/div[3]/div[2]/form[1]/input"
    xp_addAnother = "/html/body/div[1]/div[1]/div[3]/div[2]/form[2]/input"
    xp_resign = "/html/body/div[1]/div[1]/div[3]/div[2]/form[3]/input[2]"

    def selectCommodities(self, collar=False, chew=False, carrier=False, vet=False):
        if collar == True:
            t = self.driver.find_elements(by=By.ID, value=CommodityPage.id_collar)
            for x in t:
                x.click()
        if chew == True:
            t = self.driver.find_elements(by=By.ID, value=CommodityPage.id_toy)
            for x in t:
                x.click()
        if carrier == True:
            t = self.driver.find_elements(by=By.ID, value=CommodityPage.id_carrier)
            for x in t:
                x.click()
        if vet == True:
            t = self.driver.find_elements(by=By.ID, value=CommodityPage.id_vet)
            for x in t:
                x.click()
