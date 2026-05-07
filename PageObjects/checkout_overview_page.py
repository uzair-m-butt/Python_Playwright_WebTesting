class CheckoutOverviewPage:
    def __init__(self, page):
        self.page = page
        self.page.get_by_role("button", name="Finish").click()