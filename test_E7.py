import pytest
import E7

class TestLimit():
    @pytest.fixture
    def setup(self):
        self.list = [1, 2, 3, 4, 5]


    def test_limit(self, setup):
        assert E7.limit(self.list, 3) != [1, 2, 5]