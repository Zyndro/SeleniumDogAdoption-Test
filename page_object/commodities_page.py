from selenium.webdriver.common.by import By


class CommodityPage():
    id_collar = "collar"
    id_toy = "toy"
    id_carrier = "carrier"
    id_vet = "vet"
    xp_complete = "/html/body/div[1]/div[1]/div[3]/div[2]/form[1]/input"
    xp_addAnother = "/html/body/div[1]/div[1]/div[3]/div[2]/form[2]/input"
    xp_resign = "/html/body/div[1]/div[1]/div[3]/div[2]/form[3]/input[2]"
    temp = []

    def clickComplete(self):
        self.driver.find_element(by=By.XPATH, value=CommodityPage.xp_complete).click()

    def clickAnother(self):
        self.driver.find_element(by=By.XPATH, value=CommodityPage.xp_addAnother).click()

    def assignAccesoriesToDog(self, collar, chew, carrier, vet, Dognumber):
        CommodityPage.temp.append([collar, chew, carrier, vet, Dognumber])

    def selectCommodities(self, collar=False, chew=False, carrier=False, vet=False, Dognumber=0):
        if collar == True:
            t = self.driver.find_elements(by=By.ID, value=CommodityPage.id_collar)
            t[Dognumber].click()
        if chew == True:
            t = self.driver.find_elements(by=By.ID, value=CommodityPage.id_toy)
            t[Dognumber].click()
        if carrier == True:
            t = self.driver.find_elements(by=By.ID, value=CommodityPage.id_carrier)
            t[Dognumber].click()
        if vet == True:
            t = self.driver.find_elements(by=By.ID, value=CommodityPage.id_vet)
            t[Dognumber].click()

    def finalizeOrder(self):
        for x in CommodityPage.temp:
            collar = x[0]
            chew = x[1]
            carrier = x[2]
            vet = x[3]
            Dognumber = x[4]
            CommodityPage.selectCommodities(self, collar, chew, carrier, vet, Dognumber)
        CommodityPage.temp = []
