from dataclasses import dataclass
from util import int_generator

@dataclass
class Customer:
    id: int
    store_id: int


def create_customer(store_id: int):
    return Customer(id=int_generator(), store_id=store_id)