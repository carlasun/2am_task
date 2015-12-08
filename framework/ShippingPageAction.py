import configparser
from selenium.webdriver.support.ui import Select


class ShippingPageAction():
    def __init__(self, information=None):
        self.conf = configparser.ConfigParser()
        self.conf.read('framework/resource/ShippingConfig.ini')

        if information is None:
            self.info = {
                'first_name': self.conf.get('DefaultAddress', 'first_name'),
                'last_name': self.conf.get('DefaultAddress', 'last_name'),
                'company': self.conf.get('DefaultAddress', 'company'),
                'address': self.conf.get('DefaultAddress', 'address'),
                'address2': self.conf.get('DefaultAddress', 'address2'),
                'city': self.conf.get('DefaultAddress', 'city'),
                'state': self.conf.get('DefaultAddress', 'state'),
                'zip': self.conf.get('DefaultAddress', 'zip'),
                'country': self.conf.get('DefaultAddress', 'country'),
                'email': self.conf.get('DefaultAddress', 'email'),
                'phone': self.conf.get('DefaultAddress', 'phone')
            }
        else:
            self.info = {
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

    def input_info(self, kit_test):
        self.input_first_name(kit_test, self.info['first_name'])
        self.input_last_name(kit_test, self.info['last_name'])
        self.input_company(kit_test, self.info['company'])
        self.input_address(kit_test, self.info['address'])
        self.input_address2(kit_test, self.info['address2'])
        self.input_city(kit_test, self.info['city'])
        self.input_state(kit_test, self.info['state'])
        self.input_zip(kit_test, self.info['zip'])
        self.input_country(kit_test, self.info['country'])
        self.input_email(kit_test, self.info['email'])
        self.input_phone(kit_test, self.info['phone'])

    def input_first_name(self, kit_test, fname):
        field = kit_test.driver.find_element_by_xpath(self.conf.get('PageElements', 'first_name'))
        if field is not None:
            field.send_keys(fname)

    def input_last_name(self, kit_test, lname):
        field = kit_test.driver.find_element_by_xpath(self.conf.get('PageElements', 'last_name'))
        if field is not None:
            field.send_keys(lname)

    def input_company(self, kit_test, company):
        field = kit_test.driver.find_element_by_xpath(self.conf.get('PageElements', 'company'))
        if field is not None:
            field.send_keys(company)

    def input_address(self, kit_test, address):
        field = kit_test.driver.find_element_by_xpath(self.conf.get('PageElements', 'address'))
        if field is not None:
            field.send_keys(address)

    def input_address2(self, kit_test, address2):
        field = kit_test.driver.find_element_by_xpath(self.conf.get('PageElements', 'address2'))
        if field is not None:
            field.send_keys(address2)

    def input_city(self, kit_test, city):
        field = kit_test.driver.find_element_by_xpath(self.conf.get('PageElements', 'city'))
        if field is not None:
            field.send_keys(city)

    def input_state(self, kit_test, state):
        field = kit_test.driver.find_element_by_xpath(self.conf.get('PageElements', 'state'))
        Select(field).select_by_value(state)

    def input_zip(self, kit_test, zip_code):
        field = kit_test.driver.find_element_by_xpath(self.conf.get('PageElements', 'zip'))
        if field is not None:
            field.send_keys(zip_code)

    def input_country(self, kit_test, country):
        field = kit_test.driver.find_element_by_xpath(self.conf.get('PageElements', 'country'))
        Select(field).select_by_value(country)

    def input_email(self, kit_test, email):
        field = kit_test.driver.find_element_by_xpath(self.conf.get('PageElements', 'email'))
        if field is not None:
            field.send_keys(email)

    def input_phone(self, kit_test, phone):
        field = kit_test.driver.find_element_by_xpath(self.conf.get('PageElements', 'phone'))
        if field is not None:
            field.send_keys(phone)

    def click_continue(self, kit_test):
        button = kit_test.driver.find_element_by_xpath(self.conf.get('PageElements', 'continue'))
        if button is not None:
            button.click()
        else:
            assert False
