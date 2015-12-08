import configparser

class CartPageCheck():
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read('framework/resource/MasterPricing.ini')

    def page_components(self, index, kit_test):
        try:
            assert self.is_cart_count(index, kit_test)
            assert self.is_subtotal_correct(index, kit_test)
            assert self.is_amount_saved_correct(index, kit_test)
            assert self.is_total_price_correct(index, kit_test)
            assert self.is_continue_button_disabled(kit_test)
        except CartPageException("A CartPage component has failed"):
            assert False
        return True

    def is_user_on_cart_page(self, kit_test):
        current_url = kit_test.driver.current_url
        if kit_test.conf.get('URL', 'base') not in current_url:
            return False

        if kit_test.locale not in current_url:
            return False

        if kit_test.conf.get('URL', 'cart_page') not in current_url:
            return False

        return True

    def is_cart_count(self, expected_count, kit_test):
        try:
            current_count = kit_test.driver.find_element_by_xpath(kit_test.conf.get('PageElements', 'cart_count'))
        except CartPageException("Unable to find cart_count element"):
            assert False

        if current_count is not None:
            current_count = current_count.text

            if cmp(current_count, str(expected_count)) is not 0:
                return False
        else:
            return False

        return True

    def is_quantity_count(self, expected_count, kit_test):

        if self.is_cart_count(0, kit_test):
            # Quantity only appears when there is at least one kit
            return False
        else:
            try:
                quantity_count = kit_test.driver.find_element_by_xpath(
                    kit_test.conf.get('PageElements', 'quantity_count'))
            except CartPageException("Unable to retrieve quantity_count"):
                assert False

            return cmp(quantity_count, str(expected_count))

    def is_subtotal_correct(self, count, kit_test):

        if count == 0 or count == 1:
            # No Subtotal for empty cart or 1 kit
            return False
        else:
            actual_subtotal = count * int(self.conf.get(kit_test.locale, 'price'))

            try:
                page_subtotal = kit_test.driver.find_element_by_xpath(kit_test.conf.get('PageElements', 'subtotal'))
            except CartPageException("Unable to retrieve page_subtotal"):
                assert False

            page_subtotal = page_subtotal.text
            page_subtotal = page_subtotal.strip('$')
            page_subtotal = page_subtotal.strip(' ')
            if cmp(float(page_subtotal), actual_subtotal) == 0:
                return True
            else:
                return False

    def is_amount_saved_correct(self, count, kit_test):

        if count == 0 or count == 1:
            # No amount saved for empty cart or 1 kit
            return False
        else:
            price = float(self.conf.get(kit_test.locale, 'price'))
            discount_rate = float(self.conf.get(kit_test.locale, 'discount_rate'))
            actual_amount_saved = (count-1) * price * discount_rate

            page_amount_saved = kit_test.driver.find_element_by_xpath(
                kit_test.conf.get('PageElements', 'amount_saved'))

            page_amount_saved = page_amount_saved.text
            page_amount_saved = page_amount_saved.strip('$')
            page_amount_saved = page_amount_saved.strip(' ')
            actual_amount_saved = "%.2f" % actual_amount_saved
            if cmp(page_amount_saved, str(actual_amount_saved)) == 0:
                return True
            else:
                return False

    def is_total_price_correct(self, count, kit_test):
        price = int(self.conf.get(kit_test.locale, 'price'))
        discount_rate = float(self.conf.get(kit_test.locale, 'discount_rate'))

        actual_total = 0
        if count == 0:
            # No Total for empty cart
            return False
        if count >= 1:
            actual_total += price
            for x in range(1, count):
                actual_total += price - price*discount_rate

        try:
            page_total = kit_test.driver.find_element_by_xpath(
                kit_test.conf.get('PageElements', 'total'))
            page_total = page_total.text
            page_total = page_total.strip('$')
            page_total = page_total.strip(' ')
        except CartPageException("Unable to retrieve page total amount"):
            assert False

        if cmp(float(page_total), actual_total) == 0:
            return True
        elif cmp(page_total, ("%.2f" % actual_total)) == 0:
            return True
        else:
            return False

    def is_continue_button_disabled(self, kit_test):
        try:
            button = kit_test.driver.find_element_by_xpath(kit_test.conf.get('PageElements', 'disabled_continue'))
            if button is not None:
                button.click()

            if self.is_user_on_cart_page(kit_test):
                return True
            else:
                return False
        except CartPageException("Unable to find disabled continue button"):
            assert False

    def is_error_message_displayed(self, expected_count, kit_test):
        try:
            if expected_count == 1:
                error_message = kit_test.driver.find_element_by_xpath(kit_test.conf.get('PageElements', 'error'))
                # if type(error_message) is list:
                #     # if there are multiple error messages, get the last instance
                #     error_message = error_message[-1]

                if error_message is not None:
                    error_message = error_message.text

                if cmp(error_message, kit_test.conf.get('PageText', 'error_message')):
                    return True
                else:
                    return False

            elif expected_count > 1:
                pass
                # TODO: add logic to check for multiple instances of error messages
                # error_messages = kit_test.driver.find_elements_by_xpath(kit_test.conf.get('PageElements', 'error'))
        except CartPageException("Unable to find error message"):
            assert False


class CartPageException(Exception):
    def __init__(self, e):
        message = "CartPageComponentException"

        if e is not None:
            message += ": " + e
        else:
            message += " "

        print message
