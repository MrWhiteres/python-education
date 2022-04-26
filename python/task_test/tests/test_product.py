from python.task_test.func import Product
import pytest


@pytest.mark.parametrize('title, price, quantity', [('Water', 100, 10),
                                                    ('Milk', 5, 6)])
def test_class_product_create_object_good(title, price, quantity):
    """creates an object of the class and checks if the fields match"""
    product = Product(title, price, quantity)
    assert product.title == title
    assert product.price == price
    assert product.quantity == quantity


@pytest.mark.parametrize('title, price, quantity', [(100, 'Water', 'ten'),
                                                    (10.5, None, 'Milk')])
def test_class_product_create_object_bad(title, price, quantity):
    """test tries to create an object with the wrong data types"""
    product = Product(title, price, quantity)
    assert type(product.title) is not str
    assert type(product.price) not in (int, float)
    assert type(product.quantity) not in (int, None)


@pytest.mark.parametrize('title, price, quantity,num_of_products', [('Water', 100, 10, 2),
                                                                    ('Milk', 5, 6, 3)])
def test_class_product_subtract_quantity_good(title, price, quantity, num_of_products):
    """test checks the possibility of decreasing the number of objects"""
    product = Product(title, price, quantity)
    product.subtract_quantity(num_of_products)
    assert product.quantity == quantity - num_of_products


@pytest.mark.parametrize('title, price, quantity,num_of_products, exception', [('Water', 100, 10, '2', TypeError),
                                                                               ('Milk', 5, 'six', 1, TypeError),
                                                                               ('Telephone', 15, [100], [100, 123],
                                                                                TypeError)])
def test_class_product_subtract_quantity_bad(title, price, quantity, num_of_products, exception):
    """test checks the possibility of reducing the number of objects with erroneous data types"""
    with pytest.raises(exception):
        product = Product(title, price, quantity)
        product.subtract_quantity(num_of_products)
        assert product.quantity == quantity - num_of_products


@pytest.mark.parametrize('title, price, quantity,num_of_products', [('Water', 100, 10, 2),
                                                                    ('Milk', 5, 6, 3)])
def test_class_product_add_quantity_good(title, price, quantity, num_of_products):
    """test checks the function of adding an additional quantity to an object"""
    product = Product(title, price, quantity)
    product.add_quantity(num_of_products)
    assert product.quantity == quantity + num_of_products


@pytest.mark.parametrize('title, price, quantity,num_of_products, exception', [('Water', 100, 10, '2', TypeError),
                                                                               ('Milk', 5, 'six', 1, TypeError),
                                                                               ('Telephone', 1, [2], {1}, TypeError),
                                                                               ('Game TicTacToe', 2, {1: 100}, True,
                                                                                TypeError)])
def test_class_product_add_quantity_bad(title, price, quantity, num_of_products, exception):
    """test checks for erroneous data in the function of adding To the object its quantity"""
    with pytest.raises(exception):
        product = Product(title, price, quantity)
        product.add_quantity(num_of_products)
        assert product.quantity == quantity + num_of_products


@pytest.mark.parametrize('title, price, new_price', [('Water', 10, 20),
                                                     ('Milk', 5, 1)])
def test_class_product_change_price_good(title, price, new_price):
    """test checks the possibility of changing the cost of goods"""
    product = Product(title, price)
    product.change_price(new_price)
    assert product.price == new_price


@pytest.mark.parametrize('title, price, new_price, exception', [('Water', 100, 'one', AssertionError),
                                                                ('Milk', 5, [100], AssertionError),
                                                                ('Water', 100, Product, AssertionError),
                                                                ('Milk', 5, None, AssertionError),
                                                                ('Telephone', 1000, {1000: '1000'}, AssertionError)])
def test_class_product_change_price_bad(title, price, new_price, exception):
    """test checks the possibility of changing the cost of goods with erroneous data types"""
    with pytest.raises(exception):
        product = Product(title, price)
        product.change_price(new_price)
        assert type(new_price) == type(price) in (float, int)
