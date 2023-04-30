from pages.base_page import BasePage
from pages.swag_labs import SwagLabs


def test_icon(browser):
    swag = SwagLabs(browser)
    swag.visit()
    swag.exist_icon()


def  test_get_url(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.get_url()


def user_name(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.user_name()


def user_name(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.password()