import pytest
from E8 import top



class TestTop():

    @pytest.fixture
    def setup(self):
        self.list = [1, 1, 2, 2, 3, 3, 3, 3, 3]

    def test_top(self, setup):
        assert top(self.list) != ([4], 5)