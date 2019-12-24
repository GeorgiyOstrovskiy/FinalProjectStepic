from .pages.product_page import ProductPage
import pytest
# import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
promo_options = ["1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.skip), "8", "9"]


@pytest.mark.parametrize('promo', promo_options)
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_product_to_basket()
    page.solve_quiz_and_get_code()
    # time.sleep(100)
    page.should_be_correct_name_product()
    page.should_be_correct_price_product()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message_is_disappeared()
