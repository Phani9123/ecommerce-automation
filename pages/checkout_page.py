from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.checkout_button = (
            By.ID,
            "checkout"
        )

        self.first_name = (
            By.ID,
            "first-name"
        )

        self.last_name = (
            By.ID,
            "last-name"
        )

        self.postal_code = (
            By.ID,
            "postal-code"
        )

        self.continue_button = (
            By.ID,
            "continue"
        )

        self.finish_button = (
            By.ID,
            "finish"
        )

        self.success_message = (
            By.CLASS_NAME,
            "complete-header"
        )

        # Checkout validation error
        self.error_message = (
            By.CSS_SELECTOR,
            "h3[data-test='error']"
        )


    def wait_for_checkout_information(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self.first_name
            )
        )
    
    def click_checkout(self):
        self.click(self.checkout_button)
        self.wait_for_checkout_information()

    def enter_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.enter_text(
            self.first_name,
            first_name
        )

        self.enter_text(
            self.last_name,
            last_name
        )

        self.enter_text(
            self.postal_code,
            postal_code
        )

    def click_continue(self):
        self.click(self.continue_button)


    def wait_for_checkout_overview(self):
        self.wait.until(
            EC.url_contains("checkout-step-two")
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.finish_button
            )
        )


    def wait_for_checkout_error(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self.error_message
            )
        )
        
    def wait_for_checkout_result(self):
        self.wait.until(
            EC.any_of(
                EC.visibility_of_element_located(self.error_message),
                EC.element_to_be_clickable(self.finish_button)
            )
        )
            
            

    def finish_order(self):
        self.wait_for_checkout_overview()
        self.click(self.finish_button)
            
    

    def get_success_message(self):
        return self.get_text(
            self.success_message
        )

    def get_error_message(self):
        return self.get_text(
            self.error_message
        )