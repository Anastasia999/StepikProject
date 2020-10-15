from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def check_product_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_CART), \
                  "Basket contains product"

    def should_be_empty_cart_alert(self):
        alert_about_empty_cart = self.browser.find_element(*BasketPageLocators.EMPTY_CART_ALERT).text
        assert "Your basket is empty" in alert_about_empty_cart, \
                  "Cart isn't empty"

    def calculate_products_in_cart(self):
        result_amount = self.browser.find_elements(*BasketPageLocators.PRODUCTS_AMOUNT_IN_CART)
        assert result_amount != 1, "Incorrect amount of products"

    def should_be_correct_product_name(self, name):
        product_name = self.browser.find_element(*BasketPageLocators.NAME_PRODUCT_IN_CART).text
        assert name in product_name, "Incorrect product name"


    def should_be_correct_product_amount(self):
        product_amount = self.browser.find_element(*BasketPageLocators.AMOUNT_ADDED_PRODUCT_IN_CART)
        amount_value = product_amount.get_attribute("value")
        assert "1" in amount_value, "Inccorrect product amount"


    def should_be_correct_product_price(self, price):
        product_price = self.browser.find_element(*BasketPageLocators.PRICE_PRODUCT_IN_CART).text
        assert price in product_price, "Incorrect product price"


    def should_be_correct_product_image(self, name):
        product_image = self.browser.find_element(*BasketPageLocators.IMAGE_PRODUCT_IN_CART)
        attribute_value = product_image.get_attribute("alt")
        assert name in attribute_value, "Incorrect product image"