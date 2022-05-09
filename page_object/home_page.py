from selenium.webdriver.common.by import By
from page_object.overwiev_page import OverwievPage
from page_object.commodities_page import CommodityPage
import random

class PuppyPage():
    dognamelist = ["Brook", "Hanna", "Maggie Mae", "Ruby Sue", "Tipsy", "Spud", "Twinkie"]
    puppiesonpage = ["/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/h3",
                     "/html/body/div[1]/div[1]/div[3]/div[3]/div/div[2]/h3",
                     "/html/body/div[1]/div[1]/div[3]/div[4]/div/div[2]/h3",
                     "/html/body/div[1]/div[1]/div[3]/div[5]/div/div[2]/h3"]
    txt_next_page = "//*[text()='Next →']"

    def openPage(self):
        self.driver.get("https://spartantest-puppies.herokuapp.com/agency?page=1")

    def getPuppyLoc(self, name):
        dogname = str(name)
        for x in PuppyPage.puppiesonpage:
            puppy = self.driver.find_element(by=By.XPATH, value=x).text
            if str(name) == str(puppy):
                size = len(x)
                mod_string = x[:size - 9]
                mod_string = mod_string + "div[4]/form/input"
                return mod_string

        self.driver.find_element(by=By.XPATH, value=PuppyPage.txt_next_page).click()
        # infinite recursion possible, dont care for now
        return PuppyPage.getPuppyLoc(self, dogname)

    def adddog(self, collar=False, chew=False, carrier=False, vet=False):
        dog = random.choice(PuppyPage.dognamelist)
        PuppyPage.dognamelist.remove(dog)
        puppy = PuppyPage.getPuppyLoc(self, dog)
        self.driver.find_element(by=By.XPATH, value=puppy).click()
        self.driver.find_element(by=By.XPATH, value=OverwievPage.xp_confirm).click()
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
        self.assertTrue(dog in self.driver.page_source, True)