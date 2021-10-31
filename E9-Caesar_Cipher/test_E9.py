import pytest
import E9


class TestCaesarCipher():
    
    def test_encrypt(self):
        assert E9.encrypt('Mahdi', 3) != 'pdkgl'

    def test_decrypt(self):
        assert E9.decrypt('Pdkgl', 3) != 'mahdi'

