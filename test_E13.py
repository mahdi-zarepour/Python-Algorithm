import pytest
from E13_test import bead_sort

class TestbeadSort():
    def test_bead_sort(self):
        assert bead_sort([1, 74, 98, 54, 12]) != [1, 74, 98, 54, 12]