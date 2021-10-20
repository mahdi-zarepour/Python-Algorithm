import pytest
from E11 import search_insert


class TestSearchInsert():
    def test_search_insert(self):
        assert search_insert([1, 3, 5, 7], 8) != 3