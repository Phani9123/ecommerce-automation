from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_products_are_displayed(login_page):

    # Login
    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Products page
    products_page = ProductsPage(
        login_page.driver
    )

    # Verify products
    product_count = products_page.get_product_count()

    assert product_count > 0


def test_add_product_to_cart(login_page):

    # Login
    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Add backpack
    products_page = ProductsPage(
        login_page.driver
    )

    products_page.add_backpack_to_cart()

    # Open cart
    cart_page = CartPage(
        login_page.driver
    )

    cart_page.open_cart()

    # Verify cart
    assert cart_page.get_cart_item_count() == 1

    assert cart_page.is_backpack_in_cart()


def test_remove_product_from_cart(login_page):

    # Login
    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Add backpack
    products_page = ProductsPage(
        login_page.driver
    )

    products_page.add_backpack_to_cart()

    # Open cart
    cart_page = CartPage(
        login_page.driver
    )

    cart_page.open_cart()

    # Verify product was added
    assert cart_page.get_cart_item_count() == 1

    # Remove product
    cart_page.remove_backpack()

    # Verify product was removed
    assert not cart_page.is_backpack_in_cart()
    
def test_backpack_product_information(login_page):

    # Login
    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Products page
    products_page = ProductsPage(
        login_page.driver
    )

    # Get product information
    product_name = products_page.get_backpack_name()
    product_price = products_page.get_backpack_price()

    # Verify product information
    assert product_name == "Sauce Labs Backpack"
    assert product_price.startswith("$")