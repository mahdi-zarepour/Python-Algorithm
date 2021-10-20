import pytest
from E10 import is_isomorphic


class TestIsIsomorphic():

    def test_is_isomorphic(self):
        assert is_isomorphic('ali', 'key') != False