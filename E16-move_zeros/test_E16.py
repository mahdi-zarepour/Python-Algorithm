import pytest
from E16 import move_zeros

class TestMoveZeros():
    def test_move_zeros(self):
        assert move_zeros([True, 10, 'Mahdi', 23, 0, False, 0, 'Ali']) != [True, 10, 'Mahdi', 23, 0, False, 0, 'Ali']
