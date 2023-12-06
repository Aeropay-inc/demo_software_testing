
from cart_api import create_cart, add_product_to_cart, read_cart, increment_quantity, decrement_quantity

import pytest




@pytest.fixture(name="cart")
def cart_fixture(store, customer):
    return create_cart(store.id, customer.id)


def test_create_cart(cart):
    assert cart is not None
    assert cart.id is not None
    assert cart.is_empty


def test_add_product_to_cart(cart, product):
    # TODO parametrize the quantity
    add_product_to_cart(cart.id, product.id, 1)
    cart = read_cart(cart.id)
    assert cart.products[0].id == product.id
    assert cart.products[0].quantity == 1
    assert not cart.is_empty


def test_increment_quantity(cart, product):
    # TODO use a fixture to avoid calling `add_product_to_cart` here
    add_product_to_cart(cart.id, product.id, 1)
    increment_quantity(cart.id, product.id)
    cart = read_cart(cart.id)
    assert cart.products[0].quantity == 2


def test_decrement_quantity(cart, product):
    add_product_to_cart(cart.id, product.id, 2)
    decrement_quantity(cart.id, product.id)
    cart = read_cart(cart.id)
    assert cart.products[0].quantity == 1
    decrement_quantity(cart.id, product.id)
    cart = read_cart(cart.id)
    assert cart.is_empty