import string
import random
from components.CartPage import CartPageCheck


class CartPageAction():
    def __init__(self):
        pass

    def add_kit_by_link(self, kit_test):
        check = CartPageCheck()

        if check.is_cart_count(0, kit_test):
            link = kit_test.driver.find_element_by_xpath(kit_test.conf.get('PageElements', 'add_kit_link'))

            if link is None:
                return False
            else:
                link.click()
                return True
        else:
            # The Link only appears when the cart is empty
            return False

    def add_kit_by_top_button(self, kit_test):

        button = kit_test.driver.find_element_by_xpath(kit_test.conf.get('PageElements', 'add_kit_button'))
        if button is None:
            return False
        else:
            button.click()
            return True

    def add_kit_by_plus_button(self, kit_test):
        check = CartPageCheck()

        if not check.is_cart_count(0, kit_test):
            # plus button only appears when there is at least one kit in the cart
            link = kit_test.driver.find_element_by_xpath(kit_test.conf.get('PageElements', 'add_kit_plus'))

            if link is None:
                return False
            else:
                link.click()
                return True
        else:
            # The Link only appears when the cart is empty
            return False

    def click_continue_button(self, kit_test):

        button = kit_test.driver.find_element_by_xpath(kit_test.conf.get('PageElements', 'enabled_continue'))
        if button is not None:
            button.click()

    def add_name_to_kit(self, count, kit_test):
        index = count - 1
        # by index
        field = kit_test.driver.find_elements_by_xpath(kit_test.conf.get('PageElements', 'name_field'))
        if field is not None:
            name = self.generate_unique_name()
            field[index].send_keys(name)
            return name
        else:
            return None

    def generate_unique_name(self):
        return ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])