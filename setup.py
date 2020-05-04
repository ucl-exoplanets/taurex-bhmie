
import setuptools
from setuptools import find_packages
from distutils.core import setup
from distutils.core import Extension
from distutils import log
import re, os
from Cython.Build import cythonize
import numpy as np
packages = find_packages(exclude=('tests', 'doc'))
provides = ['taurex_bhmie', ]


requires = []


install_requires = ['taurex',
                    'numpy',
                    'cython']



def build_bhmie():
    import numpy
    return Extension("taurex_bhmie.external.mie",  
                        sources=["taurex_bhmie/external/bh_mie.pyx",
                                "src/MIE/bhmie_lib.c",
                                "src/MIE/complex.c",
                                "src/MIE/nrutil.c"
                                ],
                        #extra_compile_args = [],
                        include_dirs=[np.get_include(),"./src/MIE/"],
                        language="c")

extensions = build_bhmie()

extensions = cythonize(extensions, language_level=3)

entry_points = {'taurex.plugins': 'bhmie = taurex_bhmie'}

setup(name='taurex_bhmie',
      author='Ahmed Faris Al-Refaie',
      author_email='ahmed.al-refaie.12@ucl.ac.uk',
      license="BSD",
      description='TauREx 3 BH-Mie plugin',
      packages=packages,
      include_package_data=True,
      entry_points=entry_points,
      provides=provides,
      requires=requires,
      install_requires=install_requires,
      ext_modules=extensions,
      package_data={'taurex_bhmie' : ['MgSiO3.dat']},
      )