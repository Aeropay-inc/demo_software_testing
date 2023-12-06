
from demo_software_testing import *


def test_create_cart():
    cart = create_cart()
    assert cart is not None
    assert cart.id is not None
    assert cart.empty

def test_create_product():
    product = create_product()
    assert product is not None
    assert product.id is not None

def test_increment_quantity():
    cart = create_cart()
    product = create_product()
    add_to_cart(cart, product, 1)
    increment_quantity(cart, product)
    cart = read_cart(cart.id)
    assert cart.products[0].quantity == 2

def test_decrement_quantity():
    cart = create_cart()
    product = create_product()
    add_to_cart(cart, product, 2)
    cart = read_cart(cart.id)
    assert cart.products[0].quantity == 2
    decrement_quantity(cart, product)
    cart = read_cart(cart.id)
    assert cart.products[0].quantity == 1
    decrement_quantity(cart, product)
    cart = read_cart(cart.id)
    assert cart.empty