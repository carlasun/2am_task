from framework.Initialize import PurchasePageSetup
from components.CartPage import CartPageCheck
from components.ShippingPage import ShippingPageCheck
from components.VerifyAddressPage import VerifyAddressPageCheck
from framework.CartPageAction import CartPageAction
from framework.ShippingPageAction import ShippingPageAction
import pytest

@pytest.fixture
def kit_test(request):
    purchase_test = PurchasePageSetup()

    def fin():
        purchase_test.close()

    request.addfinalizer(fin)

    return purchase_test


class Test23andMe:

    def test_interview_task(self, kit_test):
        # In the USA, add 5 kits with unique names

        check = CartPageCheck()
        assert check.is_user_on_cart_page(kit_test)
        on_cart_page = CartPageAction()

        index = 0
        assert check.is_cart_count(index, kit_test)

        # 1st kit add by link
        on_cart_page.add_kit_by_link(kit_test)
        index += 1
        assert check.is_cart_count(index, kit_test)
        assert check.is_total_price_correct(index, kit_test)
        assert check.is_continue_button_disabled(kit_test)
        on_cart_page.add_name_to_kit(index, kit_test)

        # 2nd kit add by plus button
        on_cart_page.add_kit_by_plus_button(kit_test)
        index += 1
        assert check.is_cart_count(index, kit_test)
        assert check.is_subtotal_correct(index, kit_test)
        assert check.is_amount_saved_correct(index, kit_test)
        assert check.is_total_price_correct(index, kit_test)
        assert check.is_continue_button_disabled(kit_test)
        on_cart_page.add_name_to_kit(index, kit_test)

        # 3rd kit add by "add a kit" button
        on_cart_page.add_kit_by_top_button(kit_test)
        index += 1
        assert check.page_components(index, kit_test)
        # Repeat of all the assertions above
        on_cart_page.add_name_to_kit(index, kit_test)

        # 4th kit add by plus button repeated
        on_cart_page.add_kit_by_plus_button(kit_test)
        index += 1
        assert check.page_components(index, kit_test)
        on_cart_page.add_name_to_kit(index, kit_test)

        # 5th kit add by "add a kit" button repeated
        on_cart_page.add_kit_by_top_button(kit_test)
        index += 1
        assert check.page_components(index, kit_test)
        on_cart_page.add_name_to_kit(index, kit_test)

        # Click to continue
        on_cart_page.click_continue_button(kit_test)

        # input valid address on Shipping Information Page
        on_shipping_page = ShippingPageAction()
        check = ShippingPageCheck()
        assert check.is_user_on_shipping_page(kit_test)

        on_shipping_page.input_info(kit_test)
        on_shipping_page.click_continue(kit_test)

        check = VerifyAddressPageCheck(on_shipping_page.info)
        assert check.is_user_on_verify_address_page(kit_test)
        assert check.is_address_on_verification_page(kit_test)




