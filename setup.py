# setup.py and requirements.txt have a “Library” and “Application” distinction. 
from setuptools import setup, find_packages


setup(
    name='hw1_backend',
    version='0.1.0',
    author='G33',
    packages=find_packages(),
    url='http://pypi.python.org/pypi/CSC510-FALL22-HW-G33/',
    license='LICENSE.md',
    description='HW 1',
    long_description=open('README.md').read()
)