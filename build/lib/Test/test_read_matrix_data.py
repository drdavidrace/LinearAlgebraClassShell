#
# Standard imports
# 
import unittest
import os, sys
from pprint import pprint
import numpy as np
import sympy as smp
#
# Custom imports
# 
from ReadConfigLa.read_config_la import ReadConfig

class InitializeReadConfig(unittest.TestCase):

    def test_read_matrix(self):
        print("\nTesting ReadConfig with matrix data")
        current_dir = os.getcwd()
        init_dir = "ReadConfig_Test_data"
        file_name = "check_matrix_read_valid.json"
        full_path = os.path.join(current_dir, init_dir)
        ready_file_name = ReadConfig(full_path,file_name)
        ready_file_name.init_data_read()
        A = ready_file_name.get_matrix("A")
        self.assertTrue(np.array_equal(A,np.array([[1,2,3],[4,5,6]])))

    def test_read_matrix_sympy(self):
        print("\nTesting ReadConfig with matrix data - sympy")
        current_dir = os.getcwd()
        init_dir = "ReadConfig_Test_data"
        file_name = "check_matrix_read_sympy_valid.json"
        full_path = os.path.join(current_dir, init_dir)
        ready_file_name = ReadConfig(full_path,file_name)
        ready_file_name.init_data_read()
        A = ready_file_name.get_matrix("A")
        self.assertTrue(A.equals(smp.Matrix([[1,2,3],[4,5,6]])))

    def test_read_variable_None(self):
        print("\nTesting ReadConfig with variable missing")
        current_dir = os.getcwd()
        init_dir = "ReadConfig_Test_data"
        file_name = "check_matrix_read_sympy_valid.json"
        full_path = os.path.join(current_dir, init_dir)
        ready_file_name = ReadConfig(full_path,file_name)
        ready_file_name.init_data_read()
        A = ready_file_name.get_variable("A")
        self.assertIsNone(A)

    def test_read_variables(self):
        print("\nTesting ReadConfig with variable missing")
        current_dir = os.getcwd()
        init_dir = "ReadConfig_Test_data"
        file_name = "check_matrix_read_sympy_valid.json"
        full_path = os.path.join(current_dir, init_dir)
        ready_file_name = ReadConfig(full_path,file_name)
        ready_file_name.init_data_read()
        b = ready_file_name.get_variable("B")
        self.assertEqual(int(b),2)
        c = ready_file_name.get_variable("C")
        self.assertEqual(float(c),float(3.14159))