import unittest

from selenium.webdriver.common.by import By

from driversettings.browser import browser
from page_object.checkout_page import CheckoutPage
from page_object.commodities_page import CommodityPage
from page_object.home_page import PuppyPage
from page_object.overwiev_page import OverwievPage


class Adoption(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser.browserSettings(self)

    def test_adoptBrook(self):
        puppy = PuppyPage.getPuppyLoc(self, "Brook")
        self.driver.find_element(by=By.XPATH, value=puppy).click()
        self.driver.find_element(by=By.XPATH, value=OverwievPage.xp_confirm).click()
        self.driver.find_element(by=By.ID, value=CommodityPage.id_toy).click()
        self.driver.find_element(by=By.ID, value=CommodityPage.id_carrier).click()
        self.assertTrue(("Brook") in self.driver.page_source, True)
        self.driver.find_element(by=By.XPATH, value=CommodityPage.xp_complete).click()
        CheckoutPage.fillData(self)
        CheckoutPage.paymentMethod(self, "Check")
        self.driver.find_element(by=By.XPATH, value=CheckoutPage.xp_confirm).click()
        self.assertTrue(("Thank you for adopting a puppy!") in self.driver.page_source, True)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
