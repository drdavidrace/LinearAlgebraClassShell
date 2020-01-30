###########################################################################
#  Purpose:  This object provides the ability to read a json file for 
#   a Linear Algebra class to demonstrate basic Linear Algebra usage.
#
#  Inputs:  
#   in_dir - this is the name of the input directory
#   in_file - this is the name of the json file that is required for
#       the problem.  We only support one file per problem and one problem
#       per file!
#       NOTE:  the file names is required to end in ".json"
#
#  Required Values:
#   problem_number - This is the problem number and must be the same 
#       as the name of the file, without the json on the end.  This is
#       checked against the file name.
#       NOTE:  Currently nothing is done, but the name is generally of the form
#           "chapter.section.problem" similar to "2.3.12"
#   variable_names - This is a directory of the variables that are named
#       later.  This is used to perform some rudimentary checks.  These
#       checks include:
#           The type of variable, var vs matrix
#           If matrix, then that the input matches the shape
#  Variable Types:
#   "var" - Nothing more is done.  This uses sympy to define the value
#   "matrix", If matrix is the type, then the shape must be given.  The
#       use of 1 dimensional arrays is problematic; therefore, the shape
#       must be a dictionary with indices "row2" and "cols"
#       NOTE:  Since this is an elementary class environment, we don't support
#           tensors.
#       NOTE:  The rows and cols values are checked against the inputs.
#   NOTE:  All values for the inputs are checked using sympy.  There are routines
#       for returning numpy values.
#
#  Special Note:  This uses "assert" so that it isn't very graceful, maybe that 
#   will change over time.
############################################################################
#
#  Standard imports
#
import os, sys
import json
import sympy as smp 
import numpy as np
#
#  not used much
#
from pprint import pprint
class ReadConfig:
    
    def __init__(self, in_dir: str = None, in_file:str = None):
        """Initialize the class to read a set of .json files to input matrices for 
            a Linear Algebra
        
        Keyword Arguments:
            in_dir {[str]} -- [Directory to read the .json file] (default: {None})
            in_file {[str]} -- [File name to read ] (default: {None})
        """
        self.error_numbers = 0
        self.init_read_errors = 0
        self.full_file_name = None
        self.valid_matrix = set(["numpy", "sympy"])
        self.in_data = None
        self.question_number = None
        self.matrix_type = None
        try:
            assert in_dir is not None
        except AssertionError:
            print("\tReadConfig __init__ must have a directory for reading json file")
            self.error_numbers += 0b1
            pass
        try:
            assert in_file is not None
        except AssertionError:
            print("\tReadConfig __init__ must have a file for reading json file")
            self.error_numbers += 0b10
            pass
        #
        #  basic checks
        #
        try:
            assert os.path.exists(in_dir) is True
        except:
            print("\tReadConfig __init__ Input directory does not exist")
            self.error_numbers += 0b100
            pass
        try:
            self.full_file_name = os.path.join(in_dir, in_file)
            assert os.path.isfile(self.full_file_name), "file does not exist"
        except:
            print("\tReadConfig __init__ Input file does not exist")
            self.error_numbers += 0b1000
            pass
        try:
            file_extension = os.path.splitext(self.full_file_name)[-1]
            assert file_extension == ".json"
        except:
            self.error_numbers += 0b10000
            print("\tReadConfig __init__ The input file has the wrong (no no extension).  Must be json")
            pass
    #
    #  Public Methods
    #
    #
    def get_init_status(self):
        """[Returns the error_numbers to the calling routine]
        
        Returns:
            [int] -- [All of the errors that occurred testing that json file exists]
        """
        return self.error_numbers
    def get_init_read_errors(self):
        """[Returns the status from the initial read of the json file]
        
        Returns:
            [int] -- [All of the errors that occurred during the initial read of the file]
        """
        return self.init_read_errors
    #
    #  Do the initial file read and set the initial status
    #
    def init_data_read(self):
        """This does the initial data read and validate the basic required variables

        """
        in_file = self.full_file_name
        with open(in_file) as json_file:
            in_data = json.load(json_file)
            question_number = in_data.get("question",None)
            matrix_type = in_data.get("matrix_type",None)
            is_valid_question = self.__is_valid_question__(in_file, question_number)
            if not is_valid_question:
                self.init_read_errors += 0b1
            else:
                self.question_number = question_number
            if matrix_type is None:
                self.matrix_type = None
            else:
                is_valid_matrix = self.__is_valid_matrix_type__(matrix_type)
                if not is_valid_matrix:
                    self.init_read_errors += 0b10
                else:
                    self.matrix_type = matrix_type.strip()

            if self.init_read_errors == 0:
                self.in_data = in_data
    #
    def get_json_data(self):
        return self.in_data
    #
    def get_matrix(self,matrix_name):
        if self.in_data is None:
            return None
        elif not ("matrices" in self.in_data):
            return None
        else:
            if not(matrix_name in self.in_data["matrices"]):
                return None
            else:
                if self.matrix_type == "numpy":
                    return np.array(self.in_data["matrices"][matrix_name])
                elif self.matrix_type == "sympy":
                    return smp.Matrix(self.in_data["matrices"][matrix_name])
                else:
                    return self.in_data["matrices"][matrix_name]
    #
    def get_variable(self,var_name):
        #Note:  the calling program must set the type of variable on return
        if self.in_data is None:
            return None
        elif not ("variables" in self.in_data):
            return None
        else:
            if not (var_name) in self.in_data["variables"]:
                return None
            else:
                return self.in_data["variables"][var_name]
    #
    #  Internal Functions
    #
    def __is_valid_question__(self, in_file:str = None, in_question = None):
        """[Checks the question value in the json file]
        
        Keyword Arguments:
            in_file {str} -- [Name of the file] (default: {None})
            in_question {[str or None]} -- [value of the question in json file] (default: {None})
        
        Returns:
            [boolean] -- [True if valid, False otherwise]
        """
        assert in_file is not None
        try:
            assert in_question is not None
        except:
            return False
            pass
        bname = os.path.basename(in_file)
        bname = bname.split(".")[0].strip()
        qname = in_question.strip()
        return (bname == qname)
    #
    def __is_valid_matrix_type__(self, in_matrix_type = None):
        try:
            assert in_matrix_type is not None
        except:
            return False
            pass
        if in_matrix_type in self.valid_matrix:
            return True
        else:
            return False
    #
