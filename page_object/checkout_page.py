from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CheckoutPage():
    id_name = "order_name"
    id_adress = "order_address"
    id_email = "order_email"
    id_payment = "order_pay_type"
    xp_confirm = "/html/body/div[1]/div[1]/div[3]/div[2]/fieldset/form/div[5]/button/input"

    def fillData(self):
        self.driver.find_element(by=By.ID, value=CheckoutPage.id_name).send_keys('Test Test')
        self.driver.find_element(by=By.ID, value=CheckoutPage.id_adress).send_keys(
            '2137 California Ave, Saginaw, MI 48601')
        self.driver.find_element(by=By.ID, value=CheckoutPage.id_email).send_keys('test@test.com')

    def paymentMethod(self, method):
        select = Select(self.driver.find_element(by=By.ID, value=CheckoutPage.id_payment))
        select.select_by_visible_text(str(method))

    def clickConfirm(self):
        self.driver.find_element(by=By.XPATH, value=CheckoutPage.xp_confirm).click()
