class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.page.get_by_placeholder("First Name").fill("King")
        self.page.get_by_placeholder("Last Name").fill("Man")
        self.page.get_by_placeholder("Zip/Postal Code").fill("0000")


    def go_to_continue(self):
        self.page.get_by_role("button", name="Continue").click()

