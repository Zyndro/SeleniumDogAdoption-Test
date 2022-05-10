import unittest

from DriverSettings.browser import browser
from page_object.checkout_page import CheckoutPage
from page_object.commodities_page import CommodityPage
from page_object.home_page import PuppyPage


class Adoption(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser.browserSettings(self)

    def test_adoptBrook(self):
        PuppyPage.adddog(self, dogname="Brook", chew=True, carrier=True)
        self.assertTrue(("Brook") in self.driver.page_source, True)
        CommodityPage.clickComplete(self)
        CheckoutPage.fillData(self)
        CheckoutPage.paymentMethod(self, "Check")
        CheckoutPage.clickConfirm(self)
        self.assertTrue(("Thank you for adopting a puppy!") in self.driver.page_source, True)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
