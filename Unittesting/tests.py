from freezegun import freeze_time
import pytest
from to_test import *


# Testing "even_odd"
@pytest.mark.parametrize("new_val, expected", [(4, "even"), (5, "odd")])
def test_even_or_odd(new_val, expected):
    assert even_odd(new_val) == expected


# Testing "sum_all"
def test_sum_all_int():
    assert sum_all(1, 2, 3) == 6, "must be 6"


# Testing "time_of_day"
def test_time():
    assert time_of_day() in ["morning", "afternoon", "night"], "Not all branches are returns value"
    assert isinstance(time_of_day(), str), "Must be a string!"


@freeze_time("2021-10-08 08:00:01")
def test_morning():
    assert time_of_day() == "morning", "Wrong morning calculation"


@freeze_time("2021-10-08 13:00:01")
def test_afternoon():
    assert time_of_day() == "afternoon", "Wrong afternoon calculation"


@freeze_time("2021-10-08 21:00:01")
def test_night():
    assert time_of_day() == "night", "Wrong night calculation"


@pytest.fixture()
def create_product(price=10, quantity=15):
    return Product("Prod", price=price, quantity=quantity)


@pytest.mark.parametrize("test_input", [10, 0, 5])
def test_product_price(create_product, test_input):
    create_product.price = test_input
    assert create_product.price >= 0, "Product's price can't be lower zero!"


@pytest.mark.parametrize("test_input", [10, 0, -5])
def test_product_quantity(create_product, test_input):
    assert create_product.quantity >= 0, "Product's quantity must be bigger that zero!"


@pytest.mark.parametrize("test_input", [5, 0, 11])
def test_products_subtract(create_product, test_input):
    qual1 = create_product.quantity
    create_product.subtract_quantity(test_input)
    assert create_product.quantity >= 0, "Can't subtract more products then available"
    assert abs(qual1) >= abs(create_product.quantity), \
        "The subtract number must be positive!"


@pytest.mark.parametrize("test_input", [5, 0])
def test_products_add_quantity(create_product, test_input):
    qual1 = create_product.quantity
    create_product.add_quantity(test_input)
    assert create_product.quantity >= qual1, "The add number must be positive!"
    assert create_product.quantity > 0, "You can't add with negative result"


@pytest.mark.parametrize("sub_quan, expected", [(4, 19), (-10, 5)])
def test_add_quantity(sub_quan, expected, create_product):
    create_product.add_quantity(sub_quan)
    assert create_product.quantity == expected, "must be >= 0 failed (-10, 0)"


@pytest.mark.parametrize("test_input", [40, 20.5, -5, '34'])
def test_product_change_price(create_product, test_input):
    assert isinstance(test_input, int) or isinstance(test_input, float), \
        f"Argument must be a number, not a {type(test_input)}"
    create_product.change_price(test_input)
    assert create_product.price >= 0, "The price can't be less then zero!"


@pytest.fixture()
def shop(price=10, quantity=15):
    products = [
        Product(title="Banjo", price=170, quantity=20),
        Product(title="Ukulele", price=190, quantity=10),
        Product(title="Drams", price=20, quantity=5)
    ]
    return shop(products=products)


@pytest.mark.parametrize("product", [["Banjo",
                                      Product(title="Banjo", price=170, quantity=20),
                                      None]]
                         )
def test_shop_products_type(product):
    temp_shop = Shop(products=product)
    for product in temp_shop.products:
        assert isinstance(product, Product) or temp_shop.products == [], "Wrong product!"


def test_sell_product(shop):
    assert shop.sell_product("Ukulele", 10) is not None
    with pytest.raises(ValueError):
        shop.sell_product("Drams", 30), "Must be warning about amount!"
    assert shop.sell_product(1, bool) is None, "Not found item should return None"
