
from simple_math import simple_add, simple_sub, simple_mult, simple_div, poly_first, poly_second
import pytest

def test_simple_add():
    assert simple_add(1,1) == 2
    assert simple_add(2,3) == 5
    assert simple_add(4,5) == 9


def test_simple_sub():
    assert simple_sub(1,1) == 0
    assert simple_sub(2,3) == -1
    assert simple_sub(5,4) == 1

def test_simple_mult():
    assert simple_mult(1,1) == 1
    assert simple_mult(2,3) == 6
    assert simple_mult(4,5) ==20

def test_simple_div():
    assert simple_div(1,1) == 1
    assert simple_div(3,2) == 1.5
    assert simple_div(6,2) == 3

def test_poly_first():
    assert poly_first(2, 3, 4) == 3 + 4 * 2
    assert poly_first(0, 1, 5) == 1

def test_poly_second():
    assert poly_second(2, 1, 2, 3) == 1 + 2*2 + 3*(2**2)
    assert poly_second(0, 4, 5, 6) == 4
