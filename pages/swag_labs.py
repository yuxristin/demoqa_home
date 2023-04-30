

from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo').click()
        except NoSuchElementException:
            return False
        return True


    def get_url(self):
        return self.driver.current_url


    def user_name(self):
        try:
            self.find_element(locator='#user-name')
        except NoSuchElementException:
            return False
        return True


    def password(self):
        try:
            self.find_element(locator='#password')
        except NoSuchElementException:
            return False
        return True
