import unittest

from selenium.webdriver.common.by import By

from DriverSettings.browser import browser
from page_object.checkout_page import CheckoutPage
from page_object.commodities_page import CommodityPage
from page_object.home_page import PuppyPage


class Adoption(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser.browserSettings(self)

    def test_adoptTwoRandom(self):
        PuppyPage.adddog(self, collar=True)
        self.driver.find_element(by=By.XPATH, value=CommodityPage.xp_addAnother).click()
        PuppyPage.adddog(self, collar=True)
        self.driver.find_element(by=By.XPATH, value=CommodityPage.xp_complete).click()
        CheckoutPage.fillData(self)
        CheckoutPage.paymentMethod(self, "Credit card")
        self.driver.find_element(by=By.XPATH, value=CheckoutPage.xp_confirm).click()
        self.assertTrue(("Thank you for adopting a puppy!") in self.driver.page_source, True)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
