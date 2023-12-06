from dataclasses import dataclass
from util import int_generator


@dataclass
class Product:
    id: int
    store_id: int

def create_product(store_id: int):
    return Product(id=int_generator(), store_id=store_id)