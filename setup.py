from distutils.core import setup
'''
Setup for Linear_Algebra_Class_Shell
'''
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='linear_algebra_class_shell',
      version='0.1',
      author='Dr David Race',
      author_email='dr.david.race@gmail.com',
      url='https://github.com/drdavidrace/LinearAlgebraClassShell.git',
      description=(
          'Routines for reading .json files for input to Linear Algebra problems'),
      long_description=read('README.md'),
      license='GNU General Public License',
      packages=['ReadConfigLa', 'Test'],
      install_requires=['numpy', 'scipy', 'sympy', 'pandas',
                        'matplotlib', 'seaborn', 'sklearn', 'torch'],
      test_suite='test',
      zip_safe=False
      )