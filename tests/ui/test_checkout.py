from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_required_fields_validation(login_page):

    # Login
    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Add product
    products_page = ProductsPage(
        login_page.driver
    )

    products_page.add_backpack_to_cart()

    # Open cart
    cart_page = CartPage(
        login_page.driver
    )

    cart_page.open_cart()

    # Open checkout
    checkout_page = CheckoutPage(
        login_page.driver
    )

    checkout_page.click_checkout()

    # Continue without entering customer details
    checkout_page.click_continue()

    # Verify validation error
    assert (
        checkout_page.get_error_message()
        == "Error: First Name is required"
    )
    