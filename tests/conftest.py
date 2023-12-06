

from store_api import create_store

import pytest


@pytest.fixture(name="store")
def store_fixture():
    return create_store()


