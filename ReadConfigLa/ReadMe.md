#  Reading Config Files For Linear Algebra

This set of routines is designed to _"standardize"_ a way to read .json files for python code for a Linear Algebra class.  Because it is specific for providing inputs to a Linear Algebra class, it doesn't try to set environment variables nor does it try to be a general solution for all problems _(read the Limitations carefully)_.  Rather these routines are used to input variables for small Linear Algebra problems in a human readable manner.

As part of the standard process, this includes the _"test"_ subdirectory to provide test cases for the ability to read input for the problems.  These tests may not provide 100% coverage, but they will improve with usage.

#  Limitations

These routines are not meant to support large matrices _(namely ones larger than 10 on any side)_.  When using large matrices, either csv or binary input is the preferred method given the importance of input speed in these larger sizes.  Additionally, it is generally assumed that the matrices for large problems will be _"generated"_ from other routines so that the need for the clunkier classroom learning environment.

The input structure will be highly stylized, so that the input matrix structures can be derived from the from the input.  There are checks for the correct sizes for the rows and columns of the matrix to ensure that the matrix sizes and fills are complete.  Additionally the matrix addressing is assumed to be python3 sytle, so they start at 0 and must include every size up to the target size.

The input uses/abuses sympy for the input so that general calculations can be written, but the names are defined in the input json file.  This makes for some code that doesn't necessarily follow the recommendations for sympy (i.e., use the same name for the symbol as the variable name), but it does allow us a little more flexibility for the input.

#  Read Routines For JSON Inputs for Linear Algebra Education Classes

This directory contains a set of routines to read json files for use in a Linear Algebra classroom environment.  This is set up as a means for students to run tests without using Jupyter.  The graphics is more rudimentary and using Jupyter, but it is sometimes easier for students to use a standard python3 environment than loading the Jupyter environment.  While we would like for this to be completely self documenting in the json file, the user must tie the code that will use the json input to the variables in the code.

It is highly recommended that the user use the same names as the variables in the code; however, that is not a requirement.