import pytest
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from test_data.data_loader import load_json_data

LOGIN_TEST_DATA = load_json_data(
    "test_data/login_data.json"
)

CHECKOUT_DATA = load_json_data(
    "test_data/checkout_data.json"
)

@pytest.mark.regression
def test_login_add_product_and_complete_order(login_page):

    test_data = LOGIN_TEST_DATA[0]

    # 1. Login
    login_page.open()
    login_page.login(
        test_data["username"],
        test_data["password"]
    )

    # 2. Products
    products_page = ProductsPage(login_page.driver)
    products_page.add_backpack_to_cart()

    # 3. Cart
    cart_page = CartPage(login_page.driver)
    cart_page.open_cart()

    assert cart_page.is_backpack_in_cart()

    # 4. Checkout
    checkout_page = CheckoutPage(login_page.driver)
    checkout_page.click_checkout()

    # 5. Customer details
    checkout_page.enter_customer_details(
        CHECKOUT_DATA["first_name"],
        CHECKOUT_DATA["last_name"],
        CHECKOUT_DATA["postal_code"]
    )

    checkout_page.click_continue()
    checkout_page.wait_for_checkout_overview()
    checkout_page.finish_order()
    
    # 8. Verify order confirmation
    assert checkout_page.get_success_message() == "Thank you for your order!"