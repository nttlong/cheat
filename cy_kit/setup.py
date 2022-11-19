import pathlib

from setuptools import setup
from Cython.Build import cythonize
import os
build_dir = pathlib.Path(__file__).parent.__str__()
file_cy_kit_x=os.path.join(build_dir, f"cy_kit_x.py")

setup(
    name='cy_kit',
    ext_modules=cythonize(file_cy_kit_x),
    zip_safe=True,
    packages=["cy_kit"]
)

"""
cd cy_kit
python cy_kit/setup.py build_ext --inplace
python cy_kit/setup.py bdist_wheel --universal --inplace
"""