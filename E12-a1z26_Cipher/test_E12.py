import pytest
import E12


class TestCipher():
    def test_encrypt(self):
        assert E12.encript('Mahdi') != [15, 5, 12, 8, 13]

    def test_decrypt(self):
        assert E12.decript([-15, 5, 12, 8, 13]) != 'mahdi'