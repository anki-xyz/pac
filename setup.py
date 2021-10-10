from distutils.core import setup
from setuptools import find_packages

setup(name='pac',
      version='0.1a',
      author='Andreas Kist',
      author_email='me@anki.xyz',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow'])