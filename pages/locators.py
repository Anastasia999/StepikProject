from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PSWD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PSWD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_REGISTRATION = (By.CSS_SELECTOR, "[name = 'registration_submit']")
    SUCCESS_REGISTRATION_ALERT = (By.CSS_SELECTOR, ".alertinner")


class ProductPageLocators():
    ADD_TO_CART_BUTTON_FROM_PRODUCT_PAGE = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_SUCCESS_ALERT = (By.CSS_SELECTOR, "#messages .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_CART = (By.CSS_SELECTOR, ".basket-mini")
    AVAILABLE_AMOUNT = (By.CSS_SELECTOR, ".icon-ok")
    CATALOG_LINK = (By.CSS_SELECTOR, "ul .dropdown-menu :nth-child(1)")
    CATALOG_HEADER = (By.CSS_SELECTOR, ".page-header h1")
    ADD_TO_CART_BUTTON_FROM_CATALOG_PAGE = (By.CSS_SELECTOR, "[action*='/basket/add/209/']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    CART_BUTTON = (By.CSS_SELECTOR, "[href*='/basket/']")
    PAGE_HEADER = (By.CSS_SELECTOR, ".page-header h1")
    SEARCH_PRODUCT_INPUT = (By.CSS_SELECTOR, "[type='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div input[type='submit']")
    FOUND_PRODUCTS_AMOUNT = (By.CSS_SELECTOR, ".product_pod")
    FOUND_PRODUCT_IMG = (By.CSS_SELECTOR, ".product_pod img")
    FOUND_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_pod .product_price .price_color")
    FOUND_PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_pod h3")

class BasketPageLocators():
    ITEMS_IN_CART = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_CART_ALERT = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCTS_AMOUNT_IN_CART = (By.CSS_SELECTOR, ".basket-items")
    NAME_PRODUCT_IN_CART = (By.CSS_SELECTOR, ".basket-items .col-sm-4 a")
    AMOUNT_ADDED_PRODUCT_IN_CART = (By.CSS_SELECTOR, ".basket-items [type='number']")
    PRICE_PRODUCT_IN_CART = (By.CSS_SELECTOR, ".price_color")
    IMAGE_PRODUCT_IN_CART = (By.CSS_SELECTOR, ".basket-items img")


