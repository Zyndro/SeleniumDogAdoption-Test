import random
import unittest

from DriverSettings.browsersetup import BrowserSetup
from page_object.checkout_page import CheckoutPage
from page_object.commodities_page import CommodityPage
from page_object.home_page import PuppyHomePage


class AdoptionSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        BrowserSetup.browserStartup(self)

    # Adopt Brooke, add a Chewy Toy and a Travel Carrier, pay with Check
    def test_adoptDogBrook(self):
        PuppyHomePage.openPage(self)
        PuppyHomePage.addDogToOrder(self, dogname="Brook", chew=True, carrier=True, DogNumber=0)
        CommodityPage.finalizeOrder(self)
        CommodityPage.clickComplete(self)
        CheckoutPage.fillData(self)
        CheckoutPage.paymentMethod(self, "Check")
        CheckoutPage.clickConfirm(self)
        self.assertTrue(PuppyHomePage.purchaseSuccessCheck(self), True)

    # Adopt Sparky, add a Collar & Leash, pay with Credit Card
    def test_adoptDogSparky(self):
        PuppyHomePage.openPage(self)
        PuppyHomePage.addDogToOrder(self, dogname="Sparky", collar=True, DogNumber=0)
        CommodityPage.finalizeOrder(self)
        CommodityPage.clickComplete(self)
        CheckoutPage.fillData(self)
        CheckoutPage.paymentMethod(self, "Credit card")
        CheckoutPage.clickConfirm(self)
        self.assertTrue(PuppyHomePage.purchaseSuccessCheck(self), True)

    # Adopt 2 Random Dogs add a Collar & Leash to each, pay with Credit Card
    def test_adoptTwoRandomDogs(self):
        PuppyHomePage.openPage(self)
        PuppyHomePage.addDogToOrder(self, collar=True, DogNumber=0)
        CommodityPage.clickAnother(self)
        PuppyHomePage.addDogToOrder(self, collar=True, DogNumber=1)
        CommodityPage.finalizeOrder(self)
        CommodityPage.clickComplete(self)
        CheckoutPage.fillData(self)
        CheckoutPage.paymentMethod(self, "Credit card")
        CheckoutPage.clickConfirm(self)
        self.assertTrue(PuppyHomePage.purchaseSuccessCheck(self), True)

    # Adopt 2 Random Dogs add a 3 Random Accessories to 1, pay with Credit Card
    def test_adoptTwoRandomOneWithThreeAccessories(self):
        PuppyHomePage.openPage(self)
        PuppyHomePage.addDogToOrder(self, DogNumber=0)
        CommodityPage.clickAnother(self)
        # randomly selecting 3 accessories
        accessories = [True, True, True, True]
        accessories[random.randint(0, 3)] = False
        PuppyHomePage.addDogToOrder(self, collar=accessories[0], chew=accessories[1], carrier=accessories[2], vet=accessories[3], DogNumber=1)
        CommodityPage.finalizeOrder(self)
        CommodityPage.clickComplete(self)
        CheckoutPage.fillData(self)
        CheckoutPage.paymentMethod(self, "Credit card")
        CheckoutPage.clickConfirm(self)
        self.assertTrue(PuppyHomePage.purchaseSuccessCheck(self), True)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
