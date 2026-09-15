from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.backpack_add_button = (
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        )

        self.product_items = (
            By.CLASS_NAME,
            "inventory_item"
        )

        self.backpack_name = (
            By.ID,
            "item_4_title_link"
        )

        self.backpack_price = (
            By.CSS_SELECTOR,
            "#inventory_container .inventory_item_price"
        )

    def wait_for_products_page(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self.product_items
            )
        )

    def add_backpack_to_cart(self):
        self.click(self.backpack_add_button)

    def get_product_count(self):
        return len(
            self.driver.find_elements(
                *self.product_items
            )
        )

    def get_backpack_name(self):
        return self.get_text(self.backpack_name)

    def get_backpack_price(self):
        return self.get_text(self.backpack_price)