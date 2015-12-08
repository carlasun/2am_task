import configparser
from selenium import webdriver
from urlparse import urljoin


class PurchasePageSetup():
    # Setup the selenium test to go to the 23andme kit purchase page
    def __init__(self, browser_type=None, locale=None):

        try:
            self.conf = configparser.ConfigParser()
            self.conf.read('framework/resource/InitializeConfig.ini')
        except PurchasePageSetupException("Error in PurchasePageSetup() initialization"):
            assert False

        if browser_type is None:
            self.driver = webdriver.Firefox()
        else:
            # TODO: FILL THIS OUT WITH BROWSER CASES OR SAUCE CONNECT
            pass

        if locale is None:
            self.locale = self.conf.get('Locale', 'USA')
        else:
            self.locale = locale

        self.base_url = self.conf.get('URL', 'base')
        if self.base_url is not None:
            self.driver.get(urljoin(self.base_url, self.locale, self.conf.get('URL', 'cart_page')))
            self.driver.implicitly_wait(10)
        else:
            raise PurchasePageSetupException("Unable to get base url")

    def close(self):
        self.driver.close()


class PurchasePageSetupException(Exception):
    def __init__(self, e=None):
        if e is not None:
            message = "23andme Test Suite Exception: " + e
        else:
            message = "23andme Test Suite Exception"

        print message



