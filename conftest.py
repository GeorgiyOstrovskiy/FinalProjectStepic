import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en")


@pytest.fixture
def browser(request):
    print("\nstart browser")
    user_language = request.config.getoption('language')
    option = Options()
    option.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=option)
    yield browser
    print("\nquit browser")
    browser.quit()
