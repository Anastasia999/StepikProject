from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def open_cart(self):
        self.browser.find_element(*BasePageLocators.CART_BUTTON).click()
        assert self.is_element_present(*BasePageLocators.PAGE_HEADER), \
                           "Cart isn't opened"

    def input_search_request(self, search_text):
        search_field = self.browser.find_element(*BasePageLocators.SEARCH_PRODUCT_INPUT)
        search_field.clear()
        search_field.send_keys(search_text)
        self.browser.find_element(*BasePageLocators.SEARCH_BUTTON).click()
        search_title = self.browser.find_element(*BasePageLocators.PAGE_HEADER).text
        assert search_text in search_title, "Incorrect page title for found book"


    def should_be_correct_amount_search_result(self):
        result_amount = self.browser.find_elements(*BasePageLocators.FOUND_PRODUCTS_AMOUNT)
        assert result_amount != 1, "Incorrect amount of search result"


    def should_be_correct_search_product_name(self, name):
        product_name = self.browser.find_element(*BasePageLocators.FOUND_PRODUCT_TITLE).text
        assert name in product_name, "Not found book by name"

    def should_be_correct_search_product_image(self,name):
        product_image = self.browser.find_element(*BasePageLocators.FOUND_PRODUCT_IMG)
        attribute_value = product_image.get_attribute("alt")
        assert name in attribute_value, "Incorrect product image"


    def should_be_correct_search_product_price(self,price):
        product_price =  self.browser.find_element(*BasePageLocators.FOUND_PRODUCT_PRICE).text
        assert price in product_price, "Incorrect product price"

