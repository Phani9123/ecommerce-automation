from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.cart_link = (
            By.CLASS_NAME,
            "shopping_cart_link"
        )

        self.cart_badge = (
            By.CLASS_NAME,
            "shopping_cart_badge"
        )

        self.backpack_item = (
            By.ID,
            "item_4_title_link"
        )

        self.backpack_remove_button = (
            By.ID,
            "remove-sauce-labs-backpack"
        )

    def open_cart(self):
        self.click(self.cart_link)

    def get_cart_item_count(self):
        return int(
            self.get_text(self.cart_badge)
        )

    def is_backpack_in_cart(self):
        return len(
            self.driver.find_elements(
                *self.backpack_item
            )
        ) > 0

    def remove_backpack(self):
        self.click(
            self.backpack_remove_button
        )