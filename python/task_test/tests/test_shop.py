from python.task_test.func import Shop, Product
import pytest


@pytest.fixture()
def product_list():
    """function creates and returns a list as with objects of class product"""
    return [Product(title='Apple', price=10, quantity=4),
            Product(title='Milk', price=50, quantity=10),
            Product(title='Bread', price=5, quantity=40)]


@pytest.fixture()
def shop_product(product_list):
    """function creates and returns a purchase class with a list of products"""
    return Shop(product_list)


def test_shop_create_object_not_empty(shop_product):
    """test checks the number of products in the Shop class object"""
    assert len(shop_product.products) == 3


def test_shop_create_object_empty():
    """checks when creating an object of class Shop with an empty list"""
    assert len(Shop().products) == 0


@pytest.mark.parametrize('new_product', [Product('Telephone', 1000, 10),
                                         Product('Glass', 30, 1)])
def test_shop_add_product_good(shop_product, new_product):
    """function to check if a new product has been added to the list"""
    shop_product.add_product(new_product)
    assert shop_product.products[len(shop_product.products) - 1] is new_product


@pytest.mark.parametrize('new_product, exception', [([12, Product], AssertionError),
                                                    ('product', AssertionError),
                                                    (Shop(), AssertionError)])
def test_shop_add_product_bad(new_product, exception):
    """function to check the addition of a new product with an erroneous data type"""
    with pytest.raises(exception):
        assert isinstance(new_product, Product)


@pytest.mark.parametrize('product_title, index', [('Apple', 0),
                                                  ('Milk', 1),
                                                  ('Bread', 2)])
def test__get_product_index_good(shop_product, product_title, index):
    """product index check function"""
    assert shop_product._get_product_index(product_title) == index


@pytest.mark.parametrize('product_title, index, exception', [('Apple', 10, AssertionError),
                                                             ('Milk', 'one', AssertionError),
                                                             ('Bread', [2], AssertionError)])
def test__get_product_index_bad(shop_product, product_title, index, exception):
    """index check function with errors"""
    with pytest.raises(exception):
        assert shop_product._get_product_index(product_title) == index


@pytest.mark.parametrize('product_title, amount, price', [('Apple', 4, 10),
                                                          ('Milk', 1, 50),
                                                          ('Bread', 4, 5)])
def test_sell_product_good(shop_product, product_title, amount, price):
    """function check the total cost of the goods when buying"""
    shop_product.sell_product(product_title, amount)
    assert shop_product.money == amount * price


@pytest.mark.parametrize('product_title, amount, exception', [('Apple', 5, ValueError),
                                                              ('Milk', 11, ValueError),
                                                              ('Bread', [1], TypeError)])
def test_sell_product_good(shop_product, product_title, amount, exception):
    """function checks the sale of a product with an excess of
     the quantity of products or an erroneous data type"""
    with pytest.raises(exception):
        assert shop_product.sell_product(product_title, amount)
