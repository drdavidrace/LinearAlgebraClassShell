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
import sympy as smp 
#
class ReadConfig:
    def __init__(self, in_dir = None, in_file = None):
        assert in_dir is not None
        assert in_file is not None
        #
        #  basic checks
        #
        assert os.path.exists(in_dir) is True, "directory does not exist"
        full_file_name = os.path.join(in_dir, in_file)
        assert os.path.isfile(full_file_name), "file does not exist"
        ext = os.path.splitext(full_file_name)[-1].lower()
        assert ext = "json", "wrong file extension"
        self.full_file_name = full_file_name
