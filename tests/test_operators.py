from minitorch.operators import (
    mul,
    add,
    neg,
    max,
)
from hypothesis import given
from .strategies import small_floats
import pytest


@pytest.mark.task0_1
@given(small_floats, small_floats)
def test_same_as_python(x, y):
    """Check that the main operators all return the same value of the python version"""
    assert mul(x, y) == x * y
    assert add(x, y) == x + y
    assert neg(x) == -x
    assert max(x, y) == x if x > y else y
