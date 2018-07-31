"""
Unit and regression test for the FOMMS_integrate package.
"""

# Import package, test suite, and other packages as needed
import FOMMS_integrate as integrate
import pytest
import sys

def test_FOMMS_integrate_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "FOMMS_integrate" in sys.modules


"""
Testing the integrate package
"""

import numpy as np

def g(x):
    return 3.0 * x

def f(x):
    return np.power(x, 2)

def h(x):
    return np.ones(x.size)

def volume(x):
    squares = np.power(x, 2)
    return np.sum(squares, axis=1)

def test_trapz():
    x = np.array([0, 10])
    I = integrate.trapz(x, g)
    assert I == 150.00
