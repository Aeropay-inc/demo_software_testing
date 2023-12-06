

from store_api import create_store
from product_api import create_product
from customer_api import create_customer


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
