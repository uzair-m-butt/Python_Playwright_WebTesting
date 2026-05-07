from playwright.sync_api import expect


class OrderPage:
    def __init__(self, page):
        self.page = page

    def verifyOrderMessage(self):
        expect(self.page.locator(".complete-header")).to_contain_text("Thank you for your order!")