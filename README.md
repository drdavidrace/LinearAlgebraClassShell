# <center>LinearAlgebraClassShell</center>

This is a collection of shell based routines that perform the same basic function as the Colaboratory version for the Linear Algebra class developed by Dr. David Race and Dr. Denise Race.  Rather than relying on the Colaboratory environment, this uses basic "ini" files to define the inputs and processes the data.  This change in methodology is designed to support both output to the shell (somewhat crude) and optionally support output to a plain vanilla Jupyter Notebook.  This is intended to provide more flexibility for future uses of the code.

This code is a temporary solution to one of the Jupyter Notebook issues, namely version control.  This code will be version controlled; therefore, it can be more readily used in other environments (outside of Google Colaboratory).
## Notes

### Development Environment
The authors are fans of the python3 environment for Linear Algebra; however, we also have contraints from education environments that forces us to use Windows 10 and the Office 365 products.  Given these two constraints, this code has been developed and tested using the Windows Subsytem for Linux.  The code is primarily developed for a minimalist computer, but should suffice for a gentle introduction to Linear Algebra.  The products that are used for this development are:

*  python3
*  numpy
*  sympy
*  scipy
*  scikit-learn
*  torch
*  numba
*  jupyter notebook
*  jupyter lab

The last two are for those cases when we might want "better" output or mathematically complete descriptions of the tasks.  The inputs will use "ini" file inputs rather than the ed_scripts that are the default method for the Colaboratory files.

###  Jupyter

Since I am using plain jupyter within the _"Windows Subsystem for Linux"_, this subsystem doesn't normally run a browser.  For this, both *"jupyter lab"* and *"jupyter notebook"* need to be started with the _"--no-browser"_ option.  To make this easy, I add aliases in the .bashrc file to start with this option automatically.  This allows the startup so that it doesn't cause an error.  Then we attach to the jupyter lab as normal using the browser in Windows.

###  Add comment about using XWindows

## License

This is licensed using the standard GNU General Public License v3.0; therefore, the code can be reused by others as desired.  It is hoped that attribution to Dr. David Race and Dr. Denise Race will be identified if this code is reused.

## packaging

For this package, I simply use "python ./setup.py sdist" and "python ./setup.py install" to keep things simple.  For testing (using unittest), I normally go through the following three steps:

*  python ./setup.py clean --all
*  python ./setup.py install
*  ./runTests.sh
