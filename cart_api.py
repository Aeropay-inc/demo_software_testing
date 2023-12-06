from dataclasses import dataclass
from util import int_generator


@dataclass
class CartProduct:
    id: int
    quantity: int

@dataclass
class Cart:
    id: int
    store_id: int
    customer_id: int
    products: list[CartProduct]
    is_empty: bool


CARTS_DB = {}

def create_cart(store_id: int, customer_id: int):
    cart = Cart(id=int_generator(), store_id=store_id, customer_id=customer_id, products=[], is_empty=True)
    save_cart(cart)
    return cart


def save_cart(cart):
    CARTS_DB[cart.id] = cart


def add_product_to_cart(cart_id: int, product_id: int, initial_quantity: int):
    cart = read_cart(cart_id)
    cart.products.append(
        CartProduct(id=product_id, quantity=initial_quantity)
    )
    cart.is_empty = False
    save_cart(cart)


def read_cart(cart_id: int):
    return CARTS_DB[cart_id]


def increment_quantity(cart_id: int, product_id: int):
    cart = read_cart(cart_id)
    for product in cart.products:
        if product.id == product_id:
            product.quantity+= 1
            save_cart(cart)


def decrement_quantity(cart_id: int, product_id: int):
    cart = read_cart(cart_id)
    for product in cart.products:
        if product.id == product_id:
            product.quantity -= 1
            if product.quantity == 0:
                cart.products.remove(product)
            cart.is_empty = not cart.products 
            save_cart(cart)
