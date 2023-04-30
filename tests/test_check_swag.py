from pages.base_page import BasePage
from pages.swag_labs import SwagLabs


def test_icon(browser):
    swag = SwagLabs(browser)
    swag.visit()
    swag.exist_icon()
    assert swag.get_url()
    assert swag.exist_icon()
