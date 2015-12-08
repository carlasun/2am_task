__author__ = 'carlas'
import configparser


class ShippingPageCheck():
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read('framework/resource/ShippingConfig.ini')

    def is_user_on_shipping_page(self, kit_test):
        current_url = kit_test.driver.current_url

        if kit_test.conf.get('URL', 'base') not in current_url:
            return False
        if kit_test.locale not in current_url:
            return False
        if kit_test.conf.get('URL', 'shipping_page') not in current_url:
            return False

        return True


