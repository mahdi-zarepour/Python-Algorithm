import pytest
from E19 import two_sum


class TestTwoSum():
    def test_two_sum(self):
        assert two_sum([2, 7, 12, 16], 9) == [1, 2]