class ItemsPage:
    def __init__(self, page):
        self.page = page
        self.product_cards = page.locator(".inventory_item")
        self.cart_icon = page.locator(".shopping_cart_link")

    def get_all_product_names(self) -> list[str]:
        """Return a list of all product names on the page."""
        cards = self.product_cards.all()
        return [
            card.locator(".inventory_item_name").inner_text()
            for card in cards
        ]


    def get_all_products(self) -> list[dict]:
        """Return all products as a list of dicts with name, price, and card."""
        cards = self.product_cards.all()
        products = []
        for card in cards:
            name = card.locator(".inventory_item_name").inner_text()
            price_text = card.locator(".inventory_item_price").inner_text()
            price = float(price_text.replace("$", ""))
            products.append({
                "name": name,
                "price": price,
                "card": card,
            })
        return products

    def add_to_cart_by_name(self, item_names: list[str]) -> list[str]:
        """
        Loop through all products and add to cart if the name matches
        any name in item_names list.
        Returns a list of names that were successfully added.
        """
        added = []
        products = self.get_all_products()

        for product in products:
            if product["name"] in item_names:
                add_btn = product["card"].locator("button")
                add_btn.click()
                added.append(product["name"])

        return added

    def go_to_cart(self):
        """Click the cart icon to navigate to the cart page."""
        self.cart_icon.click()
