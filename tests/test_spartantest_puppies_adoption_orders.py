import random
import unittest

from DriverSettings.browsersetup import BrowserSetup
from page_object.checkout_page import CheckoutPage
from page_object.commodities_page import CommodityPage
from page_object.home_page import HomePage


class AdoptionSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        BrowserSetup.browser_startup(self)

    # Adopt Brooke, add a Chewy Toy and a Travel Carrier, pay with Check
    def test_adoptDogBrook(self):
        HomePage.open_page(self)
        HomePage.add_dog_to_order(self, dogname="Brook", chew=True, carrier=True, DogNumber=0)
        CommodityPage.finalize_order(self)
        CommodityPage.click_complete(self)
        CheckoutPage.fill_data(self)
        CheckoutPage.payment_method_select(self, "Check")
        CheckoutPage.click_confirm(self)
        self.assertTrue(HomePage.purchase_success_check(self), True)

    # Adopt Sparky, add a Collar & Leash, pay with Credit Card
    def test_adoptDogSparky(self):
        HomePage.open_page(self)
        HomePage.add_dog_to_order(self, dogname="Sparky", collar=True, DogNumber=0)
        CommodityPage.finalize_order(self)
        CommodityPage.click_complete(self)
        CheckoutPage.fill_data(self)
        CheckoutPage.payment_method_select(self, "Credit card")
        CheckoutPage.click_confirm(self)
        self.assertTrue(HomePage.purchase_success_check(self), True)

    # Adopt 2 Random Dogs add a Collar & Leash to each, pay with Credit Card
    def test_adoptTwoRandomDogs(self):
        HomePage.open_page(self)
        HomePage.add_dog_to_order(self, collar=True, DogNumber=0)
        CommodityPage.click_another(self)
        HomePage.add_dog_to_order(self, collar=True, DogNumber=1)
        CommodityPage.finalize_order(self)
        CommodityPage.click_complete(self)
        CheckoutPage.fill_data(self)
        CheckoutPage.payment_method_select(self, "Credit card")
        CheckoutPage.click_confirm(self)
        self.assertTrue(HomePage.purchase_success_check(self), True)

    # Adopt 2 Random Dogs add a 3 Random Accessories to 1, pay with Credit Card
    def test_adoptTwoRandomOneWithThreeAccessories(self):
        HomePage.open_page(self)
        HomePage.add_dog_to_order(self, DogNumber=0)
        CommodityPage.click_another(self)
        # randomly selecting 3 accessories
        accessories = [True, True, True, True]
        accessories[random.randint(0, 3)] = False
        HomePage.add_dog_to_order(self, collar=accessories[0], chew=accessories[1], carrier=accessories[2], vet=accessories[3], DogNumber=1)
        CommodityPage.finalize_order(self)
        CommodityPage.click_complete(self)
        CheckoutPage.fill_data(self)
        CheckoutPage.payment_method_select(self, "Credit card")
        CheckoutPage.click_confirm(self)
        self.assertTrue(HomePage.purchase_success_check(self), True)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
