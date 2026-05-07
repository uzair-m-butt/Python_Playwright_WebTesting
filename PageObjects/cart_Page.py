class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        #self.checkout_button = page.get_by_role("button", name="Checkout").click()

    def get_cart_item_names(self) -> list[str]:
        """Return the names of all items currently in the cart."""
        items = self.cart_items.all()
        return [
            item.locator(".inventory_item_name").inner_text()
            for item in items
        ]

    def go_to_checkout(self):
        self.page.get_by_role("button", name="Checkout").click()

