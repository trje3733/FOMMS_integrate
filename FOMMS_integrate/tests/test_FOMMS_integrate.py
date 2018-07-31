"""
Unit and regression test for the FOMMS_integrate package.
"""

# Import package, test suite, and other packages as needed
import FOMMS_integrate
import pytest
import sys

def test_FOMMS_integrate_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "FOMMS_integrate" in sys.modules
