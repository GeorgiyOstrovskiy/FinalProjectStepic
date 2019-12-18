from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_correct_name_product(self):
        message_product = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT).text
        default_product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert default_product_name in message_product, "Name product incorrect"

    def should_be_correct_price_product(self):
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        default_price_name = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert default_price_name in message_price, "Price product incorrect"
