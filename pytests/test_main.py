from main import main, PASSWORD, SALT, encrypting, is_file, multiprocessing
from types import FunctionType


class TestBasic:
    def test_main(self):
        assert callable(main)
        assert isinstance(main, FunctionType)

    def test_password(self):
        assert isinstance(PASSWORD, str)

    def test_salt(self):
        assert isinstance(SALT, str)

    def test_encrypting(self):
        assert isinstance(encrypting, bool) or encrypting is None

    def test_is_file(self):
        assert isinstance(is_file, bool) or is_file is None

    def test_multiprocessing(self):
        assert isinstance(multiprocessing, bool)
