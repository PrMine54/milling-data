# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages

version = "0.0.1"

# burası kullanılacak versiyona göre değiştirilsin
if (3, 9) <= sys.version_info < (3, 9):
    sys.exit('OPT requires Python 3.9.x')

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

with open('README.md') as f:
    readme = f.read()

with open("requirements.txt") as f:
    requirements = [i.strip() for i in f.readlines()]

setup(
    name='OPT',
    version=version,
    description='Proje Açıklaması',
    long_description=readme,
    author='B3LAB',
    author_email='b3lab',
    url='http://bitbucket.b3lab.org/proje.git',
    packages=find_packages(exclude=['*tests*']),
    python_requires='',  # hangi python sürümünde geliştirme yapıldı
)
