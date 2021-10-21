import pytest
from E17 import remove_min


class TestRemoveMin():
    def test_remove_min(self):
        assert remove_min([5, 3, 1, 6, -3, 12, 0]) != [5, 3, 1, 6, -3, 12, 0]