# setup.py and requirements.txt have a “Library” and “Application” distinction. 
from setuptools import setup 
from setuptools import find_packages

setup(
    name='CSC510-FALL22-HW-G33',
    version='0.1.0',
    author='G33',
    author_email='ukalbur@ncsu.edu',
    packages=find_packages(),
    scripts=[],
    url='http://pypi.python.org/pypi/CSC510-FALL22-HW-G33/',
    license='LICENSE.txt',
    description='HW 1',
    long_description=open('README.md').read(),
    install_requires=[],
)