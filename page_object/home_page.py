import random

from selenium.webdriver.common.by import By

from page_object.commodities_page import CommodityPage
from page_object.overwiev_page import OverwievPage


class PuppyHomePage():
    dognamelist = ["Brook", "Hanna", "Maggie Mae", "Ruby Sue", "Tipsy", "Spud", "Twinkie"]
    puppiesonpage = ["/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/h3",
                     "/html/body/div[1]/div[1]/div[3]/div[3]/div/div[2]/h3",
                     "/html/body/div[1]/div[1]/div[3]/div[4]/div/div[2]/h3",
                     "/html/body/div[1]/div[1]/div[3]/div[5]/div/div[2]/h3"]
    txt_next_page = "//*[text()='Next →']"

    def openPage(self):
        self.driver.get("https://spartantest-puppies.herokuapp.com/agency?page=1")

    # Find specific puppy on adoption list, if name not specified then random one is selected
    def findPuppyOnList(self, name):
        dogname = str(name)
        for x in PuppyHomePage.puppiesonpage:
            puppy = self.driver.find_element(by=By.XPATH, value=x).text
            if str(name) == str(puppy):
                size = len(x)
                mod_string = x[:size - 9]
                mod_string = mod_string + "div[4]/form/input"
                return mod_string

        self.driver.find_element(by=By.XPATH, value=PuppyHomePage.txt_next_page).click()
        # infinite recursion possible, dont care for now
        return PuppyHomePage.findPuppyOnList(self, dogname)

    def addDogToOrder(self,dogname=None , collar=False, chew=False, carrier=False, vet=False):
        if dogname == None:
            dog = random.choice(PuppyHomePage.dognamelist)
            PuppyHomePage.dognamelist.remove(dog)
        else:
            dog = dogname
        puppy = PuppyHomePage.findPuppyOnList(self, dog)
        self.driver.find_element(by=By.XPATH, value=puppy).click()
        self.driver.find_element(by=By.XPATH, value=OverwievPage.xp_confirm).click()
        CommodityPage.selectCommodities(self, collar, chew, carrier, vet)
        self.assertTrue(dog in self.driver.page_source, True)


