
def create_cart(store_id: int, customer_id: int):
    ...


def add_product_to_cart(cart_id: int, product_id: int, initial_quantity: int):
    ...


def read_cart(cart_id: int):
    ...


def increment_quantity(cart_id: int, product_id: int):
    ...


def decrement_quantity(cart_id: int, product_id: int):
    ...

