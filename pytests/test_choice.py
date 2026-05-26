from types import FunctionType
from py_src.choice import ask_for_file_or_folder, ask_encryption_or_decryption, ask_file_or_folder_file_path, ask_for_multiprocessing, ask_for_password, ask_for_salt

class TestBasic:
    def test_ask_for_file_or_folder(self):
        assert callable(ask_for_file_or_folder)
        assert isinstance(ask_for_file_or_folder, FunctionType)

    def test_ask_encryption_or_decryption(self):
        assert callable(ask_encryption_or_decryption)
        assert isinstance(ask_encryption_or_decryption, FunctionType)

    def test_ask_file_or_folder_file_path(self):
        assert callable(ask_file_or_folder_file_path)
        assert isinstance(ask_file_or_folder_file_path, FunctionType)

    def test_ask_for_multiprocessing(self):
        assert callable(ask_for_multiprocessing)
        assert isinstance(ask_for_multiprocessing, FunctionType)

    def test_ask_for_password(self):
        assert callable(ask_for_password)
        assert isinstance(ask_for_password, FunctionType)

    def test_ask_for_salt(self):
        assert callable(ask_for_salt)
        assert isinstance(ask_for_salt, FunctionType)
