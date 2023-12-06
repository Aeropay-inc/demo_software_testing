
from demo_software_testing import create_cart, read_cart, create_product, add_to_cart, increment_quantity, decrement_quantity


def test_create_cart():
    cart = create_cart()
    assert cart is not None
    assert cart.id is not None
    assert cart.empty

def test_add_to_cart():
    cart = create_cart()
    product = create_product()
    add_to_cart(cart, product, 1)
    cart = read_cart(cart.id)
    assert not cart.empy
    assert len(cart.products) == 1
    assert cart.products[0].product_id == product.id
    assert cart.products[0].quantity == 1


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