import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from PageObjects import cart_Page, checkout_overview_page
from PageObjects.checkout_overview_page import CheckoutOverviewPage
from PageObjects.checkout_page import CheckoutPage
from PageObjects.login_Page import LoginPage
from PageObjects.items_Page import ItemsPage
from PageObjects.cart_Page import CartPage
from PageObjects.order_page import OrderPage

with open('data/user_credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_web_e2e(playwright: Playwright, user_credentials, browser_instance):
    username = user_credentials["username"]
    password = user_credentials["password"]

    # logging into the page
    loginPage = LoginPage(browser_instance)
    loginPage.navigate()
    loginPage.login(username, password)

    # add items and go to cart
    itemsPage = ItemsPage(browser_instance)
    ProductNames = itemsPage.get_all_product_names()
    ProductstoAdd = ProductNames[:2]
    itemsPage.add_to_cart_by_name(ProductstoAdd)
    print(f"\n Items selected: {ProductstoAdd}")
    itemsPage.go_to_cart()


    # check the items in cart previously added are same
    cartPage = CartPage(browser_instance)
    cart_names = cartPage.get_cart_item_names()
    print(f"\n Items in cart: {cart_names}")

    assert cart_names == ProductstoAdd

    cartPage.go_to_checkout()

    checkoutPage = CheckoutPage(browser_instance)
    checkoutPage.go_to_continue()

    CheckoutOverviewPage(browser_instance)

    orderPage = OrderPage(browser_instance)
    orderPage.verifyOrderMessage()



