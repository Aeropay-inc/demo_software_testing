from dataclasses import dataclass

@dataclass
class Customer:
    id: int
    store_id: int


def create_customer(store_id: int):
    ...