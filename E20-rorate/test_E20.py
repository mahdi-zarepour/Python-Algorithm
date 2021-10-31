import pytest
from E20 import rotate

class TestRoteate:
    def test_rotate(self):
        assert rotate('hello', 2) == 'llohe'

