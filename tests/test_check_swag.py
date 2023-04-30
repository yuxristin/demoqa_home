from pages.swag_labs import SwagLabs


def test_icon(browser):
    swag = SwagLabs(browser)
    swag.visit()
    swag.exist_icon()
    assert swag.exist_icon()


def test_get_url(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.get_url()


def test_user_name(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.user_name()


def test_user_password(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.password()