import random

from selenium.webdriver.common.by import By

from page_object.commodities_page import CommodityPage
from page_object.overview_page import OverviewPage


class HomePage():

    id_purchase_notice = "notice"
    dog_name_list = ["Brook", "Hanna", "Maggie Mae", "Ruby Sue", "Tipsy", "Spud", "Twinkie"]
    puppy_adopt_button_location = ["/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/h3",
                     "/html/body/div[1]/div[1]/div[3]/div[3]/div/div[2]/h3",
                     "/html/body/div[1]/div[1]/div[3]/div[4]/div/div[2]/h3",
                     "/html/body/div[1]/div[1]/div[3]/div[5]/div/div[2]/h3"]
    txt_next_page = "//*[text()='Next →']"

    def purchase_success_check(self):
        if self.driver.find_element(by=By.ID, value=HomePage.id_purchase_notice).text == "Thank you for adopting a puppy!":
            return True

    def open_page(self):
        self.driver.get("https://spartantest-puppies.herokuapp.com/agency?page=1")

    # Find specific puppy on adoption list, if name not specified then random one is selected
    def find_puppy_on_list(self, name):
        dogname = str(name)
        for x in HomePage.puppy_adopt_button_location:
            puppy = self.driver.find_element(by=By.XPATH, value=x).text
            if str(name) == str(puppy):
                size = len(x)
                mod_string = x[:size - 9]
                mod_string = mod_string + "div[4]/form/input"
                return mod_string

        self.driver.find_element(by=By.XPATH, value=HomePage.txt_next_page).click()
        # infinite recursion possible, dont care for now
        return HomePage.find_puppy_on_list(self, dogname)

    # Dognumber starts at zero
    def add_dog_to_order(self, dogname=None, collar=False, chew=False, carrier=False, vet=False, DogNumber=0):
        if dogname == None:
            dog = random.choice(HomePage.dog_name_list)
            HomePage.dog_name_list.remove(dog)
        else:
            dog = dogname
        puppy = HomePage.find_puppy_on_list(self, dog)
        self.driver.find_element(by=By.XPATH, value=puppy).click()
        OverviewPage.click_confirm(self)
        self.assertTrue(dog in self.driver.page_source, True)
        CommodityPage.assign_accesories_to_dog(self, collar, chew, carrier, vet, DogNumber)


