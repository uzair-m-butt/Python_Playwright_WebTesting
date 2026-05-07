import pytest
from playwright.sync_api import Playwright

def pytest_addoption(parser):
    parser.addoption(
        "--my_browser", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--url_name", action="store", default="https://www.saucedemo.com/", help="browser selection"
    )

@pytest.fixture(scope='function')
def browser_instance(playwright: Playwright, request):
    browser_name = request.config.getoption('--my_browser')
    url_name = request.config.getoption('--url_name')


    if isinstance(browser_name, list):
        browser_name = browser_name[0] if browser_name else 'chrome'
    if browser_name == 'chrome':
        browser_context = playwright.chromium.launch()
    elif browser_name == 'firefox':
        browser_context = playwright.firefox.launch()
    else:
        raise ValueError(f"Unsupported browser: '{browser_name}'. Choose from: chrome, firefox")

    context = browser_context.new_context()
    page = context.new_page()
    #page.goto(url_name)
    yield page
    context.close()
    browser_context.close()