from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize("sort_try.pyx"),
    include_dirs=[np.get_include()]
)