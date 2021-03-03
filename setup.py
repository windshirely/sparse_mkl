import os
from setuptools import setup, find_packages

DISTNAME = 'sparse_mkl'
VERSION = '0.1.0'
DESCRIPTION = "Intel MKL wrapper for sparse matrix multiplication and addition, " \
              "all these are based on Chris Jackson's code, ref: https://github.com/flatironinstitute/sparse_dot"
MAINTAINER = 'Yang'
MAINTAINER_EMAIL = ''
URL = ''
LICENSE = 'MIT'

# Description from README.md
base_dir = os.path.dirname(os.path.abspath(__file__))
long_description = "\n\n".join([open(os.path.join(base_dir, "README.md"), "r").read()])

setup(name=DISTNAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url=URL,
      author=MAINTAINER,
      author_email=MAINTAINER_EMAIL,
      license=LICENSE,
      packages=find_packages(include=['sparse_mkl', "sparse_mkl.*"]),
      install_requires=['numpy', 'scipy'],
      tests_require=['nose', 'coverage'],
      test_suite="nose.collector",
      zip_safe=True,
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Development Status :: 4 - Beta"
      ]
)
