from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_correct_name_product(self):
        message_product = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT).text
        assert self.default_name_of_the_product() == message_product, "Name product incorrect"

    def should_be_correct_price_product(self):
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert self.default_price_of_the_product() == message_price, "Price product incorrect"

    def default_price_of_the_product(self):
        default_price_name = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        return default_price_name

    def default_name_of_the_product(self):
        default_product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        return default_product_name

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_SUCCESS), \
            "Success message is presented, but should not be"
