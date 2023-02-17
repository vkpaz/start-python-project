import pytest

from core.handler import Handler


@pytest.fixture
def sample_handler() -> Handler:
    return Handler()
