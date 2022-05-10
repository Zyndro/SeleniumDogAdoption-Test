import random
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

    def test_adoptTwoRandomOneWithThreeAccessories(self):
        PuppyPage.adddog(self)
        CommodityPage.clickAnother(self)
        x = [True, True, True, True]
        x[random.randint(0, 3)] = False
        PuppyPage.adddog(self, collar=x[0], chew=x[1], carrier=x[2], vet=x[3])
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
