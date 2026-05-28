from py_src.transform_folder import transform_folder, get_all_files, encrypt_file, decrypt_file, process_list
from pathlib import Path
import os
from types import FunctionType

class TestBasic:
    def test_transform_folder(self):
        assert callable(transform_folder)
        assert isinstance(transform_folder, FunctionType)
    def test_get_all_files(self):
        assert callable(get_all_files)
        assert isinstance(get_all_files, FunctionType)

class TestImportetFunctions:
    def test_encrypt_file(self):
        assert callable(encrypt_file)
    def test_decrypt_file(self):
        assert callable(decrypt_file)
