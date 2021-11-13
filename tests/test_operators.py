from src.operators import (
    mul,
    add,
    neg,
    max,
)
from hypothesis import given
from .strategies import small_floats


@given(small_floats, small_floats)
def test_operator(x, y):
    """Check operator return value"""
    assert mul(x, y) == x * y
    assert add(x, y) == x + y
    assert neg(x) == -x
    if x > y:
        assert max(x, y) == x
    else:
        assert max(x, y) == y
