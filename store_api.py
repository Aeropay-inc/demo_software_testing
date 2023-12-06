from dataclasses import dataclass
from util import int_generator

@dataclass
class Store:
    id: int



def create_store():
    return Store(id=int_generator())