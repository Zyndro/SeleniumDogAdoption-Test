import unittest

from selenium.webdriver.common.by import By

from DriverSettings.browser import browser
from page_object.checkout_page import CheckoutPage
from page_object.commodities_page import CommodityPage
from page_object.home_page import PuppyPage
from page_object.overwiev_page import OverwievPage


class Adoption(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser.browserSettings(self)

    def test_adoptSparky(self):
        PuppyPage.adddog(self, dogname="Sparky", collar=True)
        self.assertTrue(("Sparky") in self.driver.page_source, True)
        CommodityPage.clickComplete(self)
        CheckoutPage.fillData(self)
        CheckoutPage.paymentMethod(self, "Credit card")
        CheckoutPage.clickConfirm(self)
        self.assertTrue(("Thank you for adopting a puppy!") in self.driver.page_source, True)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
