#
# Standard imports
# 
import unittest
import os, sys
#
# Custom imports
# 
from ReadConfigLa.read_config_la import ReadConfig

class InitializeReadConfig(unittest.TestCase):

    def test_initialization_empty(self):
        print("Testing the ReadConfig empty initialization")
        read_empty = ReadConfig()
        err_nums = read_empty.get_init_status()
        self.assertEqual(err_nums & 0x1, 0x1)
        self.assertEqual(err_nums & 0x10, 0x10)
        self.assertEqual(err_nums & 0x100, 0x100)
        self.assertEqual(err_nums & 0x1000, 0x1000)
        self.assertEqual(err_nums & 0x10000, 0x10000)

    def test_initialization_file_name(self):
        print("\nTesting ReadConfig with valid file name")
        current_dir = os.getcwd()
        init_dir = "ReadConfig_Test_data"
        file_name = "check_init.json"
        full_path = os.path.join(current_dir, init_dir)
        ready_file_name = ReadConfig(full_path,file_name)
        self.assertEqual(ready_file_name.get_init_status(),0)

    def test_required_false(self):
        print("\nTesting ReadConfig required values for non-existence")
        current_dir = os.getcwd()
        init_dir = "ReadConfig_Test_data"
        file_name = "check_required_invalid.json"
        full_path = os.path.join(current_dir, init_dir)
        ready_file_name = ReadConfig(full_path,file_name)
        ready_file_name.init_data_read()
        init_read_status = ready_file_name.get_init_read_errors()
        self.assertEqual(init_read_status & 0x1,0x1)
        self.assertEqual(init_read_status & 0x10, 0x10)

    def test_required_true(self):
        print("\nTesting ReadConfig required values for existence")
        current_dir = os.getcwd()
        init_dir = "ReadConfig_Test_data"
        file_name = "check_required_valid.json"
        full_path = os.path.join(current_dir, init_dir)
        ready_file_name = ReadConfig(full_path,file_name)
        ready_file_name.init_data_read()
        init_read_status = ready_file_name.get_init_read_errors()
        self.assertEqual(init_read_status & 0x1,0x0)
        self.assertEqual(init_read_status & 0x10, 0x0)