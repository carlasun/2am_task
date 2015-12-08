import configparser


class VerifyAddressPageCheck():
    def __init__(self, information):
        self.conf = configparser.ConfigParser()
        self.conf.read('framework/resource/VerifyAddressConfig.ini')

        self.input_info = {
            'first_name': information['first_name'],
            'last_name': information['last_name'],
            'company': information['company'],
            'address': information['address'],
            'address2': information['address2'],
            'city': information['city'],
            'state': information['state'],
            'zip': information['zip'],
            'country': information['country'],
            'email': information['email'],
            'phone': information['phone']
        }

    def is_user_on_verify_address_page(self, kit_test):
        current_url = kit_test.driver.current_url
        if kit_test.conf.get('URL', 'base') not in current_url:
            return False

        if kit_test.locale not in current_url:
            return False

        if kit_test.conf.get('URL', 'verify_address_page') not in current_url:
            return False

        return True

    def is_address_on_verification_page(self, kit_test):
        unverified_address = kit_test.driver.find_element_by_xpath(
            self.conf.get('PageElements', 'unverified_address')).text

        for item in self.input_info:
            if (item is 'phone') or (item is 'email'):
                continue
            if self.input_info[item] not in unverified_address:
                return False

        return True