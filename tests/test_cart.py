
from cart_api import create_cart, add_product_to_cart, read_cart, increment_quantity, decrement_quantity
from customer_api import create_customer
from product_api import create_product
from store_api import create_store


def test_create_store():
    store = create_store()
    assert store is not None
    assert store.id is not None


def test_create_customer():
    store = create_store()
    customer = create_customer(store.id)
    assert customer is not None
    assert customer.id is not None


def test_create_cart():
    store = create_store()
    customer = create_customer(store.id)
    cart = create_cart(store.id, customer.id)
    assert cart is not None
    assert cart.id is not None
    assert cart.empty


def test_create_product():
    store = create_store()
    product = create_product(store.id)
    assert product is not None
    assert product.id is not None


def test_increment_quantity():
    store = create_store()
    customer = create_customer(store.id)
    cart = create_cart(store.id, customer.id)
    product = create_product(store.id)
    add_product_to_cart(cart.id, product.id, 1)
    increment_quantity(cart.id, product.id)
    cart = read_cart(cart.id)
    assert cart.products[0].quantity == 2


def test_decrement_quantity():
    store = create_store()
    customer = create_customer(store.id)
    cart = create_cart(store.id, customer.id)
    product = create_product(store.id)
    add_product_to_cart(cart.id, product.id, 2)
    cart = read_cart(cart.id)
    assert cart.products[0].quantity == 2
    decrement_quantity(cart.id, product.id)
    cart = read_cart(cart.id)
    assert cart.products[0].quantity == 1
    decrement_quantity(cart.id, product.id)
    cart = read_cart(cart.id)
    assert cart.empty