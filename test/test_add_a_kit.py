from framework.Initialize import PurchasePageSetup
from components.CartPage import CartPageCheck
from framework.CartPageAction import CartPageAction
import pytest

@pytest.fixture
def kit_test(request):
    purchase_test = PurchasePageSetup()

    def fin():
        purchase_test.close()

    request.addfinalizer(fin)

    return purchase_test


class TestAddingAKitBVTs:

    def test_add_a_kit_by_button(self, kit_test):
        # In the USA, add a kit by button
        check = CartPageCheck()

        assert check.is_user_on_cart_page(kit_test)

        on_cart_page = CartPageAction()

        assert check.is_cart_count(0, kit_test)

        on_cart_page.add_kit_by_link(kit_test)

        assert check.is_cart_count(1, kit_test)
