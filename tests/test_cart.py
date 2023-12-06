
from cart_api import create_cart, add_product_to_cart, read_cart, increment_quantity, decrement_quantity
from customer_api import create_customer
from product_api import create_product
from store_api import create_store


import pytest

@pytest.fixture(name="store")
def store_fixture():
    return create_store()


@pytest.fixture(name="customer")
def customer_fixture(store):
    return create_customer(store.id)


@pytest.fixture(name="product")
def product_fixture(store):
    return create_product(store.id)


def test_create_store(store):
    assert store is not None
    assert store.id is not None


def test_create_customer(customer):
    assert customer is not None
    assert customer.id is not None


def test_create_cart(store, customer):
    cart = create_cart(store.id, customer.id)
    assert cart is not None
    assert cart.id is not None
    assert cart.is_empty


def test_create_product(product):
    assert product is not None
    assert product.id is not None


def test_add_product_to_cart(product):
    cart = create_cart(store.id, customer.id)
    add_product_to_cart(cart.id, product.id, 1)
    cart = read_cart(cart.id)
    assert cart.products[0].id == product.id
    assert cart.products[0].quantity == 1


def test_increment_quantity(product):
    cart = create_cart(store.id, customer.id)
    add_product_to_cart(cart.id, product.id, 1)
    increment_quantity(cart.id, product.id)
    cart = read_cart(cart.id)
    assert cart.products[0].quantity == 2


def test_decrement_quantity(product):
    cart = create_cart(store.id, customer.id)
    add_product_to_cart(cart.id, product.id, 2)
    decrement_quantity(cart.id, product.id)
    cart = read_cart(cart.id)
    assert cart.products[0].quantity == 1
    decrement_quantity(cart.id, product.id)
    cart = read_cart(cart.id)
    assert cart.empty